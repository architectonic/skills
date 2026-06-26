---
name: Hook Development
description: Create event-driven hooks for Claude Code plugins. Use when building PreToolUse, PostToolUse, Stop, SessionStart, or other hook events.
tags: [mcp, hooks, event-driven, plugins]
type: Playbook
---

# Hook Development

Hooks are event-driven automation scripts that execute in response to Claude Code events.

## Sub-Skills

| Skill | When to Use |
|-------|-------------|
| [hook-basics](hook-basics.md) | Understand hook types (prompt vs command), configuration formats |
| [hook-events](hook-events.md) | Implement specific hook events (PreToolUse, PostToolUse, Stop, etc.) |
| [hook-security](hook-security.md) | Follow security best practices, validate inputs, handle performance |
| [hook-debugging](hook-debugging.md) | Debug, test, and troubleshoot hooks |

## Core Concepts

- **Prompt-based hooks**: LLM-driven decisions, flexible, context-aware
- **Command hooks**: Bash commands, fast, deterministic
- **Matchers**: Filter which tools/events trigger the hook
- **Output**: JSON with decision, updatedInput, systemMessage
