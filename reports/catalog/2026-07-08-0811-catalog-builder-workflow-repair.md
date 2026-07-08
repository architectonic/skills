# Catalog Builder Workflow Repair — 2026-07-08 08:11 BRT

## Role

Cataloger.

## Why Cataloger over scheduled Source Reviewer

The 08 São Paulo cadence selects Source Reviewer, but `catalog-refresh-after-foundry-smart-contract-metadata-backfill-20260708` is an open package-health queue item. Repo doctrine says catalog/package gates override discovery, source review, packaging, and publication until install-facing generated surfaces agree with package-facing skill metadata.

## Inspected state

- Inspected ref/SHA: `main` at `9c8e254a440e6164e0ec77f634e145f70ce59572`.
- Today's `status.json` and `queues.json` exist; missing-ledger initialization was not performed.
- `operations/action-runs/discover-skill-sources/latest.json` remains absent on the default branch.
- `dist/skills/auditing-foundry-smart-contract-security/SKILL.md` has updated package-facing metadata: `name: auditing-foundry-smart-contract-security`, `domain: security-defensive`, `risk_level: medium`, `requires_review: true`, `source_family: internal-skill-bundle`, `source_status: adapted`.
- `dist/catalog.json` remains stale before this repair: Foundry is still listed as `uncategorized`, with blank risk/source metadata.
- `dist/catalog.md` remains stale before this repair: `security-defensive: 59`, `uncategorized: 565`, `medium: 432`, `unspecified: 727`.

## Repair performed

Added `.github/workflows/build-catalog.yml` as a deterministic repository-side catalog producer.

The workflow:

1. runs on `workflow_dispatch` and on pushes that affect the catalog builder, `dist/skills/**`, or the enriched inventory;
2. installs `pyyaml` for `scripts/build_distribution_catalog.py`;
3. runs `npm run build:catalog`;
4. validates the Foundry metadata drift specifically while this queue is open;
5. commits only `dist/catalog.json`, `dist/catalog.md`, and `dist/install-manifest.json` when they change.

## Boundary decisions

- Did not hand-edit `dist/catalog.json`; it is a generated file and too large to safely patch piecemeal through the connector.
- Did not normalize, discover, review, package, or publish anything.
- Did not copy third-party content, clone external repositories, install candidate code, or execute untrusted material.

## Queue decision

The Cataloger queue remains open until a later Cataloger pass directly verifies that the workflow refreshed `dist/catalog.json`, `dist/catalog.md`, and `dist/install-manifest.json` on the default branch.

## Concrete value-substance delta

Converted a repeated catalog-staleness blocker into a deterministic GitHub Actions repair surface that can regenerate and validate package-facing catalog metadata after `dist/skills/**` changes. This is more valuable than another status-only blocker report because it creates the missing producer path required by the repo doctrine.
