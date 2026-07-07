---
type: Critic Report
title: DPAPI Credential Access Risk Triage
date: 2026-07-07
tags: [skills, critic, risk, metadata-backfill, security-offensive]
okf_version: "0.2"
status: active
---

# DPAPI Credential Access Risk Triage

## Run

- Model requirement status: `model_setting_unverified`
- Inspected ref/SHA: `main` @ `faec7f531fa5236ed2298f7cf47c5ef91bc6915f`
- Scheduled role: Source Reviewer
- Selected role: Critic
- Override reason: the cadence selected Source Reviewer, but `queues.review` was empty and the open Critic queue `metadata-backfill-uncategorized-and-unspecified-risk-20260707` remained the concrete actionable queue.
- Missing-ledger initialization: not performed; both `operations/daily/2026-07-07/status.json` and `operations/daily/2026-07-07/queues.json` existed.
- Action handoff state: `operations/action-runs/discover-skill-sources/latest.json` was fetched and returned 404, so no Action handoff was available.
- Online searches used: none.

## Files inspected directly from default branch

- `operations/daily/2026-07-07/status.json`
- `operations/daily/2026-07-07/queues.json`
- `operations/project-operator-prompt.md`
- `operations/aggregator-loop.md`
- `operations/operator-stability.md`
- `operations/action-runs/discover-skill-sources/README.md`
- `operations/scheduler-online-scout-contract.md`
- `operations/manual-discovery-review-fallback.md`
- `operations/log.md`
- `reports/dist-skills-inventory.json`
- `dist/skills/a11y-audit/SKILL.md`
- `dist/skills/academic-research/SKILL.md`
- `dist/skills/acceptance-orchestrator/SKILL.md`
- `dist/skills/abusing-dpapi-for-credential-access/SKILL.md`

## Finding

The next bounded Critic inspection did not proceed with routine metadata backfill because `dist/skills/abusing-dpapi-for-credential-access/SKILL.md` is already marked `security-offensive`, `high`, and `requires_review`, but still contains default installed operational credential-access procedure detail.

This is a risk-quality blocker rather than a normal metadata-quality issue. It should be handled by Risk Auditor before further package/publication endorsement.

## Decision

Created risk queue item `risk-review-dpapi-credential-access-skill-20260707`.

Risk Auditor should decide whether to:

1. redact the package-facing body into a defensive, review-gated wrapper;
2. preserve only detection, authorization, audit, and defensive validation guidance;
3. keep the source as reference-only; or
4. block it from package endorsement.

## Value-substance delta

This pass converted a live high-risk package-facing offensive procedure into an explicit risk decision queue, preventing routine metadata cleanup from accidentally endorsing credential-access operational detail.

## Boundaries observed

- No third-party content was copied.
- No external repository was cloned, installed, imported, or executed.
- No generated catalog files were hand-edited.
- No npm publication was attempted.
