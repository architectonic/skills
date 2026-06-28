---
name: project-upkeep
description: Maintain the project layer so each project namespace stays source-grounded, current, decision-aware, and small enough to remain useful.
tags: [agent-operations, upkeep, project, source-grounding, decisions, handoff, okf]
type: Playbook
---

# project-upkeep

## Purpose

Keep a project repository or project namespace current and operationally useful without letting it become a stale wiki or an unstructured summary dump.

## Trigger

Use this skill when:
- project docs no longer match the live source repo
- major architecture, workflow, or scope changes landed
- decisions, sources, or open questions need refresh
- a handoff or periodic project maintenance pass is due

## Inputs

- the current project repository or project namespace docs
- the live source repository and its current structure
- confirmed decisions, open questions, and recent changes
- relevant identity and doctrine constraints

## Procedure

1. Re-read the project entrypoints and identify the expected contract: overview, profile, sources, architecture, decisions, open questions, and handoff state.
2. Validate each major claim against source artifacts. Prefer README files, manifests, code structure, tests, and live repo docs over memory or guesswork.
3. Refresh the project’s compact operating picture: what it is, how it works, what changed, what is still uncertain, and what matters next.
4. Move misplaced content to the right layer. Identity facts leave project space, reusable procedures leave for skills, and top-level doctrine leaves for doctrine.
5. Prune noise. If a page is large but low-signal, compress it into durable distinctions, decisions, and sources.
6. Record fresh decisions and unresolved questions instead of hiding drift in prose.

## Verification

- project docs match the live source repo closely enough to guide future work
- important decisions, sources, and open questions are easy to locate
- the namespace is compact, source-grounded, and not a generated dump
- content is correctly layered relative to doctrine, identity, and skills

## Failure Modes

- project docs become stale faster than the source repo changes
- handoffs repeat raw detail instead of durable structure
- project space accumulates doctrine or identity material that belongs elsewhere
- future agents cannot tell confirmed fact from summary residue
