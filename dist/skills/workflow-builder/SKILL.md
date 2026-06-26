---
name: Multi-Agent Workflow Orchestration
description: Design and write deterministic multi-agent workflow scripts for fan-out, pipeline, loop, and judge-panel orchestration patterns.
tags: [software-development, workflow, multi-agent, orchestration, pipeline, fan-out]
type: Playbook
---

# Workflow Builder

Design and write deterministic multi-agent workflow scripts for orchestrating sub-agents (fan-out, pipeline, loop, judge-panel). Only leaf `agent()` calls spend tokens, so the main session stays clean and the whole run is resumable.

## Source

Distilled from claude-skills (`.gemini/skills/workflow-builder`), MIT license.
Inspired by [Ray Amjad's claude-code-workflow-creator](https://github.com/ray-amjad/claude-code-workflow-creator).

## When to Use

- Many sub-agents in a fixed topology, deterministic + resumable
- Parallel processing of independent items (fan-out)
- Sequential processing where each stage needs the prior result (pipeline)
- Iterative refinement until a budget or criterion is met (loop)
- Multiple independent judges scoring the same artifact (juduate-panel)

## Decide if a workflow is even the right tool

| Scenario | Use |
|----------|-----|
| Single sub-agent, one task | plain Agent tool |
| Reusable procedure, agent picks steps dynamically | a Skill |
| Many sub-agents in a fixed topology, deterministic + resumable | **Workflow** ✓ |

Workflows earn their cost when work is parallel or multi-stage, must be reproducible, long enough to fail halfway (so resume matters), or benefits from isolating each step in its own context window. For one-off tasks, just use the agent directly.

## Topologies

| Topology | Shape | Use when |
|----------|-------|----------|
| **Fan-out** | N agents in parallel, independent | Items don't depend on each other |
| **Pipeline** | Stage N feeds Stage N+1 | Each step needs the prior result |
| **Loop** | Repeat until budget/criterion | Iterative refinement |
| **Judge-panel** | N agents score same artifact | Independent perspectives needed |

## ALWAYS start every session with intake (non-negotiable)

Before proposing or writing any workflow, run the intake:

1. **Ask what kind of workflow they want:**
   - What repeatable, multi-step task do you want to automate?
   - What is the one unit of work a single sub-agent does once?
   - How many units — a known list, or discovered by looping?
   - Do later steps need *all* prior results at once, or can each item flow on its own?
   - Does any step need structured data back (a verdict, a list, scores)?
   - Roughly how many tokens / how deep should it go?

2. **If the user is vague, do NOT stall.** Run the recommendation engine to turn whatever you have into 1-2 concrete proposals, then present them *with the reasoning*.

3. **Confirm the shape with the user** (topology + phases + parallel-vs-pipeline) before writing the file. This is the only approval gate.

## Build → validate → run loop

1. **Scaffold** a starter from the confirmed topology
2. **Edit** the file: `meta` block first (pure literal, first statement), then the async body using the injected globals — `agent()`, `pipeline()`, `parallel()`, `phase()`, `log()`, `budget`, `args`, `workflow()`
3. **Validate** before running — catches the parser-fatal mistakes
4. **Run** it and watch it live. Press **P** to pause/resume, **X** to skip a sub-agent. Failed agents retry automatically.

## Hard rules (validator enforces these)

- `meta` is a **pure literal** and the **first statement** — no variables, spreads, template strings, or function calls inside it.
- **No non-determinism:** `Date.now()`, `Math.random()`, argless `new Date()` break resume — pass timestamps via `args`.
- **No filesystem / Node APIs** (`require`, `fs`, `process`, network) in the orchestrator — that work belongs *inside* `agent()` prompts.
- `parallel()` takes **thunks** (`() => agent(...)`), not bare promises. Default to `pipeline()` unless a stage needs the whole prior result set.
- **Guard every open-ended loop** with a counter or `budget.remaining()` check — unguarded loops hit caps.
- Filter skipped/failed agents: `results.filter(Boolean)`.

## Tooling

- `scripts/workflow_intake.py` — intake recommendation engine (topology + model + budget + rationale from vague input).
- `scripts/validate_workflow.py` — stdlib linter for the rules above; PASS / WARN / FAIL with line numbers.
- `scripts/scaffold_workflow.py` — generate a starter `.js` for any topology.
- `assets/templates/` — fan-out, pipeline, loop-until-budget starters. `assets/examples/` — a complete runnable workflow.

All scripts run with `--sample` (no args) and `--help`.

## Cross-References

- Related: `autonomous-ai-agents/agent-swarm-orchestration` — broader multi-agent coordination patterns
- Related: `autonomous-ai-agents/coding-agent-clis` — orchestrating coding agent CLIs
