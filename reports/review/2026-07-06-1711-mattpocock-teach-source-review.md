---
type: Review Report
title: Matt Pocock Teach Source Review
description: Source Reviewer pass for the mattpocock/skills teach delta.
tags: [skills, review, source-review, mattpocock, teach, reference-only]
okf_version: "0.2"
status: complete
reviewed_at: 2026-07-06T17:11:00-03:00
---

# Matt Pocock Teach Source Review

## Role Selection

- Scheduled role: `Radar`
- Selected role: `Source Reviewer`
- Override reason: open review queue item `review-mattpocock-teach-delta-20260706` outranked broad discovery under the review gate.
- Missing-ledger initialization: not performed; today's status and queues existed.

## Inputs Inspected

Repository doctrine and state were inspected directly from `main` through the GitHub connector:

- `operations/daily/2026-07-06/status.json`
- `operations/daily/2026-07-06/queues.json`
- `operations/project-operator-prompt.md`
- `operations/aggregator-loop.md`
- `operations/operator-stability.md`
- `operations/action-runs/discover-skill-sources/README.md`
- `operations/action-runs/discover-skill-sources/latest.json` attempted and absent
- `operations/scheduler-online-scout-contract.md`
- `operations/manual-discovery-review-fallback.md`
- `sources/candidates/mattpocock-teach.md`
- `operations/source-watchlist.json`
- existing reviewed source-profile examples under `sources/reviewed/`

Upstream public source metadata was inspected through the GitHub connector:

- `mattpocock/skills` repository metadata
- `LICENSE`
- `skills/productivity/teach/SKILL.md`
- `CHANGELOG.md`

No repository was cloned, installed, imported, or executed.

## Evidence Summary

- Upstream repository is public and defaults to `main`.
- Upstream license file is MIT.
- The `teach` skill file exists under `skills/productivity/teach/SKILL.md`.
- The visible skill metadata names the skill `teach`, describes it as teaching a new skill or concept inside the current workspace, and disables model invocation.
- The visible skill behavior is stateful and workspace-oriented: mission, resources, reference artifacts, learning records, lessons, assets, and notes are treated as learning state.
- The upstream changelog records a `1.0.1` patch for `teach` that makes lessons reuse-first through reusable components in `./assets/`.

## Review Decision

Decision: `reference-only_with_normalizer_follow_up`.

The source is useful, licensed, and distinct enough from currently reviewed Matt Pocock entries to preserve as a reviewed source profile. The safe reusable value is a general teaching-loop doctrine, not the upstream text or templates.

## Normalization Candidate

Queue a Normalizer item for an original Architectonic playbook tentatively named `mission-grounded-learning-workspace`.

Useful original doctrine to normalize:

- capture the learner's mission before lesson design;
- preserve learning records and notes as durable state;
- create short lessons tied to one tangible win;
- maintain compact reference artifacts separately from lessons;
- reuse lesson components instead of duplicating ad hoc lesson code;
- require cited current sources for factual teaching;
- separate agent-teachable knowledge from real-world wisdom/community practice;
- bound all file writes to an explicit learning workspace.

## Risk Boundary

- Do not copy upstream prose, formats, examples, lesson templates, assets, component files, or skill bodies.
- Do not use this as permission to silently write files outside an explicit learning workspace.
- Do not treat interactive lesson assets as safe without separate static-vs-executable review.
- Do not claim guaranteed learning outcomes from pedagogy terms.
- Do not recommend current communities or classes without fresh verification.

## Queue Result

- Completed: `review-mattpocock-teach-delta-20260706`
- Created: `normalize-mission-grounded-learning-workspace-20260706`

## Value Delta

Converted a watched-source delta into a reviewed source profile with a clear license/provenance decision, explicit risk boundary, and a bounded normalization follow-up. This is not broad discovery and not content ingestion.