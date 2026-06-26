---
type: Entry Point
title: Start Here
description: First-run traversal guide for agents using the reusable skill bundle.
tags: [start-here, skills, procedures, okf]
okf_version: "0.1"
status: draft
---

# Start Here

This is the first-run guide for agents reading `skills`.

## First Run

1. Read `AGENTS.md` for repository rules.
2. Read `README.md` for package purpose and boundaries.
3. Read `index.md` for progressive disclosure.
4. Read `doctrine/index.md` for available doctrine concepts.
5. Read `doctrine/skill.md` before using or adding skills.
6. Read `doctrine/okf-frontmatter.md` before editing metadata.
7. Read `doctrine/ingestion-policy.md` and `doctrine/normalization-pipeline.md` before importing external material.

## Skill Test

A skill belongs only if it changes future agent behavior in a useful way.

Keep a skill if it teaches a non-obvious procedure, prevents recurring failure, improves truth-finding or verification, reduces repeated explanation, or improves handoff continuity.

Remove a skill if it repeats generic model knowledge, has no clear trigger, cannot be verified, or belongs in doctrine, project templates, agents, or operator procedures instead.

## Canonical Loop

```text
Read → Classify → Inspect → Plan → Act → Verify → Reconcile → Handoff
```

Use this loop for all durable changes.
