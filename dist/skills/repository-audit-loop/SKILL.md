---
name: repository-audit-loop
description: Audit a codebase using a strong model for judgment and prioritization, then delegate implementation to cheaper agents via self-contained plans in disposable worktrees. Use when the user wants systematic repository improvement, codebase health audits, or prioritized fix campaigns. Covers strong-model audit, false-positive vetting, plan writing, cheap-model execution, diff review, and backlog reconciliation.
tags: [loops, skill-management, repository-audit, evaluator-optimizer, worktree, delegation]
type: Playbook
---

# Repository Audit Loop

Strong model audits and plans. Cheap model executes. Human decides on merge.

## When to use

- User wants a systematic codebase health audit
- User wants prioritized improvement suggestions with implementation
- Repository has accumulated technical debt needing triage
- You need to separate expensive judgment from cheap execution

## Core Pattern (from shadcn/improve)

```text
Map repository
→ Audit findings
→ Vet false positives
→ Prioritize by leverage
→ Write executable plan
→ Delegate execution (disposable worktree)
→ Review diff against plan
→ Reconcile backlog
```

## Roles

### Strong Model (Auditor + Planner)
- Performs codebase understanding, judgment, prioritization, spec writing
- Produces prioritized findings with evidence (file paths, line numbers)
- Writes self-contained implementation plans

### Cheap Model (Executor)
- Reads the plan, nothing else from the audit
- Implements in a disposable worktree
- Produces a diff the auditor can review

### Human (Decider)
- Reviews audit findings before execution begins
- Reviews diffs before merge
- Decides what to merge, defer, or reject

## Plan Format

Each plan must be self-contained:

- File paths and current-state excerpts
- Repository conventions observed
- Commands to run and expected outputs
- Done criteria (binary, testable)
- Scope boundaries (what NOT to change)
- Stop conditions (when to ask rather than guess)

## Execution Rules

1. Create a disposable worktree for each plan or plan batch
2. Executor reads only the plan, not the full audit
3. Review diff against plan before any merge
4. Reconcile backlog: verify landed work, refresh drifted plans, retire stale findings
5. Never merge without human review

## Anti-Patterns

- Do not let the executor improvise beyond the plan
- Do not merge without diff review
- Do not let audit findings accumulate without reconciliation
- Do not use the same model for audit and execution (defeats the cost/quality separation)

## Workframe Position

This is a high-value loop for Workframe. The plan is the durable artifact. The worktree is disposable. The human is the merge gate.
