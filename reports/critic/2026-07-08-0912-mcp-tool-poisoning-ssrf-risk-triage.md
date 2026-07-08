# MCP Tool Poisoning / SSRF Risk Triage — 2026-07-08 09:12 -03:00

## Decision

Selected `Critic` instead of the 09 cadence `Normalizer` because the standing Critic metadata backlog is concrete, and the next directly inspected uncategorized package-facing skill is not safe for routine metadata classification.

## Inspected state

- Repository: `architectonic/skills`
- Inspected ref: `main`
- Inspected SHA: `a00d179bc21fbe8b4761367dae05c93b07a991b9`
- Daily ledger present: yes
- Missing-ledger initialization: no
- Discovery Action handoff: `operations/action-runs/discover-skill-sources/latest.json` absent on default branch
- Online searches used: none

## Files inspected directly

- `operations/project-operator-prompt.md`
- `operations/aggregator-loop.md`
- `operations/operator-stability.md`
- `operations/action-runs/discover-skill-sources/README.md`
- `operations/scheduler-online-scout-contract.md`
- `operations/manual-discovery-review-fallback.md`
- `operations/daily/2026-07-08/status.json`
- `operations/daily/2026-07-08/queues.json`
- `operations/log.md`
- `dist/catalog.json`
- `dist/skills/auditing-mcp-servers-for-tool-poisoning/SKILL.md`

## Candidate processed

`dist/skills/auditing-mcp-servers-for-tool-poisoning/SKILL.md`

## Finding

The entry is currently package-facing, uncategorized in `dist/catalog.json`, and lacks explicit frontmatter risk metadata. Its body includes defensive MCP security review value, but also includes live probing procedures for MCP configs and endpoints, SSRF target testing against internal/metadata/loopback targets, unauthenticated endpoint checks, and tool-description prompt-injection inspection.

That combination crosses the routine Critic metadata-backfill boundary. It should not be given a normal metadata endorsement until a Risk Auditor decides whether the package-facing body must be redacted into a review-gated defensive wrapper.

## Queue update

Created Risk Auditor queue item:

`risk-review-mcp-tool-poisoning-ssrf-skill-20260708`

## Boundaries preserved

- No third-party source was copied.
- No repository was cloned.
- No code or MCP server was executed.
- No generated catalog surface was hand-edited.
- No npm publication was attempted.

## Value-substance delta

Prevented a high-risk MCP/tool-poisoning and SSRF audit skill from receiving routine metadata classification or package endorsement before safety review. The reusable procedure preserved in this pass is the triage boundary: MCP security skills with live server probing, SSRF tests, unauthenticated endpoint checks, or prompt-injection payload inspection are routed to Risk Auditor before catalog/package endorsement.

## Next action

Risk Auditor should inspect `risk-review-mcp-tool-poisoning-ssrf-skill-20260708`, preserve defensive MCP audit value, and redact or wrap executable probing detail if needed before Cataloger refresh or publication/package work.
