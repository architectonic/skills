---
type: Report
title: Catalog Plan 2026-07-02
description: Cataloger checkpoint for reconciling skill distribution catalog surfaces.
tags: [skills, catalog, dist, install-manifest, daily-ledger]
okf_version: "0.2"
status: active
---

# Catalog Plan — 2026-07-02

## Selected Role

Cataloger.

## Scheduled Role

Risk Auditor.

## Override Reason

The risk queue is empty, while two priority-1 catalog items remain open. Catalog drift and the uncataloged high-risk MCP local skill block Packager and Publisher work.

## Queue Item Inspected

`catalog-mcp-security-skill-20260702`

## Finding

The local high-risk skill exists at:

```text
skills/mcp-external-tool-security-review.md
```

It is not present in `dist/skills/`, `dist/catalog.json`, `dist/catalog.md`, `dist/install-manifest.json`, or the distribution reports.

The current catalog builder reads from:

```text
reports/dist-skills-enriched-inventory.json
dist/skills/**/SKILL.md
```

Because this run is operating through the GitHub connector rather than a checked-out working tree, it cannot execute:

```bash
npm run build:catalog
```

Hand-editing `dist/catalog.json` is not acceptable. It would risk corrupting a generated file with more than one thousand entries and would not prove that `dist/catalog.md`, `dist/install-manifest.json`, and reports agree.

## Decision

Do not hand-edit generated catalog surfaces.

Do not copy the MCP skill into `dist/skills/` without running or reproducing the full catalog builder, because that would increase drift rather than resolve it.

Keep catalog/package/publication blocked until a local or CI-backed Cataloger pass can run the builder and verify all install-facing surfaces together.

## Required Next Action

Run from a checked-out repository:

```bash
npm run build:catalog
```

Then verify:

```text
dist/catalog.json
dist/catalog.md
dist/install-manifest.json
reports/dist-skills-report.md
reports/dist-skills-summary.json
```

Expected checks:

- catalog skill count agrees across generated surfaces;
- high-risk count agrees across generated surfaces;
- `requires_review` count is computed and recorded in daily status;
- the MCP security skill is either represented in `dist/skills/` and catalog surfaces, or explicitly left canonical-only with a documented packaging decision;
- Packager and Publisher remain blocked until these checks pass.

## Follow-up Cataloger Checkpoint — 18:58

Selected role: Cataloger.

Scheduled role: Source Reviewer.

Override reason: priority-1 catalog drift and install-surface mismatch block Packager and Publisher; broad discovery remains inappropriate while catalog/package gates are unresolved. The remaining review item is lower priority than generated-surface reconciliation.

Queue item consumed: `catalog-reconcile-dist-catalog-surfaces-20260702`.

Inspected ref: `main`.

Inspected commit SHA: `db26a99d7905ffecc7849f2c7983f2b5e6ec89d7` from today's prior ledger; direct default-branch fetches for required files succeeded during this pass.

Finding: `package.json` defines `npm run build:catalog` as `python scripts/build_distribution_catalog.py`. The builder reads `reports/dist-skills-enriched-inventory.json` and `dist/skills/**/SKILL.md`, then writes `dist/catalog.json`, `dist/install-manifest.json`, and `dist/catalog.md` as a coupled generated set. A connector-only pass cannot execute that builder or prove generated-surface parity.

Decision: mark `catalog-reconcile-dist-catalog-surfaces-20260702` blocked with the same build-surface requirement. Do not hand-edit generated catalog files. Do not advance Packager or Publisher.

## Cataloger Checkpoint — 21:00

Selected role: Cataloger.

Scheduled role: Cataloger.

Override reason: none.

Queue item consumed: `maintenance-catalog-build-runner-20260702`.

Inspected ref: `main`.

Inspected commit SHA: `c296f24ee1b2659a11f8b1c5f56801032aff65b4`.

Finding: the repository had no existing `.github/workflows/build-catalog.yml` file when fetched directly. `package.json` exposes `npm run build:catalog`, and `scripts/build_distribution_catalog.py` writes `dist/catalog.json`, `dist/install-manifest.json`, and `dist/catalog.md` as a coupled generated set.

Action: added `.github/workflows/catalog-refresh.yml` with `workflow_dispatch` plus path triggers for `dist/skills/**`, `skills/**`, `reports/dist-skills-enriched-inventory.json`, `scripts/build_distribution_catalog.py`, and `package.json`. The workflow checks out the repository, installs `pyyaml`, runs `npm run build:catalog`, diffs the generated catalog surfaces, and commits refreshed `dist/catalog.json`, `dist/catalog.md`, and `dist/install-manifest.json` when changed.

Decision: mark `maintenance-catalog-build-runner-20260702` done. Keep catalog and package blockers open because this connector pass created the execution path but did not execute the workflow or verify generated-surface parity.

## Blockers

- `dist/catalog.json` and `dist/catalog.md` already disagree.
- The new high-risk MCP skill has not been distribution-cataloged.
- `catalog-mcp-security-skill-20260702` remains blocked until the catalog refresh workflow or a checked-out build runs and verifies generated outputs.
- `catalog-reconcile-dist-catalog-surfaces-20260702` remains blocked until the catalog refresh workflow or a checked-out build reconciles generated surfaces.
- Publication remains not ready.
