---
type: Report
title: Source Review Plan - 2026-07-02
description: Source Reviewer checkpoint for public source candidate review and follow-up queues.
tags: [skills, source-review, provenance, license, security, daily-ledger]
okf_version: "0.2"
status: active
---

# Source Review Plan - 2026-07-02

## 04:59 Source Review - Model Context Protocol

### Selected Item

Consumed `review-mcp-20260702`.

Target: `sources/candidates/model-context-protocol.md`

Reviewed source: Model Context Protocol

### Decision

MCP is accepted as a reviewed reference-only source profile.

Reviewed profile created at:

```text
sources/reviewed/model-context-protocol.md
```

### Evidence Summary

- Official documentation describes MCP as an open-source standard for connecting AI applications to external systems, including data sources, tools, and workflows.
- Official GitHub repository states that it contains the MCP specification, protocol schema, and documentation.
- Official repository license is MIT.
- The repository has substantial public activity and adoption signals, but popularity is not treated as validation.

### Risk Decision

Do not normalize or package MCP-derived skills yet.

MCP involves high-risk surfaces: local command execution, filesystem access, network calls, OAuth, remote server trust, tool metadata poisoning, prompt injection, descriptor mutation, and state-changing external actions.

### Queue Updates

- Removed `review-mcp-20260702` from `queues.review`.
- Added `risk-mcp-security-checklist-20260702` to `queues.risk`.

## 13:00 Source Review - Agent Skill Security Research

### Selected Item

Consumed `review-skill-security-20260702`.

Target: `sources/candidates/agent-skill-security-research.md`

Reviewed source: `Context Matters: Repository-Aware Security Analysis of the Agent Skill Ecosystem`

### Decision

Agent skill security research is accepted as a reviewed reference-only source profile.

Reviewed profile created at:

```text
sources/reviewed/agent-skill-security-research.md
```

### Evidence Summary

- The arXiv record identifies the work as a 2026 security paper about repository-aware analysis of the agent skill ecosystem.
- The paper reports a 238,180-skill cross-platform analysis and argues that isolated scanner outputs should be treated as alerts rather than ground truth.
- The paper identifies abandoned-repository hijacking as a concrete agent-skill supply-chain risk.
- The reproduction repository is public and documents code/data artifacts for rebuilding reported results, but large data is hosted externally.

### License Decision

License remains unresolved.

The arXiv page exposes a license link, but no redistribution decision was made. The reproduction repository was reachable, but no top-level `LICENSE` file was found through the GitHub connector.

Default ingestion remains reference-only. Do not copy paper text, code, data, scanner prompts, payloads, or attack examples.

### Risk Decision

Do not normalize this source directly.

The source is high-risk because it discusses malicious skill behavior, marketplace scanner outputs, shell/code execution risk, repository hijacking, and credential exposure. It is useful for defensive review gates, but any normalized local procedure should be routed through Risk Auditor first.

### Queue Updates

- Removed `review-skill-security-20260702` from `queues.review`.
- Added `risk-third-party-skill-security-checklist-20260702` to `queues.risk`.

## 17:01 Source Review - Agent Skills Open Standard

### Selected Item

Consumed `review-agent-skills-standard-20260702`.

Target: `sources/candidates/agent-skills-open-standard.md`

Reviewed source: Agent Skills Open Standard

### Decision

Agent Skills Open Standard is accepted as a reviewed reference-only source profile.

Reviewed profile created at:

```text
sources/reviewed/agent-skills-open-standard.md
```

### Evidence Summary

- Official documentation describes Agent Skills as a lightweight open format for extending agents with reusable capabilities and workflows.
- The official repository README describes the required `SKILL.md` file and optional `scripts/`, `references/`, and `assets/` directories.
- The official repository README states that repository code is Apache-2.0 and documentation is CC-BY-4.0.
- The specification defines required `name` and `description` frontmatter fields, optional `license`, `compatibility`, `metadata`, and experimental `allowed-tools` fields.
- The client-implementation guide documents progressive disclosure, `.agents/skills/` conventions, parser leniency, collision handling, and trust checks for project-level skills.

### Risk Decision

Do not normalize the upstream specification into a local skill.

The standard is useful as package-format guidance, but skill packages can include executable scripts, support files, network assumptions, and project-level instructions. A package can be format-compatible while still unsafe.

### Queue Updates

- Removed `review-agent-skills-standard-20260702` from `queues.review`.
- Added `package-agent-skills-compatibility-review-20260702` to `queues.packaging`.
- Kept catalog blockers unchanged; Agent Skills compatibility review should run only after generated catalog drift is resolved.

## 18:01 Source Review - SWE-Skills-Bench

### Selected Item

Consumed `review-swe-skills-bench-20260702`.

Target: `sources/candidates/swe-skills-bench.md`

Reviewed source: SWE-Skills-Bench

### Decision

SWE-Skills-Bench is accepted as a reviewed reference-only source profile.

Reviewed profile created at:

```text
sources/reviewed/swe-skills-bench.md
```

### Evidence Summary

- Repository metadata shows `GeniusHTX/SWE-Skills-Bench` is public, not archived, and uses `main` as its default branch.
- The README describes 49 real-world software-engineering tasks paired with curated skill documents to test whether skill injection improves agent outcomes.
- The README and top-level `LICENSE` file declare MIT licensing.
- The README documents two usage modes: Hugging Face dataset loading and a full Docker-based evaluation framework.
- The evaluation framework requires Python, Docker, Claude Code CLI inside the container image, and an Anthropic API key.
- The benchmark configuration defines task repositories, pinned commits, Docker images, resource limits, network mode, test commands, and evaluation thresholds.
- Lifecycle code validates task files, starts containers, copies local skills into the Claude skills directory when enabled, clones configured repositories, runs Claude Code, and writes run reports.
- The arXiv abstract reports limited average benefit from skill injection, with many skills showing no pass-rate improvement, a few specialized skills helping, and some version-mismatched skills hurting performance.

### Risk Decision

Do not normalize benchmark task prompts, skill documents, test code, Docker images, or evaluation scripts into local skills.

This source is useful as validation evidence for local skill governance, but running it requires separate isolation, credentials, image review, cost controls, and benchmark execution planning. It should inform future Critic or maintenance work after catalog drift is resolved.

### Queue Updates

- Removed `review-swe-skills-bench-20260702` from `queues.review`.
- Added `maintenance-swe-skills-bench-validation-policy-20260702` to `queues.maintenance` for later evidence-aware validation and pruning policy.
- Kept catalog blockers unchanged; catalog drift remains the package/publication blocker.

## Next Review Item

Source Reviewer should next consume `review-agentskillos-20260702` unless Cataloger or another gate has more concrete pressure.
