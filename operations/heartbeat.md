# Skills heartbeat

Resolve and record the inspected SHA, read `operations/ledger.json`, gates, and
the selected item's sources, then consume one dependency-clear `ready` item.
Produce or verify its output, run acceptance checks, record evidence and one
transition, report directly, and stop. No eligible item means a clean stop with
no status, queue, value-ledger, or log write.

High-risk review and discovery repair outrank metadata cleanup. Publication and
external mutation require explicit authorization.
