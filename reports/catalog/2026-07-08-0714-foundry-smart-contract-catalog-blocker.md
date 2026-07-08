# Cataloger Report — Foundry Smart Contract Catalog Blocker

- Date: 2026-07-08
- Role: Cataloger
- Scheduled role: Radar
- Inspected ref: `main`
- Inspected SHA: `afb311029679a14644febdd72e6c65f2aebf3c15`
- Model requirement status: `model_setting_unverified`

## Queue item

`catalog-refresh-after-foundry-smart-contract-metadata-backfill-20260708`

## Decision

Do not close the queue yet.

The package-facing skill file `dist/skills/auditing-foundry-smart-contract-security/SKILL.md` now carries explicit metadata:

- `domain: security-defensive`
- `risk_level: medium`
- `requires_review: true`
- `source_family: internal-skill-bundle`
- `source_status: adapted`

However, the generated catalog surfaces are still stale:

- `dist/catalog.json` summary still reports `security-defensive: 59`, `uncategorized: 565`, `medium: 432`, and `unspecified: 727`.
- `dist/catalog.json` still lists `Auditing Foundry Smart Contract Security` under `domains.uncategorized`.
- `dist/catalog.md` still mirrors the stale summary counts.
- `dist/install-manifest.json` remains structurally coherent, but it points installers at the stale catalog surfaces.

## Value-substance delta

This run prevented a false Cataloger close. It verified that the Foundry skill metadata edit is not yet reflected in generated catalog/install-facing surfaces, so package/publication endorsement remains blocked instead of silently shipping stale metadata.

## Required next action

Run or repair `npm run build:catalog` in a workflow/local environment that can regenerate `dist/catalog.json`, `dist/catalog.md`, and `dist/install-manifest.json`, then rerun Cataloger verification and close the queue only after the Foundry entry appears under `security-defensive` and the summary counts are updated.
