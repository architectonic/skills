---
type: Source Profile
title: SkillOpt
description: Reviewed reference-only profile for Microsoft SkillOpt, a validation-gated framework for optimizing agent skill documents without model-weight training.
tags: [source-profile, skills, skill-optimization, validation-gates, agent-sleep, reference-only]
okf_version: "0.2"
source_url: https://github.com/microsoft/SkillOpt
source_name: SkillOpt
source_author: Microsoft
license: MIT
runtime_targets: [codex, claude, copilot, openclaw, generic-agent]
skill_format: trainable-skill-document-and-offline-sleep-cycle
risk_level: medium
ingestion_status: reference-only
reviewed_at: 2026-07-06
---

# SkillOpt

## What It Is

SkillOpt is a public Microsoft repository for optimizing agent skill documents while keeping model weights fixed. Its main claim is that a skill document can be treated as trainable state and improved by bounded text edits, scored rollouts, held-out validation, rejected-edit buffers, and staged acceptance.

The repository also ships SkillOpt-Sleep, a preview deployment-time companion that harvests agent transcripts, mines recurring tasks, replays tasks offline, consolidates bounded edits behind a validation gate, stages proposals, and requires adoption before the optimized skill becomes active.

## Why It Matters

This source is directly relevant to the Architectonic skills repository because it gives a concrete design vocabulary for safe skill improvement loops:

- optimize skill text rather than model weights;
- treat validation gates as mandatory safety rails, not optional polish;
- separate offline optimization from inference-time execution;
- keep rejected edits as evidence instead of silently discarding failure modes;
- stage learned skill changes for review/adoption before they affect future work.

The highest-value reusable lesson is not the upstream code. It is the doctrine: every self-improving skill loop needs a held-out gate, bounded edit surface, rollback/rejection memory, and explicit adoption step.

## Provenance

- Repository: `microsoft/SkillOpt`
- Default branch inspected: `main`
- README modified date observed by GitHub connector: `2026-07-02T14:11:10Z`
- Package metadata inspected: `pyproject.toml`, version `0.2.0`, Python `>=3.10`
- License file inspected directly: MIT, copyright Microsoft Corporation, 2026

## License

MIT license found in the repository license file. This permits reuse under the license terms, but this profile remains reference-only and does not copy upstream implementation, examples, benchmark data, or skill artifacts.

## Runtime Targets

Observed runtime/plugin surfaces include Claude Code, Codex, Copilot, Devin, OpenClaw, generic Python package/CLI usage, and multiple model backends. These are execution surfaces, not ingestion permission. Scheduler review must not install packages, run CLIs, execute benchmarks, harvest transcripts, or process local agent session history.

## Candidate Capabilities

Useful concepts for future normalization, if converted narrowly and with attribution:

1. Validation-gated skill editing: accept skill-document changes only when they improve held-out tasks.
2. Bounded edit budget: constrain optimizer edits to add/delete/replace patches rather than broad rewrites.
3. Rejected-edit memory: retain failed edit proposals as evidence for future optimization boundaries.
4. Offline sleep cycle: harvest recurring tasks, replay offline, consolidate proposals, then stage for review/adoption.
5. Headroom-aware optimization: expect larger gains where the target model/task has measurable room to improve.

## Risks

- Execution risk: the package exposes training, evaluation, web UI, and sleep-cycle CLIs. The Skills scheduler must not run these tools.
- Data risk: SkillOpt-Sleep can harvest local agent transcripts. This repository must not ingest private transcripts or user sessions.
- Benchmark risk: benchmark claims are useful as evidence pointers, but benchmark data, configs, and result tables should not be copied wholesale.
- Overclaim risk: upstream reports are single-seed in some places and scope-limited to recurring tasks with checkable correctness signals. Any normalized doctrine must preserve that limitation.
- Automation risk: ungated self-evolution can degrade behavior severely; the validation gate is the central safety boundary.

## Ingestion Decision

Decision: `reference-only`.

Rationale: SkillOpt is licensed and highly relevant, but the safe immediate value is a reviewed source profile and a narrow future normalization queue item. No code, benchmark data, prompts, skill artifacts, or upstream documentation should be copied into the package in this pass.

## Next Action

Queue a Normalizer pass to create a small original skill or playbook for validation-gated skill-improvement loops. The normalized artifact should teach the general procedure, boundaries, and failure modes without copying upstream prose or implementation.
