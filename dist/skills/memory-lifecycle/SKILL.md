---
name: Memory Lifecycle
description: Manage memory through explicit lifecycle states. Use when promoting observations to durable memory, demoting stale rules, or deciding whether to keep, archive, or delete memory entries.
tags: [agent-operations, agent-operations, memory, lifecycle, promotion, pruning]
type: Playbook
---

# Memory Lifecycle

## Principle

Not every observation deserves to become durable memory. Most task-local context should disappear after the task is complete. Memory without lifecycle becomes a landfill.

## Lifecycle States

```
Observation → Assumption → Verified Fact → Decision → Rule → Superseded → Deprecated → Deleted
```

## State Definitions

| State | Meaning | Action |
|-------|---------|--------|
| Observation | Raw data point | Do not store automatically |
| Assumption | Provisional explanation | Label clearly; do not treat as fact |
| Verified Fact | Source-backed statement | Link to source; can become memory |
| Decision | Chosen direction with reason | Record in decision log |
| Rule | Durable instruction | Keep rare; justify by repeated evidence |
| Superseded | Was valid, now replaced | Mark but keep for traceability |
| Deprecated | Should not guide future work | Keep only when history matters |
| Deleted | No longer serves a reader | Remove when uncertain, prefer deletion |

## Trigger

Use when:
- An agent wants to write new durable memory
- Performing memory maintenance or dream cycle
- A source changes and existing memory may be stale
- Deciding between keeping and deleting a note

## Promotion Rules

Promote only when:
- the information survived verification;
- future agents are likely to need it;
- it reduces repeated confusion;
- it has durable value beyond the current task.

## Demotion Rules

Demote when:
- a source weakens;
- evidence disappears;
- a stronger source contradicts it;
- requirements change.

## Deletion Bias

When uncertain between keeping and deleting task-local context, prefer deletion. The goal is operational clarity, not archival completeness.

## Procedure

1. Classify the information into its current lifecycle state.
2. Verify the source exists and supports the claim.
3. Check: "Would this still be useful six months from now?"
4. If yes and verified → promote to next state.
5. If no or stale → demote or delete.
6. If deleting, check for cross-references that also need updating.

## Verification

- Every promoted memory entry has a source link.
- No assumption is stored as a fact.
- Superseded items are marked, not silently deleted.
- Deleted items leave no dangling references.

## Failure Modes

- Promoting every observation → memory landfill
- Never deleting → stale context misleads future agents
- Storing assumptions as facts → false confidence
- Deleting too aggressively → loss of useful traceability

## Security Notes

- Low risk: memory operations do not mutate external systems.
- Medium risk: incorrect promotion can cause future agents to act on stale information.
- Always verify source before promoting to "Verified Fact" or higher.
