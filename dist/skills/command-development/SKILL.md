---
name: Command Development
description: Create slash commands for Claude Code plugins. Use when building custom commands with frontmatter, dynamic arguments, file references, bash execution, or plugin integration.
tags: [mcp, commands, slash-commands, plugins]
type: Playbook
---

# Command Development

Create slash commands that extend Claude Code with reusable, parameterized workflows.

## Sub-Skills

| Skill | When to Use |
|-------|-------------|
| [command-basics](command-basics.md) | Understand command locations, file format, and basic structure |
| [command-frontmatter](command-frontmatter.md) | Configure command frontmatter (allowed-tools, model, argument-hint) |
| [command-dynamic-features](command-dynamic-features.md) | Use dynamic arguments ($1, $ARGUMENTS) and file references (@ syntax) |
| [command-organization](command-organization.md) | Organize commands with namespaces, best practices, and common patterns |
| [command-plugin-integration](command-plugin-integration.md) | Integrate commands with agents, skills, hooks, and CLAUDE_PLUGIN_ROOT |

## Core Principles

1. **Commands are instructions FOR Claude** — write as directives to the agent, not messages to the user
2. **Progressive disclosure** — keep command lean, use references for detail
3. **Explicit dependencies** — declare `allowed-tools` when command needs specific tools
4. **Validate early** — check arguments and file existence before processing
