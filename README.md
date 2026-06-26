---
type: Entry Point
title: skills
description: Runtime-neutral package for compact, reusable, verifiable procedures that improve human-agent collaboration.
tags: [skills, procedures, verification, failure-modes, agents, okf]
okf_version: "0.1"
status: draft
---

# skills

`skills` is the reusable procedure package for a runtime-neutral knowledge operating system for human-agent collaboration.

It defines compact procedures that help agents perform specific kinds of work better, safer, faster, or with fewer repeated failures.

This repository is not a prompt pack, a private memory vault, a project-specific playbook, or a runtime-specific skill dump. It should contain only skills that teach a useful procedure an agent would not reliably perform by default.

The current GitHub namespace is only a publishing location. It is not the project name.

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
a large workflow that should be a playbook or agent loop
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

What the agent must inspect, receive, or confirm before using the skill.

## Procedure

The smallest coherent ordered procedure.

## Verification

How the agent knows the procedure worked.

## Failure Modes

What this skill prevents or catches.
```

## Relationship to OKF

This repository should be maintained as an OKF-compatible knowledge bundle.

Concept documents should use Markdown with YAML frontmatter. `index.md` files should provide progressive disclosure. `log.md` files should record meaningful changes. Cross-links should connect related concepts. Citations should be used when factual claims depend on external sources.

OKF is the carrier format. Skills are the procedural content.

## Runtime neutrality

The canonical source should remain runtime-neutral Markdown.

Runtime-specific formats may be generated as exports:

```text
dist/claude/
dist/codex/
dist/cursor/
dist/hermes/
dist/generic/
```

Do not make the canonical skill corpus depend on one runtime's current convention. Claude skills, Codex skills, Cursor rules, Hermes profiles, and custom runtimes are consumers or export targets, not the source of truth.

## Possible structure

```text
README.md
AGENTS.md
index.md
log.md

doctrine/
  skill.md
  skill-vs-playbook.md
  verification.md
  failure-modes.md

skills/
  engineering/
    source-review.md
    code-review.md
    architecture-review.md
  project/
    grill-with-docs.md
    intent-to-contract.md
    handoff-writing.md
  memory/
    wiki-maintenance.md
    decision-recording.md
    assumption-grilling.md

dist/
  claude/
  codex/
  cursor/
  hermes/
  generic/
```

## Relationship to other packages

```text
teleology = defines what the collaboration is for and how truth, authority, and memory should be handled
identity  = defines who or what is participating
project   = defines the operating unit where work happens
skills    = defines reusable procedures
agents    = composes doctrine, identity, skills, tools, prompts, scripts, and loops
operator  = installs, updates, audits, and exports packages into runtimes
```

Skills should be composed by agents and playbooks. Skills should not become agents themselves.

## Public boundary

This repository may contain:

```text
general reusable skills
skill schemas
skill templates
verification procedures
failure-mode checklists
runtime-neutral examples
```

It must not contain:

```text
private user facts
private project facts
private source paths
client-sensitive details
runtime secrets
raw transcript dumps
project-specific operational state
```

## Quality rule

A skill belongs only if it changes future agent behavior in a useful way.

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

## Installation vs instantiation

Installation copies or exports public skill files into a runtime or workspace.

Instantiation adapts a template or skill set to a specific project, user, agent, or private vault.

Do not preserve template language as if it were instantiated knowledge.

## Status

Draft. The immediate goal is to define a small, high-signal, runtime-neutral skill corpus and export it into runtime-specific formats only when useful.
