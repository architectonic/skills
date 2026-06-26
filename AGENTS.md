---
type: Agent Instruction
title: Skills Agent Instructions
description: Rules for agents reading or modifying the reusable skill bundle.
tags: [agents, instructions, skills, okf]
okf_version: "0.1"
status: draft
---

# Agent Instructions

## Scope

These instructions apply to agents working with this repository.

`skills` defines compact reusable procedures with trigger, inputs, procedure, verification, and failure modes.

It does not store private project memory, private user facts, runtime secrets, or unreviewed skill dumps.

## Read Order

1. Read `README.md`.
2. Read `START_HERE.md`.
3. Read `index.md`.
4. Read `doctrine/index.md`.
5. Read `doctrine/skill.md` before adding a skill.
6. Read `doctrine/ingestion-policy.md` before importing or adapting external skills.
7. Read `doctrine/okf-frontmatter.md` before editing frontmatter.

## Core Rules

- A skill must teach a useful procedure.
- If it teaches nothing, remove it.
- A skill needs a clear trigger.
- A skill needs verification.
- A skill should name failure modes.
- Do not copy third-party content unless license, attribution, security, and usefulness are clear.
- Prefer distilled, summarized, or reference-only ingestion over mirroring.
- Runtime-specific exports are not canonical source.

## Before Writing

Before creating or editing a skill:

1. Verify the target repository and path.
2. Read the current file or nearest existing pattern.
3. Classify the material as skill, playbook, workflow, runbook, source profile, doctrine, or temporary context.
4. Confirm trigger, inputs, procedure, verification, and failure modes.
5. Reject private facts, secrets, raw dumps, unlicensed material, and unreviewed risky instructions.
6. Make the smallest coherent change.
7. Read back the result.
8. Report changed paths and commit SHAs.

## Completion Standard

A skill change is complete only when:

1. the intended file was created or updated;
2. the content is compact and procedure-grounded;
3. the content has OKF-compatible frontmatter unless it is `index.md` or `log.md`;
4. private or unsafe content was not introduced;
5. the result was read back or otherwise verified.
