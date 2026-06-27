---
name: skill-lifecycle-states
description: Canonical skill lifecycle states (S0–S7) for tracking skill maturity
  from raw experience to archived. Use when designing skill registries, ingestion
  pipelines, or governance workflows that need explicit state transitions.
type: Playbook
title: Skill Lifecycle States
domain: software-engineering
tags:
- software-engineering
- okf
risk_level: medium
requires_review: true
source_family: agent-skills-standard
source_status: adapted
---

# Skill Lifecycle States

Canonical lifecycle for agent skills, adapted from SkillWiki. Each state represents a gate that must be explicitly passed before promotion.

## States

| State | Name | Meaning | Promotion Trigger |
|-------|------|---------|-------------------|
| S0 | Raw | Unprocessed experience, document, or trajectory | Ingest pipeline extracts candidate |
| S1 | Candidate | Extracted, awaiting review | Audit passes (schema, safety, postconditions) |
| S2 | Draft | Under verification | Verify loop passes postconditions |
| S3 | Verified | Postconditions passed on held-out tasks | Human or policy gate approves release |
| S4 | Released | Production-ready | Deployed to agents |
| S5 | Degraded | Health issues detected (low success rate, stale deps) | Repair proposal accepted and verified |
| S6 | Deprecated | Superseded or scheduled for removal | Replacement skill reaches S4 |
| S7 | Archived | Retained for history, not active use | No active dependents |

## State Transitions

```
S0 → S1 → S2 → S3 → S4 → S5 → S6 → S7
              ↑    ↓    ↑         ↓
              └────┘    └─────────┘
           (repair loop)  (deprecate + replace)
```

Key rules:
- **No skip promotions**: A skill must pass through each state in order.
- **S5 is reversible**: A degraded skill can return to S3/S4 after repair.
- **S6 requires replacement**: Deprecate only when a replacement skill exists or the capability is genuinely obsolete.
- **S7 is terminal**: Archived skills are read-only.

## Health Monitoring

At S4 (released), track:
- **Success rate**: Execution success / total invocations
- **Stale dependencies**: Upstream tools, APIs, or packages that have changed
- **Postcondition drift**: Whether the skill's stated outcomes still match reality
- **Usage frequency**: Unused skills are candidates for S6

When health drops below threshold → transition to S5 and generate a repair proposal.

## Repair Proposals

Repair proposals are first-class artifacts:
- Each proposal has a unique ID, timestamp, and author (human or automated engine)
- Proposals include: diagnosis, proposed edit, expected impact, rollback plan
- Proposals require explicit acceptance before mutation
- Rejected proposals are retained as negative evidence

## Implementation Notes

- Store lifecycle state as a frontmatter field: `lifecycle_state: S3`
- Log all state transitions with timestamp, actor, and reason
- Expose state in catalog listings so agents can filter by maturity
- Never auto-promote from S3 to S4 without human or policy-gated approval

## Source

Distilled from SkillWiki (`Huangdingcheng/SkillWiki`), which implements this lifecycle with a CLI (`skillwiki promote <id> S3`) and audit/verify loops.
