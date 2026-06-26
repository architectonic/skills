---
name: Hook Debugging
description: Debug, test, and troubleshoot hooks. Use when hooks aren't firing, producing errors, or behaving unexpectedly. Covers lifecycle, validation, testing, and implementation workflow.
tags: [mcp, hooks, debugging, testing, lifecycle, troubleshooting]
type: Playbook
---

# Hook Debugging

## Hook Lifecycle

### Hooks Load at Session Start

Changes to hook configuration require restarting Claude Code.

**Cannot hot-swap hooks:**
- Editing `hooks/hooks.json` won't affect current session
- Adding new hook scripts won't be recognized
- Must restart: exit and run `claude` again

**To test hook changes:**
1. Edit hook configuration or scripts
2. Exit Claude Code session
3. Restart: `claude` or `cc`
4. Test with `claude --debug`

### Hook Validation at Startup

Hooks are validated when Claude Code starts:
- Invalid JSON in hooks.json causes loading failure
- Missing scripts cause warnings
- Syntax errors reported in debug mode

Use `/hooks` command to review loaded hooks in current session.

## Debugging

### Enable Debug Mode

```bash
claude --debug
```

Look for: hook registration, execution logs, input/output JSON, timing information.

### Test Hook Scripts Directly

```bash
echo '{"tool_name": "Write", "tool_input": {"file_path": "/test"}}' | \
  bash ${CLAUDE_PLUGIN_ROOT}/scripts/validate.sh

echo "Exit code: $?"
```

### Validate JSON Output

Ensure hooks output valid JSON:

```bash
output=$(./your-hook.sh < test-input.json)
echo "$output" | jq .
```

## Quick Reference

### Hook Events Summary

| Event | When | Use For |
|-------|------|---------|
| PreToolUse | Before tool | Validation, modification |
| PostToolUse | After tool | Feedback, logging |
| UserPromptSubmit | User input | Context, validation |
| Stop | Agent stopping | Completeness check |
| SubagentStop | Subagent done | Task validation |
| SessionStart | Session begins | Context loading |
| SessionEnd | Session ends | Cleanup, logging |
| PreCompact | Before compact | Preserve context |
| Notification | User notified | Logging, reactions |

### Best Practices

**DO:**
- Use prompt-based hooks for complex logic
- Use ${CLAUDE_PLUGIN_ROOT} for portability
- Validate all inputs in command hooks
- Quote all bash variables
- Set appropriate timeouts
- Return structured JSON output
- Test hooks thoroughly

**DON'T:**
- Use hardcoded paths
- Trust user input without validation
- Create long-running hooks
- Rely on hook execution order
- Modify global state unpredictably
- Log sensitive information

## Implementation Workflow

1. Identify events to hook into (PreToolUse, Stop, SessionStart, etc.)
2. Decide between prompt-based (flexible) or command (deterministic) hooks
3. Write hook configuration in `hooks/hooks.json`
4. For command hooks, create hook scripts
5. Use ${CLAUDE_PLUGIN_ROOT} for all file references
6. Validate configuration with `scripts/validate-hook-schema.sh hooks/hooks.json`
7. Test hooks with `scripts/test-hook.sh` before deployment
8. Test in Claude Code with `claude --debug`
9. Document hooks in plugin README

Focus on prompt-based hooks for most use cases. Reserve command hooks for performance-critical or deterministic checks.
