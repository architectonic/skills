---
name: teleagent-system-upkeep
description: Coordinate a full maintenance pass across doctrine, identity, project, and skills so the Architectonic stack remains coherent top-down.
tags: [agent-operations, upkeep, teleagent, system-maintenance, cross-repo, orchestration, okf]
type: Playbook
---

# teleagent-system-upkeep

## Purpose

Run a deliberate top-down maintenance pass across the Architectonic layers without losing the distinction between doctrine, identity, procedures, and project state.

## Trigger

Use this playbook when:
- multiple sibling repos changed and coherence needs checking
- a release, restructuring, or major doctrine shift touched several layers
- the user asks for a general system refresh
- repo-local upkeep reveals cross-repo contradictions

## Composes

- `doctrine-upkeep`
- `identity-upkeep`
- `skills-upkeep`
- `project-upkeep`

## Order

```text
doctrine -> identity -> skills -> project
```

Start from governing doctrine, then participant boundaries, then reusable procedures, then active project/application state.

## Procedure

1. Run `doctrine-upkeep` first and note any doctrine changes that affect the other layers.
2. Run `identity-upkeep` next so participant boundaries and privacy rules are refreshed under the current doctrine.
3. Run `skills-upkeep` after that so reusable procedures reflect the latest doctrine and identity constraints.
4. Run `project-upkeep` last so project documentation and operating state are aligned with the current doctrine, identity rules, and available procedures.
5. Compare the outputs and record any cross-repo contradictions, missing references, or structural gaps.
6. Update entrypoints or indexes so each repo points to the relevant upkeep skill rather than duplicating procedure text.

## Verification

- each layer still serves its own role without leakage
- cross-repo references remain coherent and top-down
- no major contradiction remains between doctrine, identity, procedures, and project state
- follow-up work is clearly split into repo-local vs system-level items

## Failure Modes

- maintenance starts from project detail and never reconnects to first principles
- layers blur together and duplicate each other
- one repo is refreshed in isolation while the others drift
- cross-repo contradictions are noticed but not recorded
