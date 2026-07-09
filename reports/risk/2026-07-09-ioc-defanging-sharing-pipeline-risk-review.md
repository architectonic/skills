---
type: RiskReview
title: IOC Defanging and Sharing Pipeline Risk Review
date: 2026-07-09
status: complete
board_ticket: skills-risk-review-ioc-defanging-sharing-pipeline-001
---

# IOC Defanging and Sharing Pipeline Risk Review

## Scope

Board ticket: `skills-risk-review-ioc-defanging-sharing-pipeline-001`.

Selected role: `Risk Auditor`.

Inspected ref/SHA before first content write: `main` at `4908c0e60938e781fe95437b433141d380d61c85`.

## Files reviewed directly

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
- `dist/skills/building-ioc-defanging-and-sharing-pipeline/SKILL.md`
- `reports/critic/2026-07-09-metadata-backfill-batch-006.md`

## Risk findings

Direct file review found package-facing content that crossed the high-risk review gate:

- IOC extraction and normalization code handled malicious URLs, domains, IPs, email addresses, and file hashes.
- Refanging logic converted inert indicators back into active forms.
- STIX conversion generated machine-readable indicator bundles.
- MISP and TAXII distribution logic performed authenticated external submissions.
- API-key and credential parameters were present in package-facing examples.
- Validation criteria endorsed successful external distribution.

These surfaces can expose private incident evidence, activate malicious indicators, leak API credentials, or mutate external threat-intelligence systems. They must not be package-endorsed as routine metadata or executable implementation guidance.

## Remediation

Converted `dist/skills/building-ioc-defanging-and-sharing-pipeline/SKILL.md` into a high-risk, `requires_review: true`, defensive governance wrapper.

The revised skill preserves useful defensive guidance for:

- authorized IOC handling;
- safe defanging policy;
- review gates before sharing;
- TLP, confidence, retention, and audience controls;
- separation between analysis, approval, export, and audit.

The revised skill removes or blocks package-facing:

- executable IOC extractors and refanging routines;
- STIX bundle generation snippets for malicious indicators;
- MISP and TAXII client code;
- API-key, username, password, and token examples;
- authenticated external submission examples;
- automated sharing to partners, email, chat, SIEM, SOAR, blocklists, MISP, or TAXII;
- operational malicious indicator examples.

## Acceptance tests

| Test | Result | Evidence |
|---|---|---|
| IOC extraction/refanging/defanging and malicious indicator handling surfaces are classified | Pass | Risk findings identify IOC extraction, refanging, defanging, malicious URL/domain/IP/email/hash handling, and private-evidence concerns. |
| STIX/TAXII/MISP/API-key and external sharing/submission boundaries are classified | Pass | Risk findings and remediation classify STIX bundle generation, MISP/TAXII authenticated submission, API keys, credentials, and external mutation boundaries. |
| Safe defensive IOC handling guidance is preserved or bounded | Pass | Revised skill keeps defensive governance, review, TLP, confidence, audience, approval, and audit guidance. |
| Package-facing authenticated external submission snippets are review-gated, redacted, or removed | Pass | Revised skill omits executable submission code, credentials, connector calls, and automated distribution snippets. |
| Catalog refresh remains blocked until review completes | Pass | This review completes the blocker and leaves catalog parity for `skills-catalog-refresh-after-metadata-backfill-006`. |

## Boundaries preserved

- No online discovery or public source review was performed.
- No repository was cloned.
- No IOC extraction, refanging, STIX generation, MISP, TAXII, API-key, threat-intelligence feed, SIEM, SOAR, package, npm, registry, or publication action occurred.
- No third-party content was copied or normalized.
- No generated catalog file was hand-edited.

## Value delta

Removed the IOC defanging/sharing pipeline risk blocker while preserving safe defensive IOC handling governance.

## Next gate

`skills-catalog-refresh-after-metadata-backfill-006` should verify catalog/install-manifest parity after this risk review.
