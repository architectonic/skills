---
type: Skill
title: Validation-Gated Skill Improvement
description: Use when improving an existing skill, playbook, runbook, or workflow entry so edits are bounded, tested against held-out tasks, and adopted only after evidence improves.
tags: [skill, skill-improvement, validation, self-improvement, review-gates, okf]
timestamp: 2026-07-06T13:13:00-03:00
okf_version: "0.2"
source_status: normalized
source_name: SkillOpt source-profile synthesis
source_url: https://github.com/microsoft/SkillOpt
source_profile: sources/reviewed/skillopt.md
license: MIT reference source; this normalized skill is original Architectonic procedure text
risk_level: medium
requires_review: true
---

# Validation-Gated Skill Improvement

## Trigger

Use this when an agent is asked to improve an existing reusable procedure, especially a skill, playbook, workflow, runbook, operating prompt, or scheduler instruction that will affect future work.

Do not use this for routine copyediting, one-off user writing, speculative refactors, or changes that cannot be evaluated against a concrete task.

## Inputs

- The current entry to improve.
- The intended runtime or repository context.
- A narrow improvement goal.
- At least one held-out task, prior failure, acceptance test, or review criterion that was not used to draft the edit.
- Any known safety, license, privacy, tool-use, or execution boundaries.
- A rollback target or previous commit reference.

## Procedure

1. State the improvement goal in one sentence.
2. Select the smallest useful edit shape: add, delete, replace, or split.
3. Define the validation gate before editing. The gate must include at least one concrete task, acceptance criterion, or prior failure that the revised entry should handle better.
4. Propose the edit as a bounded patch. Avoid broad rewrites unless the existing entry is structurally unusable.
5. Check the patch against the validation gate.
6. Check for regression against the entry's existing trigger, inputs, procedure, verification, and failure modes.
7. Record rejected edits when they reveal a useful boundary, unsafe shortcut, false assumption, or recurring failure mode.
8. Accept the edit only when the evidence improves utility, safety, or clarity without weakening the intended scope.
9. Record adoption explicitly: changed file, validation evidence, remaining uncertainty, rollback target, and follow-up queue item if catalog or packaging surfaces need refresh.

## Verification

A valid improvement pass has all of the following:

- The edit is smaller than the entry it improves unless a split/rewrite was explicitly justified.
- The validation gate was written before acceptance.
- The accepted edit is tied to a concrete task, prior failure, acceptance criterion, or review note.
- Rejected edits are retained when they teach a reusable boundary.
- The resulting entry still has trigger, inputs, procedure, verification, and failure modes.
- Any install-facing or distribution-facing changes create a catalog/package follow-up before publication.

## Failure Modes

- Optimizing wording without testing behavior.
- Accepting a change because it is longer, more detailed, or more impressive rather than measurably more useful.
- Using the same examples to draft and validate the edit.
- Letting the entry mutate itself during live task execution without review.
- Dropping rejected edits and losing negative evidence.
- Expanding scope until the skill becomes a doctrine essay or generic advice.
- Changing package or catalog surfaces without a refresh path.

## Boundaries

- Do not ingest private transcripts, user sessions, credentials, or hidden prompts as optimization data.
- Do not run third-party optimization tools from scheduler passes.
- Do not copy upstream benchmark tasks, result tables, examples, source code, or skill bodies into this repository.
- Do not claim a skill is improved unless the validation evidence supports that specific claim.

## Provenance Note

This skill was normalized from the reviewed `SkillOpt` source profile as an original Architectonic procedure. The reusable lesson is the validation discipline: bounded edits, held-out checks, rejected-edit memory, staged adoption, and explicit rollback context. It is not an import of upstream implementation, examples, benchmark data, or documentation.
