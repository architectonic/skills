---
type: RiskReview
title: Cloud SIEM with Sentinel Risk Review
date: 2026-07-09
status: done
board_ticket: skills-risk-review-cloud-siem-sentinel-001
---

# Cloud SIEM with Sentinel Risk Review

## Inspected state

- Repository: `architectonic/skills`
- Inspected ref: `main`
- Inspected SHA before this ticket's first content write: `3f241fbeeef473d67cbd189246d325cb42565f3d`
- Selected role: `Risk Auditor`
- Board ticket: `skills-risk-review-cloud-siem-sentinel-001`
- Model requirement status: `model_setting_unverified`
- External connector used: GitHub only
- Online/source discovery used: no

## Sources reviewed directly

- `operations/heartbeat.md`
- `operations/board.json`
- `operations/gates.md`
- `operations/value-ledger.json`
- `operations/daily/2026-07-09/status.json`
- `operations/daily/2026-07-09/queues.json`
- `operations/daily/2026-07-09/report.md`
- `operations/log.md`
- `reports/critic/2026-07-09-metadata-backfill-batch-005.md`
- `dist/skills/building-cloud-siem-with-sentinel/SKILL.md`

## Risk surfaces classified

The original package-facing skill included high-risk operational surfaces:

- Microsoft Sentinel / Log Analytics workspace provisioning.
- Azure CLI setup and data connector creation.
- AWS CloudTrail connector wiring with IAM role assumptions.
- KQL detections over identity, CloudTrail, object deletion, network flow, and threat-intelligence telemetry.
- Microsoft Threat Intelligence connector setup and indicator matching.
- Logic Apps / SOAR playbook JSON that performs account disablement.
- Scenario guidance that included automatic Azure AD account disablement and AWS STS revocation.

These surfaces are legitimate in an authorized security operations environment, but they are not safe as executable package-facing skill content.

## Remediation performed

Converted `dist/skills/building-cloud-siem-with-sentinel/SKILL.md` into a high-risk, requires-review defensive governance wrapper.

Metadata now marks the skill as:

- `domain: security-defensive`
- `risk_level: high`
- `requires_review: true`
- `source_status: existing_package_skill_risk_reviewed`
- `review_status: defensive_wrapper_only`

The rewritten skill preserves useful SIEM/SOAR governance guidance while removing package-facing operational snippets.

## Removed or redacted package-facing content

- Azure CLI provisioning commands.
- Sentinel onboarding and data connector commands.
- AWS connector configuration details.
- Production-style KQL detection and hunting queries.
- Threat-intelligence connector command snippets.
- Logic Apps JSON account-disable payload.
- Automatic account-disablement and STS-revocation scenario instructions.
- Example output claims that implied live automation metrics and auto-disabled accounts.

## Preserved safe guidance

- Authorized defensive use cases.
- Required review gate for authority, data handling, connector scope, detection impact, SOAR controls, and publication boundary.
- SIEM/SOAR planning workflow.
- Threat-intelligence data-handling cautions.
- SOAR action-tier model.
- Safe implementation handoff and review output format.

## Acceptance tests

| Test | Result | Evidence |
|---|---|---|
| Sentinel workspace provisioning, cloud connector setup, KQL detection, threat-intelligence matching, Logic Apps/SOAR, account-disable, and STS revocation surfaces are classified | Pass | All surfaces are named in this report and the skill safety classification. |
| Safe authorized SIEM/SOAR governance guidance is preserved or bounded | Pass | The rewritten skill keeps architecture, detection-governance, connector-governance, and SOAR-tier guidance without deployable commands. |
| Package-facing executable cloud setup and account-mutation snippets are review-gated, redacted, or removed | Pass | Azure CLI, KQL, Logic Apps JSON, threat-intelligence connector commands, and account/STSescalation instructions were removed. |
| Catalog refresh remains blocked until review completes | Pass | This ticket completes the risk review and opens catalog parity as the next ticket; catalog surfaces were not edited in this pass. |

## Boundaries preserved

- No online discovery or source review was performed.
- No repository was cloned.
- No Azure CLI, KQL, Logic Apps, Microsoft Graph, AWS connector, STS revocation, threat-intelligence connector, package, npm, registry, or publication action occurred.
- No third-party content was copied or normalized.
- No generated catalog files were hand-edited.

## Value delta

Removed the open Sentinel SIEM/SOAR risk blocker by converting a package-facing cloud setup and account-mutation playbook into a review-gated defensive governance wrapper.

## Next action

Run `skills-catalog-refresh-after-metadata-backfill-005` to verify catalog/install-manifest parity for the updated Sentinel skill before further metadata backlog cleanup.
