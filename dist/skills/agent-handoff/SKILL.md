---
name: Agent Handoff
description: Compact the current conversation into a handoff document for another agent to pick up. Use when work must be transferred to a fresh session or a different agent. Covers summarization, context preservation, and redaction of sensitive information.
tags: [agent-operations, agent-operations, handoff, context, cross-session]
type: Playbook
---

# Agent Handoff

Write a handoff document summarizing the current conversation so a fresh agent can continue the work.

## When to use

- Work must transfer to a fresh session
- A different agent will continue the task
- Context window is about to be lost
- Long-running work needs a checkpoint

## What to include

1. **Summary of work done** — what was accomplished
2. **Files changed** — with paths and commit SHAs if available
3. **Next action** — specific, not vague
4. **Decisions made** — with reasoning
5. **Assumptions** — labeled as assumptions
6. **Open questions** — not filled by inference
7. **Evidence of verification** — test output, API responses
8. **Suggested skills** — which skills the next agent should invoke

## Where to save

Save to the temporary directory of the user's OS, not the current workspace. Use a clear filename with timestamp.

## What NOT to include

- Do not duplicate content already in PRDs, plans, ADRs, issues, commits, diffs. Reference them by path or URL instead.
- Redact sensitive information: API keys, passwords, personally identifiable information.
- Do not include secrets or credentials.

## Tailoring

If the user passed arguments describing what the next session will focus on, tailor the handoff to that scope. A handoff for "fix the auth bug" is different from a handoff for "continue the refactor".
