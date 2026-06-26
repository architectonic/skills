---
name: Hook Security
description: Follow security best practices for hooks — input validation, path safety, quote discipline, timeouts, parallel execution, and temporary activation. Use when building hooks that validate or modify tool calls.
tags: [mcp, hooks, security, validation, path-safety, performance]
type: Playbook
---

# Hook Security

## Input Validation

Always validate inputs in command hooks:

```bash
#!/bin/bash
set -euo pipefail

input=$(cat)
tool_name=$(echo "$input" | jq -r '.tool_name')

# Validate tool name format
if [[ ! "$tool_name" =~ ^[a-zA-Z0-9_]+$ ]]; then
  echo '{"decision": "deny", "reason": "Invalid tool name"}' >&2
  exit 2
fi
```

## Path Safety

Check for path traversal and sensitive files:

```bash
file_path=$(echo "$input" | jq -r '.tool_input.file_path')

# Deny path traversal
if [[ "$file_path" == *".."* ]]; then
  echo '{"decision": "deny", "reason": "Path traversal detected"}' >&2
  exit 2
fi

# Deny sensitive files
if [[ "$file_path" == *".env"* ]]; then
  echo '{"decision": "deny", "reason": "Sensitive file"}' >&2
  exit 2
fi
```

## Quote All Variables

```bash
# GOOD: Quoted
echo "$file_path"
cd "$CLAUDE_PROJECT_DIR"

# BAD: Unquoted (injection risk)
echo $file_path
cd $CLAUDE_PROJECT_DIR
```

## Set Appropriate Timeouts

```json
{
  "type": "command",
  "command": "bash script.sh",
  "timeout": 10
}
```

**Defaults:** Command hooks (60s), Prompt hooks (30s)

## Parallel Execution

All matching hooks run **in parallel**:
- Hooks don't see each other's output
- Non-deterministic ordering
- Design for independence

## Performance Optimization

1. Use command hooks for quick deterministic checks
2. Use prompt hooks for complex reasoning
3. Cache validation results in temp files
4. Minimize I/O in hot paths

## Temporarily Active Hooks

Create hooks that activate conditionally:

**Flag file activation:**
```bash
#!/bin/bash
FLAG_FILE="$CLAUDE_PROJECT_DIR/.enable-strict-validation"
if [ ! -f "$FLAG_FILE" ]; then
  exit 0  # Not enabled, skip
fi
# Enabled, run validation
```

**Configuration-based activation:**
```bash
#!/bin/bash
CONFIG_FILE="$CLAUDE_PROJECT_DIR/.claude/plugin-config.json"
if [ -f "$CONFIG_FILE" ]; then
  enabled=$(jq -r '.strictMode // false' "$CONFIG_FILE")
  if [ "$enabled" != "true" ]; then
    exit 0
  fi
fi
```

Use cases: Strict validation on demand, debugging hooks, feature flags, project-specific behavior.
