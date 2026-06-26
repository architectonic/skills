---
name: Hook Events
description: Implement specific hook events — PreToolUse, PostToolUse, Stop, SubagentStop, UserPromptSubmit, SessionStart, SessionEnd, PreCompact, Notification. Use when building hooks for specific Claude Code lifecycle events.
tags: [mcp, hooks, events, PreToolUse, PostToolUse, Stop, SessionStart]
type: Playbook
---

# Hook Events

## PreToolUse

Execute before any tool runs. Use to approve, deny, or modify tool calls.

```json
{
  "PreToolUse": [
    {
      "matcher": "Write|Edit",
      "hooks": [
        {
          "type": "prompt",
          "prompt": "Validate file write safety. Check: system paths, credentials, path traversal, sensitive content. Return 'approve' or 'deny'."
        }
      ]
    }
  ]
}
```

**Output:**
```json
{
  "hookSpecificOutput": {
    "permissionDecision": "allow|deny|ask",
    "updatedInput": {"field": "modified_value"}
  },
  "systemMessage": "Explanation for Claude"
}
```

## PostToolUse

Execute after tool completes. Use to react to results, provide feedback, or log.

```json
{
  "PostToolUse": [
    {
      "matcher": "Edit",
      "hooks": [
        {
          "type": "prompt",
          "prompt": "Analyze edit result for potential issues: syntax errors, security vulnerabilities, breaking changes. Provide feedback."
        }
      ]
    }
  ]
}
```

**Output behavior:** Exit 0 = stdout shown, Exit 2 = stderr fed back to Claude

## Stop

Execute when main agent considers stopping. Use to validate completeness.

```json
{
  "Stop": [
    {
      "matcher": "*",
      "hooks": [
        {
          "type": "prompt",
          "prompt": "Verify task completion: tests run, build succeeded, questions answered. Return 'approve' to stop or 'block' with reason to continue."
        }
      ]
    }
  ]
}
```

**Decision output:**
```json
{
  "decision": "approve|block",
  "reason": "Explanation",
  "systemMessage": "Additional context"
}
```

## SubagentStop

Similar to Stop hook, but for subagents. Ensures subagent completed its task.

## UserPromptSubmit

Execute when user submits a prompt. Use to add context, validate, or block prompts.

```json
{
  "UserPromptSubmit": [
    {
      "matcher": "*",
      "hooks": [
        {
          "type": "prompt",
          "prompt": "Check if prompt requires security guidance. If discussing auth, permissions, or API security, return relevant warnings."
        }
      ]
    }
  ]
}
```

## SessionStart

Execute when Claude Code session begins. Use to load context and set environment.

```json
{
  "SessionStart": [
    {
      "matcher": "*",
      "hooks": [
        {
          "type": "command",
          "command": "bash ${CLAUDE_PLUGIN_ROOT}/scripts/load-context.sh"
        }
      ]
    }
  ]
}
```

**Special capability:** Persist environment variables using `$CLAUDE_ENV_FILE`:
```bash
echo "export PROJECT_TYPE=nodejs" >> "$CLAUDE_ENV_FILE"
```

## SessionEnd

Execute when session ends. Use for cleanup, logging, and state preservation.

## PreCompact

Execute before context compaction. Use to add critical information to preserve.

## Notification

Execute when Claude sends notifications. Use to react to user notifications.

## Matchers

**Exact match:** `"matcher": "Write"`
**Multiple tools:** `"matcher": "Read|Write|Edit"`
**Wildcard:** `"matcher": "*"`
**Regex:** `"matcher": "mcp__.*__delete.*"`

Common patterns:
```json
"matcher": "mcp__.*"          // All MCP tools
"matcher": "mcp__plugin_.*"    // Specific plugin's MCP tools
"matcher": "Read|Write|Edit"    // All file operations
"matcher": "Bash"              // Bash commands only
```

Note: Matchers are case-sensitive.
