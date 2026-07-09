---
name: Diagnosing Bugs
description: Systematic diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug this", or reports something broken/throwing/failing/slow. Covers feedback-loop construction, bisection, differential testing, and instrumentation with browser, trace, fuzz, and human-in-the-loop surfaces review-gated.
tags: [software-development, debugging, diagnosis, performance, testing]
type: Playbook
domain: software-engineering
risk_level: medium
requires_review: true
review_gate: repository-owner-authorized-diagnostics-only
source_status: reviewed-metadata-only
review_notes:
  - Browser/headless automation, captured trace replay, real payload fixtures, fuzzing, bisection automation, and human-in-the-loop scripts can expose credentials, private data, account state, or external systems.
  - Package-facing use must preserve read-only, authorized diagnostic boundaries and redact captured artifacts before sharing or persistence.
---

# Diagnosing Bugs

A discipline for hard bugs. Skip phases only when explicitly justified.

## Authorization and data boundary

Use this skill only on systems, repositories, accounts, test fixtures, logs, and traces that the user is authorized to inspect. Treat browser sessions, captured requests, event logs, screenshots, DOM dumps, console output, and network payloads as sensitive by default.

Before persisting or sharing diagnostic artifacts, remove secrets, session tokens, cookies, personal data, private URLs, production identifiers, and unrelated user content. Prefer synthetic fixtures over real payloads whenever they reproduce the failure.

## Phase 1 — Build a feedback loop

This is the skill. Everything else is mechanical. If you have a tight pass/fail signal for the bug — one that goes red on this bug — you will find the cause. If you do not have one, staring at code is usually wasted effort.

Spend disproportionate effort here. Be aggressive about reducing the bug to a reliable signal, but keep the loop bounded, reversible, and safe.

### Feedback-loop options

Try the lowest-risk loop that reaches the bug:

1. Failing test at the smallest seam that reproduces the issue: unit, integration, or end-to-end.
2. HTTP-level reproduction against an authorized development or staging service.
3. CLI invocation with a minimal fixture input and a known-good output snapshot.
4. Throwaway harness that exercises only the relevant code path.
5. Property or fuzz loop with bounded input ranges, runtime limits, and no external side effects.
6. Bisection harness for an isolated repository state with deterministic setup and teardown.
7. Differential loop that compares old and new versions using the same sanitized fixture.
8. Browser or headless UI loop only after explicit review, using test accounts, non-production data, and redacted outputs.
9. Captured-trace replay only after explicit review, with sanitized payloads and no credential/session material.
10. Human-in-the-loop script only as a last resort, with clear stop conditions and no hidden mutation.

## High-risk diagnostic surfaces

The following surfaces require explicit review before use in package-facing or automated workflows:

- browser or headless automation that touches authenticated sessions, accounts, production URLs, or third-party services;
- DOM, console, screenshot, storage, cookie, or network capture;
- replay of real requests, payloads, event logs, or customer traces;
- fuzz/property loops that can trigger external mutation, denial-of-service behavior, or unbounded resource use;
- bisection harnesses that boot services, mutate data, or depend on external accounts;
- human-in-the-loop scripts that can direct someone to perform destructive or account-changing actions.

When a high-risk surface is necessary, document the authorization, environment, data minimization, redaction plan, retention policy, and rollback/cleanup path before running it.

## Phase 2 — Find the cause

Once you have a tight feedback loop:

- bisect between known-good and known-bad states when history can isolate the regression;
- form one hypothesis at a time and test it through the loop;
- narrow to the smallest code path that reproduces the issue;
- read the local project context, architecture notes, and decision records for the affected area;
- keep diagnostic artifacts scoped to the bug and remove unrelated captured data.

## Phase 3 — Fix and verify

- Make the smallest change that fixes the bug.
- Verify the feedback loop now passes.
- Run the relevant broader test suite to check for regressions.
- Add a regression test so this bug cannot return silently.
- Remove temporary harnesses, logs, captures, and fixtures unless they are sanitized and intentionally retained.

## Key principles

- No feedback loop means no diagnosis.
- Prefer synthetic fixtures over production traces.
- Prefer read-only inspection over mutation.
- Vertical slices beat broad rewrites: one test, one fix, one verification pass.
- The bug is often in the code you least want to inspect.
