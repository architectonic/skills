---
name: teleology-upkeep
description: Maintain the teleology layer so purpose, truth rules, authority boundaries, and memory doctrine stay coherent with the rest of the TeleAgent system.
tags: [agent-operations, upkeep, teleology, doctrine, governance, system-design, okf]
type: Playbook
---

# teleology-upkeep

## Purpose

Keep the teleology repository coherent as the top-level doctrine layer for purpose, truth, authority, memory, and evaluation.

## Trigger

Use this skill when:
- teleology documents have drifted from actual system behavior
- identity, project, or skills changed in ways that affect doctrine
- a new policy about truth, authority, or memory must be recorded
- a periodic architecture or doctrine refresh is due

## Inputs

- the current teleology repository docs and indexes
- the current states of `identity`, `project`, and `skills`
- confirmed decisions from the user or source artifacts
- any open contradictions between doctrine and implementation

## Procedure

1. Re-read the top-level teleology entrypoints and identify the currently asserted purpose, truth chain, authority rules, memory policy, and evaluation stance.
2. Compare those claims against the live sibling repos. Look for drift, contradiction, or missing doctrine caused by newer operational practice.
3. Distinguish doctrine from implementation. Teleology should define governing principles and decision rules, not repo-local operational detail.
4. Update only what is supported by source or explicit user direction. If a principle is still undecided, record it as an open question rather than hardening it into doctrine.
5. Check that cross-repo relationships still read top-down: `teleology -> identity -> skills -> project`.
6. Record any consequential change in a durable change log, decision log, or linked doctrine note.

## Verification

- teleology still answers what the system is for and how truth and authority should be handled
- no repo-local procedural detail has leaked into doctrine unnecessarily
- sibling repos do not materially contradict the current teleology layer
- unresolved design disagreements are explicit rather than silently papered over

## Failure Modes

- teleology becomes a slogan layer with no operational consequence
- implementation details crowd out first-principles doctrine
- sibling repos evolve but teleology remains stale
- ambiguous doctrine gets presented as settled truth
