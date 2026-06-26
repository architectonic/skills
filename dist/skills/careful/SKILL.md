---
name: Careful
description: Safety guardrails for destructive commands — warn before rm -rf, force-push, DROP TABLE, or production mutations. Use when touching production, debugging live systems, or working in shared environments.
tags: [agent-operations, agent-operations, safety, guardrails, destructive-commands]
type: Playbook
---

# Careful

Warn before destructive operations. User can override each warning.

## When to invoke

- Before any production-touching command
- When debugging live systems
- In shared environments
- When asked "be careful", "safety mode", "prod mode"

## Destructive commands to guard

| Command pattern | Risk | Default action |
|----------------|------|----------------|
| `rm -rf /` or `rm -rf` on important paths | Data loss | BLOCK, require explicit confirmation |
| `git push --force` to shared branches | Overwrites others' work | BLOCK, require explicit confirmation |
| `git reset --hard` | Loses uncommitted work | WARN, require confirmation |
| `DROP TABLE` or `DROP DATABASE` | Data loss | BLOCK, require explicit confirmation |
| `kubectl delete` on production | Service disruption | BLOCK, require explicit confirmation |
| `curl | sh` or untrusted install scripts | Supply chain risk | BLOCK, require explicit confirmation |
| Modifying production configs | Service disruption | WARN, require confirmation |
| Sending external messages (email, Slack, etc.) | External mutation | WARN, require confirmation |

## Override protocol

User can override any warning by confirming. But the warning must be explicit:
1. State what the command will do
2. State the risk
3. Require explicit "yes, I know" confirmation
4. Log the override for audit

## Key principles

- Default-deny for the most dangerous operations
- Warn for medium-risk operations
- Never block read-only operations
- When in doubt, warn
- A blocked command with explanation is better than an accidental data loss
