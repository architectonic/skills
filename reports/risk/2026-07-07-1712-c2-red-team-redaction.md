# High-Risk Security Entry Redaction

- Date: 2026-07-07
- Role: Risk Auditor
- Scheduled role: Radar
- Selected role: Risk Auditor
- Override reason: The hour cadence selected Radar, but `queues.risk` contained the open high-priority item `risk-review-c2-red-team-infrastructure-skills-20260707`. Safety review overrides discovery and growth work.
- Inspected ref/SHA: `main` at `7eba28f61caabbfd8e22ef694387c8bb0050e1f0`
- Action handoff: `operations/action-runs/discover-skill-sources/latest.json` returned 404 on the default branch.
- Online searches used: none.

## Files inspected directly

- `operations/daily/2026-07-07/status.json`
- `operations/daily/2026-07-07/queues.json`
- `operations/project-operator-prompt.md`
- `operations/aggregator-loop.md`
- `operations/operator-stability.md`
- `operations/action-runs/discover-skill-sources/README.md`
- `operations/scheduler-online-scout-contract.md`
- `operations/manual-discovery-review-fallback.md`
- `operations/log.md`
- `reports/critic/2026-07-07-1614-c2-red-team-risk-triage.md`
- `dist/skills/building-c2-infrastructure-with-sliver-framework/SKILL.md`
- `dist/skills/building-c2-redirector-infrastructure/SKILL.md`
- `dist/skills/building-red-team-c2-infrastructure-with-havoc/SKILL.md`

## Risk decision

The three package-facing entries contained high-risk dual-use operational material that should not be installed as reusable default skills. The risk queue was consumed by replacing the three package-facing bodies with high-risk, review-gated safety placeholders.

## Entries changed

- `dist/skills/building-c2-infrastructure-with-sliver-framework/SKILL.md`
- `dist/skills/building-c2-redirector-infrastructure/SKILL.md`
- `dist/skills/building-red-team-c2-infrastructure-with-havoc/SKILL.md`

Each entry now preserves title, provenance/license metadata, high-risk classification, `requires_review: true`, and a defensive review boundary. Operational instructions, commands, configuration examples, and procedure bodies were removed from the default package surface.

## Queue outcome

- Resolved: `risk-review-c2-red-team-infrastructure-skills-20260707`
- Created: `catalog-refresh-after-c2-red-team-redaction-20260707`

## Boundaries observed

- No third-party content was copied.
- No external repository was cloned, installed, imported, or executed.
- No live host, domain, account, cloud, network, credential, or security action was run.
- No generated catalog files were hand-edited.
- No npm publication was attempted.

## Value-substance delta

Removed high-risk operational procedure bodies from three default installed package-facing security entries and replaced them with review-gated safety placeholders, preventing accidental package/publication endorsement until Cataloger verifies generated surfaces.
