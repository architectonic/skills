---
type: Source Profile
title: Agent Skill Security Research
description: Candidate source cluster for reviewing malicious or unsafe third-party agent skills before ingestion.
tags: [source-profile, skills, security, risk-audit, marketplace]
okf_version: "0.2"
source_url: https://arxiv.org/abs/2603.16572
source_name: Malicious Or Not: Adding Repository Context to Agent Skill Classification
source_author: Florian Holzbauer, David Schmidt, Gabriel Gegenhuber, Sebastian Schrittwieser, Johanna Ullrich
license: UNKNOWN
runtime_targets: [claude-code, openclaw, local-agent-skills, skill-marketplaces]
skill_format: security-research
risk_level: high
ingestion_status: candidate
reviewed_at: 2026-07-02
---

# Agent Skill Security Research

## What It Is

A public research source about classifying malicious and benign agent skills using repository context, plus a broader public signal that agent skill marketplaces contain security risk.

## Why It Matters

This repository already carries a large installable skill surface. Before growth, the aggregator needs a stronger security model for third-party skill candidates, especially markdown-defined skills with tool, shell, filesystem, credential, or network behavior.

## Provenance

- Paper candidate: https://arxiv.org/abs/2603.16572
- Public web discovery on 2026-07-02 also surfaced current security reporting about malicious skill extensions in public marketplaces.

## License

Unknown from the Radar pass. Source Reviewer must inspect paper and any released dataset or repository licenses before reuse.

## Runtime Targets

- Claude Code style skill directories
- OpenClaw / local agent skill ecosystems
- Marketplace-distributed skills
- Repository-context security review

## Candidate Capabilities

- Repository-context skill review checklist
- Abandoned-repository risk detection
- Marketplace candidate triage
- False-positive-aware malicious skill classification

## Risks

- High risk because the topic includes malicious skill behavior, shell execution, credential theft, prompt injection, and possibly malware examples.
- Do not copy examples, payloads, or operational attack details. Use only summarized defensive review criteria after Source Reviewer and Risk Auditor approval.

## Ingestion Decision

Candidate only. Reference-only until reviewed.

## Next Action

Source Reviewer should inspect license, whether safe defensive criteria can be summarized, and whether Risk Auditor should create a durable third-party skill security checklist.
