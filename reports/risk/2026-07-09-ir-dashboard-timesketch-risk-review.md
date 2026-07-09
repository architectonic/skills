# IR Dashboard and Timesketch Risk Review

## Board ticket

- Ticket: `skills-risk-review-ir-dashboard-timesketch-001`
- Role: `Risk Auditor`
- Inspected ref/SHA: `main` at `051df1294ec1264d8f34237a9a630ebd755e33ba`
- External action allowed: false
- External action used: no

## Inputs reviewed

- `operations/heartbeat.md`
- `operations/board.json`
- `operations/gates.md`
- `operations/value-ledger.json`
- `operations/action-runs/discover-skill-sources/latest.json` attempted and absent
- `operations/daily/2026-07-09/status.json`
- `operations/daily/2026-07-09/queues.json`
- `operations/daily/2026-07-09/report.md`
- `operations/log.md`
- `dist/catalog.json`
- `dist/catalog.md`
- `dist/install-manifest.json`
- `reports/critic/2026-07-09-metadata-backfill-batch-008.md`
- `dist/skills/building-incident-response-dashboard/SKILL.md`
- `dist/skills/building-incident-timeline-with-timesketch/SKILL.md`

## Decision

Converted both package-facing skills into high-risk, `requires_review: true` defensive governance wrappers.

## Risk evidence classified

### Building Incident Response Dashboard

Classified and removed/re-gated package-facing material involving:

- active incident SIEM dashboard searches;
- live IOC handling;
- affected-system and analyst lookup data;
- scheduled searches;
- lookup table writes;
- dashboard data that can expose incident scope, response state, identities, hosts, or containment progress;
- any SOAR, endpoint, ticket, account, or incident-record mutation boundary.

The safe replacement preserves dashboard planning value: audience classification, field classification, aggregate metrics, redaction, read-only requirements, retention/export controls, and implementation boundaries.

### Building Incident Timeline with Timesketch

Classified and removed/re-gated package-facing material involving:

- Timesketch/OpenSearch/PostgreSQL/Redis/Celery/Plaso/Dissect deployment commands;
- disk image, event log, mounted image, browser history, cloud log, and endpoint-artifact ingestion;
- Sigma uploads and analyzer execution;
- API connection examples with username/password placeholders;
- event tagging, annotation, sketch/story mutation, export, and investigation-record mutation;
- private forensic evidence and regulated data handling.

The safe replacement preserves defensive forensic planning value: authorization, chain of custody, evidence classification, access model, redaction rules, retention/export controls, and synthetic-data timeline schema design.

## Files changed

- `dist/skills/building-incident-response-dashboard/SKILL.md`
- `dist/skills/building-incident-timeline-with-timesketch/SKILL.md`

No generated catalog, install manifest, package, npm, registry, or publication file was changed.

## Acceptance tests

| Test | Result | Evidence |
|---|---|---|
| Live incident/SIEM dashboard data, IOC handling, scheduled searches, and lookup mutation surfaces are classified | Pass | The dashboard skill is now high-risk/requires_review and explicitly blocks live SIEM queries, raw incident data, IOC publication, lookup writes, scheduled searches, SOAR, and account/device mutation. |
| Timesketch deployment, private forensic evidence ingestion, credential placeholders, API usage, and investigation-record mutation surfaces are classified | Pass | The Timesketch skill is now high-risk/requires_review and explicitly blocks deployment, evidence ingestion, credentialed API use, analyzer execution, investigation-record mutation, and private evidence examples. |
| Safe defensive IR dashboard and forensic timeline guidance is preserved or bounded | Pass | Both skills retain defensive planning workflows, data classification, redaction, authorization, access, retention, and approval checklists. |
| Package-facing executable or mutation snippets are review-gated, redacted, or removed | Pass | Executable Splunk/SIEM, Timesketch, Plaso, API, upload, ingestion, and mutation snippets were removed from package-facing content. |
| Catalog refresh remains blocked until review completes | Pass | This review completes the risk gate and queues catalog parity as the next ticket; generated catalog files were not hand-edited in this ticket. |

## Value delta

Removed the open IR dashboard/Timesketch package risk blocker while preserving safe defensive incident-dashboard and forensic-timeline planning guidance.

## Risk and publication state

- Risk queue: clear after this review.
- Catalog queue: open for `skills-catalog-refresh-after-metadata-backfill-008`.
- Discovery Action handoff: still absent.
- GitTaskBench: still watch/license-blocked.
- Remaining metadata backlog: open.
- Package/publication endorsement: still blocked.

## Next action

`Cataloger` should consume `skills-catalog-refresh-after-metadata-backfill-008`.
