---
type: Source Profile
title: Model Context Protocol
description: Candidate source for MCP tool/server procedures and risk-aware external-tool integration patterns.
tags: [source-profile, mcp, tools, agent-runtime, security]
okf_version: "0.2"
source_url: https://modelcontextprotocol.io
source_name: Model Context Protocol
source_author: Model Context Protocol project / Anthropic-originated ecosystem
license: UNKNOWN
runtime_targets: [mcp, claude, openai-agents, google, ide-agents]
skill_format: protocol-docs-and-server-procedures
risk_level: high
ingestion_status: candidate
reviewed_at: 2026-07-02
---

# Model Context Protocol

## What It Is

A public protocol and ecosystem for connecting AI systems to tools, servers, data sources, prompts, and external actions.

## Why It Matters

Many reusable agent skills depend on tools, MCP servers, OAuth flows, filesystems, or external actions. The aggregator needs a reviewed source profile for MCP procedures and a strong risk boundary before normalizing MCP-related skills.

## Provenance

- Documentation candidate: https://modelcontextprotocol.io
- GitHub organization candidates include `modelcontextprotocol/*` repositories discovered in public GitHub search.
- Public web sources describe MCP as an open standard introduced by Anthropic in late 2024 and adopted by multiple agent platforms.

## License

Unknown from the Radar pass. Source Reviewer must inspect documentation and repository licenses before any reuse.

## Runtime Targets

- MCP clients and servers
- Tool-using agent runtimes
- IDE agents
- External data and action integrations

## Candidate Capabilities

- MCP server review checklist
- Tool permission and transport risk classification
- OAuth and external-action verification procedure
- Runtime-neutral MCP source profile template

## Risks

- High risk because MCP sources can involve local command execution, filesystem access, network calls, OAuth credentials, browser automation, and state-changing external systems.
- Risk Auditor should inspect MCP-related entries before any endorsed packaging or publication.

## Ingestion Decision

Candidate only. Reference-only until license and security review.

## Next Action

Source Reviewer should verify official docs, repository licenses, server examples, SDK transport behavior, and whether this should feed a Risk Auditor checklist before normalization.
