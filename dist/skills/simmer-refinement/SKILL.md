---
name: simmer-refinement
description: Iterative artifact refinement with criteria-driven judge board. Takes any artifact (code, doc, prompt, config, pipeline) and hones it over multiple rounds — each round, a panel of judges scores against your criteria and proposes the single highest-leverage improvement (ASI). Use when you have an artifact and want it better, especially when you can define what "better" means.
tags: [skill-management, software-development, refinement, iterative, quality, judge-board]
type: Playbook
---

# simmer-refinement

Iterative artifact refinement. A panel of judges reads your artifact, scores it against criteria, and proposes the single highest-leverage improvement (ASI). The generator applies it. Repeat.

**Source:** 2389-research/simmer (MIT) — https://github.com/2389-research/simmer

## When to Use

**Use simmer when:**
- You have an artifact and want it better
- You can define 2-3 quality criteria
- The artifact is worth iterating on (not throwaway)
- You want compound improvement, not random edits

**Don't use simmer when:**
- The artifact is already good enough
- You can't articulate what "better" means
- You need parallel exploration (use cookoff/omakase-off instead)

## Trigger Phrases

"simmer this", "refine this", "hone this", "iterate on this", "make this better", "polish this", "tighten this up"

## Setup

1. **Identify the artifact** — file or workspace
2. **Elicit 2-3 quality criteria** — what does "better" mean?
3. **Determine evaluation method** — judge-only (default), runnable (has test script), or hybrid

## The Loop

```
Iteration 0: Judge scores the seed artifact
Iteration 1: Generator applies ASI → Judge scores new candidate
Iteration 2: Generator applies ASI → Judge scores new candidate
... (default 3 rounds per batch, then ask whether to continue)
```

**ASI (Actionable Side Information):** The single highest-leverage fix the judge identifies. Not a rewrite — one focused direction per iteration. Compound gains over scattered edits.

## Judge Board

Simmer auto-selects between single judge and multi-judge board:

| Complexity | Setup | When |
|------------|-------|------|
| Simple | Single judge | Short email, tweet, ≤2 criteria |
| Complex | Judge board with deliberation | 3+ criteria, long artifact, code, pipelines |

The board constructs three judges tailored to your specific problem — not from a fixed menu, but by reading your artifact, criteria, and constraints and designing judges with diverse perspectives.

**Judges investigate before scoring** — they read the evaluator script, ground truth, prior candidates, and config files to understand the problem deeply.

## Evaluation Modes

| Mode | When to use |
|------|-------------|
| **Judge-only** (default) | Text artifacts — judge scores against criteria |
| **Runnable** | Code/pipelines — judge interprets script output |
| **Hybrid** | Both — run script AND judge results against criteria |

No format contract on evaluator output. The judge reads whatever your script produces.

## Regression Safety

The reflect subskill tracks the best candidate seen so far. If a new iteration scores lower, the best-so-far is preserved. `result.md` always contains the highest-scoring candidate, not just the latest.

## Output Structure

Single-file mode (`docs/simmer/`):
```
iteration-0-candidate.md    # Seed (original)
iteration-1-candidate.md    # Each improved candidate
iteration-2-candidate.md
trajectory.md               # Running score table
result.md                   # Final best candidate
```

Workspace mode: iterations tracked as git commits in the target directory.

## Criteria Suggestions by Artifact Type

| Artifact type | Suggested criteria |
|---------------|-------------------|
| Document / spec | clarity, completeness, actionability |
| Creative writing | narrative tension, specificity, voice consistency |
| Email / comms | value prop clarity, tone match, call to action strength |
| Prompt / instructions | instruction precision, output predictability, edge case coverage |
| API design | contract completeness, developer ergonomics, consistency |
| Pipeline / workflow | coverage, efficiency, noise |
| Configuration / infra | correctness, resource efficiency, maintainability |

## Advanced Features

- **Workspace targets** — refine a multi-file directory, iterations tracked as git commits
- **Runnable evaluators** — point at `python evaluate.py`, judge interprets output
- **Background constraints** — generator knows what's available (models, budget, latency)
- **Output contracts** — valid output has a defined shape (JSON schema), violations score 1/10
- **Validation commands** — cheap pre-check (`./validate.sh`) catches broken pipelines before full evaluator
- **Search space tracking** — reflect tracks tried vs. untried regions, judge steers toward gaps

## Context Isolation

- Generator doesn't see scores (avoids anchoring)
- Judge doesn't see previous scores (avoids drift)
- Each role gets only the context it needs

## Pitfalls

- **Don't skip criteria elicitation** — without clear criteria, the judge scores randomly
- **Don't use for parallel exploration** — simmer is serial iteration; use cookoff for parallel
- **Don't ignore the ASI** — the whole point is focused improvement, not random edits
- **Don't forget regression safety** — always check `result.md`, not the latest iteration
