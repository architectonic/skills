---
name: skill-optimization-loop
description: Pattern for optimizing agent skills through bounded text-space edits
  with validation gates. Use when you want to improve a skill document systematically
  without human rewriting — treat the skill as trainable state.
type: Playbook
title: Skill Optimization Loop
domain: agent-operations
tags:
- agent-operations
- okf
risk_level: medium
requires_review: true
source_family: agent-skills-standard
source_status: adapted
---

# Skill Optimization Loop

Treat agent skills as trainable artifacts. A separate optimizer model proposes bounded edits to a skill document; edits are accepted only when they improve held-out validation scores. The deployed artifact is a compact `best_skill.md` that runs against the unchanged target model.

## The Loop

```
Current skill (best_skill.md)
  ↓ Rollout: Execute skill on training tasks
  ↓ Reflect: Score each execution (pass/fail, quality metrics)
  ↓ Aggregate: Summarize failure patterns across the batch
  ↓ Select: Choose the worst-performing task as optimization target
  ↓ Update: Propose bounded edit (add/delete/replace) to skill text
  ↓ Evaluate: Run edited skill on HELD-OUT validation tasks
  ↓ Gate: Accept edit only if validation score strictly improves
  ↓ Reject buffer: Log rejected edits as negative evidence
Repeat for N epochs or until budget exhausted
```

## Edit Types

| Edit | Description | Risk |
|------|-------------|------|
| `add` | Insert a new instruction, example, or constraint | Low — expands skill |
| `delete` | Remove an instruction that causes confusion | Medium — may remove needed context |
| `replace` | Swap one instruction for a better one | Medium — changes behavior |

**Bounded**: Each epoch applies at most one edit type to one location in the skill document. No bulk rewrites.

## Validation Gate Rules

1. **Held-out only**: Validation tasks must never be used for training/optimization
2. **Strict improvement**: Edit is accepted only if validation score increases (no ties)
3. **Rollback**: Keep the previous best skill; rejected edits don't degrade the artifact
4. **Budget cap**: Maximum N edits per optimization run (prevents drift)

## Rejected Edit Buffer

Every rejected edit is logged:
- The proposed edit (diff)
- The validation score before and after
- The reason for rejection (score decreased, no change, or side effects)

This buffer prevents the optimizer from cycling through the same failed edits.

## Textual Learning Rate

Control optimization aggressiveness:
- **Conservative**: Only `add` edits, small insertions
- **Moderate**: `add` + `replace`, single-sentence scope
- **Aggressive**: All edit types, paragraph-level scope

Start conservative. Increase only when the skill is stable and the optimizer has a strong signal.

## Epoch-Wise Meta Update

After each epoch, the optimizer can update its own strategy (not the skill):
- Which edit types have been most successful
- Which sections of the skill are most sensitive to change
- Whether to increase or decrease learning rate

This is the "meta" layer — it optimizes the optimizer, not the skill directly.

## Deployment

The output is a single `best_skill.md`:
- Typically 300–2,000 tokens
- No inference-time model calls (the optimization is offline)
- Transfers across model scales and agent harnesses without re-optimization
- Version each released skill with the validation score and epoch count

## Anti-Patterns

- **Don't optimize against training tasks**: Always validate on held-out data
- **Don't allow unbounded edits**: One change at a time, measure impact
- **Don't deploy untested optimizations**: The gate is the gate
- **Don't mix optimization with runtime**: Keep the optimizer offline

## Source

Distilled from SkillOpt (`microsoft/SkillOpt`, `arxiv:2605.23904`), which implements this loop with multi-backend support (OpenAI, Azure, Claude, Qwen, MiniMax) and reports +23.5 point accuracy improvement on direct chat and +24.8 inside Codex agentic loops.
