---
type: Source Profile
title: AgentSkillOS
description: Candidate source for skill selection, orchestration, and ecosystem-scale benchmark organization.
tags: [source-profile, skills, orchestration, benchmark, retrieval]
okf_version: "0.2"
source_url: https://github.com/ynulihao/AgentSkillOS
source_name: AgentSkillOS
source_author: ynulihao / paper authors
license: UNKNOWN
runtime_targets: [agent-skills, skill-orchestration]
skill_format: framework-and-benchmark
risk_level: medium
ingestion_status: candidate
reviewed_at: 2026-07-02
---

# AgentSkillOS

## What It Is

A public repository associated with ecosystem-scale organization, selection, orchestration, and benchmarking of agent skills.

## Why It Matters

The local catalog currently contains many skills but still needs stronger structure around capability trees, retrieval, orchestration, and validation. This source may help the aggregator reason about catalog organization and skill selection without copying third-party skill content.

## Provenance

- Repository: https://github.com/ynulihao/AgentSkillOS
- Public paper discovered during Radar pass on 2026-07-02.
- GitHub repository search confirmed `ynulihao/AgentSkillOS` is public and not archived.

## License

Unknown from the Radar pass. Source Reviewer must inspect the repository license and any dataset or benchmark terms before reuse.

## Runtime Targets

- Agent skill ecosystems
- Skill retrieval and orchestration
- Multi-skill task solving
- Benchmark/evaluation workflows

## Candidate Capabilities

- Capability-tree catalog organization
- Skill retrieval and routing
- Multi-skill workflow composition
- Evaluation surface for large skill corpora

## Risks

- Medium review burden because orchestration frameworks may include executable pipelines, benchmark harnesses, model calls, or third-party datasets.
- Do not ingest implementation details or benchmark artifacts before license and security review.

## Ingestion Decision

Candidate only. Reference-only until reviewed.

## Next Action

Source Reviewer should inspect README, license, benchmark data, scripts, dependency graph, and whether its organization concepts can inform local catalog reports or critic checks.
