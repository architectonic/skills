---
name: ai-native-cli
description: Design spec with 98 rules for building CLI tools that AI agents can safely use. Covers structured JSON output, error handling, input contracts, safety guardrails, exit codes, and agent self-description.
tags: [agent-operations, cli, agent-safety, json-output, error-handling, spec]
type: Playbook
domain: agent-operations
risk_level: medium
requires_review: true
source_family: antigravity-awesome-skills
source_license: unknown
source_status: adapted
---

# Agent-Friendly CLI Spec

When building or modifying CLI tools, follow these rules to make them safe and reliable for AI agents to use.

## Overview

A comprehensive design specification for building AI-native CLI tools. It defines 98 rules across three certification levels (Agent-Friendly, Agent-Ready, Agent-Native) with prioritized requirements (P0/P1/P2). The spec covers structured JSON output, error handling, input contracts, safety guardrails, exit codes, self-description, and a feedback loop via a built-in issue system.

## When to Use This Skill

- Use when building a new CLI tool that AI agents will invoke
- Use when retrofitting an existing CLI to be agent-friendly
- Use when designing command-line interfaces for automation pipelines
- Use when auditing a CLI tool's compliance with agent-safety standards

## Core Philosophy

1. **Agent-first** — default output is JSON; human-friendly is opt-in via `--human`
2. **Agent is untrusted** — validate all input at the same level as a public API
3. **Fail-Closed** — when validation logic itself errors, deny by default
4. **Verifiable** — every rule is written so it can be automatically checked

## Layer Model

This spec uses two orthogonal axes:

- **Layer** answers rollout scope: `core`, `recommended`, `ecosystem`
- **Priority** answers severity: `P0`, `P1`, `P2`

Certification maps to layers:

- **Agent-Friendly** — all `core` rules pass
- **Agent-Ready** — all `core` + `recommended` rules pass
- **Agent-Native** — all layers pass

## How It Works

### Step 1: Output Mode

Default is agent mode (JSON). Explicit flags to switch:

```bash
$ mycli list              # default = JSON output (agent mode)
$ mycli list --human      # human-friendly: colored, tables, formatted
$ mycli list --agent      # explicit agent mode (override config if needed)
```

### Step 2: agent/ Directory Convention

Every CLI tool SHOULD have an `agent/` directory at its project root. This is the tool's identity and behavior contract for AI agents.

```
agent/
  brief.md          # One paragraph: who am I, what can I do
  rules/            # Behavior constraints (auto-registered)
    trigger.md      # When should an agent use this tool
    workflow.md     # Step-by-step usage flow
    writeback.md    # How to write feedback back
  skills/           # Extended capabilities (auto-registered)
    getting-started.md
```

### Step 3: Four Levels of Self-Description

1. `--brief` (business card, injected into agent config)
2. Every Command Response (always-on context: data + rules + skills + issue)
3. `--help` (full self-description: brief + commands + rules + skills + issue)
4. `skills <name>` (on-demand deep dive into a specific skill)

## Certification Requirements

### Level 1: Agent-Friendly (core — 20 rules)

**Output** — default is JSON, stable schema:
- `[P0]` Default output is JSON. No `--json` flag needed
- `[P0]` JSON MUST pass `jq .` validation
- `[P0]` JSON schema MUST NOT change within same version

**Error** — structured, to stderr, never interactive:
- `[P0]` Errors → `{"error":true, "code":"...", "message":"...", "suggestion":"..."}` to stderr
- `[P0]` Error has machine-readable `code` (e.g. `MISSING_REQUIRED`)
- `[P0]` Error has human-readable `message`
- `[P0]` On error, NEVER enter interactive mode — exit immediately
- `[P0]` Error codes are API contracts — MUST NOT rename across versions

**Exit Code** — predictable failure signals:
- `[P0]` Parameter/usage errors MUST exit 2
- `[P0]` Failures MUST exit non-zero — never exit 0 then report error in stdout

**Composability** — clean pipe semantics:
- `[P0]` stdout is for data ONLY
- `[P0]` logs, progress, warnings go to stderr ONLY

**Input** — fail fast on bad input:
- `[P1]` Missing required param → structured error, never interactive prompt
- `[P1]` Type mismatch → exit 2 + structured error

**Safety** — protect against agent mistakes:
- `[P1]` Destructive ops require `--yes` confirmation
- `[P1]` Reject `../../` path traversal, control chars

