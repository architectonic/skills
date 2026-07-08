# Skills Heartbeat Protocol

## Operator loop

Every scheduled Skills heartbeat must:

1. Resolve `architectonic/skills` through GitHub.
2. Fetch exact default-branch state and record inspected ref/SHA.
3. Fetch `operations/board.json`, `operations/gates.md`, today's daily status/queues, `operations/log.md`, discovery handoff if present, catalog surfaces, and relevant ticket inputs.
4. Select the highest-priority `ready` board ticket allowed by `operations/gates.md`.
5. Produce the ticket output artifact or mark the ticket blocked/killed with evidence.
6. Run ticket acceptance tests.
7. Update `operations/board.json` ticket status and next ticket state.
8. Append one value event to `operations/value-ledger.json`.
9. Update today's status/report/log with concise evidence.
10. Report inspected SHA, ticket consumed, sources/files reviewed, files changed, commit SHA, value delta, blockers, and next ticket.

## Anti-slop rule

If the run only changes status, report, or queue files, it must mark itself `low_value_status_only` unless it removed a risk blocker, restored discovery, repaired catalog parity, or promoted/killed a board ticket.

## Current priority

```text
skills-restore-discovery-handoff-001
skills-risk-review-mcp-tool-poisoning-001
skills-catalog-refresh-after-risk-review-001
skills-metadata-backfill-batch-001
```

Discovery restoration and high-risk review outrank routine metadata cleanup.
