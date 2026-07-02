---
type: Report
title: Skills Packaging Plan — 2026-07-02
description: Packager pass notes for installability and package-surface coherence.
tags: [skills, packaging, installability, catalog, npx]
okf_version: "0.2"
status: active
---

# Skills Packaging Plan — 2026-07-02

## Selected Role

Packager.

## Selection Reason

Default 06 cadence selected Packager. The packaging queue was empty, but the repository still required a bounded installability check after discovery and review work introduced new operational state.

## Package Surface Checked

- `package.json`
- `bin/architectonic-skills.js`
- `dist/install-manifest.json`
- `dist/catalog.json`
- `dist/catalog.md`
- `reports/dist-skills-report.md`
- `reports/dist-skills-summary.json`
- `README.md` install instructions
- daily ledger and queues

## Findings

### Healthy surfaces

- `package.json` defines package `architectonic-skills` at version `0.1.2` with Apache-2.0 license.
- `package.json` exposes the CLI binary at `bin/architectonic-skills.js`.
- Package `files` includes `bin`, `README.md`, `index.md`, `doctrine`, `operations`, `dist`, and `scripts`.
- The CLI help points users to the shipped catalog and `dist/skills` bundle.
- `dist/install-manifest.json` declares `dist/skills` as the install root and lists `README.md`, `dist/catalog.json`, `dist/catalog.md`, and `dist/install-manifest.json` as discovery files.
- `README.md` documents `npx architectonic add skills` as the install surface.

### Packaging blocker

`dist/catalog.md` and `dist/catalog.json` disagree on install-facing catalog metrics:

- `dist/catalog.md` reports `Skill count: 1173`, `high: 2`, and `medium: 409`.
- `dist/catalog.json` reports `skill_count: 1170`, `high: 1`, and `medium: 407`.

This makes the human-readable package catalog stale or generated from a different source state than the machine-readable catalog. Because the current role is Packager and not Cataloger, this pass did not rebuild catalog artifacts. A Cataloger queue item was added instead.

## Package Status

Installability is mostly coherent, but package catalog surfaces are not fully trustworthy until `npm run build:catalog` reconciles `dist/catalog.json`, `dist/catalog.md`, `dist/install-manifest.json`, and related reports.

## Next Action

Cataloger should consume `catalog-reconcile-dist-catalog-surfaces-20260702` and rebuild or reconcile catalog artifacts before packaging/publication claims are treated as final.
