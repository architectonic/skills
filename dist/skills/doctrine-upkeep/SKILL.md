---
name: doctrine-upkeep
description: Maintain the doctrine layer so purpose, truth rules, authority boundaries, and memory doctrine stay coherent with the rest of the Architectonic system.
tags: [agent-operations, upkeep, doctrine, governance, system-design, okf]
type: Playbook
---

# doctrine-upkeep

## Purpose

Keep the doctrine repository coherent as the top-level doctrine layer for purpose, truth, authority, memory, and evaluation.

## Trigger

Use this skill when:
- doctrine documents have drifted from actual system behavior
- identity, project, or skills changed in ways that affect doctrine
- a new policy about truth, authority, or memory must be recorded
- a periodic architecture or doctrine refresh is due

## Inputs

- the current doctrine repository docs and indexes
- the current states of `identity`, `project`, and `skills`
- confirmed decisions from the user or source artifacts
- any open contradictions between doctrine and implementation

## Procedure

1. Re-read the top-level doctrine entrypoints and identify the currently asserted purpose, truth chain, authority rules, memory policy, and evaluation stance.
2. Compare those claims against the live sibling repos. Look for drift, contradiction, or missing doctrine caused by newer operational practice.
3. Distinguish doctrine from implementation. Doctrine should define governing principles and decision rules, not repo-local operational detail.
4. Update only what is supported by source or explicit user direction. If a principle is still undecided, record it as an open question rather than hardening it into doctrine.
5. Check that cross-repo relationships still read top-down: `doctrine -> identity -> skills -> project`.
6. Record any consequential change in a durable change log, decision log, or linked doctrine note.

## Verification

- doctrine still answers what the system is for and how truth and authority should be handled
- no repo-local procedural detail has leaked into doctrine unnecessarily
- sibling repos do not materially contradict the current doctrine layer
- unresolved design disagreements are explicit rather than silently papered over

## Failure Modes

- doctrine becomes a slogan layer with no operational consequence
- implementation details crowd out first-principles doctrine
- sibling repos evolve but doctrine remains stale
- ambiguous doctrine gets presented as settled truth
