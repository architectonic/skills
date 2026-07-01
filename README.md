---
type: Entry Point
title: skills
description: Runtime-neutral package for compact, reusable, verifiable procedures and a loop-engineered aggregator for discovering and maintaining public agent skills.
tags: [skills, procedures, verification, failure-modes, agents, okf, loop-engineering, aggregator]
okf_version: "0.2"
status: draft
---

# skills

`skills` is the reusable procedure package for an Architectonic constitution.

Install it with:

```bash
npx architectonic add skills
```

Optional addon for teams that want structured corpus upkeep loops:

```bash
npx architectonic add living-knowledge
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

## Skills Aggregator Role

This repository is also the first concrete living-knowledge instance for reusable agent skills.

The aggregator mission is:

```text
scan public web and GitHub signals
find skill, loop, workflow, runbook, and agent-procedure sources
catalog sources with provenance and license context
normalize useful procedures into OKF-compatible entries
classify domain, runtime target, risk, and review status
build installable distribution manifests
prepare future web publishing surfaces
```

The aggregator must not mirror the internet.

Default posture:

```text
discover broadly
catalog carefully
copy rarely
normalize conservatively
publish only reviewed, useful, license-compatible entries
```

## Loop-Engineered Operation

`skills` should be maintained by one recurring project operator, not many independent scheduled prompts.

Canonical loop:

```text
Observe
-> Plan
-> Act
-> Evaluate
-> Repair / Learn
-> Persist memory
-> Repeat
```

Operating model:

```text
single project-operator scheduler
many roles
shared daily ledger
queued + scheduled execution
```

The operator reads durable state, chooses exactly one role for the current run, executes that role, updates queues and status, and stops cleanly.

The reusable project-operator prompt lives in:

```text
operations/project-operator-prompt.md
```

## Default Aggregator Roles

- Reporter — daily memory, metrics, and changed artifacts.
- Radar — public web/GitHub discovery for new skill and loop sources.
- Source Reviewer — provenance, license, risk, and usefulness review.
- Normalizer — converts accepted source behavior into OKF-compatible entries.
- Cataloger — maintains `dist/catalog.json`, `dist/install-manifest.json`, and reports.
- Risk Auditor — inspects unsafe actions, prompt injection, tool abuse, and review burden.
- Packager — keeps installable `dist/skills/` and package surfaces coherent.
- Publisher — prepares future website/export surfaces.
- Critic — removes duplication, stale entries, overbroad skills, and process debt.

## Relationship to the stack

```text
constitution      = root scaffold
doctrine          = what must govern the work
identity          = who performs or approves the work
project           = where the work is situated
skills            = how repeatable work is carried out
knowledge         = what reviewed claims and evidence are retained
meta              = how the system audits and improves itself
living-knowledge  = optional addon for campaign-based maintenance of knowledge
```

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
