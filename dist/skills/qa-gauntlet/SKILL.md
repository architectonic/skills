---
name: QA Gauntlet
description: Pre-completion checklist for agent work. Use before declaring work done, handing off, or reporting completion. Covers scope, correctness, test, and review checks.
tags: [agent-operations, agent-operations, quality-gate, completion, checklist]
type: Playbook
---

# QA Gauntlet

## Purpose

A final checklist before declaring work complete. Catches scope creep, unverified claims, and missing documentation.

## When to Use

- Before declaring a task done
- Before handing off to another agent
- Before reporting completion to a user
- After any substantial change

## Checklist

### Scope Check

- [ ] The named problem is understood.
- [ ] The affected files are known.
- [ ] The change is no broader than necessary.
- [ ] Non-goals were respected.

### Correctness Check

- [ ] The implementation matches the requested behavior.
- [ ] Edge cases were considered.
- [ ] Errors are handled intentionally.
- [ ] No unrelated behavior was changed.

### Test Check

Record what was run:

```
Command:
Result:
Notes:
```

When tests cannot run, record why:

```
Reason:
Risk:
Manual verification:
```

### Review Check

- [ ] No secrets or private data were added.
- [ ] No dead code or placeholder logic was left behind.
- [ ] No speculative abstractions were added.
- [ ] The final response names changed files and verification.

## Completion Statement

When declaring work complete, always state:

```
Changed:
Verified:
Known risks:
Next step:
```

## Procedure

1. Run through all four checks (scope, correctness, test, review).
2. For each unchecked item, either complete it or explicitly state why it does not apply.
3. Write the completion statement.
4. If any check fails, fix the issue before declaring done.

## Verification

- The completion statement is present and specific.
- Changed files are listed.
- Known risks are stated.

## Failure Modes

- Skipping the checklist → undetected scope creep or unverified claims.
- Checking boxes without actually performing the check → false completion.
- Leaving "Known risks" empty when risks exist → misleading completion report.

## Security Notes

- Low risk: QA Gauntlet is a verification discipline.
- The main risk is false completion — declaring done when issues remain.
