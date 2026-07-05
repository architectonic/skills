---
type: Source Profile
title: Snyk Agent Scan
author_or_org: Snyk
source_name: snyk/agent-scan
source_url: https://github.com/snyk/agent-scan
repository: snyk/agent-scan
repository_url: https://github.com/snyk/agent-scan
repository_ref: main
repository_commit_inspected: 962024783-metadata-default-main
review_date: 2026-07-05
runtime_targets: [claude-code, cursor, windsurf, gemini-cli, amp, amazon-q, opencode, openclaw, codex, mcp, agent-skills]
skill_format: security-scanner-and-review-source
capabilities: [agent-supply-chain-inventory, skill-security-review, mcp-security-review, prompt-injection-detection, credential-handling-review, tool-poisoning-review]
risk_level: high
ingestion_status: reference-only
license: Apache-2.0
source_status: summarized
review_boundary: metadata_only_no_content_copy_no_code_execution
okf_version: "0.2"
---

# Snyk Agent Scan

## Review decision

Keep as a reviewed `reference-only` source profile and send to Risk Auditor before any normalization.

This source is relevant to the skills repository because it is specifically about discovering and scanning installed agent components, including MCP servers and skills, for agent-supply-chain threats such as prompt injection, tool poisoning, toxic flows, credential handling, hardcoded secrets, untrusted content, and malware payloads.

Do not normalize it into a first-class skill yet. The repository describes security-scanning behavior that can execute commands from MCP configuration files during MCP inspection. That makes it useful as a source for review doctrine, but unsafe to treat as a routine scheduler action or install recommendation without a dedicated risk audit.

## Evidence inspected

- Repository metadata through the GitHub connector: `snyk/agent-scan`, public, default branch `main`, not archived.
- `README.md` on `main` says Agent Scan discovers and scans agent components, MCP servers, and skills for prompt injections and vulnerabilities.
- `README.md` explicitly warns that scanning MCP configurations executes the commands defined in those configurations and recommends sandboxing scans for untrusted or third-party MCP configs.
- `README.md` describes supported agent coverage across Claude Code/Desktop, Cursor, Windsurf, Gemini CLI, Amp, Amazon Q, OpenClaw, OpenCode, Antigravity, Codex, VS Code, MCP servers, and skills.
- `LICENSE` is Apache License 2.0.
- `pyproject.toml` declares package name `snyk-agent-scan`, version `0.5.12`, Python `>=3.10`, license `Apache-2.0`, and a CLI entry point `snyk-agent-scan`.

## Usefulness

High for risk doctrine and reviewer checklists.

Reusable ideas for this repository:

1. inventory skills and MCP/tool surfaces before trusting them;
2. treat natural-language files as possible malware or prompt-injection carriers;
3. distinguish skill scanning from MCP server scanning because MCP inspection can cross into command execution;
4. require explicit sandbox and consent boundaries before running third-party scanner workflows;
5. capture credential-handling and hardcoded-secret checks as standard review fields.

## Security and runtime surface

Risk level: high.

Risk drivers:

- MCP inspection may execute commands from local MCP configuration files;
- scanner usage may require a Snyk API token;
- analysis can share skill, agent application, tool-name, and description data with Snyk service endpoints;
- control-server bootstrap behavior can emit host and process fingerprint metadata when configured;
- broad local discovery touches user, project, system, extension, and plugin paths across multiple agent runtimes.

Safe boundary for this repository:

- reference-only profile;
- no cloned repository;
- no code execution;
- no scanner invocation from the scheduler;
- no normalization until Risk Auditor decides whether the useful review ideas can be distilled without adopting the tool execution model.

## Reviewer outcome

- Consumed queue item: `review-snyk-agent-scan-20260705`.
- Created risk queue item: `risk-snyk-agent-scan-runtime-boundary-20260705`.
- No third-party content was copied into `skills/` or `dist/skills/`.
- No package/catalog surface change is required from this profile alone.

## Next action

Risk Auditor should decide whether to extract a small review checklist update from this source into existing agent-skill security doctrine, while preserving the rule that scanner execution, MCP command execution, token use, and network egress are not scheduler-safe defaults.
