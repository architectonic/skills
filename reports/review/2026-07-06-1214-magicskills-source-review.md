---
type: Review Report
title: MagicSkills Source Review
description: Source Reviewer pass for Narwhal-Lab/MagicSkills.
tags: [skills, source-review, magicskills, skill-library, registry, reference-only]
okf_version: "0.2"
reviewed_at: 2026-07-06T12:14:00-03:00
source_url: https://github.com/Narwhal-Lab/MagicSkills
queue_item: review-magicskills-20260705-0711
selected_role: Source Reviewer
scheduled_role: Publisher
status: complete
---

# MagicSkills Source Review

## Decision

`reference-only_with_normalizer_follow_up`

MagicSkills is useful as a reference source for shared skill-library governance across multiple agent runtimes. It should not be installed, executed, copied, or treated as a package dependency by this repository from a scheduler pass.

## Why Source Reviewer Overrode Publisher

The noon cadence role was Publisher, but `queues.review` still had the open item `review-magicskills-20260705-0711`. The operator stability doctrine says open review pressure and safety outrank Radar/Publisher work. Source Reviewer therefore consumed the queue item before any broad publication activity.

## Evidence Inspected

- `Narwhal-Lab/MagicSkills` `README.md`
- `LICENSE`
- `pyproject.toml`
- `doc/cli.md`
- `doc/python-api.md`
- `src/magicskills/cli.py`

No repository was cloned. No package was installed. No code was executed. No upstream docs, examples, templates, images, command examples, implementation snippets, or skill bodies were copied into package surfaces.

## Useful Reusable Doctrine

The source contributes a practical skill-library governance pattern:

1. Keep a canonical physical skill pool.
2. Build named collections as runtime-specific working sets.
3. Sync into `AGENTS.md` only for document-driven agents.
4. Use CLI/Python dispatch only when the runtime needs tool/function integration.
5. Persist collection metadata as references rather than duplicating skill bodies.
6. Treat execution/upload/install capabilities as higher-risk than list/read/sync capabilities.
7. Require explicit path references when skill names collide.

## Risk Review

- License: MIT file inspected directly.
- Execution surface: `execskill` and `skill-tool` can execute commands or expose executable capabilities; blocked from scheduler use.
- Install surface: `install` can bring in local or Git repository skill content; blocked from this pass.
- Upload/account surface: upload flows can involve GitHub CLI/authentication and PR creation; blocked from scheduler use.
- Context mutation surface: `syncskills` can mutate `AGENTS.md`; any equivalent behavior in Architectonic must be review-gated.
- Provenance risk: shared registries can reference mutable local filesystem paths; normalized doctrine must require source/version/review metadata.

## Files Changed

- `sources/reviewed/magicskills.md`
- `reports/review/2026-07-06-1214-magicskills-source-review.md`
- `operations/daily/2026-07-06/queues.json`
- `operations/daily/2026-07-06/status.json`
- `operations/log.md`

## Follow-Up Queue

Create a Normalizer queue item for an original Architectonic playbook:

`normalize-shared-skill-library-governance-20260706`

The future normalized artifact should describe the shared-pool / named-collection / runtime-exposure pattern in original language, with explicit safety gates, verification, and failure modes. It must not copy upstream prose, code, examples, templates, or command documentation.
