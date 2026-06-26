---
name: Autonomy Loop
description: Implement a builder-reviewer autonomy loop where two agents pass a git baton between worktrees and prove each new test catches its fix. Use when a repository has deterministic test, build, and lint gates plus a task suited to repeated builder-reviewer handoffs.
tags: [loops, autonomy, builder-reviewer, worktrees, testing]
type: Playbook
---

# Autonomy Loop

A builder-reviewer autonomy loop that passes a git baton between worktrees and proves each new test catches its fix.

## When to use

- Repository has deterministic test, build, and lint gates
- Task is suited to repeated builder-reviewer handoffs
- You want adversarial verification that tests actually catch bugs

## How to run

1. **Initialize**: Configure deterministic gates and protected paths. Create separate builder and reviewer worktrees.
2. **Builder wave**: Builder reads LOOP-STATE.md, makes one bounded change, adds a red-before-green-after test, hands off.
3. **Reviewer wave**: Reviewer reruns every gate and uses revert-or-mutate proof to show the test catches the change.
4. **Accept**: Only on both passes. Otherwise return findings or park the wave for a human when a circuit breaker fires.
5. **Finish**: Commit, gate evidence, test proof, trust tier, and risks.

## Verify / stop

Every accepted wave passes the proof-of-test gate:
- New test fails without the change
- New test passes with the change
- Every configured gate passes
- Protected production changes remain human-gated

## Why it works

Separate worktrees and a git-backed LOOP-STATE.md baton keep the roles independent and resumable. The revert-or-mutate check catches tests that execute code without proving the fix.

## Key rules

- Builder makes exactly one bounded change per wave
- Reviewer must prove the test catches the change (not just that it passes)
- Protected changes always require human approval
- Park repeated-failure work for a human (circuit breaker)
- Log every wave in LOOP-STATE.md for resumability
