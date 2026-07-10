---
type: RiskReview
title: Phishing Reporting Button Workflow Risk Review
status: passed_risk_gated
date: 2026-07-09
board_ticket: skills-risk-review-phishing-reporting-button-workflow-001
selected_role: Risk Auditor
---

# Phishing Reporting Button Workflow Risk Review

## Decision

Converted `Building Phishing Reporting Button Workflow` into a high-risk, `requires_review: true`, defensive governance wrapper.

The skill remains useful for program design, approval routing, redaction policy, audit expectations, and human-review boundaries. It no longer exposes package-facing operational guidance for tenant administration, mailbox monitoring, external submissions, automated remediation, reporter notifications, or private-message handling.

## Evidence reviewed

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
- `dist/skills/building-phishing-reporting-button-workflow/SKILL.md`
- `reports/critic/2026-07-09-metadata-backfill-batch-010.md`

## Classified risk surfaces

- Email-suite administrative configuration for Microsoft 365, Google Workspace, or similar systems.
- SOAR monitoring of a dedicated reporting mailbox.
- User-submitted email contents, headers, URLs, attachments, sender data, recipients, and reporter identities.
- Indicator extraction from reported messages.
- URL, attachment, header, or message submission to VirusTotal, URLScan, sandbox, or reputation services.
- Automated classification with potential user, privacy, legal, or evidence-handling impact.
- Inbox retraction, message movement, sender/domain blocking, and other tenant-wide mailbox mutations.
- Reporter notifications and security-awareness metrics tied to individual users.

## Package-facing changes

Changed `dist/skills/building-phishing-reporting-button-workflow/SKILL.md` to:

- set `domain: security-defensive`;
- set `risk_level: high`;
- set `requires_review: true`;
- set `source_status: package_risk_reviewed`;
- preserve bounded defensive governance value;
- remove or review-gate package-facing deployment, mailbox monitoring, IOC extraction, external submission, remediation, and notification instructions.

## Boundaries preserved

No online discovery or external source review was performed. No third-party content was copied. No package, npm, registry, tenant, mailbox, SOAR, sandbox, reputation-service, or email-platform action was performed.

## Acceptance tests

| Test | Result | Evidence |
|---|---|---|
| Email-suite admin configuration and SOAR mailbox monitoring surfaces are classified | Pass | The review and rewritten skill classify tenant admin and mailbox monitoring as high-risk review-gated surfaces. |
| IOC extraction, URL/attachment submission, sandbox/reputation service, and private-data surfaces are classified | Pass | The review and rewritten skill explicitly classify these as blocked from package-facing guidance. |
| Automated inbox retraction, sender-domain blocking, message movement, and reporter notification actions are review-gated or removed | Pass | The rewritten skill blocks package-facing mutation and notification workflows and requires human review/change control. |
| Safe defensive reporting-program governance is preserved or bounded | Pass | The rewritten skill preserves governance checklists, approval routing, redaction rules, and audit expectations. |
| Catalog refresh remains blocked until review completes | Pass | This review completes the risk gate and opens catalog parity as the next required step before metadata/package endorsement. |

## Board effect

- `skills-risk-review-phishing-reporting-button-workflow-001`: done.
- `skills-catalog-refresh-after-metadata-backfill-010`: should be opened as the next ready catalog-parity gate.
- Package/publication remains blocked.

## Next action

Cataloger should consume `skills-catalog-refresh-after-metadata-backfill-010` and verify catalog/install-manifest parity for the rewritten high-risk skill.
