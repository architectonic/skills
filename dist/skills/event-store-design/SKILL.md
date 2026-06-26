---
name: event-store-design
description: Design and implement event stores for event-sourced systems. Use when building event sourcing infrastructure, choosing event store technologies, or implementing event persistence patterns.
type: Playbook
---

# Event Store Design

Design and implement event stores for event-sourced applications.

## When to Use

- Designing event sourcing infrastructure
- Choosing between event store technologies
- Implementing custom event stores
- Optimizing event storage and retrieval
- Setting up event store schemas
- Planning for event store scaling

## When NOT to Use

- You're not using event sourcing
- A simple message queue suffices (use Kafka, RabbitMQ instead)

## Event Store Architecture

```
┌─────────────────────────────────────────────────────┐
│                    Event Store                       │
├─────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐ │
│  │   Stream 1   │  │   Stream 2   │  │   Stream 3   │ │
│  │ (Aggregate)  │  │ (Aggregate)  │  │ (Aggregate)  │ │
│  ├─────────────┤  ├─────────────┤  ├─────────────┤ │
│  │ Event 1     │  │ Event 1     │  │ Event 1     │ │
│  │ Event 2     │  │ Event 2     │  │ Event 2     │ │
│  │ Event 3     │  │ ...         │  │ Event 3     │ │
│  │ ...         │  │             │  │ Event 4     │ │
│  └─────────────┘  └─────────────┘  └─────────────┘ │
├─────────────────────────────────────────────────────┤
│  Global Position: 1 → 2 → 3 → 4 → 5 → 6 → ...     │
└─────────────────────────────────────────────────────┘
```

## Event Store Requirements

| Requirement       | Description                        |
| ----------------- | ---------------------------------- |
| **Append-only**   | Events are immutable, only appends |
| **Ordered**       | Per-stream and global ordering     |
| **Versioned**     | Optimistic concurrency control     |
| **Subscriptions** | Real-time event notifications      |
| **Idempotent**    | Handle duplicate writes safely     |

## Technology Comparison

| Technology       | Best For                  | Limitations                      |
| ---------------- | ------------------------- | -------------------------------- |
| **EventStoreDB** | Pure event sourcing       | Single-purpose                   |
| **PostgreSQL**   | Existing Postgres stack   | Manual implementation            |
| **Kafka**        | High-throughput streaming | Not ideal for per-stream queries |
| **DynamoDB**     | Serverless, AWS-native    | Query limitations                |
| **Marten**       | .NET ecosystems           | .NET specific                    |

## PostgreSQL Event Store Schema

```sql
-- Events table
CREATE TABLE events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    stream_id VARCHAR(255) NOT NULL,
    stream_type VARCHAR(255) NOT NULL,
    event_type VARCHAR(255) NOT NULL,
    event_data JSONB NOT NULL,
    metadata JSONB DEFAULT '{}',
    version BIGINT NOT NULL,
    global_position BIGSERIAL,
    created_at TIMESTAMPTZ DEFAULT NOW(),

    CONSTRAINT unique_stream_version UNIQUE (stream_id, version)
);

-- Indexes
CREATE INDEX idx_events_stream_id ON events(stream_id, version);
CREATE INDEX idx_events_global_position ON events(global_position);
CREATE INDEX idx_events_event_type ON events(event_type);
CREATE INDEX idx_events_created_at ON events(created_at);

-- Snapshots table
CREATE TABLE snapshots (
    stream_id VARCHAR(255) PRIMARY KEY,
    stream_type VARCHAR(255) NOT NULL,
    snapshot_data JSONB NOT NULL,
    version BIGINT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Subscriptions checkpoint table
CREATE TABLE subscription_checkpoints (
    subscription_id VARCHAR(255) PRIMARY KEY,
    last_position BIGINT NOT NULL DEFAULT 0,
    updated_at TIMESTAMPTZ DEFAULT NOW()
);
```

## Core Operations

### Append Events (with Optimistic Concurrency)

```python
async def append_events(self, stream_id, stream_type, events, expected_version=None):
    async with self.pool.acquire() as conn:
        async with conn.transaction():
            # Check expected version
            if expected_version is not None:
                current = await conn.fetchval(
                    "SELECT MAX(version) FROM events WHERE stream_id = $1",
                    stream_id
                )
                current = current or 0
                if current != expected_version:
                    raise ConcurrencyError(
                        f"Expected version {expected_version}, got {current}"
                    )
            
            # Insert events
            start_version = await conn.fetchval(
                "SELECT COALESCE(MAX(version), 0) + 1 FROM events WHERE stream_id = $1",
                stream_id
            )
            
            for i, event in enumerate(events):
                event.version = start_version + i
                await conn.execute(
                    """INSERT INTO events 
                    (id, stream_id, stream_type, event_type, event_data, metadata, version)
                    VALUES ($1, $2, $3, $4, $5, $6, $7)""",
                    event.event_id, stream_id, stream_type,
                    event.event_type, json.dumps(event.data),
                    json.dumps(event.metadata), event.version
                )
```

### Read Stream

```python
async def read_stream(self, stream_id, from_version=0, limit=1000):
    async with self.pool.acquire() as conn:
        rows = await conn.fetch(
            """SELECT * FROM events 
            WHERE stream_id = $1 AND version >= $2
            ORDER BY version LIMIT $3""",
            stream_id, from_version, limit
        )
        return [self._row_to_event(row) for row in rows]
```

### Subscribe (Catch-Up)

```python
async def subscribe(self, subscription_id, handler, from_position=0, batch_size=100):
    position = await self._get_checkpoint(subscription_id) or from_position
    
    while True:
        events = await self.read_all(position, batch_size)
        if not events:
            await asyncio.sleep(1)
            continue
        
        for event in events:
            await handler(event)
            position = event.global_position
        
        await self._save_checkpoint(subscription_id, position)
```

## DynamoDB Event Store

```python
class DynamoEventStore:
    def __init__(self, table_name: str):
        self.table = boto3.resource('dynamodb').Table(table_name)
    
    def append_events(self, stream_id, events, expected_version=None):
        with self.table.batch_writer() as batch:
            for i, event in enumerate(events):
                version = (expected_version or 0) + i + 1
                batch.put_item(Item={
                    'PK': f"STREAM#{stream_id}",
                    'SK': f"VERSION#{version:020d}",
                    'GSI1PK': 'EVENTS',
                    'GSI1SK': datetime.utcnow().isoformat(),
                    'event_type': event['type'],
                    'event_data': json.dumps(event['data']),
                    'version': version
                })
```

**Table design**: PK = `STREAM#{stream_id}`, SK = `VERSION#{version}`, GSI1 for global ordering.

## Best Practices

### Do's

- **Use stream IDs that include aggregate type** — `Order-{uuid}`
- **Include correlation/causation IDs** — for tracing
- **Version events from day one** — plan for schema evolution
- **Implement idempotency** — use event IDs for deduplication
- **Index appropriately** — for your query patterns
- **Use optimistic concurrency** — prevents data corruption

### Don'ts

- **Don't update or delete events** — they're immutable facts
- **Don't store large payloads** — keep events small
- **Don't skip optimistic concurrency** — prevents data corruption
- **Don't ignore backpressure** — handle slow consumers

## Related Skills

- `event-sourcing-architect` — event sourcing and CQRS patterns
- `saga-orchestration` — distributed transaction patterns
- `projection-patterns` — building read models from event streams
