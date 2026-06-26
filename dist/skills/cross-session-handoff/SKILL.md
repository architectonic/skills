---
name: cross-session-handoff
description: Compact the current conversation into a handoff document for another agent or fresh session to pick up. Use when a thread is full, you need to branch off (e.g., into a prototype session), or you want to preserve context across session boundaries. This is a fork — you open a new session and reference the handoff file to carry context across.
tags: [agent-operations, agent-operations, handoff, session-management, context-preservation]
source: mattpocock/skills — skills/productivity/handoff/SKILL.md (MIT license)
type: Playbook
---

# Cross-Session Handoff

Compact the current conversation into a handoff document so a fresh agent or session can continue the work.

## When to Use

- The current context window is approaching its limit and you need a fresh session
- You need to branch off into a parallel session (e.g., a prototype session)
- You want to preserve the full conversation state for later resumption
- Work will continue in a different context window but needs the current thinking

## What to Include

Write the handoff document to a temporary directory (not the current workspace). Include:

1. **What was being done** — the task or goal
2. **Current state** — where things stand right now
3. **Key decisions made** — any decisions that affect future work
4. **Open questions** — things still unresolved
5. **Suggested skills** — which skills the next agent/session should invoke
6. **References** — paths or URLs to PRDs, plans, ADRs, issues, commits, diffs

## What NOT to Include

- **Do not duplicate** content already captured in other artifacts (PRDs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.
- **Do not include sensitive information** — redact API keys, passwords, or personally identifiable information.

## Tailoring

If the user specifies what the next session will focus on, tailor the handoff document accordingly. Emphasize the context most relevant to that focus.

## How It Differs from Compact

- **`/handoff`** (this skill): **Fork** — you open a new session and reference the handoff file. The original session ends.
- **`/compact`** (built-in): **Continue** — stay in the same conversation, letting earlier turns be summarized. Use at intentional breaks between phases.

## Verification

A fresh agent reading only the handoff document should be able to continue the work without rereading the full original conversation.
