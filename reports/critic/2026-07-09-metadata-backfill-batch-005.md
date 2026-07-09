---
type: CriticReport
title: Metadata Backfill Batch 005
date: 2026-07-09
status: blocked_for_risk_review
board_ticket: skills-metadata-backfill-batch-005
---

# Metadata Backfill Batch 005

## Inspected state

- Repository: `architectonic/skills`
- Inspected ref: `main`
- Inspected SHA before this ticket's first content write: `6560a5e0b259b0d369158aad50cd52830e74e626`
- Selected role: `Critic`
- Board ticket: `skills-metadata-backfill-batch-005`
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
- `dist/catalog.json`
- `dist/catalog.md`
- `dist/install-manifest.json`
- `reports/catalog/2026-07-09-metadata-backfill-004-catalog-parity.md`
- `dist/skills/building-cloud-siem-with-sentinel/SKILL.md`

## Candidate inspected

### `dist/skills/building-cloud-siem-with-sentinel/SKILL.md`

Current metadata:

- `name`: `Building Cloud SIEM with Sentinel`
- `description`: `This skill covers deploying Microsoft Sentinel as a cloud-native SIEM`
- `license`: `Apache-2.0`
- Current catalog domain: `uncategorized`
- Current catalog risk: `unspecified`

## Stop decision

Metadata-backfill batch 005 stopped on the first candidate instead of routine classifying it.

Reason: the skill is package-facing and includes high-risk operational cloud/SOAR surfaces:

- Azure subscription, Sentinel workspace, Log Analytics, and data-connector prerequisites.
- Azure CLI provisioning commands for Log Analytics workspaces and Sentinel data connectors.
- AWS CloudTrail connector configuration with an IAM role ARN placeholder.
- KQL detections over identity, CloudTrail, storage-deletion, network, and threat-intelligence telemetry.
- Logic Apps/SOAR JSON that disables Azure AD users through Microsoft Graph-style mutation.
- Threat-intelligence connector setup and indicator matching against network flow logs.
- Scenario guidance that includes automatic account disablement and AWS STS revocation.

This is not safe to pass through routine metadata cleanup. It needs a Risk Auditor pass to convert it into a bounded, authorized defensive SIEM/SOAR wrapper or quarantine unsafe operational snippets.

## Board action

Created next high-priority risk-review ticket:

- `skills-risk-review-cloud-siem-sentinel-001`

No skill file, generated catalog, package manifest, npm, registry, or publication surface was changed.

## Acceptance tests

| Test | Result | Evidence |
|---|---|---|
| Processes a bounded batch, not the entire catalog | Pass | Inspected the next uncategorized/unspecified package-facing candidate and stopped on the first unsafe surface. |
| Adds domain/risk/requires_review/source status when justified | Pass | No routine metadata was added because the candidate requires risk review first. |
| Stops and creates risk ticket on unsafe material | Pass | Created `skills-risk-review-cloud-siem-sentinel-001` for Sentinel provisioning, KQL detection, cloud connector, and SOAR account-disable surfaces. |
| Creates catalog refresh ticket after metadata changes | Pass | No catalog refresh ticket was created because no skill metadata changed in this pass. |

## Value delta

Prevented routine catalog endorsement of a package-facing Sentinel/SOAR skill that contains credentialed cloud setup and account-mutation automation. This converts a latent package risk into an explicit review queue item.

## Boundaries preserved

- No online discovery or source review was performed.
- No third-party content was copied or normalized.
- No repository was cloned.
- No commands, Azure CLI, KQL, Logic Apps, Microsoft Graph, DNS, malware tooling, browser automation, package, npm, registry, or publication action occurred.
- No generated catalog files were hand-edited.

## Next action

A `Risk Auditor` should consume `skills-risk-review-cloud-siem-sentinel-001` before any further metadata backlog cleanup or catalog/package endorsement.
