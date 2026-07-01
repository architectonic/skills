---
type: Agent Instruction
title: Skills Agent Instructions
description: Rules for agents reading or modifying the reusable skill bundle and its loop-engineered aggregator operations.
tags: [agents, instructions, skills, okf, loop-engineering]
okf_version: "0.2"
status: draft
---

# Agent Instructions

## Scope

These instructions apply to agents working with this repository.

`skills` defines compact reusable procedures with trigger, inputs, procedure, verification, and failure modes.

It also acts as a living-knowledge aggregator for public skills, loops, workflows, runbooks, source profiles, and installable skill distributions.

It does not store private project memory, private user facts, runtime secrets, or unreviewed skill dumps.

## Read Order

1. Read `README.md`.
2. Read `START_HERE.md`.
3. Read `index.md`.
4. Read `doctrine/index.md`.
5. Read `doctrine/skill.md` before adding a skill.
6. Read `doctrine/ingestion-policy.md` before importing or adapting external skills.
7. Read `doctrine/normalization-pipeline.md` before normalizing public material.
8. Read `doctrine/okf-frontmatter.md` before editing frontmatter.
9. Read `operations/aggregator-loop.md` and `operations/project-operator-prompt.md` before running or editing scheduled aggregator behavior.
10. Read `operations/daily/README.md` before writing daily ledger or queue state.

## Core Rules

- A skill must teach a useful procedure.
- If it teaches nothing, remove it.
- A skill needs a clear trigger.
- A skill needs verification.
- A skill should name failure modes.
- Do not copy third-party content unless license, attribution, security, and usefulness are clear.
- Prefer distilled, summarized, or reference-only ingestion over mirroring.
- Runtime-specific exports are not canonical source.
- The aggregator must catalog broadly but normalize conservatively.
- Use queues before inventing work.
- Health, provenance, and risk review outrank growth.

## Before Writing

Before creating or editing a skill:

1. Verify the target repository and path.
2. Read the current file or nearest existing pattern.
3. Classify the material as skill, playbook, workflow, runbook, source profile, doctrine, operation, report, or temporary context.
4. Confirm trigger, inputs, procedure, verification, and failure modes.
5. Reject private facts, secrets, raw dumps, unlicensed material, and unreviewed risky instructions.
6. Make the smallest coherent change.
7. Read back the result.
8. Report changed paths and commit SHAs.

## Aggregator Writes

Before writing aggregator output:

1. Check `operations/daily/YYYY-MM-DD/status.json` and `queues.json` when present.
2. Prefer source profiles, candidate records, review notes, and catalog metadata over copied third-party content.
3. Preserve URL, author or organization, license, review date, runtime targets, risk level, and ingestion status.
4. Do not promote a candidate to normalized skill without a concrete trigger, procedure, verification method, and failure modes.
5. Rebuild or request rebuild of distribution catalog artifacts when `dist/skills/` changes.

## Completion Standard

A skill or aggregator change is complete only when:

1. the intended file was created or updated;
2. the content is compact and procedure-grounded;
3. the content has OKF-compatible frontmatter unless it is `index.md`, `log.md`, or a machine-readable JSON state file;
4. private or unsafe content was not introduced;
5. source, license, and review state are explicit where external material is involved;
6. the result was read back or otherwise verified.
