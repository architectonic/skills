---
type: Source Profile
title: AWS Labs MCP
author_or_org: AWS Labs
source_name: awslabs/mcp
source_url: https://github.com/awslabs/mcp
repository: awslabs/mcp
repository_url: https://github.com/awslabs/mcp
repository_ref: main
repository_commit_inspected: 952238700-metadata-default-main
review_date: 2026-07-05
runtime_targets: [mcp, aws, cursor, vscode, claude-code, cline, kiro, windsurf, agent-workflows]
skill_format: mcp-server-suite-and-connector-workflow-source
capabilities: [mcp-server-catalog, aws-documentation-access, aws-workflow-automation, cloud-infrastructure-agent-tools, mcp-install-patterns, agent-tool-boundary-review]
risk_level: high
ingestion_status: reference-only
license: Apache-2.0
source_status: summarized
review_boundary: metadata_only_no_content_copy_no_code_execution
okf_version: "0.2"
---

# AWS Labs MCP

## Review decision

Keep as a reviewed `reference-only` source profile and send to Risk Auditor before any normalization.

This source is relevant because it is a broad public catalogue of AWS-focused MCP servers and installation patterns for agentic coding tools. It can inform source-review doctrine for MCP server catalogues, cloud-tool boundaries, install metadata, and agent access to managed external systems.

Do not normalize any AWS MCP server workflow into a first-class skill yet. The repository describes MCP servers that expose AWS documentation, AWS APIs, infrastructure workflows, databases, messaging, analytics, operations, and other cloud surfaces to AI clients. Even when a server is read-oriented, the catalogue includes local command execution, package runners, AWS credentials, network access, and possible external-system mutation. That makes the source valuable for review and risk doctrine but unsafe for scheduler-side execution or generic install endorsement.

## Evidence inspected

- Repository metadata through the GitHub connector: `awslabs/mcp`, public, default branch `main`, not archived.
- `README.md` on `main` describes a suite of specialized MCP servers for AWS.
- `README.md` states the repository now points production builders toward Agent Toolkit for AWS, while this repository continues to work and accept contributions.
- `README.md` states these MCP servers use stdio transport and that users are responsible for legal, policy, and standards compliance.
- `README.md` lists one-click or config-based install flows for Kiro, Cursor, and VS Code, commonly using package runners such as `uvx` and MCP configuration files.
- `README.md` includes remote managed AWS MCP and AWS Knowledge MCP options as well as local/package-backed server entries.
- `LICENSE` is Apache License 2.0.
- `CONTRIBUTING.md` requires RFC discussion for significant work such as proposing a new MCP server and points security issues to AWS/Amazon Security rather than public issues.
- `DEVELOPER_GUIDE.md` states some servers require AWS credentials, describes local development with `uv`, `uvx`, MCP client config, the MCP Inspector, local server execution, tests, and detect-secrets remediation.

## Usefulness

High for MCP source-review and cloud-tool boundary doctrine.

Reusable ideas for this repository:

1. treat MCP catalogues as source families, not individual skills, until each server's tool surface is reviewed;
2. distinguish managed remote MCP endpoints from local package-runner servers;
3. record transport, credential, filesystem, network, and external mutation boundaries before any normalization;
4. require explicit review before installing package-runner MCP commands into user editor configuration;
5. prefer reference profiles for broad vendor catalogues unless a narrow, safe, procedure-grounded pattern is extracted.

## Security and runtime surface

Risk level: high.

Risk drivers:

- MCP server usage can expose AWS account credentials or profile context;
- cloud infrastructure, database, deployment, messaging, support, operations, and cost workflows can mutate external systems;
- common install flows place executable package-runner commands into editor or agent MCP configuration;
- local development and inspection paths require command execution, network access, dependency resolution, and local filesystem access;
- broad catalogue scope means one source profile cannot prove safety for every included server.

Safe boundary for this repository:

- reference-only profile;
- no cloned repository;
- no MCP server startup;
- no package-runner execution;
- no AWS credential handling;
- no install recommendation or normalized procedure until Risk Auditor decides whether a narrow checklist or doctrine update is justified.

## Reviewer outcome

- Consumed queue item: `review-awslabs-mcp-20260705`.
- Created risk queue item: `risk-awslabs-mcp-cloud-tool-boundary-20260705`.
- No third-party content was copied into `skills/` or `dist/skills/`.
- No package/catalog surface change is required from this profile alone.

## Next action

Risk Auditor should decide whether to extract a small MCP catalogue/cloud-tool boundary checklist into existing MCP external tool security doctrine, while preserving the rule that scheduler runs must not start MCP servers, install packages, use AWS credentials, mutate cloud resources, or modify editor MCP configuration by default.
