---
name: skills-upkeep
description: Maintain the skills layer so reusable procedures stay normalized, categorized, source-aware, packageable, and safe for progressive discovery.
tags: [agent-operations, upkeep, skills, curation, packaging, distribution, okf]
type: Playbook
---

# skills-upkeep

## Purpose

Keep the skills repository healthy as a reusable procedural library rather than a pile of partially normalized imports.

## Trigger

Use this skill when:
- new skills are ingested or existing skills are normalized
- categories, tags, or risk metadata drift
- packaging and distribution manifests need refresh
- overlapping or stale skills make discovery harder

## Inputs

- the current skills corpus and distribution manifests
- enrichment reports, quality-gate reports, and source metadata
- known licensing or provenance information
- current packaging expectations for GitHub and installer consumption

## Procedure

1. Inventory the current skill corpus and refresh metadata reports.
2. Normalize frontmatter, titles, descriptions, tags, and risk markers where the source supports it.
3. Check categorization and discovery quality. A large library must be progressively discoverable, not only technically present.
4. Review provenance and license signals. Unknown or incompatible origin should block promotion to a trusted distributable surface.
5. Detect overlap, low-signal entries, and stale procedural residue. Merge, quarantine, rewrite, or prune as needed.
6. Refresh packaging artifacts such as catalogs, install manifests, and bundle documentation.
7. Verify that install units remain directory-based and machine-discoverable for downstream runtimes.

## Verification

- the corpus is normalized enough for consistent discovery and installation
- metadata and category counts match the generated distribution artifacts
- high-risk skills are clearly marked and not silently auto-promoted
- packaging manifests regenerate cleanly from the current library state

## Failure Modes

- the library grows faster than discovery quality
- categorization drifts from actual content
- provenance and licensing remain too vague for safe distribution
- packaging docs and machine manifests diverge from the real corpus
