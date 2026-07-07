---
type: Risk Report
title: DPAPI Credential Access Redaction
date: 2026-07-07
role: Risk Auditor
status: completed
---

# DPAPI Credential Access Redaction

## Scope

Queue item: `risk-review-dpapi-credential-access-skill-20260707`.

Inspected file:

- `dist/skills/abusing-dpapi-for-credential-access/SKILL.md`

## Decision

The package-facing entry contained live credential-access procedure material, including copyable commands and operational steps for decrypting DPAPI-protected secrets. It is not safe as a default installed skill in that form.

Risk decision:

- domain: `security-offensive`
- risk_level: `high`
- requires_review: `true`
- source_status: `blocked-pending-redaction`

## Action taken

Replaced the package-facing body with a review-gated defensive wrapper. The wrapper preserves the existence of the entry and provenance/license metadata while removing default executable credential-access procedure detail from the installed package surface.

## Boundary

No third-party repository was cloned, installed, imported, or executed. No external procedure content was copied. No live host, domain, tenant, or network commands were run. No generated catalog files were hand-edited.

## Follow-up

Created Cataloger queue item `catalog-refresh-after-dpapi-credential-access-redaction-20260707` because one `dist/skills/**/SKILL.md` file changed and generated catalog surfaces are stale until rebuilt or verified.
