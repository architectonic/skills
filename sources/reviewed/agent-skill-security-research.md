---
type: Source Profile
title: Agent Skill Security Research
description: Reviewed reference-only source profile for repository-context and marketplace security research about malicious or unsafe agent skills.
tags: [source-profile, skills, security, risk-audit, marketplace, repository-context]
okf_version: "0.2"
source_url: https://arxiv.org/abs/2603.16572
source_name: Context Matters: Repository-Aware Security Analysis of the Agent Skill Ecosystem
source_author: Florian Holzbauer, David Schmidt, Gabriel Gegenhuber, Sebastian Schrittwieser, Johanna Ullrich
license: UNKNOWN
runtime_targets: [claude-code, openclaw, local-agent-skills, skill-marketplaces]
skill_format: security-research
risk_level: high
ingestion_status: reviewed-reference-only-risk-audited
reviewed_at: 2026-07-02
risk_audited_at: 2026-07-02
---

# Agent Skill Security Research

## What It Is

A reviewed reference-only research source about security analysis for public agent skills, skill marketplaces, and repository-context classification.

The reviewed paper is `Context Matters: Repository-Aware Security Analysis of the Agent Skill Ecosystem`, also discovered earlier under the title `Malicious Or Not: Adding Repository Context to Agent Skill Classification`.

## Provenance

- Paper: https://arxiv.org/abs/2603.16572
- Reproduction repository: https://github.com/holzsec/repository-context-agentskills
- Authors: Florian Holzbauer, David Schmidt, Gabriel Gegenhuber, Sebastian Schrittwieser, Johanna Ullrich
- First arXiv submission: 2026-03-17
- Revised arXiv version inspected: 2026-06-01

## Review Summary

The source is useful for the skills aggregator because it directly studies the same risk surface this repository is beginning to operate: public agent skills distributed through marketplaces, GitHub repositories, and markdown skill definitions.

Key reviewed signals:

- The paper reports a large cross-platform empirical study of agent skills.
- It argues that isolated skill scanners can overstate maliciousness and that repository context improves triage quality.
- It identifies abandoned-repository hijacking as a concrete agent-skill supply-chain risk.
- The reproduction repository includes scripts and data-download instructions for rebuilding the reported analyses.

## License

License is unresolved.

The arXiv page exposes a paper license link, but no redistribution decision was made in this pass. The reproduction repository was reachable, but a top-level `LICENSE` file was not found through the GitHub connector.

Default ingestion mode remains reference-only. Do not copy paper text, datasets, code, scanner prompts, payloads, or attack examples into this repository.

## Runtime Targets

- Claude Code style skill directories
- OpenClaw-style local agent skills
- Public skill marketplaces
- GitHub-hosted skill repositories
- Local installable skill bundles

## Useful Local Takeaways

The source should inform defensive process, not content import.

Durable local checklist themes now captured in `operations/daily/2026-07-02/risk-audit.md`:

- inspect skill files together with repository context;
- treat scanner output as an alert, not ground truth;
- check whether skill behavior aligns with repository purpose and implementation;
- flag abandoned or weakly maintained repositories as supply-chain risk;
- distinguish security research tooling from malicious behavior;
- avoid publishing or packaging skills whose provenance, license, and behavior context are unclear.

## Risk Review

High risk.

This source discusses malicious skills, executable payload classes, marketplace scanner outputs, repository hijacking, local command execution, credential exposure, and supply-chain abuse. It is safe as a reviewed reference-only source, but any local normalization must be defensive, summarized, and avoid operational attack content.

## Risk Audit Outcome

Accepted as `reviewed-reference-only-risk-audited`.

The Risk Auditor created a local defensive checklist for third-party agent-skill ingestion, scanner interpretation, abandoned-repository risk, and repository-context validation.

This does not authorize copying source material or endorsing any third-party skills from the research corpus. It only authorizes using the reviewed source as evidence for local defensive review gates.

## Ingestion Decision

Accepted as `reviewed-reference-only-risk-audited`.

Do not normalize paper text, repository code, datasets, scanner prompts, payloads, attack examples, or exploit descriptions. Any future normalized entry must be a local defensive checklist or review procedure, must preserve attribution, and must remain high-risk/requires-review if it touches execution, marketplace trust, or repository supply-chain review.

## Queue Outcome

- Consumed: `review-skill-security-20260702`
- Consumed: `risk-third-party-skill-security-checklist-20260702`

## Next Action

Cataloger should reconcile catalog and install surfaces for the already-created local MCP security skill before any package or publication endorsement. Source Reviewer should later continue with `review-agent-skills-standard-20260702` after catalog drift is handled.
