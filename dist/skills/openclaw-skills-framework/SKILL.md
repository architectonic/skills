---
name: openclaw-skills-framework
description: OpenClaw skill system architecture — SKILL.md format, loading order,
  workshop, and gating.
tags:
- software-engineering
- research
- openclaw
- skill-architecture
- skill-format
- skill-workshop
- skill-loading
- okf
type: Playbook
title: OpenClaw Skills Framework
domain: software-engineering
risk_level: medium
requires_review: true
source_family: agent-skills-standard
source_status: adapted
---

# OpenClaw Skills Framework

## Overview

OpenClaw skills are markdown instruction files that teach agents how and when to use tools. Each skill lives in a directory with SKILL.md (YAML frontmatter + markdown body).

## Loading Order (Precedence, highest first)

1. Workspace skills: `<workspace>/skills`
2. Project agent skills: `<workspace>/.agents/skills`
3. Personal agent skills: `~/.agents/skills`
4. Managed / local skills: `~/.openclaw/skills`
5. Bundled skills: shipped with install
6. Extra directories: `skills.load.extraDirs` + plugin skills

## Per-Agent vs Shared

| Scope | Path | Visible to |
|-------|------|-----------|
| Per-agent | `<workspace>/skills` | Only that agent |
| Project | `<workspace>/.agents/skills` | Workspace agent |
| Personal | `~/.agents/skills` | All local agents |
| Shared | `~/.openclaw/skills` | All local agents |

## SKILL.md Required Fields

| Field | Description |
|-------|-------------|
| name | Unique slug: lowercase letters, digits, hyphens |
| description | One-line, under 160 characters |

## Optional Frontmatter Keys

- user-invocable (default: true)
- disable-model-invocation (default: false)
- command-dispatch: "tool" for slash-to-tool routing
- command-tool: tool name when dispatch is tool
- command-arg-mode: "raw" forwards raw args
- homepage: URL for UI

## Gating Options (metadata.openclaw.requires)

- requires.bins: All binaries must exist on PATH
- requires.anyBins: At least one binary
- requires.env: Each env var must exist
- requires.config: Each config path must be truthy
- os: Platform filter ["darwin"], ["linux"], ["win32"]
- always: true to skip all gates

## Skill Workshop

Proposal queue between agent and active skill files:
```bash
openclaw skills workshop propose-create --name "x" --description "y" --proposal ./PROPOSAL.md
openclaw skills workshop inspect <proposal-id>
openclaw skills workshop apply <proposal-id>
```

## Installing from ClawHub

```bash
openclaw skills install <slug>
openclaw skills install git:owner/repo@ref
openclaw skills install <slug> --global
openclaw skills update --all
```

## Best Practices
- Be concise — instruct model what to do, not how to be an AI
- Safety first — prevent command injection with exec
- Test locally before sharing
- Browse ClawHub before building from scratch
