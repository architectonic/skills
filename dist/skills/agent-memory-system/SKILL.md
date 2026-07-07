---
name: agent-memory-system
description: Design and maintain agent memory systems. Use when setting up agent memory, designing memory schemas, implementing memory lifecycle management, or reconciling memory across sessions. Covers memory classes, lifecycle states, demotion rules, and canonicalization.
tags: [agent-operations, memory, self-improvement]
type: Playbook
title: agent-memory-system
domain: agent-operations
risk_level: medium
requires_review: true
source_family: architectonic-curator
source_status: adapted
---

# agent-memory-system

Design and maintain agent memory systems that survive across sessions and improve over time.

## Memory architecture

### Core files
| File | Purpose | Update frequency |
|------|---------|------------------|
| `AGENTS.md` | Hard rules, project context, authority hierarchy | Rarely (only for structural changes) |
| `MEMORY.md` | Durable lessons, preferences, conventions | After each significant discovery |
| `USER.md` | User profile, communication style, context | As user reveals preferences |
| `start_here.md` | Current state, active goals, next steps | Every session start |

### Memory classes
- **Identity:** Who the agent is, name, role, operating principles
- **Environment:** OS, paths, tools, runtime configuration
- **User:** Preferences, style, email, identity
- **Project:** Current work, decisions, blockers, goals
- **Durable lessons:** Source-backed patterns that survived verification
- **Temporary context:** Session-scoped state (do not persist)

## Memory lifecycle

### Promotion (temporary → durable)
1. Pattern observed in ≥ 2 sessions or ≥ 2 source artifacts
2. Verified against source code/docs (not just conversation)
3. Rewritten in agent-neutral, declarative form
4. Stored in MEMORY.md with source attribution

### Demotion (durable → archived)
1. Pattern hasn't been used in 30+ days
2. Source artifact changed making the pattern stale
3. Pattern conflicts with newer, better evidence
4. Move to `.archived/` — never delete

### Canonicalization rules
- One fact per entry — no compound statements
- Source citation for every claim (file:line or URL)
- Timestamp for temporal facts (decisions, preferences)
- Review cadence: monthly for active projects, quarterly for stable knowledge

## Memory reconciliation

When contradictory memories exist:
1. Check timestamps — newer wins for preferences, older wins for decisions
2. Verify against source artifacts — ground truth wins
3. If still contradictory, flag for human review
4. Never silently overwrite — log the conflict

## Anti-patterns
- **Accumulating without pruning:** Memory grows unbounded, becomes noise
- **Promoting too fast:** Single observation becomes "doctrine"
- **Deleting instead of archiving:** Lost context can't be recovered
- **Mixing levels:** Don't put session TODOs in MEMORY.md
- **No source links:** Unverifiable claims accumulate

## Sources
- curator/legacy/memory/ — canonicalization, source hierarchy patterns
- curator/root-meta/memory_model.md — memory classes and lifecycle
- curator/root-meta/memory_ops_doctrine.md — operational rules
- curator/root-meta/memory_lifecycle.md — state transitions