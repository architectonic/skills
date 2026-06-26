---
name: Hook Basics
description: Understand hook types (prompt-based vs command), configuration formats (plugin hooks.json vs settings.json), and when to use each. Use when creating your first hook or deciding between prompt and command approaches.
tags: [mcp, hooks, basics, configuration, prompt-based]
type: Playbook
---

# Hook Basics

## Hook Types

### Prompt-Based Hooks (Recommended)

Use LLM-driven decision making for context-aware validation:

```json
{
  "type": "prompt",
  "prompt": "Evaluate if this tool use is appropriate: $TOOL_INPUT",
  "timeout": 30
}
```

**Supported events:** Stop, SubagentStop, UserPromptSubmit, PreToolUse

**Benefits:** Context-aware decisions, flexible logic, better edge case handling, easier to maintain

### Command Hooks

Execute bash commands for deterministic checks:

```json
{
  "type": "command",
  "command": "bash ${CLAUDE_PLUGIN_ROOT}/scripts/validate.sh",
  "timeout": 60
}
```

**Use for:** Fast deterministic validations, file system operations, external tool integrations, performance-critical checks

## Configuration Formats

### Plugin hooks.json Format (Wrapper)

For plugin hooks in `hooks/hooks.json`:

```json
{
  "description": "Brief explanation of hooks (optional)",
  "hooks": {
    "PreToolUse": [...],
    "Stop": [...],
    "SessionStart": [...]
  }
}
```

Key points: `description` is optional, `hooks` is required wrapper. This is the plugin-specific format.

### Settings Format (Direct)

For user settings in `.claude/settings.json`:

```json
{
  "PreToolUse": [...],
  "Stop": [...],
  "SessionStart": [...]
}
```

Key points: No wrapper, no description, events directly at top level.

## Hook Output Format

### Standard Output (All Hooks)

```json
{
  "continue": true,
  "suppressOutput": false,
  "systemMessage": "Message for Claude"
}
```

- `continue`: If false, halt processing (default true)
- `suppressOutput`: Hide output from transcript (default false)
- `systemMessage`: Message shown to Claude

### Exit Codes

- `0` — Success (stdout shown in transcript)
- `2` — Blocking error (stderr fed back to Claude)
- Other — Non-blocking error

## Hook Input Format

All hooks receive JSON via stdin:

```json
{
  "session_id": "abc123",
  "transcript_path": "/path/to/transcript.txt",
  "cwd": "/current/working/dir",
  "permission_mode": "ask|allow",
  "hook_event_name": "PreToolUse"
}
```

**Event-specific fields:**
- PreToolUse/PostToolUse: `tool_name`, `tool_input`, `tool_result`
- UserPromptSubmit: `user_prompt`
- Stop/SubagentStop: `reason`

Access in prompts via `$TOOL_INPUT`, `$TOOL_RESULT`, `$USER_PROMPT`, etc.

## Environment Variables

- `$CLAUDE_PROJECT_DIR` — Project root path
- `$CLAUDE_PLUGIN_ROOT` — Plugin directory (use for portable paths)
- `$CLAUDE_ENV_FILE` — SessionStart only: persist env vars here
- `$CLAUDE_CODE_REMOTE` — Set if running in remote context

**Always use ${CLAUDE_PLUGIN_ROOT} in hook commands for portability.**
