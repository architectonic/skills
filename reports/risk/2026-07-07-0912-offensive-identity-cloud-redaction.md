---
type: Risk Report
title: Offensive Identity Cloud Redaction
date: 2026-07-07
role: Risk Auditor
status: completed
---

# Offensive Identity Cloud Redaction

## Scope

Queue item: `risk-review-offensive-identity-cloud-skills-20260707`.

Inspected files:

- `dist/skills/attacking-entra-id-with-roadtools/SKILL.md`
- `dist/skills/attacking-oauth-with-device-code-phishing/SKILL.md`
- `dist/skills/auditing-entra-id-with-aadinternals/SKILL.md`

## Decision

The three package-facing entries contained live identity/cloud offensive procedure material. They are not safe as default installed skills in their prior form.

Risk decision:

- domain: `security-offensive`
- risk_level: `high`
- requires_review: `true`
- source_status: `blocked-pending-redaction`

## Action taken

Replaced each package-facing body with a review-gated defensive wrapper. The wrappers preserve the existence of the entry and provenance/license metadata while removing default executable procedure detail from the installed package surface.

## Boundary

No third-party repository was cloned, installed, imported, or executed. No external procedure content was copied. No live tenant commands were run. No generated catalog files were hand-edited.

## Follow-up

Created Cataloger queue item `catalog-refresh-after-identity-cloud-risk-redaction-20260707` because three `dist/skills/**/SKILL.md` files changed and generated catalog surfaces are stale until rebuilt or verified.
