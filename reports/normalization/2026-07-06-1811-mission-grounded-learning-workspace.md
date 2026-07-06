---
type: Normalization Report
title: Mission-Grounded Learning Workspace Normalization
status: completed
date: 2026-07-06
tags: [normalization, teaching, learning-workspace, source-profile, agent-operations]
okf_version: "0.2"
---

# Mission-Grounded Learning Workspace Normalization

## Role

Normalizer

## Scheduled Role

Source Reviewer

## Override Reason

The 18:00 São Paulo cadence selected Source Reviewer, but today's review queue is clear and `normalize-mission-grounded-learning-workspace-20260706` is the highest-priority concrete open queue item. Queue pressure and the consume-concrete-work rule justify Normalizer for this pass.

## Source Profile

- Source profile: `sources/reviewed/mattpocock-teach.md`
- Source URL: `https://github.com/mattpocock/skills/tree/main/skills/productivity/teach`
- Review decision: `reference-only_with_normalizer_follow_up`
- Normalization queue item: `normalize-mission-grounded-learning-workspace-20260706`

## Work Performed

Created original Architectonic skill:

```text
skills/mission-grounded-learning-workspace.md
```

The skill defines a runtime-neutral procedure for turning a learner's concrete mission into a durable, workspace-scoped learning loop with:

- learner mission capture;
- explicit workspace write boundary;
- compact learning ledger;
- source notes, short lessons, reference sheets, and practice records;
- current-source verification for factual teaching;
- practice-backed lesson design;
- reusable artifact boundaries;
- explicit failure modes and safety boundaries.

## Boundary Check

No upstream prose, templates, lesson examples, format files, assets, component files, command documentation, skill bodies, package metadata, scripts, or repository code were copied.

No upstream repository was cloned, installed, imported, or executed.

The normalized output is original procedure text derived from the reviewed source profile's abstract operating pattern.

## Queue Impact

Closed:

```text
normalize-mission-grounded-learning-workspace-20260706
```

Created:

```text
catalog-refresh-after-mission-grounded-learning-workspace-20260706
```

The catalog queue is required because a new file under `skills/` makes install/catalog surfaces stale until `dist/skills/`, `dist/catalog.json`, `dist/catalog.md`, and `dist/install-manifest.json` are refreshed or verified.

## Catalog / Package / NPM Status

Package publication is not endorsed after this pass.

Reason: a new source skill was added under `skills/`, but no distribution copy or catalog rebuild occurred in this Normalizer pass. Cataloger must repair or verify distribution surfaces before package/publication work.

## Value-Substance Delta

Converted a reviewed reference-only teaching source into an original Architectonic skill that teaches non-default agent behavior: mission-first lesson planning, durable learning-state management, source-aware factual teaching, explicit workspace-write boundaries, practice-backed verification, reusable artifact boundaries, and failure-mode control.
