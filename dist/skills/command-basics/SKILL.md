---
name: Command Basics
description: Understand what slash commands are, where they live, and their file format. Use when creating your first command or deciding between project/personal/plugin command locations.
tags: [mcp, commands, basics, file-format]
type: Playbook
---

# Command Basics

## What is a Slash Command?

A slash command is a Markdown file containing a prompt that Claude executes during interactive sessions.

Commands provide:
- **Reusability**: Define once, use repeatedly
- **Consistency**: Standardize common workflows
- **Sharing**: Distribute across team or projects
- **Efficiency**: Quick access to complex prompts

## Critical: Commands are Instructions FOR Claude

Commands are written for agent consumption, not human consumption.

**Correct (instructions for Claude):**
```markdown
Review this code for security vulnerabilities including:
- SQL injection
- XSS attacks
- Authentication issues
Provide specific line numbers and severity ratings.
```

**Incorrect (messages to user):**
```markdown
This command will review your code for security issues.
You'll receive a report with vulnerability details.
```

The first tells Claude what to do. The second tells the user what will happen but doesn't instruct Claude.

## Command Locations

**Project commands** (shared with team):
- Location: `.claude/commands/`
- Scope: Available in specific project
- Label: Shown as "(project)" in `/help`

**Personal commands** (available everywhere):
- Location: `~/.claude/commands/`
- Scope: Available in all projects
- Label: Shown as "(user)" in `/help`

**Plugin commands** (bundled with plugins):
- Location: `plugin-name/commands/`
- Scope: Available when plugin installed
- Label: Shown as "(plugin-name)" in `/help`

## File Format

Commands are Markdown files with `.md` extension:

```
.claude/commands/
├── review.md           # /review command
├── test.md             # /test command
└── deploy.md           # /deploy command
```

**Simple command (no frontmatter):**
```markdown
Review this code for security vulnerabilities including:
- SQL injection
- XSS attacks
- Authentication bypass
- Insecure data handling
```

**With YAML frontmatter:**
```markdown
---
description: Review code for security issues
allowed-tools: Read, Grep, Bash(git:*)
model: sonnet
---

Review this code for security vulnerabilities...
```
