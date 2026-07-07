# C2 / Red-Team Infrastructure Risk Triage

- Date: 2026-07-07
- Role: Critic
- Scheduled role: Risk Auditor
- Selected role: Critic
- Override reason: The hour cadence selected Risk Auditor, but `queues.risk` was empty and the concrete Critic metadata-quality backlog remained open. Critic inspection found uncategorized package-facing C2/red-team infrastructure entries with offensive procedure detail, so the correct action was to create a bounded Risk Auditor queue rather than perform routine metadata backfill.
- Inspected ref/SHA: `main` at `0fe1f73363252a56ecbb4aa4657fac42c20cb9f3`
- Action handoff: `operations/action-runs/discover-skill-sources/latest.json` returned 404 on the default branch.
- Online searches used: none.

## Files inspected directly

- `dist/skills/building-c2-infrastructure-with-sliver-framework/SKILL.md`
- `dist/skills/building-c2-redirector-infrastructure/SKILL.md`
- `dist/skills/building-red-team-c2-infrastructure-with-havoc/SKILL.md`
- `dist/catalog.json`
- `dist/catalog.md`
- `dist/install-manifest.json`
- today’s `operations/daily/2026-07-07/status.json` and `queues.json`
- required operations doctrine files

## Risk findings

### `building-c2-infrastructure-with-sliver-framework`

Decision: route to Risk Auditor before classification/package endorsement.

Reason: the installed package-facing entry is uncategorized/unspecified-risk in the catalog but contains concrete C2 listener, redirector, implant generation, post-exploitation, pivoting, and BOF procedure detail. This exceeds routine metadata backfill and should be converted to a high-risk review-gated defensive wrapper or explicitly blocked from default install endorsement.

### `building-c2-redirector-infrastructure`

Decision: route to Risk Auditor before classification/package endorsement.

Reason: the entry includes an authorized-use warning, but still exposes redirector build commands, filtering proxy rules, decoy diversion patterns, malleable-profile rule generation, TLS setup, and OPSEC controls on the package-facing surface. It should be reviewed as high-risk dual-use material before any catalog/package/publication endorsement.

### `building-red-team-c2-infrastructure-with-havoc`

Decision: route to Risk Auditor before classification/package endorsement.

Reason: the entry contains Havoc teamserver build/configuration steps, listener profile material, redirector configuration, payload generation, post-exploitation commands, credential-access commands, token manipulation, lateral movement, and pivoting. This is high-risk offensive detail and must not remain an uncategorized/unspecified-risk package entry.

## Queue created

Created `risk-review-c2-red-team-infrastructure-skills-20260707` for Risk Auditor.

## Boundaries observed

- No third-party content was copied.
- No external repository was cloned, installed, imported, or executed.
- No live C2, network, host, domain, cloud, credential, or payload command was run.
- No generated catalog files were hand-edited.
- No npm publication was attempted.

## Value-substance delta

Converted three uncategorized C2/red-team package-surface findings into an explicit high-priority risk decision and queue, preventing routine metadata classification or publication/package endorsement before safety review.
