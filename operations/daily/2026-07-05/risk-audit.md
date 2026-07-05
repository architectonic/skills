---
type: Risk Audit
title: Snyk Agent Scan Runtime Boundary Audit
description: Risk Auditor decision for whether snyk/agent-scan can inform Skills repository doctrine without adopting unsafe scanner execution behavior.
tags: [skills, risk-audit, agent-supply-chain, mcp, prompt-injection, snyk-agent-scan]
okf_version: "0.2"
status: active
---

# Snyk Agent Scan Runtime Boundary Audit

## Decision

`Snyk Agent Scan` remains a reviewed `reference-only` source profile.

Do not run the scanner from the scheduled Skills operator. Do not recommend it as a scheduler default. Do not normalize tool-invocation, CLI usage, MCP execution, token configuration, control-server, or background-monitoring behavior into a reusable skill.

A future Normalizer may create a narrow checklist-only update only if it preserves these boundaries:

- no repository clone;
- no scanner execution;
- no package-manager execution;
- no MCP server startup;
- no Snyk token handling;
- no network/API submission;
- no home-directory or multi-user filesystem enumeration;
- no copied third-party prose;
- source remains attributed as `Snyk Agent Scan`, Apache-2.0, reference-only.

## Evidence inspected

- Existing source profile: `sources/reviewed/snyk-agent-scan.md`.
- Repository metadata through the GitHub connector: `snyk/agent-scan`, public, default branch `main`, not archived.
- `README.md` directly fetched from `snyk/agent-scan` on `main`.
- `LICENSE` directly fetched from `snyk/agent-scan` on `main`.
- `pyproject.toml` directly fetched from `snyk/agent-scan` on `main`.

## Risk findings

The source is useful but operationally high risk for this repository's scheduler.

The upstream README describes agent-component inventory and scanning across agent applications, MCP servers, and skills. It explicitly states that scanning MCP configurations starts stdio MCP servers by executing commands and arguments from the scanned config, with user consent in interactive runs.

The README also states that non-interactive environments require a flag that starts all MCP servers automatically, and that analysis can invoke the Agent Scan API with skill, agent application, tool-name, and description data.

The README describes optional control-server bootstrap behavior that can send host and process fingerprint metadata, including OS/Python details, hostname, username, shell, locale, timezone, current working directory, home directory, executable path, and readable home directories when configured.

The package metadata declares a Python CLI package, `snyk-agent-scan`, with runtime dependencies and a console entry point. That confirms this is executable tooling, not just inert documentation.

Apache-2.0 licensing is compatible with summarized/source-profile treatment, but license compatibility does not lower the runtime risk.

## Safe extraction boundary

Allowed for this repo:

- cite the reviewed source profile as evidence that agent-skill and MCP surfaces need supply-chain review;
- distill only generic reviewer fields into local doctrine: component inventory, natural-language malware/prompt-injection review, credential-handling review, hardcoded-secret review, MCP command-execution classification, API/network egress classification, and sandbox/consent boundary;
- keep any future normalized text as local procedure written from review judgment, not copied upstream content.

Blocked unless a separate explicit operator run is scoped for local security tooling:

- running `uvx snyk-agent-scan`;
- setting or reading `SNYK_TOKEN`;
- scanning local user, project, system, extension, or plugin paths;
- scanning MCP configs that may start servers;
- using non-interactive auto-start flags;
- submitting skill or tool metadata to remote APIs;
- enabling control-server or background-monitoring behavior;
- recommending package installation as part of the Skills scheduler loop.

## Queue outcome

- Consumed risk queue item: `risk-snyk-agent-scan-runtime-boundary-20260705`.
- Closed the high-risk scheduler boundary blocker.
- Created no normalization queue item in this pass because the existing `skills/mcp-external-tool-security-review.md` already covers the core MCP trust, execution, prompt-injection, secret, and audit boundaries.
- Future Critic or Source Reviewer may later propose a small checklist refinement if it identifies a concrete gap not already covered.

## Verification

- No third-party content was copied into `skills/` or `dist/skills/`.
- No external code was executed.
- No package, catalog, or npm surface changed.
- The Snyk source remains `reference-only`.
- Risk queue pressure is cleared so Source Reviewer can continue with the remaining review-next candidates.