**Guardrails** — runtime input protection:
- `[P1]` Unknown flags rejected with exit 2
- `[P1]` Detect API key / token patterns in args, reject execution
- `[P1]` Reject sensitive file paths (*.env, *.key, *.pem)
- `[P1]` Reject shell metacharacters in arguments (; | && $())

### Level 2: Agent-Ready (+ recommended — 59 rules)

**Self-Description** — agent discovers what CLI can do:
- `[P1]` `--help` outputs structured JSON with `commands[]`
- `[P1]` All parameters have type declarations
- `[P1]` Parameters annotated as required/optional
- `[P1]` Every command has a description
- `[P1]` `--brief` outputs `agent/brief.md` content

**Input** — unambiguous calling convention:
- `[P1]` All flags use `--long-name` format
- `[P1]` No positional argument ambiguity

**Safety**:
- `[P1]` `--sanitize` flag for external input
- `[P2]` `--dry-run` flag for preview without executing

**Exit Code**:
- `[P1]` 0 = success
- `[P2]` 1=general, 10=auth, 11=permission, 20=not-found, 30=conflict

**Naming** — predictable flag conventions:
- `[P1]` Reserved flags: `--agent`, `--human`, `--brief`, `--help`, `--version`, `--yes`, `--dry-run`, `--quiet`, `--fields`

### Level 3: Agent-Native (+ ecosystem — 19 rules)

**Agent Directory** — tool identity and behavior contract:
- `[P1]` `agent/brief.md` exists
- `[P1]` `agent/rules/` has trigger.md, workflow.md, writeback.md
- `[P1]` `agent/skills/*.md` have YAML frontmatter

**Response Structure** — inline context on every call:
- `[P1]` Every response includes `rules[]` (full content from agent/rules/)
- `[P1]` Every response includes `skills[]` (name + description + command)
- `[P1]` Every response includes `issue` (feedback guide)

**Feedback** — built-in issue system:
- `[P2]` `issue` subcommand (create/list/show)
- `[P2]` Structured submission with version/context/exit_code
- `[P2]` Categories: bug / requirement / suggestion / bad-output

## Quick Implementation Checklist

**Phase 1: Agent-Friendly (core)**
1. Default output is JSON — no `--json` flag needed
2. Error handler: `{ error, code, message, suggestion }` to stderr
3. Exit codes: 0 success, 2 param error, 1 general
4. stdout = data only, stderr = logs only
5. Missing param → structured error (never interactive)
6. `--yes` guard on destructive operations
7. Guardrails: reject secrets, path traversal, shell metacharacters

**Phase 2: Agent-Ready (+ recommended)**
8. `--help` returns structured JSON (help, commands[], rules[], skills[])
9. `--brief` reads and outputs `agent/brief.md` content
10. `--human` flag switches to human-friendly format
11. Reserved flags: --agent, --version, --dry-run, --quiet, --fields
12. Exit codes: 20 not found, 30 conflict, 10 auth, 11 permission

**Phase 3: Agent-Native (+ ecosystem)**
13. Create `agent/` directory: `brief.md`, `rules/trigger.md`, `rules/workflow.md`, `rules/writeback.md`
14. Every command response appends: rules[] + skills[] + issue
15. `skills` subcommand: list all / show one with full content
16. `issue` subcommand for feedback (create/list/show/close/transition)
17. AGENTS.md at project root

## Best Practices

- Do: Default to JSON output so agents never need to add flags
- Do: Include `suggestion` field in every error response
- Do: Use the three-level certification model for incremental adoption
- Do: Keep `agent/brief.md` to one paragraph for token efficiency
- Don't: Enter interactive mode on errors — always exit immediately
- Don't: Change JSON schema or error codes within the same version
- Don't: Put logs or progress info on stdout — use stderr only
- Don't: Accept unknown flags silently — reject with exit code 2

## Common Pitfalls

- **Problem:** CLI outputs human-readable text by default, breaking agent parsing
  **Solution:** Make JSON the default output format; add `--human` flag for human-friendly mode

- **Problem:** Errors reported in stdout with exit code 0
  **Solution:** Always exit non-zero on failure and write structured error JSON to stderr

- **Problem:** CLI prompts for missing input interactively
  **Solution:** Return structured error with suggestion field and exit immediately

## Related Skills

- `cli-creator` — General CLI design patterns (this skill focuses specifically on AI agent compatibility)
- `context-engineering` — Context management for agent systems

## Source

- [Agent CLI Spec Repository](https://github.com/ChaosRealmsAI/agent-cli-spec)
- Distilled from antigravity-awesome-skills collection
