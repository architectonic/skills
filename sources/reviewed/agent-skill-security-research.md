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
ingestion_status: reviewed-reference-only
reviewed_at: 2026-07-02
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

Potential future local checklist themes:

- inspect skill files together with repository context;
- treat scanner output as an alert, not ground truth;
- check whether skill behavior aligns with repository purpose and implementation;
- flag abandoned or weakly maintained repositories as supply-chain risk;
- distinguish security research tooling from malicious behavior;
- avoid publishing or packaging skills whose provenance, license, and behavior context are unclear.

## Risk Review

High risk.

This source discusses malicious skills, executable payload classes, marketplace scanner outputs, repository hijacking, local command execution, credential exposure, and supply-chain abuse. It is safe as a reviewed reference-only source, but any normalization must be defensive, summarized, and routed through Risk Auditor before being added as a reusable skill or public recommendation.

## Ingestion Decision

Accepted as `reviewed-reference-only`.

Do not normalize yet. Queue a Risk Auditor pass to derive a safe third-party skill security checklist without copying operational attack content.

## Queue Outcome

- Consumed: `review-skill-security-20260702`
- Created: `risk-third-party-skill-security-checklist-20260702`

## Next Action

Risk Auditor should inspect this reviewed profile and create a durable defensive checklist for third-party skill ingestion, scanner interpretation, abandoned-repository risk, and repository-context validation.
