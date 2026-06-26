---
name: Agent Context Validation
description: Validate any artifact that changes what an agent reads, installs, executes, or treats as authority. Use when reviewing skills, prompts, MCP configs, hooks, subagent definitions, or runtime adapters before promotion.
tags: [agent-operations, agent-operations, validation, safety, linting, skills, mcp]
type: Playbook
---

# Agent Context Validation

## Purpose

Validate any artifact that changes what an agent reads, installs, executes, routes, or treats as authority. Agent context files fail dangerously when they are almost correct.

## Scope

Validate at least: SKILL.md, AGENTS.md, CLAUDE.md, GEMINI.md, slash commands, subagent definitions, hooks, MCP config, plugin manifests, package-manager generated files, runtime adapters.

## Validation Gate

```
Collect changed files → classify runtime targets → validate schema/frontmatter
→ validate authority and scope → inspect executable surfaces
→ preview safe fixes → require review for mutating fixes → emit receipt
```

## Required Checks

| Check | Requirement |
|-------|-------------|
| Syntax | File parses under expected runtime format |
| Authority | Does not conflict with higher-authority instructions |
| Scope | Declares what it may and may not affect |
| Invocation | Trigger metadata is valid and discoverable |
| Tool powers | Shell, browser, MCP, API, package, mutation powers explicit |
| Secret handling | No token, credential, or local-only value embedded |
| Adapter drift | Generated runtime files agree with canonical source |
| Risk label | High-review surfaces marked before use |

## Autofix Rules

Autofix allowed only for: safe formatting/metadata normalization, explicit human-approved patches, CI-only generated patches not auto-merged.

Never allow unattended autofix for: hooks, MCP config, package installs, shell commands, browser automation, auth, deployment, destructive operations.

## GUI and Multimodal Skill Policy

For GUI, browser, desktop, and multimodal skills:

| Artifact Class | Review Level |
|----------------|-------------|
| Text-only GUI guide | medium |
| Action graph with screenshots | high |
| Browser automation with credentials | critical |
| Multimodal with MCP topic loading | high |

Required checks for GUI skills: action graph review, credential handling, session isolation, rollback procedure, human confirmation for state-changing actions.

## Repository Improvement Loop

For systematic repository improvement:
```
Recon → Audit → Plan → Delegate → Implement → Review → Reconcile
```

Use stronger models for understanding and planning, cheaper agents for execution. Keep judgment separate from implementation.

## Receipt Shape

```
artifact path | runtime target | validator | checks run | findings by severity
| fixes previewed | fixes applied | reviewer decision | remaining risks
```

## Trigger

Use this skill when:
- A new skill or prompt is promoted to canonical status
- An MCP server configuration changes
- A hook or runtime adapter is added or modified
- A subagent definition is created or updated

## Procedure

1. Collect all changed files in the target change set.
2. Classify each file by runtime target and authority level.
3. Validate YAML frontmatter schema and required fields.
4. Check authority: does the file conflict with higher-priority sources?
5. Check scope: are affected systems and boundaries declared?
6. Inspect executable surfaces: shell, browser, network, mutation.
7. Verify no embedded secrets, credentials, or private identifiers.
8. Check adapter drift: do generated files match canonical source?
9. Preview safe fixes; flag mutating fixes for human review.
10. Emit a receipt with findings, decisions, and remaining risks.

## Verification

- All checked files pass the required checks.
- No authority conflicts detected.
- Embedded secrets scan clean.
- Receipt is written for any mutating change.

## Failure Modes

- Agent trusts "almost correct" config that silently changes agent behavior.
- Autofix modifies a hook that bypasses human review.
- GUI skill with credentials lacks session isolation.
- Adapter drift causes runtime behavior to diverge from canonical source.

## Security Notes

- Low risk: validation is a read-only review process.
- High stakes: a missed validation can propagate bad instructions to every agent using the context.
- Always require human review for mutating fixes to executable surfaces.

## Sources

- curator/loops/agent-context.md — full validation gate with supply chain policy
