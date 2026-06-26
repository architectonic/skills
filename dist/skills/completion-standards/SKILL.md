---
name: completion-standards
description: Define and verify completion criteria for agent tasks. Use when starting a task, verifying work is done, or handing off to another agent. Covers done standards, completion statements, proceed criteria, and anti-patterns.
tags: [agent-operations, agent-operations, quality-gate, handoff]
type: Playbook
---

# completion-standards

Define and verify that agent work is truly complete before declaring done or handing off.

## The completion standard

Every task must satisfy **all** of:
1. **Explicit criteria met** — all stated requirements fulfilled
2. **Verification performed** — tests run, output inspected, diff reviewed
3. **No known defects** — no TODOs, FIXMEs, or known issues left unresolved
4. **Clean state** — no debug code, temporary files, or commented-out experiments
5. **Documented** — changes are explained, decisions are logged

## Completion statement format

When declaring a task complete, state:
```
DONE: [what was completed]
VERIFIED: [how you verified it]
CHANGED: [files modified]
OPEN: [any remaining questions or follow-ups]
```

## Proceed criteria

Before starting any task, confirm:
- [ ] Goal is clear and specific
- [ ] Success criteria are defined
- [ ] Dependencies are available
- [ ] Scope boundaries are set (what's NOT included)
- [ ] Rollback plan exists (how to undo if wrong)

## Anti-patterns

- **"It probably works"** — not verification
- **"I'll clean it up later"** — later never comes
- **"The tests pass"** — but you didn't check edge cases
- **"Done enough"** — either it meets the criteria or it doesn't
- **Handing off incomplete work** — the next agent shouldn't inherit your debt

## Sources
- curator/root-meta/qa_gauntlet.md — scope check and correctness verification
- curator/legacy/cognition/decision_principles.md — decision review framework
- curator/legacy/cognition/reasoning_principles.md — reasoning discipline
