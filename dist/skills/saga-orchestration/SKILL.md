---
name: saga-orchestration
description: Patterns for managing distributed transactions and long-running business processes. Use when coordinating multi-service transactions, implementing compensating transactions, or managing long-running business workflows.
type: Playbook
---

# Saga Orchestration

Patterns for managing distributed transactions and long-running business processes.

## When to Use

- Coordinating multi-service transactions (e.g., order fulfillment across inventory, payment, shipping)
- Implementing compensating transactions for rollback
- Managing long-running business workflows
- Handling failures in distributed systems gracefully
- Building order fulfillment, booking, or approval workflows

## When NOT to Use

- Single-database transactions (use ACID transactions instead)
- Operations that must be atomic with strong consistency
- Simple request/response flows without multi-step coordination

## Saga Types

### Choreography-Based Saga

Services communicate through events. Each service listens for events and produces new events.

```
┌─────┐  ┌─────┐  ┌─────┐
│Svc A│─►│Svc B│─►│Svc C│
└─────┘  └─────┘  └─────┘
   │        │        │
   ▼        ▼        ▼
 Event    Event    Event
```

**Pros**: Decoupled services, no single point of failure
**Cons**: Harder to track overall saga state, circular dependencies possible

### Orchestration-Based Saga

A central orchestrator directs the saga, telling each service what to do.

```
┌─────────────┐
│ Orchestrator│
└──────┬──────┘
       │
  ┌────┼────┐
  ▼    ▼    ▼
┌────┐┌────┐┌────┐
│Svc1││Svc2││Svc3│
└────┘└────┘└────┘
```

**Pros**: Centralized state management, easier to track progress
**Cons**: Orchestrator is a single point of failure (mitigate with durable execution)

## Saga Execution States

| State            | Description                    |
| ---------------- | ------------------------------ |
| **Started**      | Saga initiated                 |
| **Pending**      | Waiting for step completion    |
| **Compensating** | Rolling back due to failure    |
| **Completed**    | All steps succeeded            |
| **Failed**       | Saga failed after compensation |

## Core Pattern: Orchestration with Compensation

### Step 1: Define the Saga

```python
@dataclass
class SagaStep:
    name: str
    action: str           # Command to execute
    compensation: str     # Compensating command
    status: str = "pending"

class OrderFulfillmentSaga:
    saga_type = "OrderFulfillment"
    
    def define_steps(self, data: Dict) -> List[SagaStep]:
        return [
            SagaStep("reserve_inventory", 
                     "InventoryService.ReserveItems",
                     "InventoryService.ReleaseReservation"),
            SagaStep("process_payment",
                     "PaymentService.ProcessPayment",
                     "PaymentService.RefundPayment"),
            SagaStep("create_shipment",
                     "ShippingService.CreateShipment",
                     "ShippingService.CancelShipment"),
            SagaStep("send_confirmation",
                     "NotificationService.SendOrderConfirmation",
                     "NotificationService.SendCancellationNotice")
        ]
```

### Step 2: Execute with Compensation

```
For each step:
  1. Register compensation BEFORE executing
  2. Execute the step (via activity/command)
  3. On success → continue to next step
  4. On failure → run all compensations in reverse order (LIFO)
```

### Step 3: Handle Compensation

```python
async def _compensate(self, saga: Saga):
    """Execute compensation for completed steps in reverse order."""
    for i in range(saga.current_step - 1, -1, -1):
        step = saga.steps[i]
        if step.status == "completed":
            step.status = "compensating"
            await self.saga_store.save(saga)
            
            await self.event_publisher.publish(
                step.compensation,
                {
                    "saga_id": saga.saga_id,
                    "step_name": step.name,
                    "original_result": step.result,
                    **saga.data
                }
            )
```

## Choreography Pattern

```python
class OrderChoreographySaga:
    def __init__(self, event_bus):
        self.event_bus = event_bus
        self._register_handlers()
    
    def _register_handlers(self):
        self.event_bus.subscribe("OrderCreated", self._on_order_created)
        self.event_bus.subscribe("InventoryReserved", self._on_inventory_reserved)
        self.event_bus.subscribe("PaymentProcessed", self._on_payment_processed)
        self.event_bus.subscribe("PaymentFailed", self._on_payment_failed)
    
    async def _on_order_created(self, event):
        await self.event_bus.publish("ReserveInventory", {
            "saga_id": event["order_id"],
            "items": event["items"]
        })
    
    async def _on_inventory_reserved(self, event):
        await self.event_bus.publish("ProcessPayment", {
            "saga_id": event["saga_id"],
            "amount": event["total_amount"]
        })
    
    async def _on_payment_failed(self, event):
        # Compensation: release inventory
        await self.event_bus.publish("ReleaseInventory", {
            "saga_id": event["saga_id"],
            "reservation_id": event["reservation_id"]
        })
```

## Saga with Timeouts

```python
async def _execute_next_step(self, saga: Saga):
    step = saga.steps[saga.current_step]
    step.status = "executing"
    step.timeout_at = datetime.utcnow() + timedelta(minutes=5)
    
    # Schedule timeout check
    await self.scheduler.schedule(
        f"saga_timeout_{saga.saga_id}_{step.name}",
        self._check_timeout,
        {"saga_id": saga.saga_id, "step_name": step.name},
        run_at=step.timeout_at
    )
    
    await self.event_publisher.publish(step.action, {...})
```

## Durable Execution Alternative

The templates above build saga infrastructure from scratch. **Durable execution frameworks** (like DBOS, Temporal) eliminate much of this boilerplate:

- Workflow runtime automatically persists state to a database
- Retries failed steps automatically
- Resumes from last checkpoint after crashes
- Handles exactly-once execution semantics

Consider durable execution when you want saga-like reliability without managing the coordination infrastructure yourself. See `workflow-orchestration` skill for details.

## Best Practices

### Do's

- **Make steps idempotent** — safe to retry
- **Design compensations carefully** — they must work under all conditions
- **Use correlation IDs** — for tracing across services
- **Implement timeouts** — don't wait forever for a step to complete
- **Log everything** — for debugging failures
- **Register compensation BEFORE executing** — ensure rollback is always possible

### Don'ts

- **Don't assume instant completion** — sagas take time
- **Don't skip compensation testing** — this is the most critical part
- **Don't couple services** — use async messaging
- **Don't ignore partial failures** — handle gracefully
- **Don't forget to test compensation paths** — they're harder than happy paths

## Related Skills

- `event-sourcing-architect` — event sourcing and CQRS patterns
- `event-store-design` — event store implementation
- `workflow-orchestration` — durable workflow orchestration with Temporal
