---
name: agent-development
description: Create autonomous agent configurations for Claude Code plugins. Use when building subagents, designing agent frontmatter, writing system prompts, defining triggering conditions, or structuring agent files. Covers agent file format, description writing, tool restriction, model selection, and validation rules.
type: Playbook
title: Agent Development for Claude Code Plugins
domain: agent-operations
risk_level: medium
requires_review: true
source_family: claude-code-plugin
source_status: adapted
tags:
- agent-operations
- subagents
- claude-code
- plugin-development
- okf
---

# Agent Development for Claude Code Plugins

## Overview

Agents are autonomous subprocesses for complex, multi-step tasks. Commands are for user-initiated actions.

**Key concepts:**
- Agents = FOR autonomous work; commands = FOR user-initiated actions
- Markdown file format with YAML frontmatter
- Triggering via description field with examples
- System prompt defines agent behavior
- Model and color customization

## Agent File Structure

```markdown
---
name: agent-identifier
description: Use this agent when [triggering conditions]. Typical triggers include [scenario 1], [scenario 2], and [scenario 3]. See "When to invoke" in the agent body.
model: inherit
color: blue
tools: ["Read", "Write", "Grep"]
---

You are [agent role]...

## When to invoke

- **[Scenario A].** [Description.]
- **[Scenario B].** [Description.]

**Your Core Responsibilities:**
1. [Responsibility 1]
2. [Secondary responsibility]

**Analysis Process:**
[Step-by-step workflow]

**Output Format:**
[What to return]
```

## Frontmatter Fields

### name (required)
- Format: lowercase, numbers, hyphens only (3-50 chars)
- Must start and end with alphanumeric
- Good: `code-reviewer`, `test-generator`, `api-docs-writer`
- Bad: `helper` (too generic), `-agent-` (starts with hyphen), `my_agent` (underscore)

### description (required)
**This is the most critical field** — loaded into context whenever the agent is registered.

Must include:
1. Triggering conditions ("Use this agent when...")
2. Short prose summary of 2-4 typical trigger scenarios
3. Pointer to "When to invoke" section in body

Best practices:
- Cover both proactive and reactive triggering
- Cover different phrasings of the same intent
- Be specific about when NOT to use the agent
- Put detailed scenarios in body under "When to invoke"

### model (required)
- `inherit` — Use same model as parent (recommended)
- `sonnet` — Balanced
- `opus` — Most capable, expensive
- `haiku` — Fast, cheap

### color (required)
Visual identifier: `blue`, `cyan`, `green`, `yellow`, `magenta`, `red`
- Blue/cyan: Analysis, review
- Green: Success-oriented tasks
- Yellow: Caution, validation
- Red: Critical, security
- Magenta: Creative, generation

### tools (optional)
Restrict agent to specific tools (principle of least privilege):
- Read-only: `["Read", "Grep", "Glob"]`
- Code generation: `["Read", "Write", "Grep"]`
- Testing: `["Read", "Bash", "Grep"]`
- Full access: Omit field

## System Prompt Design

Write in second person. Standard template:

```markdown
You are [role] specializing in [domain].

**Your Core Responsibilities:**
1. [Primary responsibility]
2. [Secondary responsibility]

**Analysis Process:**
1. [Step one]
2. [Step two]

**Quality Standards:**
- [Standard 1]
- [Standard 2]

**Output Format:**
[What to include]

**Edge Cases:**
- [Edge case 1]: [How to handle]
```

**DO:** Second person, specific responsibilities, step-by-step process, defined output format, quality standards, edge cases, under 10,000 chars.

**DON'T:** First person, vague/generic, omit process steps, leave output undefined, skip quality guidance, ignore errors.
