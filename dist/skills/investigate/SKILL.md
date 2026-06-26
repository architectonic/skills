---
name: Investigate
description: Systematic root-cause investigation and debugging. Use when asked to "debug this", "fix this bug", "why is this broken", or "root cause analysis". Covers evidence gathering, hypothesis testing, and fix verification.
tags: [software-development, software-development, debugging, investigation, root-cause]
type: Playbook
---

# Investigate

Systematic debugging with root cause investigation. No fixes without investigation.

## When to invoke

- When asked "debug this", "why is this broken", "root cause analysis"
- When a bug report lacks clear reproduction steps
- When the cause of a failure is not obvious
- Before attempting any fix

## Investigation discipline

### Phase 1 — Understand the symptom
- What exactly is happening vs. what should happen?
- When did it start? What changed?
- Can it be reproduced consistently?
- What's the blast radius (who/what is affected)?

### Phase 2 — Gather evidence
- Read logs, error messages, traces
- Check recent commits, deployments, config changes
- Reproduce in a controlled environment
- Collect metrics, logs, and telemetry around the failure

### Phase 3 — Form hypotheses
- List possible causes ranked by likelihood
- For each hypothesis: what evidence would confirm or refute it?
- Design the cheapest test to eliminate the most likely cause
- Work from most likely to least likely

### Phase 4 — Test hypotheses
- Run the diagnostic test
- If confirmed → move to fix
- If refuted → go back to hypotheses, try next most likely
- Document what you ruled out and why

### Phase 5 — Fix and verify
- Make the smallest change that addresses the root cause
- Verify the symptom is gone
- Run regression tests
- Document the root cause and fix

## Key principles

- Never fix before you understand the cause
- A fix without investigation is a guess
- Evidence beats intuition
- The bug is always in the code you haven't looked at yet
- Document what you learned for future investigators
