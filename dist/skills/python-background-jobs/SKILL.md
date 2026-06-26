---
name: python-background-jobs
description: Implement background job processing and task queues in Python. Use when building async task processing, job queues, long-running operations, event-driven architectures, or decoupling work from request/response cycles. Covers Celery, RQ, Dramatiq, idempotency, DLQ, and job state management.
type: Playbook
---

# Python Background Jobs & Task Queues

Decouple long-running or unreliable work from request/response cycles. Return immediately to the user while background workers handle the heavy lifting.

## When to Use

- Tasks taking longer than a few seconds
- Sending emails, notifications, or webhooks
- Generating reports or exporting data
- Processing uploads or media transformations
- Integrating with unreliable external services
- Building event-driven architectures

## Core Concepts

1. **Task Queue Pattern**: API accepts request, enqueues job, returns job ID immediately
2. **Idempotency**: Tasks may be retried — design for safe re-execution
3. **Job State Machine**: pending → running → succeeded/failed
4. **At-Least-Once Delivery**: Most queues guarantee at-least-once — handle duplicates

## Quick Start (Celery)

```python
from celery import Celery

app = Celery("tasks", broker="redis://localhost:6379")

@app.task
def send_email(to: str, subject: str, body: str) -> None:
    email_client.send(to, subject, body)

# In API handler — returns immediately
send_email.delay("user@example.com", "Welcome!", "Thanks for signing up")
```

## Pattern 1: Return Job ID Immediately

```python
async def start_export(request: ExportRequest) -> JobResponse:
    job_id = str(uuid4())
    await jobs_repo.create(Job(id=job_id, status=JobStatus.PENDING, created_at=datetime.utcnow()))
    await task_queue.enqueue("export_data", job_id=job_id, params=request.model_dump())
    return JobResponse(job_id=job_id, status="pending", poll_url=f"/jobs/{job_id}")
```

## Pattern 2: Celery Task Configuration

```python
@app.task(
    bind=True,
    max_retries=3,
    default_retry_delay=60,
    autoretry_for=(ConnectionError, TimeoutError),
)
def process_payment(self, payment_id: str) -> dict:
    try:
        result = payment_gateway.charge(payment_id)
        return {"status": "success", "transaction_id": result.id}
    except PaymentDeclinedError as e:
        return {"status": "declined", "reason": str(e)}  # Don't retry permanent failures
    except TransientError as e:
        raise self.retry(exc=e, countdown=2 ** self.request.retries * 60)
```

## Pattern 3: Make Tasks Idempotent

Workers may retry on crash or timeout. Design for safe re-execution:

1. **Check-before-write**: Verify state before action
2. **Idempotency keys**: Use unique tokens with external services
3. **Upsert patterns**: `INSERT ... ON CONFLICT UPDATE`
4. **Deduplication window**: Track processed IDs for N hours

```python
@app.task(bind=True)
def process_order(self, order_id: str) -> None:
    order = orders_repo.get(order_id)
    if order.status == OrderStatus.COMPLETED:
        return  # Already processed
    result = payment_provider.charge(amount=order.total, idempotency_key=f"order-{order_id}")
    orders_repo.update(order_id, status=OrderStatus.COMPLETED)
```

## Pattern 4: Dead Letter Queue

```python
@app.task(bind=True, max_retries=3)
def process_webhook(self, webhook_id: str, payload: dict) -> None:
    try:
        result = send_webhook(payload)
        if not result.success:
            raise WebhookFailedError(result.error)
    except Exception as e:
        if self.request.retries >= self.max_retries:
            dead_letter_queue.send({"task": "process_webhook", "webhook_id": webhook_id, "error": str(e)})
            return
        raise self.retry(exc=e, countdown=2 ** self.request.retries * 60)
```

## Pattern 5: Status Polling Endpoint

```python
@app.get("/jobs/{job_id}")
async def get_job_status(job_id: str) -> JobStatusResponse:
    job = await jobs_repo.get(job_id)
    if job is None:
        raise HTTPException(404, f"Job {job_id} not found")
    return JobStatusResponse(
        job_id=job.id, status=job.status.value,
        is_terminal=job.status in (JobStatus.SUCCEEDED, JobStatus.FAILED),
    )
```

## Pattern 6: Task Chaining and Workflows

```python
from celery import chain, group, chord

# Chain: A → B → C
workflow = chain(extract_data.s(source_id), transform_data.s(), load_data.s(destination_id))

# Parallel: A, B, C all at once
parallel = group(send_email.s(user_email), send_sms.s(user_phone), update_analytics.s(event_data))

# Chord: Parallel tasks → callback
workflow = chord([process_item.s(item_id) for item_id in item_ids], send_completion_notification.s(batch_id))
```

## Alternative Task Queues

**RQ (Redis Queue):** Simple, Redis-based. `queue.enqueue(send_email, to, subject, body)`

**Dramatiq:** Modern Celery alternative. `@dramatiq.actor` decorator.

**Cloud-native:** AWS SQS + Lambda, Google Cloud Tasks, Azure Functions.

## Best Practices

1. **Return immediately** — Don't block requests for long operations
2. **Persist job state** — Enable status polling and debugging
3. **Make tasks idempotent** — Safe to retry on any failure
4. **Use idempotency keys** — For external service calls
5. **Set timeouts** — Both soft and hard limits
6. **Implement DLQ** — Capture permanently failed tasks
7. **Log transitions** — Track job state changes
8. **Retry appropriately** — Exponential backoff for transient errors
9. **Don't retry permanent failures** — Validation errors, invalid credentials
10. **Monitor queue depth** — Alert on backlog growth

## Source

Distilled from `GeniusHTX/SWE-Skills-Bench` → `skills/python-background-jobs/SKILL.md` (MIT).
