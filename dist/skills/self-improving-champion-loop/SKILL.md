---
name: Self-Improving Champion Loop
description: Bounded optimization loop that tests targeted challengers, protects an independently evaluated champion, and rejects suspiciously easy wins. Use when improving a prompt, policy, configuration, or other testable artifact where cheap iteration is useful but final acceptance must use fresh evidence.
tags: [loops, self-improvement, optimization, champion, evaluation]
type: Playbook
---

# Self-Improving Champion Loop

A bounded optimization loop that keeps a champion, tests challengers against fresh evidence, and rejects Goodhart's-law wins.

## When to use

- Improving a prompt, policy, configuration, or testable artifact
- Cheap iteration is useful but final acceptance must use fresh evidence
- You want bounded self-improvement without overfitting the metric

## How to run

1. **Initialize**: Set up champion state, independent working and gate signals, guard checks, improvement margin [N], budget, and experiment log.
2. **Propose**: Each cycle, read the latest failure in the log, propose one untried targeted change to the champion that addresses it. Skip any change already tried.
3. **Score**: Score the challenger on a cheap working signal. If not better than champion, log and continue.
4. **Gate**: If better on working signal, freeze the challenger and run the gate on fresh examples you did not inspect while editing, plus guard checks.
5. **Accept**: Only if gate score beats champion by [minimum margin] AND no guard regresses. Otherwise keep champion.
6. **Stop**: Budget exhausted → return champion. Log every outcome.

## State to track

- Champion: best current genome + gate score
- Budget: starts at [N], decrements each cycle
- Log: every tried genome and score
- Working signal: cheap tunable metric (separate from gate)
- Gate: fresh acceptance examples (never reuse for editing)
- Guards: safety/invariant checks that must not regress

## Verify / stop

Budget exhausted and the strongest verified champion is returned. Every challenger logged, no accepted change regresses a guard check.

## Key rules

- Separate the working signal from the gate (prevents overfitting)
- Fixed budget keeps search bounded
- Champion rule makes regression the default-safe outcome
- Treat suspiciously easy wins as Goodhart's law — reject them
- When uncertain, keep the champion
- Never reuse gate examples for editing
