# Skills operator stability

- Validate `operations/ledger.json` before autonomous selection.
- Select only dependency-clear `ready` items allowed by `operations/gates.md`.
- Reconcile stale claims against source evidence before reassignment.
- Missing or malformed ledger state blocks autonomous work; it does not trigger
  daily-state initialization.
- Catalog, provenance, license, privacy, and risk evidence outrank throughput.
- No eligible item means a clean stop.
