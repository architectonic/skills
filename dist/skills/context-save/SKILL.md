---
name: Context Save
description: Save working context (git state, decisions, remaining work) so any future session can pick up without losing progress. Use when asked to "save progress", "save state", "context save", or before switching tasks.
tags: [agent-operations, agent-operations, context, state-management, checkpoint]
type: Playbook
---

# Context Save

Capture git state, decisions made, and remaining work so a future session can resume.

## When to invoke

- Before switching tasks or contexts
- Before a session might end
- After completing a meaningful chunk of work
- When asked "save progress" or "save state"

## What to capture

1. **Git state**: current branch, uncommitted changes, recent commits
2. **Decisions made**: key architectural or implementation choices with reasoning
3. **Remaining work**: what's left to do, in priority order
4. **Open questions**: unknowns that need resolution
5. **Blockers**: external dependencies or approvals needed
6. **File paths**: key files modified or referenced

## Output format

Save to a context file (location configurable). Include:
- Timestamp
- Session summary
- Git status (branch, modified files, last 5 commits)
- Decisions log (decision | reasoning | alternatives considered)
- TODO list (priority-ordered)
- Blockers and open questions

## Pairing

Use with context-restore to resume from a saved state. The restore skill reads this file and re-establishes the working context.

## Key principles

- Save proactively, not just when asked
- Include enough detail for a fresh agent to understand the context
- Don't save secrets or credentials
- Reference artifacts (PRs, issues, ADRs) by URL rather than duplicating content
