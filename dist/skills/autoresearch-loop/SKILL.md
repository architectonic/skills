---
name: Autoresearch Loop
description: Autonomous iteration loop — modify, verify, keep/discard against any metric. Use when the user wants to iteratively improve code, hunt bugs, audit security, or optimize against a measurable goal without manual step-by-step guidance.
tags: [loops, autonomous, iteration, optimization, debugging, security, evaluation]
domain: agent-operations
risk_level: medium
requires_review: true
source_license: Apache-2.0 with skill-specific notices
source_status: distilled-reviewed
review_note: Requires explicit human approval before push, publish, deploy, irreversible mutation, security testing outside authorized scope, or unbounded iteration.
distilled_at: 2026-06-22
type: Metric
---

# Autoresearch Loop

## Purpose

Run autonomous iteration loops that modify, verify, and keep/discard changes against a measurable metric. The agent drives the loop; the human sets the goal and constraints.

## Safety Invariants

- **Never push, publish, or deploy** without explicit user approval.
- **Bounded by default** — override only with `Iterations: unlimited`.
- **All results logged** to `autoresearch/{subcommand}-{YYMMDD}-{HHMM}/`.
- **Chain handoff** via `handoff.json`. Evals read `*-results.tsv`.

## Subcommands

| Command | Purpose | Default Iterations |
|---|---|---|
| `$autoresearch` | Iterate against a metric: modify → verify → keep/discard | 25 |
| `$autoresearch plan` | Convert goal into validated Scope, Metric, Verify config | N/A |
| `$autoresearch debug` | Hunt bugs: hypothesize → test → falsify → repeat | 15 |
| `$autoresearch fix` | Crush errors one-by-one until zero remain | 20 |
| `$autoresearch security` | STRIDE + OWASP audit with red-team personas | 15 |
| `$autoresearch ship` | Ship through 8 phases: checklist → dry-run → deploy → verify | N/A |
| `$autoresearch scenario` | Generate edge cases across 12 dimensions | 20 |
| `$autoresearch predict` | 5 expert personas debate before implementation | N/A |
| `$autoresearch learn` | Scout codebase → generate docs/wiki → validate → fix loop | 10 |
| `$autoresearch reason` | Adversarial debate with blind judges until convergence | 8 |
| `$autoresearch probe` | 8 personas interrogate requirements until saturation | 15 |
| `$autoresearch improve` | Research ICP challenges, discover improvements, generate PRDs | 15 |
| `$autoresearch evals` | Analyze iteration results: trends, plateaus, regressions | N/A |
| `$autoresearch regression` | Regression stability gate: baseline vs candidate, verdict STABLE/UNSTABLE | N/A |

## Universal Flags

| Flag | Applies To | Purpose |
|---|---|---|
| `Iterations: N` | All looping | Set iteration count |
| `Iterations: unlimited` | All looping | Opt-in unbounded |
| `--evals` | All looping | Mid-loop checkpoints + final summary |
| `--evals-interval N` | All looping | Override checkpoint frequency |
| `--chain <targets>` | All | Sequential handoff after completion |

## Workflow

1. **Define the goal** — what does "better" mean? Get a measurable metric.
2. **Set the scope** — which files, which functions, which behaviors are in play.
3. **Set the budget** — iteration count, time limit, or cost ceiling.
4. **Run the loop** — modify → verify → keep/discard.
5. **Report** — what changed, what improved, what regressed, what's next.

## Anti-patterns

- **No metric** — "make it better" is not a goal. Define a number.
- **Unbounded without approval** — always cap iterations unless the user explicitly says "unlimited".
- **Silent mutation** — log every iteration. If you can't show the trace, you didn't do the work.

## When to Use

- Optimizing a function against a benchmark
- Hunting a Heisenbug with repeated test runs
- Security auditing with STRIDE personas
- Iteratively improving code quality metrics
- Generating edge-case test scenarios

## When NOT to Use

- The task requires human judgment at each step
- The change is irreversible and the user hasn't approved the approach
- No measurable metric exists
