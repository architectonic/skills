---
name: skill-library-evolution
description: Maintain agent skill libraries as self-evolving software ecosystems. Use when pruning stale skills, resolving skill conflicts, tracking technical debt, or planning library-wide maintenance cycles. Covers typed skill contracts, ecosystem graphs, compatibility/risk/validation diagnostics, and campaign-based evolution.
tags: [skill-management, skill-management, skillops, skill-library, ecosystem, maintenance, evolution]
type: Playbook
---

# skill-library-evolution

Maintain agent skill libraries as self-evolving software ecosystems rather than flat collections.

## When to use

- The skill library has grown beyond easy human comprehension
- Skills conflict, overlap, or have unclear precedence
- Technical debt accumulates (broken links, stale references, outdated patterns)
- A campaign of additions or pruning is planned
- Library health metrics need diagnosis

## Core Concepts (from SkillOps + SkillFoundry)

### Typed Skill Contracts
Each skill should declare:
- Purpose and preconditions
- Required inputs and expected outputs
- Authority scope (what it may/may not mutate)
- Dependencies and runtime targets
- Collision/overlap with sibling skills
- Promotion/demotion/prune/block status

### Ecosystem Graph
- Skills are nodes; dependencies and conflicts are edges
- Hierarchical grouping by capability family
- DAG-like structure enables dependency analysis and impact prediction
- Graph health: detect cycles, orphaned skills, and overly dense clusters

### Library Health Diagnostics

| Dimension | What to check |
|-----------|---------------|
| Utility | Does the skill still get triggered? Is it useful? |
| Compatibility | Does it conflict with newer skills or runtime changes? |
| Risk | Does it have unsafe patterns, external mutation without guards, or stale credentials? |
| Validation | Do its verification steps still pass? |

## Evolution Workflow (from SkillFoundry)

```text
Build domain knowledge tree
→ select high-value frontier branches
→ mine heterogeneous resources
→ extract operational contracts
→ compile skill package
→ validate at multiple levels
→ insert validated skill as tree leaf
→ repair, merge, or prune weak skills
→ repeat as a campaign
```

## Pruning Rules

- **Merge:** Two skills cover the same capability → consolidate into one
- **Demote:** A skill is useful but risky → move to quarantine, not delete
- **Prune:** A skill is unreferenced, untested, and unmaintained → remove with receipt
- **Repair:** A skill has fixable defects → apply anchored revision (see skill-revision)
- **Block:** A skill is harmful or misleading → block promotion, document why

## Campaign Mechanics

For large library maintenance:
1. Define scope (e.g., "audit all skills in `media/` category")
2. Set checkpoint interval (every N skills, pause and report)
3. Record receipts for each decision (merge/prune/repair/block)
4. Stop if error rate exceeds threshold
5. Produce a summary report with metrics

## AOMK Integration

- Use Graphify on `skills/` to detect community cohesion drops
- Flag communities with cohesion < 0.1 as merge candidates
- Flag isolated nodes (≤1 edge) as prune or link candidates
- Track skill lifecycle status in SKILLS_INDEX.md

## Sources

- skillops-2026 (arxiv) — skill library as software ecosystem with tech debt diagnostics
- ma-compbio-lab/SkillFoundry — closed-loop skill library evolution with campaign mechanics
- skill-distillation.md — contrastive induction for skill improvement
