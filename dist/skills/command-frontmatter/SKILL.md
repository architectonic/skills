---
name: Command Frontmatter
description: Configure command YAML frontmatter fields including description, allowed-tools, model, argument-hint, disable-model-invocation. Use when adding configuration to a command or troubleshooting command triggering.
tags: [mcp, commands, frontmatter, yaml, configuration]
type: Playbook
---

# Command Frontmatter

## YAML Frontmatter Fields

### description

**Purpose:** Brief description shown in `/help`
**Type:** String
**Default:** First line of command prompt

```yaml
---
description: Review pull request for code quality
---
```

Best practice: Clear, actionable description (under 60 characters)

### allowed-tools

**Purpose:** Specify which tools command can use
**Type:** String or Array
**Default:** Inherits from conversation

```yaml
---
allowed-tools: Read, Write, Edit, Bash(git:*)
---
```

Patterns:
- `Read, Write, Edit` — Specific tools
- `Bash(git:*)` — Bash with git commands only
- `*` — All tools (rarely needed)

### model

**Purpose:** Specify model for command execution
**Type:** String (sonnet, opus, haiku)
**Default:** Inherits from conversation

```yaml
---
model: haiku
---
```

Use cases: `haiku` for fast/simple, `sonnet` for standard, `opus` for complex analysis

### argument-hint

**Purpose:** Document expected arguments for autocomplete
**Type:** String
**Default:** None

```yaml
---
argument-hint: [pr-number] [priority] [assignee]
---
```

Benefits: Helps users understand arguments, improves discovery

### disable-model-invocation

**Purpose:** Prevent SlashCommand tool from programmatically calling command
**Type:** Boolean
**Default:** false

```yaml
---
disable-model-invocation: true
---
```

Use when: Command should only be manually invoked
