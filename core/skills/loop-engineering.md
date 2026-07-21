---
type: Skill
title: Loop Engineering
description: Use when agent work must recur across runs, schedules, workers, or handoffs with durable state, verification, budgets, and human-controlled stopping authority.
tags: [architectonic, core-skill, loops, agents]
source_status: native
source_name: Architectonic reviewed core
source_license: Apache-2.0
risk_level: medium
requires_review: true
status: reviewed
---

# Loop Engineering

## Trigger

Use when repeated or long-running work cannot be completed safely and economically in one bounded session.

## Inputs

The objective, value hypothesis, trigger, durable state, work queue, workers, verifier, approved tools and skills, budgets, mutation boundaries, human authority, evidence requirements, and stop conditions.

## Procedure

1. State the bounded objective and how verified value will be measured against cost and review burden.
2. Define the trigger or schedule and the durable state read at the start of every run.
3. Define how work is selected, claimed, isolated, and reconciled when several workers operate in parallel.
4. Separate worker and verifier responsibilities where independent checking adds value.
5. Bound tokens, money, time, tool calls, child-agent spawns, and external effects.
6. Require explicit authority for credentials, spending, production mutation, legal commitments, publication, or destructive action.
7. Record compact run evidence: objective, inputs, actions, outputs, verification, costs, failures, decisions, and next state.
8. Promote outputs into knowledge only after source and evidence rules are satisfied.
9. Stop, pause, escalate, or retire the loop when value, budget, confidence, authority, or safety conditions fail.

## Verification

- State survives independently of model context.
- No worker can exceed declared budgets or authority by spawning descendants.
- Verification checks outcomes rather than merely confirming file creation.
- Concurrent work has isolation and merge rules.
- A human can pause or stop the loop.
- Run evidence supports cost, failure, and value review.

## Failure Modes

- Infinite execution without a stop condition.
- Verifier theater or self-approval.
- Token burn caused by repeated rediscovery.
- Parallel agents mutating the same canonical artifact without coordination.
- Treating tool access as permission.
- Producing permanent reports that do not change future action.
