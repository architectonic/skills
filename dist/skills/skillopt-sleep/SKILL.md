---
name: skillopt-sleep
description: Nightly offline self-evolution pattern for coding agents. Use when designing agent memory consolidation, offline skill improvement, or background optimization loops. Covers harvesting past sessions, replaying recurring tasks, bounded skill edits gated by held-out validation, and staged adoption. Derived from Microsoft SkillOpt-Sleep.
tags: [skill-management, skill-management, self-improvement, offline-consolidation, memory, skill-optimization]
type: Playbook
---

# SkillOpt-Sleep Pattern

Nightly offline self-evolution for local coding agents. An agent reviews past sessions, replays recurring tasks on its own API budget, and consolidates validated learnings into long-term memory and skills — behind a held-out gate, staged for human review.

The agent gets better the more you use it, with no weight training and zero inference-time overhead at deployment.

## When to use

- Designing agent memory consolidation loops
- Building offline skill improvement pipelines
- Harvesting recurring patterns from past agent sessions
- Implementing background optimization for long-running agent deployments

## The Sleep Cycle

```
One "night":
harvest transcripts → mine recurring tasks → replay offline
   → consolidate (reflect → bounded edit → GATE on held-out tasks)
   → stage proposal → (human) adopt
```

## Phases

### 1. Harvest

Collect execution transcripts from coding agent sessions (Claude Code, Codex, Copilot). Mine for recurring tasks — patterns the agent encounters repeatedly.

### 2. Mine

Identify recurring tasks from transcripts. Focus on tasks with:
- Clear correctness signals (tests pass/fail, builds succeed/fail)
- High recurrence frequency
- Room for improvement (not already near ceiling)

### 3. Replay (Dream Rollouts)

Run each recurring task K times with different variations. Learn from good-vs-bad contrast. This is optional and off by default — enable with `dream_rollouts=N`.

Optional experience recall: pull K most-similar past tasks from a persisted archive into tonight's dream (`recall_k=N`).

### 4. Consolidate

Apply bounded add/delete/replace edits to skill documents. For each edit:

```
reflect on contrast between successes and failures
→ propose bounded edit to current best skill
→ evaluate on held-out task set
→ accept only if held-out score improves
→ stage rejected edits as negative evidence
```

### 5. Stage and Adopt

Proposed improvements are staged for human review, not auto-merged. The human inspects the diff, the validation evidence, and decides whether to adopt.

## Configuration

| Knob | Default | Effect |
|------|---------|--------|
| `dream_rollouts` | 1 | Run each task K times → learn from contrast |
| `recall_k` | 0 | Pull K similar past tasks from archive |
| `dream_factor` | 0 | Add N synthetic variants per task |

## Validation Gate (Always On)

The gate is the critical safety mechanism. It prevents regressions by:

1. Scoring current best skill on held-out tasks (baseline)
2. Proposing bounded edit
3. Scoring edited skill on held-out tasks
4. Accepting only if score strictly improves
5. Rejecting and logging failed edits

Keep the validation gate **on** by default. Disabling it removes the safety boundary.

## Expected Behavior

- **Where tasks recur and have checkable correctness:** measurable improvement over nights
- **Where models are already near ceiling or benchmarks are noisy:** flat within run-to-run variance (±1–2 pts)
- **The gate keeps the worst case bounded:** failed edits don't ship

## Design Principles

- **Offline only:** Sleep happens between sessions, not during active work
- **Human in the loop:** Staged proposals, not auto-promoted changes
- **Zero inference-time overhead:** Deployed artifact is a compact `best_skill.md` with no extra model calls
- **Provenance preserved:** Every accepted edit carries source evidence, held-out context, and rollback guidance

## Applicability to AOMK

This pattern is relevant to AOMK's evaluator-optimizer and self-improvement work:

- **Dream cycle** maps to AOMK's dream-cycle skill
- **Evaluator-optimizer loop** maps to AOMK's evaluator-optimizer playbook
- **Skill revision** maps to AOMK's skill-revision skill

SkillOpt-Sleep provides a concrete implementation pattern for these abstract skills.

## Distillation note

Source: microsoft-skillopt `docs/sleep/README.md` and `skillopt_sleep/` package. Licensed under MIT. Adapted to AOMK pattern conventions.
