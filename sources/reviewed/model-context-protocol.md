---
type: Source Profile
title: Model Context Protocol
description: Reviewed source profile for MCP protocol documentation, SDKs, tool/server procedures, and high-risk external-tool integration patterns.
tags: [source-profile, mcp, tools, agent-runtime, security, reviewed]
okf_version: "0.2"
source_url: https://modelcontextprotocol.io
source_name: Model Context Protocol
source_author: Model Context Protocol project; originally created by Anthropic ecosystem contributors David Soria Parra and Justin Spahr-Summers
license: MIT for the official modelcontextprotocol/modelcontextprotocol repository; individual SDK/server repositories require per-repository license checks before reuse
runtime_targets: [mcp, claude, chatgpt, vscode, cursor, ide-agents, tool-using-agent-runtimes]
skill_format: protocol-docs-and-server-procedures
risk_level: high
ingestion_status: reviewed-reference-only
reviewed_at: 2026-07-02
reviewed_by: Source Reviewer
---

# Model Context Protocol

## Review Decision

MCP is accepted as a reviewed source profile for reference-only use.

Do not normalize MCP behavior into endorsed local skills yet. MCP procedures involve external tools, local servers, transports, OAuth, filesystem access, network access, and potentially state-changing actions. The correct next step is Risk Auditor review before any MCP checklist, runbook, package, or publication surface is endorsed.

## Provenance

- Official documentation: https://modelcontextprotocol.io
- Official specification and documentation repository: https://github.com/modelcontextprotocol/modelcontextprotocol
- The official repository states that it contains the MCP specification, protocol schema, and documentation.
- The official repository attributes MCP creation to David Soria Parra and Justin Spahr-Summers.

## License

- The official `modelcontextprotocol/modelcontextprotocol` repository is MIT licensed.
- License does not automatically cover every MCP SDK, server, registry entry, or third-party MCP package.
- Any future normalized skill or runbook must cite the specific upstream repository and verify that repository's license separately.

## Maintenance and Adoption Signals

- The official repository shows thousands of commits and active public project structure.
- The official documentation presents MCP as an open-source standard for connecting AI applications to data sources, tools, and workflows.
- The documentation identifies ecosystem support across AI assistants and developer tools including Claude, ChatGPT, Visual Studio Code, Cursor, and other MCP-supporting clients.
- GitHub repository signals show substantial public attention, but popularity is not validation and does not reduce the security review requirement.

## Usefulness

MCP is useful to this repository because many future skills will need to distinguish safe tool-use procedure from unsafe tool execution. MCP also gives this aggregator a concrete external-tool integration class for risk taxonomy, source-profile structure, and future package compatibility checks.

Acceptable local uses now:

- reference-only source profile;
- risk taxonomy input;
- future MCP server review checklist;
- future tool permission and transport classification;
- future OAuth and external-action verification procedure.

Unacceptable local uses now:

- copying MCP documentation into local skills;
- endorsing MCP servers as safe because they use MCP;
- normalizing server setup commands before license and security review;
- publishing MCP-derived skills as approved package entries without Risk Auditor review.

## Security Review Notes

MCP is high risk for this corpus.

Risk areas:

- local command execution;
- filesystem read/write access;
- network calls;
- OAuth and account authorization flows;
- remote server trust;
- tool metadata and descriptor poisoning;
- prompt injection through tools or returned content;
- cross-server trust propagation;
- state-changing external actions;
- supply-chain risk from registries and third-party servers.

Recent public security research and reporting describe MCP-specific tool poisoning, prompt injection, descriptor mutation, governance, and transport/execution concerns. These are not reasons to block MCP as a source profile, but they require MCP-derived entries to pass Risk Auditor review before normalization.

## Ingestion Decision

Status: reviewed-reference-only.

MCP should remain reference-only until a Risk Auditor creates or approves a durable MCP security checklist. After that, a Normalizer may create a local runbook or skill only if it has a narrow trigger, explicit inputs, bounded procedure, verification, and failure modes.

## Follow-Up Queue

Create a Risk Auditor queue item for an MCP external-tool security checklist before any normalization.
