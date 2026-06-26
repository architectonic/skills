---
name: pr-comment-handler
description: Address review and issue comments on an open GitHub PR using gh CLI. Use when the user wants to respond to reviewer feedback, apply suggested fixes, or resolve review threads on the current branch's PR.
tags: [devops, github, pr, review, comments, gh-cli]
source: openai/skills gh-address-comments
type: Playbook
---

# PR Comment Handler

Find the open PR for the current branch and address its review comments using `gh` CLI.

## Prerequisites
- `gh` CLI installed and authenticated (`gh auth login` with repo + workflow scopes)
- Run `gh auth status` to verify before starting

## Workflow

### 1. Inspect comments needing attention
```bash
# Use the bundled script to fetch all comments and review threads
python scripts/fetch_comments.py
```

### 2. Summarize and ask
- Number all review threads and comments
- Provide a short summary of what would be required to apply a fix for each
- Ask the user which numbered comments should be addressed

### 3. Apply fixes
- Apply fixes for the selected comments only
- After each fix, summarize the diff and ask about opening a PR or pushing directly

## Notes
- If `gh` hits auth/rate issues mid-run, prompt the user to re-authenticate with `gh auth login`
- Only address comments the user explicitly selects
- Always show the diff before committing changes
