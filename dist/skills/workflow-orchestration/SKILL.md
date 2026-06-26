---
name: workflow-orchestration
description: Master workflow orchestration architecture with Temporal, covering fundamental design decisions, resilience patterns, and best practices for building reliable distributed systems. Use for multi-step processes, long-running workflows, and failure recovery.
type: Playbook
---

# Workflow Orchestration Patterns

Master workflow orchestration architecture with Temporal, covering fundamental design decisions, resilience patterns, and best practices for building reliable distributed systems.

## When to Use

- **Multi-step processes** spanning machines/services/databases
- **Distributed transactions** requiring all-or-nothing semantics
- **Long-running workflows** (hours to years) with automatic state persistence
- **Failure recovery** that must resume from last successful step
- **Business processes**: bookings, orders, campaigns, approvals
- **Entity lifecycle management**: inventory tracking, account management, cart workflows
- **Infrastructure automation**: CI/CD pipelines, provisioning, deployments
- **Human-in-the-loop** systems requiring timeouts and escalations

## When NOT to Use

- Simple CRUD operations (use direct API calls)
- Pure data processing pipelines (use Airflow, batch processing)
- Stateless request/response (use standard APIs)
- Real-time streaming (use Kafka, event processors)

## Critical Design Decision: Workflows vs Activities

**The Fundamental Rule:**

- **Workflows** = Orchestration logic and decision-making
- **Activities** = External interactions (APIs, databases, network calls)

```
Does it touch external systems? → Activity
Is it orchestration/decision logic? → Workflow
```

### Workflows (Orchestration)

**Characteristics:**
- Contain business logic and coordination
- **MUST be deterministic** (same inputs → same outputs)
- **Cannot** perform direct external calls
- State automatically preserved across failures
- Can run for years despite infrastructure failures

**Allowed in Workflows:**
- Pure functions and calculations
- Calling activities (non-deterministic operations)
- `workflow.now()` (deterministic time)
- `workflow.random()` (deterministic random)

**Prohibited in Workflows:**
- ❌ Threading, locks, synchronization primitives
- ❌ `random()`, `datetime.now()` (non-deterministic)
- ❌ Global state or static variables
- ❌ Direct file I/O or network calls
- ❌ Non-deterministic libraries

### Activities (External Interactions)

**Characteristics:**
- Handle all external system interactions
- Can be non-deterministic (API calls, DB writes)
- Include built-in timeouts and retry logic
- **Must be idempotent** (calling N times = calling once)
- Short-lived (seconds to minutes typically)

## Core Workflow Patterns

### 1. Saga Pattern with Compensation

```
For each step:
  1. Register compensation BEFORE executing
  2. Execute the step (via activity)
  3. On failure, run all compensations in reverse order (LIFO)
```

**Example: Payment Workflow**
1. Reserve inventory (compensation: release inventory)
2. Charge payment (compensation: refund payment)
3. Fulfill order (compensation: cancel fulfillment)

**Critical Requirements:**
- Compensations must be idempotent
- Register compensation BEFORE executing step
- Run compensations in reverse order
- Handle partial failures gracefully

### 2. Entity Workflows (Actor Model)

- One workflow execution = one entity (cart, account, inventory item)
- Workflow persists for entity lifetime
- Receives signals for state changes
- Supports queries for current state

**Example Use Cases:**
- Shopping cart (add items, checkout, expiration)
- Bank account (deposits, withdrawals, balance checks)
- Product inventory (stock updates, reservations)

### 3. Fan-Out/Fan-In (Parallel Execution)

- Spawn child workflows or parallel activities
- Wait for all to complete
- Aggregate results
- Handle partial failures

**Scaling Rule:**
- Don't scale individual workflows
- For 1M tasks: spawn 1K child workflows × 1K tasks each
- Keep each workflow bounded

### 4. Async Callback Pattern

- Workflow sends request and waits for signal
- External system processes asynchronously
- Sends signal to resume workflow
- Workflow continues with response

**Use Cases:** Human approval workflows, webhook callbacks, long-running external processes

## State Management and Determinism

### Automatic State Preservation

- Complete program state preserved automatically
- Event History records every command and event
- Seamless recovery from crashes
- Applications restore pre-failure state

### Versioning Strategies

**Challenge**: Changing workflow code while old executions still running

**Solutions:**
1. **Versioning API**: Use `workflow.get_version()` for safe changes
2. **New Workflow Type**: Create new workflow, route new executions to it
3. **Backward Compatibility**: Ensure old events replay correctly

## Resilience and Error Handling

### Retry Policies

**Default Behavior**: Temporal retries activities forever

**Configure Retry:**
- Initial retry interval
- Backoff coefficient (exponential backoff)
- Maximum interval (cap retry delay)
- Maximum attempts (eventually fail)

**Non-Retryable Errors:**
- Invalid input (validation failures)
- Business rule violations
- Permanent failures (resource not found)

### Idempotency Requirements

Activities may execute multiple times due to network failures and retries. Implementation strategies:
- Idempotency keys (deduplication)
- Check-then-act with unique constraints
- Upsert operations instead of insert
- Track processed request IDs

### Activity Heartbeats

- Activity sends periodic heartbeat with progress information
- Timeout if no heartbeat received
- Enables progress-based retry

## Best Practices

### Workflow Design

1. **Keep workflows focused** — single responsibility per workflow
2. **Small workflows** — use child workflows for scalability
3. **Clear boundaries** — workflow orchestrates, activities execute
4. **Test locally** — use time-skipping test environment

### Activity Design

1. **Idempotent operations** — safe to retry
2. **Short-lived** — seconds to minutes, not hours
3. **Timeout configuration** — always set timeouts
4. **Heartbeat for long tasks** — report progress
5. **Error handling** — distinguish retryable vs non-retryable

### Common Pitfalls

**Workflow Violations:**
- Using `datetime.now()` instead of `workflow.now()`
- Threading or async operations in workflow code
- Calling external APIs directly from workflow
- Non-deterministic logic in workflows

**Activity Mistakes:**
- Non-idempotent operations (can't handle retries)
- Missing timeouts (activities run forever)
- No error classification (retry validation errors)
- Ignoring payload limits (2MB per argument)

## Related Skills

- `saga-orchestration` — saga pattern implementation details
- `event-sourcing-architect` — event sourcing patterns
- `event-store-design` — event store implementation
