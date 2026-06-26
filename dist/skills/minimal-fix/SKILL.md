---
name: Minimal Fix
description: Produce the smallest possible code change that fixes a specific, well-scoped issue (CI failure, reviewer comment, typo). Use only when the fix target is explicit. Never refactor unrelated code. One problem per invocation.
source: loop-engineering/skills/minimal-fix/SKILL.md (MIT license, https://github.com/anthropics/loop-engineering)
category: agent-operations
tags: [agent-operations, loop, fix, minimal, ci, bug-fix, agent-operations]
type: Playbook
---

# Minimal Fix

You fix **one specific problem** with the **smallest diff** that could work.

## Inputs

- Exact failure message, reviewer comment, or issue description
- File(s) implicated (if known)
- Project build/test commands (from AGENTS.md or project skills)
- Path denylist (from loop safety policy — never edit `.env`, `auth/`, `payments/`, secrets)

## Process

1. Reproduce or confirm the failure locally if possible.
2. Identify the minimal root cause — not symptoms in distant files.
3. Change only what is required. No drive-by refactors.
4. Run tests/lint relevant to the change.
5. Summarize: what changed, why, what you ran.

## Output

```markdown
## Minimal Fix Proposal

### Target
(one sentence)

### Diff summary
(files + what changed)

### Verification run
(command + result)

### Risks / human review needed?
(yes/no + why)
```

## Rules

- One problem per invocation. Multiple failures → escalate or triage first.
- Respect denylist paths — escalate instead of editing.
- Prefer worktree isolation when the loop runs unattended.
- Do not mark your own work done — the verifier decides.

## Denylist Paths

The following paths must NEVER be edited by an automated loop:
- `.env` and any file containing secrets/credentials
- `auth/` — authentication logic (security-sensitive)
- `payments/` — payment processing (financial risk)
- Any file containing API keys, tokens, or private keys
- Database migration files (require human review)

If the fix requires changes to denylist paths, escalate to human with a clear explanation of what needs to change and why.

## Scope Discipline

```
❌ BAD: "Fixed the bug and also refactored the nearby function"
✅ GOOD: "Fixed the off-by-one error in line 42"

❌ BAD: "Updated the config and also cleaned up imports"
✅ GOOD: "Changed timeout from 5000 to 10000 in config.yaml"

❌ BAD: "Fixed the test and also updated 3 other test files"
✅ GOOD: "Added missing assertion in test_auth.py line 87"
```

## Integration with Loop Verifier

This skill produces a fix proposal. The **loop-verifier** skill must independently verify the fix before it is applied. The minimal-fix agent must NOT:
- Mark its own work as done
- Apply the fix without verifier approval
- Skip the verification step
