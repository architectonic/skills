---
type: Source Profile
title: Model Context Protocol
description: Reviewed source profile for MCP protocol documentation, SDKs, tool/server procedures, and high-risk external-tool integration patterns.
tags: [source-profile, mcp, tools, agent-runtime, security, reviewed, audited]
okf_version: "0.2"
source_url: https://modelcontextprotocol.io
source_name: Model Context Protocol
source_author: Model Context Protocol project; originally created by Anthropic ecosystem contributors David Soria Parra and Justin Spahr-Summers
license: MIT for the official modelcontextprotocol/modelcontextprotocol repository; individual SDK/server repositories require per-repository license checks before reuse
runtime_targets: [mcp, claude, chatgpt, vscode, cursor, ide-agents, tool-using-agent-runtimes]
skill_format: protocol-docs-and-server-procedures
risk_level: high
ingestion_status: reviewed-reference-only-risk-audited
reviewed_at: 2026-07-02
reviewed_by: Source Reviewer
risk_audited_at: 2026-07-02
risk_audited_by: Risk Auditor
---

# Model Context Protocol

## Review Decision

MCP is accepted as a reviewed source profile for reference-only use.

Do not normalize MCP behavior into endorsed local skills yet. MCP procedures involve external tools, local servers, transports, OAuth, filesystem access, network access, and potentially state-changing actions. The correct next step is a narrow local checklist or runbook derived from the Risk Auditor checklist, not direct copying of MCP documentation or server setup instructions.

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
- future OAuth and external-action verification procedure;
- local checklist or runbook normalized from `operations/daily/2026-07-02/risk-audit.md`.

Unacceptable local uses now:

- copying MCP documentation into local skills;
- endorsing MCP servers as safe because they use MCP;
- normalizing server setup commands before license and security review;
- publishing MCP-derived skills as approved package entries without catalog and package review;
- treating protocol compliance as a security guarantee.

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

Recent public security research and reporting describe MCP-specific tool poisoning, prompt injection, descriptor mutation, governance, transport, execution, and multi-tool poisoning concerns. These are not reasons to block MCP as a source profile, but they require MCP-derived entries to pass Risk Auditor review before normalization.

## Risk Auditor Decision

Status: reviewed-reference-only-risk-audited.

The Risk Auditor checklist was recorded in:

```text
operations/daily/2026-07-02/risk-audit.md
```

The checklist approves only a narrow local normalization target: an OKF-compatible MCP external-tool security checklist or runbook. That future entry must be derived from the local audit, cite MCP as a reference source, avoid copied third-party documentation, preserve the high-risk classification, and include trigger, inputs, procedure, verification, and failure modes.

## Ingestion Decision

Status: reviewed-reference-only-risk-audited.

MCP is not blocked as a source profile. MCP-derived operational entries remain blocked from publication or package endorsement until a Normalizer creates a narrow local checklist/runbook and a later Cataloger/Packager pass reconciles catalog and install-facing review flags.

## Follow-Up Queue

Normalizer may consume `normalize-mcp-external-tool-security-checklist-20260702` to create the local checklist or runbook from the risk audit.
