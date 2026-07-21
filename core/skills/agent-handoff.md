---
type: Skill
title: Agent Handoff
description: Use when another human or agent must resume unfinished work.
tags: [architectonic, core-skill]
source_status: native
source_name: Architectonic reviewed core
source_license: Apache-2.0
risk_level: low
requires_review: false
status: reviewed
---

# Agent Handoff

## Trigger

Use when another human or agent must resume unfinished work.

## Inputs

The relevant sources, task boundary, authority context, and intended durable output.

## Procedure

1. State the objective and current status.
2. Name canonical sources, decisions, changed files, and verification evidence.
3. Record blockers, unknowns, permissions, and next bounded action.
4. Exclude disposable chain-of-thought and stale narration.

## Verification

- A fresh worker can resume without reconstructing settled context or repeating completed work.

## Failure Modes

- Writing a narrative that omits source paths, decisions, or verification state.
