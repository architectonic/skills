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

## Blockers

- No checked-out repository or package execution surface was available in this connector-only run.
- `dist/catalog.json` and `dist/catalog.md` already disagree.
- The new high-risk MCP skill has not been distribution-cataloged.
- Publication remains not ready.
