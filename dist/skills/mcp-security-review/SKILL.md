---
name: MCP Security Review
description: Security review framework for Model Context Protocol servers. Use before adding an MCP server, when auditing existing MCP tools, or when evaluating MCP server trust boundaries.
tags: [mcp, security, review, inventory]
type: Playbook
---

# MCP Security Review

## Purpose

MCP servers can expose powerful local or remote capabilities to agents. Treat every MCP tool as an execution boundary. This skill provides the security review framework for evaluating MCP servers before and after integration.

## Trigger

Use when:
- A new MCP server is proposed for installation
- Auditing existing MCP tools in a workspace
- Evaluating whether an MCP server should be project-scoped or global
- Reviewing MCP server permissions and data access

## Before Adding an MCP Server

Record:

```
Server name:
Source:
Transport:
Permissions requested:
Data exposed:
Write capabilities:
Authentication method:
```

## Review Questions

Ask these questions for every MCP server:

1. What files, APIs, accounts, or services can this server access?
2. Can it mutate external systems?
3. Can it read secrets or private local files?
4. Is the package/source trusted?
5. Is the server pinned to a version?
6. Is the server scoped to one project or global?
7. Are logs safe to share?

## Rules

- Prefer least privilege.
- Prefer project-scoped config over global config.
- Do not expose broad filesystem roots unless necessary.
- Do not pass secrets through prompts.
- Do not install untrusted MCP servers into a sensitive workspace.
- Document every server that can mutate state.

## MCP Server Inventory Template

```markdown
## Server Name

Purpose:
Source:
Transport:
Read access:
Write access:
Secrets required:
Risk level: low | medium | high
Review date:
Notes:
```

## Procedure

1. Record the server name, source, and transport.
2. Answer all review questions.
3. Classify risk level based on write capabilities and data access.
4. Decide: project-scoped or global.
5. If high risk, require explicit human approval before use.
6. Document the server in the MCP inventory.
7. Re-review when the server version changes or new tools are added.

## Risk Classification

| Level | Indicators |
|-------|-----------|
| Low | Read-only, no secrets, project-scoped |
| Medium | Local file writes, limited API access, no credentials |
| High | External mutation, credential access, broad filesystem access, network calls |

## Verification

- All MCP servers in the workspace are documented.
- High-risk servers have explicit approval records.
- No untrusted servers are installed in sensitive workspaces.
- Project-scoped servers are not globally accessible.

## Failure Modes

- Installing without review → untrusted code execution
- Global scope for project-specific server → cross-project contamination
- Missing inventory → unknown attack surface
- Passing secrets through prompts → credential exposure

## Security Notes

- High risk: MCP servers are execution boundaries with tool capabilities.
- Always treat MCP tools as potentially privileged.
- The `native-mcp` skill covers connection and registration; this skill covers security review.
