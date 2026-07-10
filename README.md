---
type: Entry Point
title: skills
description: Runtime-neutral package for compact, reusable, verifiable procedures and the governed discovery of public agent skills.
tags: [skills, procedures, verification, failure-modes, agents, provenance, okf]
okf_version: "0.2"
status: draft
---

# skills

`skills` is the reusable procedure package for an Architectonic constitution.

Install it with:

```bash
npx architectonic add skills
```

Optional addon for teams that want structured corpus maintenance:

```bash
npx architectonic add living-knowledge
```

It defines compact procedures that help humans or agents perform recurring work with clearer inputs, verification, and failure handling.

This repository is not a prompt collection, private memory store, project-specific playbook, or unreviewed runtime dump. A skill belongs here only when it teaches a reusable procedure that would otherwise be performed inconsistently.

## Purpose

A useful skill may help a worker:

```text
find source truth
review evidence
clarify intent
avoid unsupported inference
execute a recurring workflow
verify an outcome
record a consequential decision
prepare a useful handoff
prevent a known failure mode
resume work from durable state
```

A category alone does not justify a skill. If an entry adds no procedure or verification value, it should be merged or removed.

## What a skill is

A skill is a compact, reusable procedure with:

```text
trigger        # when the skill applies
inputs         # what must be inspected, received, or confirmed
procedure      # the ordered method
verification   # how success is checked
failure modes  # errors the procedure is intended to prevent or expose
```

A skill is not:

```text
a doctrine essay
a complete agent definition
a private project note
a generic tip
a tool wrapper without procedural value
a decorative instruction file
a large operating system disguised as one procedure
```

Skill execution may produce knowledge, but a successful procedure does not make every resulting claim true. Claims and evidence remain subject to the knowledge layer.

## Discovery and aggregation

This repository may discover, review, normalize, and package useful public procedures.

A restrained aggregation process should:

```text
scan public sources
record provenance and license context
identify the specific reusable behavior
compare it with existing skills
normalize only when the procedure is distinct and useful
classify runtime assumptions, risk, and review status
publish only reviewed and license-compatible material
```

The aggregator should not mirror the internet or preserve every variation. Discovery is broad; inclusion is selective.

Copied or adapted procedures should retain recoverable provenance, including source repository or URL, path, version or commit, license context, and local modifications.

## Maintenance

Skills may be maintained through a scheduler, board, ledger, or ordinary human review. No particular orchestration pattern is required.

A minimal maintenance loop is:

```text
observe a recurring failure or useful procedure
inspect sources and existing entries
propose one bounded change
verify it against examples or evaluations
record provenance and review state
retain, revise, or remove it based on evidence
```

Operational roles and artifacts should be created only when they improve accountability or preserve necessary state. They should not become additional sources of truth for the skill itself.

## Relationship to the stack

```text
constitution      = root scaffold
doctrine          = principles and boundaries governing the work
identity          = actors, authority, delegation, and privacy
project           = operating context
skills            = reusable procedures and verification methods
knowledge         = reviewed claims, sources, and evidence
meta              = maintenance and revision policy
living-knowledge  = optional addon for campaign-based corpus maintenance
agents             = may select or vendor skills for a concrete software actor
```

## Base skill format

```md
---
type: Skill
title: Skill Name
description: One sentence explaining what this skill helps a worker do.
tags: [skill, okf]
timestamp: 2026-06-26T00:00:00-03:00
risk_level: low
source:
  repository: owner/repository
  path: path/to/source
  ref: commit-or-version
status: draft
---

# Skill Name

## Trigger

When this skill should be used.

## Inputs

What must be inspected, received, or confirmed before using it.

## Procedure

The smallest coherent ordered procedure.

## Verification

How the worker knows the procedure worked.

## Failure Modes

What the procedure prevents or exposes.
```

## Boundary

This public repository should not contain credentials, private project facts, personal memory, client data, or procedures whose safe use depends on undisclosed context.
