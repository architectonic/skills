---
name: Diagnosing Bugs
description: Systematic diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug this", or reports something broken/throwing/failing/slow. Covers feedback-loop construction, bisection, differential testing, and instrumentation.
tags: [software-development, software-development, debugging, diagnosis, performance, testing]
type: Playbook
---

# Diagnosing Bugs

A discipline for hard bugs. Skip phases only when explicitly justified.

## Phase 1 — Build a feedback loop

This is the skill. Everything else is mechanical. If you have a tight pass/fail signal for the bug — one that goes red on THIS bug — you will find the cause. If you don't have one, no amount of staring at code will save you.

Spend disproportionate effort here. Be aggressive. Be creative. Refuse to give up.

### Ways to construct a feedback loop (try in order)

1. **Failing test** at whatever seam reaches the bug — unit, integration, e2e
2. **Curl / HTTP script** against a running dev server
3. **CLI invocation** with a fixture input, diffing stdout against a known-good snapshot
4. **Headless browser script** (Playwright / Puppeteer) — drives UI, asserts on DOM/console/network
5. **Replay a captured trace** — save a real network request / payload / event log to disk; replay through the code path in isolation
6. **Throwaway harness** — spin up a minimal subset of the system that exercises the bug code path
7. **Property / fuzz loop** — run 1000 random inputs and look for the failure mode
8. **Bisection harness** — automate "boot at state X, check, repeat" so you can `git bisect run`
9. **Differential loop** — run same input through old vs new version and diff outputs
10. **HITL bash script** — last resort. Drive the human with a structured loop.

## Phase 2 — Find the cause

Once you have a tight feedback loop:
- Bisect between known-good and known-bad states
- Form hypotheses and test them with the loop
- Narrow to the smallest code path that reproduces the issue
- Read CONTEXT.md and ADRs in the area you're touching

## Phase 3 — Fix and verify

- Make the smallest change that fixes the bug
- Verify the feedback loop now passes
- Run the full test suite to check for regressions
- Add a regression test so this bug cannot return silently

## Key principles

- No feedback loop = no diagnosis. Don't skip phase 1.
- Vertical slices, not horizontal. One test → one fix → repeat.
- The bug is always in the code you don't want to look at.
