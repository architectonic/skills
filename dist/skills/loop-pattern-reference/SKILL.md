---
name: Loop Pattern Reference
description: Design bounded, observable, and auditable agent feedback cycles. Use when creating or evaluating any repeatable agent workflow (reconciliation, review, discovery, ingestion, curation, testing). Defines the canonical loop shape, required boundaries, terminal states, and validation rules that all AMOK loops must follow.
tags: [loops, feedback-cycle, safety, bounded-automation, pattern]
type: Reference
---

# Loop Pattern Reference

A loop is a skill with a feedback cycle and a stopping condition. This reference defines the pattern that all AMOK loops must follow.

## Canonical Loop Shape

```
Observe → Choose → Act → Verify → Record → Repeat or Stop
```

1. **Observe:** Read fresh state. Do not act on assumptions from a previous pass.
2. **Choose:** Select the highest-value in-scope action from explicit criteria.
3. **Act:** Make one bounded, reversible change or produce one candidate.
4. **Verify:** Run the same acceptance check under recorded conditions.
5. **Record:** Save the action, evidence, outcome, and remaining work.
6. **Repeat or Stop:** Continue only while progress is measurable and any user-set limit remains; otherwise enter a named terminal state.

## Required Boundaries

Every loop must define:

| Boundary | Why |
|----------|-----|
| **Stop condition** | Prevents infinite repetition. "No progress" is a stop, not a failure. |
| **Maximum attempts or budget** | Bounded cost. Prevents runaway compute/time. |
| **Observable state** | Each pass can see fresh evidence, not stale assumptions. |
| **Verification method** | Same check every pass. Reproducible, not subjective. |
| **Escalation rule** | When to ask a human instead of retrying. |
| **Rollback or recovery path** | How to undo if the action made things worse. |
| **External-system mutation boundary** | What requires human approval before acting. |
| **Record/receipt format** | What the next pass (or a human) needs to resume. |

## Terminal States

A loop must name at least one terminal state:

- **Success:** Goal met, acceptance check passes.
- **Clean no-op:** Nothing to do, no changes made.
- **Blocked:** Needs human input or external dependency.
- **Approval-required:** Needs human sign-off before continuing.
- **Exhausted:** Budget/attempts exhausted without success.
- **Stagnated:** No measurable progress across consecutive passes.

Never report an error or exhausted budget as success.

## Loop Families

| Family | Shape | Use For |
|--------|-------|---------|
| Plan-Act-Observe | plan → act → observe → update plan | Normal tool-using agents |
| Evaluator-Optimizer | generate → evaluate → revise → repeat | Generated output scoring |
| Reflection | produce → reflect → identify defect → revise | Self-critique |
| Reviewer-Coder | coder changes → reviewer inspects → tests verify | Separation of concerns |
| Memory Reconciliation | collect claims → verify → promote → prune | Working memory maintenance |
| Recovery | failure → classify → retry/repair/escalate/stop | Task failure |
| Control-Plane | intent → policy validate → execute → receipt | External system mutation |

## Staged Rollout

| Level | Mode | Allowed Behavior |
|-------|------|------------------|
| L0 | Design only | Describe loop, risks, verification. No execution. |
| L1 | Report only | Run on cadence, write observations. No mutation. |
| L2 | Assisted fixes | Create bounded patches, draft PRs behind human approval. |
| L3 | Full automation | Execute within defined boundaries. Escalate per rules. |

## Grounding Rules

- Use only details the user supplied or facts found in scoped files.
- Do not invent tools, metrics, schedules, permissions, or owners.
- When a detail is unknown, ask one short question or use neutral wording.
- Never present a guess as a "sensible default."
- Destructive, production, financial, privacy-sensitive, or external-message actions require explicit approval.

## Anti-Patterns

- **"Until happy"** — subjective finish line. Replace with a rubric, threshold, or finite scenario set.
- **Self-approval** — the same actor creates and approves. Use independent verification for high-impact output.
- **Stale state** — acting on assumptions from a previous pass. Re-read current state before consequential actions.
- **Manufactured loop** — forcing a loop when no new feedback can change the next action. Use a one-shot workflow instead.
- **Invisible budget** — no limit on retries/cost. Always name the limit.

## Source

Distilled from Forward-Future/loop-library (MIT, https://github.com/Forward-Future/loop-library), which ships 31 published loops following this pattern. AMOK extends with OKF frontmatter, grounding rules, and staged rollout levels.
