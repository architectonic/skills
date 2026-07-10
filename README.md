---
type: Entry Point
title: skills
description: Runtime-neutral package for compact, reusable, verifiable procedures and the governed discovery of public agent skills.
tags: [skills, procedures, verification, failure-modes, agents, provenance, okf]
okf_version: "0.2"
status: draft
---

# skills

```bash
npx architectonic add skills
```

`skills` defines compact procedures that help humans or agents perform recurring work with clearer inputs, verification, and failure handling.

This repository is not a prompt collection, private memory store, or unreviewed runtime dump. A skill belongs here only when it teaches a reusable procedure that would otherwise be performed inconsistently.

## In the ensemble

```text
constitution      composition contract for the ensemble
doctrine          purpose, principles, ontology, epistemology, ethics, governance, incentives
identity          actors, roles, authority, delegation, incentives, privacy
project           operating-unit context, sources, decisions, risks, continuity
skills            reusable procedures, verification, failure handling
knowledge         claims, sources, evidence, uncertainty, known unknowns
models            model metadata, evaluations, capability requirements, routing policy
agents            software actors composed from identity, skills, models, knowledge, permissions
living-knowledge  optional: governed maintenance of frequently changing corpora
meta              audit, upkeep, drift review, revision policy
```

Skills define how recurring work is performed and verified. Agents may select or vendor skills for a concrete software actor. Skill execution may produce knowledge, but successful procedure does not make every resulting claim true.

## Commands

```bash
npx architectonic add skills
npx architectonic add skills --source npm
npx architectonic init
npx architectonic list
npx architectonic doctor
```

CLI: https://github.com/architectonic/architectonic

## What a skill is

```text
trigger        when the skill applies
inputs         what must be inspected, received, or confirmed
procedure      the ordered method
verification   how success is checked
failure modes  errors the procedure is intended to prevent or expose
```

A skill is not a doctrine essay, a complete agent definition, a private project note, or a tool wrapper without procedural value.

## Discovery and aggregation

This repository may discover, review, normalize, and package useful public procedures with recoverable provenance and license context. Discovery is broad; inclusion is selective.

## Base skill format

```md
---
type: Skill
title: Skill Name
description: One sentence explaining what this skill helps a worker do.
tags: [skill, okf]
risk_level: low
source:
  repository: owner/repository
  path: path/to/source
  ref: commit-or-version
status: draft
---

# Skill Name

## Trigger
## Inputs
## Procedure
## Verification
## Failure Modes
```

## Boundary

This public repository should not contain credentials, private project facts, personal memory, client data, or procedures whose safe use depends on undisclosed context.
