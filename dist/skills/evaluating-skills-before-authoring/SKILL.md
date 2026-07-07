---
name: evaluating-skills-before-authoring
description: Build evaluations before writing skill documentation — baseline the agent without the skill, write minimal instructions to close observed gaps, and iterate from watched behavior using an author/consumer two-agent loop. Use when creating or improving a skill, deciding whether a skill is needed at all, or when a skill exists but agents ignore or misuse it.
tags: [skills, evaluation, skill-authoring, iteration, agent-operations, okf]
type: Playbook
domain: agent-operations
risk_level: low
requires_review: false
---

# Evaluating Skills Before Authoring

Write evaluations before documentation. Skills written from imagination document problems that never occur and miss the ones that do; skills written from observed failures earn every token they cost.

## Evaluation-driven development

```text
1. GAP       run the agent on representative tasks WITHOUT the skill; record specific failures
2. EVALS     write ≥3 scenarios that reproduce those failures (query, files, expected behavior)
3. BASELINE  measure performance without the skill — this is the bar to beat
4. MINIMAL   write just enough instruction to pass the evals; nothing speculative
5. ITERATE   run evals, compare to baseline, trim what didn't move the needle
```

Evaluation record shape:

```json
{
  "skills": ["target-skill"],
  "query": "representative user request",
  "files": ["fixtures/input.x"],
  "expected_behavior": ["observable check 1", "observable check 2", "observable check 3"]
}
```

Expected behaviors must be observable (file produced, rule applied, step not skipped) — not "understands the task."

## The author/consumer loop

Develop skills with two agent instances in different roles:

- **Author agent** — helps design and refine the skill; understands what agents need to be told.
- **Consumer agent** — a fresh instance with the skill loaded, given real tasks (not demos).

Cycle: author drafts → consumer runs a real task → human observes → specific failures go back to the author ("it forgot the date filter on regional reports — make that rule prominent") → revise → re-run. Iterate from observed behavior, never from assumption.

## Observe how the consumer navigates

- Reads files in an unexpected order → the structure isn't as intuitive as believed.
- Never follows a reference link → the link is under-signaled, or the content is dead weight.
- Re-reads one file constantly → that content belongs in the SKILL.md body.
- Skill never triggers → the description lacks the trigger vocabulary users actually use (fix discovery before touching the body).

## Test across models

A skill rides on a model. Verify with every model class that will use it: smaller models may need more scaffolding; stronger models are hindered by over-explanation. Aim for instructions that work across the fleet, or state the floor explicitly.

## When NOT to write the skill

If the baseline passes without the skill, stop — the model already knows. If failures trace to missing tools or permissions rather than missing knowledge, fix the harness instead (`engineering-agent-harnesses`). If the procedure changes weekly, keep it as a pointer to living docs, not a skill.

## Related skills

- `authoring-agent-skills` — format and structure once evals justify writing.
- `validation-gated-skill-improvement` — governance for changes to published skills.
