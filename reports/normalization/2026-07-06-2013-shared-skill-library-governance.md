---
type: Normalization Report
title: Shared Skill Library Governance Normalization
status: complete
date: 2026-07-06
tags: [normalization, skills, governance, skill-library, magicskills]
okf_version: "0.2"
---

# Shared Skill Library Governance Normalization

## Role

Normalizer

## Queue Item

`normalize-shared-skill-library-governance-20260706`

## Source Profile

`sources/reviewed/magicskills.md`

## Decision

Created an original Architectonic skill:

- `skills/shared-skill-library-governance.md`

## Normalized Behavior

The new skill teaches a runtime-neutral governance procedure for shared skill libraries:

1. keep one canonical physical skill pool;
2. expose skills through named collections rather than broad implicit access;
3. distinguish runtime exposure surfaces such as instruction blocks, package manifests, tool descriptors, and installer catalogs;
4. separate trust levels for listing, reading, syncing, installing, and executing;
5. preserve provenance and review metadata in every surfaced entry;
6. require explicit canonical identifiers when skill names collide;
7. treat generated distribution copies as rebuildable outputs rather than authoring sources;
8. create catalog/package follow-up when canonical or distribution skill files change.

## Safety Boundary

No upstream prose, code, examples, templates, command documentation, package metadata, screenshots, skill bodies, or CLI behavior were copied.

No upstream repository was cloned, installed, imported, or executed.

The normalized entry remains `requires_review: true` with `risk_level: medium` because it describes runtime exposure and trust-boundary management.

## Follow-Up

Created Cataloger queue item:

`catalog-refresh-after-shared-skill-library-governance-20260706`

Reason: a new file under `skills/` makes `dist/skills/`, `dist/catalog.json`, `dist/catalog.md`, and package/install surfaces stale until refreshed or verified.
