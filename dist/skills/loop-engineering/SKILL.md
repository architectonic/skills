---
name: Loop Engineering
description: Design bounded, observable, and auditable agent loops. Use when creating or evaluating any repeatable agent cycle (reconciliation, review, discovery, ingestion, etc).
tags: [agent-operations, loops, safety, rollout, taxonomy]
type: Playbook
---

# Loop Engineering

## Purpose

Design repeatable agent cycles that work without constant human prompting while remaining bounded, observable, and interruptible. A loop is a control structure around an agent, not just a prompt.

## Canonical Loop Shape

```
Goal → Plan → Act → Observe → Evaluate → Update State → Continue, Escalate, or Stop
```

## Loop Families

| Family | Use For | Shape |
|--------|---------|-------|
| Plan-Act-Observe | Normal tool-using agents | plan → act → observe → update plan |
| Evaluator-Optimizer | Generated output scoring | generate → evaluate → revise → repeat |
| Reflection | Self-critique | produce → reflect → identify defect → revise |
| Reviewer-Coder | Software with separation of concerns | coder changes → reviewer inspects → tests verify |
| Memory Reconciliation | Working memory maintenance | collect claims → verify → promote → prune |
| Recovery | Task failure | failure → classify → retry/repair/escalate/stop |
| Control-Plane | External system mutation | intent → policy validate → execute → receipt |

## Required Boundaries

Every loop must define:
- stop condition
- maximum attempts or budget
- observable state
- verification method
- escalation rule
- rollback or recovery path
- external-system mutation boundary
- log or receipt format

## Staged Rollout

| Level | Mode | Allowed Behavior |
|-------|------|-----------------|
| L0 | Design only | Describe loop, risks, verification. No execution. |
| L1 | Report only | Run on cadence, write observations. No mutation. |
| L2 | Assisted fixes | Create bounded patches, draft PRs behind human approval. |
| L3 | Guarded unattended | Execute allowlisted low-risk actions with receipts, caps, rollback. |
| L4 | Blocked by default | External mutation, account workflows, production, finance. Requires explicit policy. |

## Readiness Gate (before level promotion)

1. No secrets, credentials, or private data exposed
2. At least three report-only cycles with useful receipts
3. False positives recorded and not repeatedly rediscovered
4. Verification commands deterministic enough for risk class
5. Budget and early-exit behavior work
6. State drift reconciled before action
7. Human can inspect and override decisions

## Bad Loop Signs

- No stop condition
- Expands scope every cycle
- Mutates external systems without policy checks
- Uses hidden state the user cannot inspect
- Retries the same failure without changing strategy
- Optimizes against a vague or untrusted evaluator
- Consumes tokens without producing durable artifacts

## Security Note

Treat loops as higher-risk than one-shot skills. Repetition amplifies bad instructions, stale context, weak permissions, and cost leakage.

## Sources

- curator/loops/loop-engineering.md — full playbook with OKF frontmatter
