---
name: Source Hierarchy
description: How to rank sources and resolve conflicting information. Use when two sources disagree, when evaluating evidence strength, or when deciding what to trust.
tags: [agent-operations, agent-operations, authority, conflict-resolution, epistemic-hygiene]
type: Playbook
---

# Source Hierarchy

## Order Of Trust

When sources conflict, use this order:

```
1. Current user instruction
2. Current repository source files
3. Tests, typechecks, build output, CI, and runtime evidence
4. Repo-local AGENTS.md
5. Repo contract
6. Accepted decision records
7. Current handoff
8. Memory facts with recoverable sources
9. Assumptions explicitly labeled as assumptions
10. Agent inference
11. Model prior knowledge
```

Higher levels override lower levels. The hierarchy does not remove judgment — it prevents weaker sources from silently overruling stronger ones.

## Important Rule

Memory is context, not evidence. A memory file may help locate knowledge, but it does not automatically prove a claim.

## Conflict Resolution

When two sources disagree:

1. Prefer the more primary source.
2. Prefer the more recent source when authority is equal.
3. Label unresolved conflicts explicitly.
4. Do not silently merge contradictions.

## Anti-Pattern

Do not use hidden model memory, assumptions, prior chats, or intuition as authoritative project facts.

## Sources

- curator/legacy/root-meta/authority.md — full authority model
- curator/legacy/memory/source_hierarchy.md — source hierarchy summary
- curator/legacy/cognition/reasoning_principles.md — evidence before inference
