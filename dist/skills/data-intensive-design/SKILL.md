---
name: data-intensive-design
description: Distributed data system design from Martin Kleppmann's "Designing Data-Intensive Applications" — consistency, replication, partitioning, stream processing, and schema evolution as agent operating discipline.
tags: [software-development, data-intensive, kleppmann, distributed-systems, consistency, replication, partitioning, streams]
type: Playbook
---

# Data-Intensive Design

## When to Use

Apply for systems where correctness depends on data ownership, consistency, durability, replication, partitioning, schema evolution, event flow, replay, or derived-data maintenance.

## Core Principle

Do not design distributed data behavior as if every write, read, queue, cache, replica, clock, and downstream side effect were local, ordered, fresh, and exactly once.

## Decision Rules

1. **Make core trade-offs explicit** — Source of truth, consistency expectation, retry behavior, duplicate/reordered work, partial failure, data evolution, whether state is durable/cached/derived/ephemeral.
2. **Treat crashes, partial writes, duplicate work, timeouts, stale reads, and unknown downstream success as normal inputs** — Distinguish accepted, persisted, applied, and durable success.
3. **Describe load concretely** — Request rates, data volume, access patterns, latency, throughput, percentiles, bottlenecks, contention, tail behavior before changing architecture.
4. **Choose data models from access patterns** — Relationships, consistency needs, update locality, evolution pressure, whether data is primary or derived.
5. **Match storage engines to workload** — Write patterns, read patterns, range scans, recovery needs, write amplification, OLTP-vs-analytics separation.
6. **Derived data needs explicit propagation** — Indexes, caches, search copies, read models, materialized views, denormalized copies must have explicit ownership, lag, observability, repair, and rebuild paths.
7. **Define write semantics** — When a write is durable, when visible, whether stale reads allowed, which conflicts can happen, how conflicts detected/resolved.
8. **Make commands/jobs/events safe under retry and replay** — Deduplication keys, naturally idempotent transitions, or explicit transactional recovery contract.
9. **Preserve only the ordering business logic actually needs** — Scope per key/stream/partition/record/entity history. Keep ordering-sensitive logic close to that scope.
10. **Separate commands, events, durable logs, streams, materialized views** — Events describe facts; consumers must tolerate lag, duplicates, restart, replay, stable identifiers, versioned payloads.
11. **Design schemas/APIs/messages as evolving contracts** — Across old readers, old writers, old data, in-flight messages, rolling upgrades, cross-service formats.
12. **Partition by workload-relevant locality** — With hot-key, skew, routing, secondary-index, rebalancing, and cross-partition-operation costs explicit.
13. **Match transactions and isolation to invariants** — Make atomicity scope, commit behavior, recovery, reconciliation, lost-update, write-skew, phantom, and side-effect repair semantics explicit.
14. **Network delay, partitions, duplicate messages, stale leaders, timeouts, clock uncertainty are assumptions needing a fault model** — Not edge cases.
15. **Use linearizability, total order broadcast, atomic commit, consensus only where truly required** — The availability/latency cost must be acceptable.
16. **Batch and stream processing must be recomputable and recoverable** — Define inputs, outputs, intermediate state, checkpoints, external side effects, event time, processing time, windows, late data, joins, source-to-sink guarantees.
17. **Align service boundaries with data ownership and update semantics** — Do not casually split one tightly consistent business concept across services.

## Trigger Rules

- Changing a write path → state source of truth, consistency boundary, durability point, visibility point, downstream effects, rollback/repair path
- Adding/changing a cache/index/projection → define ownership, propagation, staleness, write cost, lag visibility, rebuild, repair
- Changing a schema/API/message/event → plan compatibility for old readers, old writers, old data, in-flight messages, rolling upgrades
- Adding retries/jobs/consumers/queues/CDC/stream processors → prove duplicate, replay, ordering, retention, side-effect, recovery safety
- Routing reads to replicas → identify read-your-writes, monotonic-read, consistent-prefix, staleness, failover expectations
- Partitioning data → test for locality, skew, hot keys, routing metadata, rebalancing cost, cross-partition coordination
- Choosing transaction isolation → map each anomaly to the invariant it can break
- Using timestamps/leases/locks/consensus → define clock assumption, quorum/session semantics, stale-authority behavior, fencing

## Final Checklist

- [ ] Source of truth and derived representations explicit?
- [ ] Consistency expectations, durability points, visibility points concrete?
- [ ] Retries, duplicate delivery, replay, reordering, timeouts handled?
- [ ] Schemas/APIs/messages evolve safely across mixed versions?
- [ ] Storage, indexing, replication, partitioning match actual workload?
- [ ] Transaction isolation and coordination protect named invariants?
- [ ] Events, logs, streams, batch jobs replayable or have repair paths?
- [ ] Service boundaries follow data ownership and update semantics?
- [ ] Lag, retries, failures, rebuilds, repair paths observable?
- [ ] No exactly-once wishful thinking or hidden distributed-system contracts?
