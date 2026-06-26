---
name: event-sourcing-architect
description: Expert in event sourcing, CQRS, and event-driven architecture patterns. Use when building systems requiring audit trails, temporal queries, complex domain modeling, or separating read and write models for performance.
type: Playbook
---

# Event Sourcing Architect

Expert in event sourcing, CQRS, and event-driven architecture patterns. Masters event store design, projection building, saga orchestration, and eventual consistency patterns.

## When to Use

- Building systems requiring complete audit trails
- Implementing complex business workflows with compensating actions
- Designing systems needing temporal queries ("what was state at time X")
- Separating read and write models for performance
- Building event-driven microservices architectures
- Implementing undo/redo or time-travel debugging
- Domain models where the history of changes is as important as current state

## When NOT to Use

- The domain is simple and CRUD is sufficient
- You cannot support event store operations or projections
- Strong immediate consistency is required everywhere
- The team has no experience with event-driven patterns (steep learning curve)

## Core Concepts

### Events as Immutable Facts

Events represent things that have happened in the past. They are:
- **Immutable**: Never modified or deleted after creation
- **Descriptive**: Named in past tense (e.g., `OrderPlaced`, `PaymentReceived`)
- **Self-contained**: Include all data needed to understand what happened
- **Ordered**: Maintain strict per-stream and global ordering

### Aggregate Design

```
Command → Aggregate (validates against current state) → Event(s)
```

1. Load aggregate state by replaying its event stream
2. Validate the command against business rules
3. Produce new events representing the state change
4. Append events to the stream (optimistic concurrency control)

### CQRS (Command Query Responsibility Segregation)

```
         ┌──────────────┐
Command →│  Write Model  │→ Event(s)
         └──────┬───────┘
                │
         ┌──────▼───────┐
         │  Projections  │→ Read Model(s)
         └──────────────┘
```

- **Write model**: Handles commands, enforces invariants, produces events
- **Read models**: Optimized for query patterns, built from projections
- **Eventual consistency**: Read models lag behind write model (typically milliseconds)

## Implementation Steps

### 1. Identify Aggregate Boundaries

- Group related entities that must maintain consistency
- Each aggregate has a root entity that serves as the entry point
- Keep aggregates small and focused on a single transactional boundary
- Reference other aggregates by ID, not by object reference

### 2. Design Events

```python
@dataclass(frozen=True)
class Event:
    event_id: UUID
    stream_id: str
    event_type: str
    data: dict
    metadata: dict  # correlation_id, causation_id, user_id, timestamp
    version: int
    created_at: datetime
```

**Event design principles:**
- Name in past tense: `OrderPlaced`, not `PlaceOrder`
- Include all data needed for projections (avoid lazy loading)
- Keep events small and focused
- Version events from day one (plan for schema evolution)

### 3. Implement Command Handlers

```python
class OrderAggregate:
    def __init__(self, events: List[Event]):
        self.state = self._apply_events(events)
    
    def place_order(self, items: List[Item], customer_id: str) -> List[Event]:
        # Validate business rules
        if self.state.status != "draft":
            raise InvalidOperation("Order already placed")
        if not items:
            raise ValidationError("Order must have items")
        
        # Produce events
        return [OrderPlaced(
            order_id=self.state.order_id,
            customer_id=customer_id,
            items=[i.to_dict() for i in items],
            placed_at=datetime.utcnow()
        )]
```

### 4. Build Projections

```python
class OrderSummaryProjection:
    def __init__(self, db):
        self.db = db
    
    async def handle_order_placed(self, event: OrderPlaced):
        await self.db.orders.insert_one({
            "order_id": event.order_id,
            "customer_id": event.customer_id,
            "status": "placed",
            "item_count": len(event.items),
            "total": sum(i["price"] * i["quantity"] for i in event.items),
            "placed_at": event.placed_at
        })
    
    async def handle_order_shipped(self, event: OrderShipped):
        await self.db.orders.update_one(
            {"order_id": event.order_id},
            {"$set": {"status": "shipped", "shipped_at": event.shipped_at}}
        )
```

### 5. Design Sagas/Process Managers

For cross-aggregate workflows, use sagas (see `saga-orchestration` skill):
- Each step produces events that trigger the next step
- Compensating actions handle failures
- Use correlation IDs for tracing across aggregates

### 6. Implement Snapshotting

For long-lived aggregates with many events:

```python
class SnapshotStore:
    async def save_snapshot(self, stream_id: str, state: dict, version: int):
        await self.snapshots.update_one(
            {"stream_id": stream_id},
            {"$set": {"state": state, "version": version}},
            upsert=True
        )
    
    async def load_aggregate(self, stream_id: str, events: List[Event]):
        snapshot = await self.snapshots.find_one({"stream_id": stream_id})
        if snapshot:
            # Replay only events after snapshot
            events_after = [e for e in events if e.version > snapshot["version"]]
            return Aggregate(snapshot["state"], events_after)
        return Aggregate.empty(events)
```

## Event Versioning Strategies

### Upcasting (Recommended)

```python
def upcast_event(event: dict) -> dict:
    """Transform old event format to current format."""
    if event["version"] == 1:
        # v1 didn't have currency field
        event["data"]["currency"] = "USD"  # default
        event["version"] = 2
    return event
```

### Parallel Streams

For breaking changes, create a new stream type and migrate gradually.

## Best Practices

### Do's

- **Events are facts** — never delete or modify them
- **Keep events small and focused** — one fact per event
- **Version events from day one** — plan for schema evolution
- **Design for eventual consistency** — accept read model lag
- **Use correlation IDs** — for tracing across services
- **Implement idempotent event handlers** — safe to reprocess
- **Plan for projection rebuilding** — projections are derived, can be rebuilt
- **Use durable execution for process managers** — frameworks like DBOS persist workflow state automatically

### Don'ts

- **Don't mutate or delete committed events** in production
- **Don't store large payloads** in events — keep them small
- **Don't skip optimistic concurrency** — prevents data corruption
- **Don't rebuild projections in production** without testing in staging first
- **Don't use event sourcing for simple CRUD** — the complexity isn't justified

## Technology Comparison

| Technology       | Best For                  | Limitations                      |
| ---------------- | ------------------------- | -------------------------------- |
| **EventStoreDB** | Pure event sourcing       | Single-purpose                   |
| **PostgreSQL**   | Existing Postgres stack   | Manual implementation            |
| **Kafka**        | High-throughput streaming | Not ideal for per-stream queries |
| **DynamoDB**     | Serverless, AWS-native    | Query limitations                |
| **Marten**       | .NET ecosystems           | .NET specific                    |

## Related Skills

- `saga-orchestration` — distributed transaction patterns with compensation
- `event-store-design` — event store implementation details
- `cqrs-implementation` — CQRS read/write model separation
- `projection-patterns` — building read models from event streams
- `workflow-orchestration` — Temporal-style durable workflow orchestration
