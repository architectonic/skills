---
type: Doctrine
title: Skill Doctrine
description: Definition and quality bar for compact, reusable, verifiable agent skills.
tags: [skills, procedures, verification, failure-modes, okf]
timestamp: 2026-06-26T00:00:00-03:00
okf_version: "0.1"
source_status: distilled
source_name: Agent Memory Ops Kit and private dogfood patterns
risk_level: low
---

# Skill Doctrine

A skill is a compact, reusable procedure that improves future agent behavior.

It teaches an agent how to do something, not merely what to know.

## Skill Structure

A useful skill has:

```text
trigger
inputs
procedure
verification
failure modes
```

## Trigger

The trigger defines when the skill applies.

A skill without a clear trigger is hard to route and should be rewritten or removed.

## Inputs

Inputs define what the agent must inspect, receive, or confirm before using the skill.

## Procedure

The procedure should be the smallest coherent ordered method.

If the method becomes a large workflow, split it into smaller skills or compose it in a playbook or agent loop.

## Verification

Verification defines how the agent knows the skill worked.

A skill that cannot be verified should not be promoted as reliable operational knowledge.

## Failure Modes

Failure modes define the errors this skill is meant to prevent or catch.

## Quality Bar

Keep a skill if it:

1. teaches a non-obvious procedure;
2. prevents a recurring failure;
3. improves source review, truth-finding, verification, or handoff quality;
4. reduces repeated human explanation;
5. helps an agent continue work faster or more safely.

Remove a skill if it:

1. repeats generic model knowledge;
2. is too vague to execute;
3. cannot be verified;
4. has no clear trigger;
5. belongs in doctrine, project templates, agents, or operator procedures instead.

## Failure Modes

This doctrine prevents:

```text
prompt-pack slop
generic advice masquerading as skill
unverifiable procedure libraries
skills becoming full agents
skills duplicating doctrine
```
