---
type: Catalog Verification
title: DPAPI Credential Access Redaction Catalog Verification
description: Verifies package catalog surfaces after review-gated DPAPI credential-access redaction.
tags: [skills, catalog, package-health, dpapi, risk-review]
okf_version: "0.2"
status: complete
---

# DPAPI Credential Access Redaction Catalog Verification

## Scope

Cataloger pass for `catalog-refresh-after-dpapi-credential-access-redaction-20260707`.

## Inspected state

- Repository: `architectonic/skills`
- Inspected ref: `main`
- Inspected SHA: `c2487f92125c20be8b106d2833c0fbd61796b8c9`
- Model requirement status: `model_setting_unverified`
- Missing-ledger initialization: not performed
- Action handoff: `operations/action-runs/discover-skill-sources/latest.json` is absent on the default branch

## Files inspected directly

- `operations/project-operator-prompt.md`
- `operations/aggregator-loop.md`
- `operations/operator-stability.md`
- `operations/action-runs/discover-skill-sources/README.md`
- `operations/scheduler-online-scout-contract.md`
- `operations/manual-discovery-review-fallback.md`
- `operations/daily/2026-07-07/status.json`
- `operations/daily/2026-07-07/queues.json`
- `operations/log.md`
- `dist/catalog.json`
- `dist/catalog.md`
- `dist/install-manifest.json`
- `dist/skills/abusing-dpapi-for-credential-access/SKILL.md`

## Verification

The DPAPI package-facing skill now has review-gated high-risk metadata and a defensive wrapper body:

- `name`: `abusing-dpapi-for-credential-access`
- `domain`: `security-offensive`
- `risk_level`: `high`
- `requires_review`: `true`
- `source_status`: `blocked-pending-redaction`

Generated package surfaces were checked directly from the default branch:

- `dist/catalog.json`: 1182 skills, 9 `security-offensive`, 575 `uncategorized`, 6 `high`, 427 `medium`, 740 `unspecified`
- `dist/catalog.md`: same headline counts as `dist/catalog.json`
- `dist/install-manifest.json`: coherent installer entrypoints and selection fields

The catalog still lists `abusing-dpapi-for-credential-access` under `security-offensive`, and the package-facing skill body no longer exposes default executable credential-access procedure detail. No generated catalog files were hand-edited in this pass.

## Queue decision

Closed `catalog-refresh-after-dpapi-credential-access-redaction-20260707`.

## Package / npm status

Catalog surfaces are verified after the DPAPI redaction. No npm publish was performed. Publication remains blocked by the open Critic metadata backlog and absent discovery Action handoff.

## Value-substance delta

Removed a package-health blocker by verifying that the high-risk DPAPI credential-access redaction is reflected by the package-facing skill and compatible catalog/install surfaces, allowing the loop to return to bounded Critic metadata cleanup next.
