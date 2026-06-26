---
name: Skill Library Maintenance
description: Maintain large agent skill libraries with contracts, neighbor graphs, diagnostics, and prune/merge/quarantine decisions. Use when performing periodic maintenance on canonical skill collections.
tags: [skill-management, agent-operations, skillops, maintenance, contracts, pruning, validation]
type: Playbook
---

# Skill Library Maintenance

## Purpose

Maintain a large agent skill library without accumulating technical debt. The operating assumption is that a skill library fails as an ecosystem before each individual skill obviously fails.

## Required Skill Contract

Each cataloged skill must have:

| Field | Meaning |
|-------|---------|
| Purpose | What recurring task the skill improves |
| Preconditions | Runtime, files, services, credentials, dependencies |
| Inputs | What the agent or user must provide |
| Outputs | Expected files, messages, actions, artifacts |
| Authority scope | What the skill can override, and what overrides the skill |
| Powers | Shell, browser, GUI, MCP, network, package install, account, mutation |
| Validation | Evidence of improvement without unacceptable regressions |
| Failure modes | Known bad behavior, brittleness, misuse cases |
| Neighbors | Similar, superseded, conflicting, composable skills |
| Status | candidate, cataloged, normalized, audited, quarantined, pruned, blocked |

## Maintenance Loop

```
Inventory skills → write/refresh contracts → build neighbor graph
→ detect overlaps and conflicts → diagnose utility/compatibility/risk/validation gaps
→ choose action → record receipt
```

## Actions

| Action | Use When |
|--------|----------|
| Promote | Evidence shows repeatable improvement and bounded risk |
| Merge | Multiple skills duplicate intent and can become one pattern |
| Split | One skill mixes unrelated capabilities or authority scopes |
| Quarantine | Risk or provenance unclear but source useful for study |
| Prune | Skill is stale, redundant, misleading, or consistently unhelpful |
| Block | Skill is malicious, unsafe, license-incompatible, or unreviewingly mutating |

## Diagnostics

Before promotion, check:
- **Utility:** Does it improve an identified task class?
- **Compatibility:** Does it conflict with existing rules or related skills?
- **Risk:** What external powers can it exercise?
- **Validation:** What tests, traces, benchmarks, or receipts support it?

## Artifacts for Multi-Runtime Skills

| Class | Role |
|-------|------|
| Canonical source | Reviewed source of truth |
| Intermediate contract | Structured metadata, relationships, capabilities |
| Runtime adapter | Generator/compiler for runtime-specific files |
| Runtime output | SKILL.md, AGENTS.md, CLAUDE.md, etc. |
| Receipt | Validation, diff, source hash, target paths, outcome |

Validation: canonical source reviewed → runtime adapters generated → runtime outputs verified.

Drift rule: if a runtime output is hand-edited, it becomes suspect until reconciled with canonical source.

## Loop Contract (for recurring maintenance loops)

Each loop should declare: purpose, cadence, owner, allowed inputs, allowed writes, forbidden actions, tool permissions, budget cap, human gates, verification commands, retry limit, escalation path, rollback path, retirement condition.

## Memory Contract (for continual learning)

For memory that persists across sessions:
- Did memory improve sequential work?
- Was forgetting prevented?
- Was unsafe persistence blocked?
- Were tool-use decisions better with memory than without?

## Trigger

Use this skill when:
- Periodic maintenance is scheduled (e.g., weekly cron)
- A new skill is promoted and may overlap with existing ones
- A skill has not been reviewed in 30+ days
- The user asks to clean up the skill library

## Procedure

1. Inventory all cataloged skills and their current status.
2. Write or refresh contracts for each skill (purpose, powers, neighbors, etc.).
3. Build a neighbor graph: identify similar, conflicting, and composable skills.
4. Detect overlaps: are there skills with duplicate intent?
5. Diagnose gaps: which skills lack validation evidence or have compatibility issues?
6. Choose actions: promote, merge, split, quarantine, prune, or block.
7. Record receipts for every action taken.
8. Update the catalog index.

## Verification

- All cataloged skills have current contracts.
- Neighbor graph is up to date.
- No duplicate-intent skills remain without explicit justification.
- Quarantined skills have documented reasons.
- Pruned skills are archived (not deleted).

## Failure Modes

- Skills accumulate without pruning (library bloat).
- Duplicate skills create retrieval confusion.
- Hand-edited runtime outputs drift from canonical source.
- Contracts become stale and no longer reflect actual skill behavior.

## Security Notes

- Medium risk: a bloated library increases the chance of an agent using a stale or wrong skill.
- Quarantine risky skills rather than deleting them — useful patterns may be extractable later.
- Always archive pruned skills (move to `.archived/`) for traceability.

## Sources

- curator/loops/skill-library-maintenance.md — full maintenance policy with contract schema
