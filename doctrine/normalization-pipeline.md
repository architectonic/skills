---
type: Workflow
title: Skill Normalization Pipeline
description: Workflow for converting public agent skills, workflows, and runbooks into reviewed OKF-compatible entries.
tags: [skills, okf, normalization, workflow, provenance]
timestamp: 2026-06-26T00:00:00-03:00
okf_version: "0.1"
source_status: distilled
source_name: Agent Memory Ops Kit OKF pipeline
risk_level: low
---

# Skill Normalization Pipeline

Use this workflow when adding public agent knowledge to a skill bundle.

## Steps

1. Discover public sources from repositories, official docs, marketplaces, posts, or videos that link to source material.
2. Score candidates by usefulness, source quality, license clarity, maintenance activity, runtime coverage, review burden, and uniqueness.
3. Record license before ingestion.
4. Create a source profile or source note.
5. Convert reusable behavior into OKF-compatible `Skill`, `Playbook`, `Workflow`, `Runbook`, or `Source Profile` concepts.
6. Cross-link entries by runtime target, capability, source, and related skills.
7. Verify frontmatter, source URL, license, attribution, and private-context boundary.
8. Attach validation evidence or mark the entry as unvalidated.
9. Merge in small batches.

## Default Mode

Default to summary and reference records.

Copy third-party content only when terms permit it, attribution is preserved, and security review passes.

## Review Signals

Mark entries that involve:

```text
local commands
dependency changes
filesystem writes
browser automation
account flows
MCP or external tools
network activity
reduced human review
production or external-system mutation
```

## Validation Gates

Skills and workflows should not be promoted only because they are popular or well written.

Promotion needs evidence that the entry is useful in its intended context.

Minimum evidence should include at least one of:

```text
a reproducible task or benchmark where the skill improves outcomes
explicit acceptance criteria tied to a project, runtime, or repository class
a credible upstream evaluation with date, version, and runtime target
a human review note explaining why validation is not yet practical
```

## Self-Improving Entries

For self-improving entries, use bounded edits and validation gates:

1. propose a narrow add, delete, or replace change;
2. evaluate against held-out or previously failing tasks;
3. accept only if the measured result improves or safety improves without reducing utility;
4. retain rejected edits as negative evidence when useful;
5. keep rollback context near the changed entry.

## Maintenance Checks

Run periodic library-level checks for:

```text
duplicated capabilities
stale runtime assumptions
incompatible runtime targets
missing validation evidence
unsafe action scope
unclear provenance
entries whose token cost exceeds measured utility
```
