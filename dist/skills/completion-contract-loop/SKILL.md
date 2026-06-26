---
name: Completion Contract Loop
description: Define completion up front, track proof for every requirement, and prevent partial work from being reported as done. Use for long-running tasks, pull requests, runtime checks, or user-visible artifacts where a plausible partial result could be mistaken for completion.
tags: [loops, completion, verification, requirements, evidence]
type: Playbook
---

# Completion Contract Loop

A goal-planner workflow that defines completion up front, tracks proof for every requirement, and prevents partial work from being reported as done.

## When to use

- Long-running tasks where partial work could be mistaken for done
- Pull requests that must be verified against requirements
- Runtime checks or user-visible artifacts
- Any task where "done" is ambiguous

## How to run

1. **Define done**: Before acting, define every required outcome and its evidence. Record requirements, scope, non-goals, evidence plan, and current status.
2. **Execute**: One bounded action at a time. After each action, mark requirements as: proved, weak, missing, or contradicted.
3. **Audit**: Before closure, audit every requirement. Preserve honest blocked, exhausted, stalled, or contradicted states.
4. **Complete**: Only when ALL requirements are proved. Otherwise stop as blocked, stalled, or exhausted.

## State tracking

For each requirement, track:
- Status: proved | weak | missing | contradicted
- Evidence: what proves this requirement is met
- Owner: who is responsible
- Next action: what would move this forward

## Verify / stop

Every requirement has current, adequate proof. The final audit contains no weak, missing, or contradicted required item. Otherwise the work remains open, blocked, or exhausted.

## Why it works

A durable completion contract keeps the definition of done visible across long sessions. Mapping every requirement to evidence makes false completion easy to detect.

## Key rules

- Define completion BEFORE acting (not after)
- Never report budget exhaustion or errors as success
- Weak, missing, or contradicted = work remains open
- Ask before creating persistent state (e.g. goal files)
- Honest blocked/stalled states are better than false done
