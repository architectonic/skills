---
type: Entry Point
title: skills
description: Runtime-neutral package for compact, reusable, verifiable procedures that improve human-agent collaboration.
tags: [skills, procedures, verification, failure-modes, agents, okf]
okf_version: "0.1"
status: draft
---

# skills

`skills` is the reusable procedure package for an Architectonic constitution.

Install it with:

```bash
npx architectonic add skills
```

It defines compact procedures that help agents perform specific kinds of work better, safer, faster, or with fewer repeated failures.

This repository is not a prompt pack, a private memory vault, a project-specific playbook, or a runtime-specific skill dump. It should contain only skills that teach a useful procedure an agent would not reliably perform by default.

## Purpose

A skill exists to improve future agent behavior.

A useful skill helps an agent:

```text
find truth
review sources
clarify intent
avoid false inference
execute a recurring workflow
verify work
record decisions
write useful handoffs
prevent known failure modes
resume work faster
```

A skill should not exist merely because a category exists.

If it teaches nothing, remove it.

## What a skill is

A skill is a compact, reusable procedure with:

```text
trigger        # when the skill applies
inputs         # what the agent needs before using it
procedure      # the ordered method
verification   # how success is checked
failure modes  # what errors the skill is meant to prevent
```

A skill is not:

```text
a doctrine essay
a full agent
a private project note
a generic tip
a tool wrapper without reasoning value
a decorative instruction file
a large workflow that should be a playbook, living-knowledge campaign, or agent loop
```

In the constitutional vocabulary, `skills` operationalizes Technē: reusable craft and procedure. Skill success is not truth; knowledge claims still belong in the knowledge layer.

## Base skill format

```md
---
type: Skill
title: Skill Name
description: One sentence explaining what this skill helps an agent do.
tags: [skill, okf]
timestamp: 2026-06-26T00:00:00-03:00
risk_level: low
---

# Skill Name

## Trigger

When this skill should be used.

## Inputs

What the agent must inspect, receive, or confirm before using it.

## Procedure

The smallest coherent ordered procedure.

## Verification

How the agent knows the procedure worked.

## Failure Modes

What this skill prevents or catches.
```
