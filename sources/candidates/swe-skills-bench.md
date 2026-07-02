---
type: Source Profile
title: SWE-Skills-Bench
description: Candidate benchmark source for measuring whether agent skills improve real software engineering task outcomes.
tags: [source-profile, skills, benchmark, software-engineering, evaluation]
okf_version: "0.2"
source_url: https://github.com/GeniusHTX/SWE-Skills-Bench
source_name: SWE-Skills-Bench
source_author: GeniusHTX / paper authors
license: UNKNOWN
runtime_targets: [agent-skills, software-engineering-agents]
skill_format: benchmark-corpus
risk_level: medium
ingestion_status: candidate
reviewed_at: 2026-07-02
---

# SWE-Skills-Bench

## What It Is

A public benchmark repository and paper associated with evaluating the marginal utility of injected agent skills on real software engineering tasks.

## Why It Matters

The skills aggregator needs evidence surfaces, not only more skills. This source can help identify which kinds of software engineering skills are actually useful, harmful, too broad, or version-sensitive.

## Provenance

- Repository: https://github.com/GeniusHTX/SWE-Skills-Bench
- Public paper discovered during Radar pass on 2026-07-02.
- GitHub repository search confirmed `GeniusHTX/SWE-Skills-Bench` is public and not archived.

## License

Unknown from the Radar pass. Source Reviewer must inspect repository license before any normalization or reuse.

## Runtime Targets

- Agent skill evaluation
- Software engineering agent workflows
- Benchmark-driven skill validation

## Candidate Capabilities

- Skill usefulness evaluation
- Skill regression detection
- Acceptance-criteria-linked verification
- Skill catalog pruning evidence

## Risks

- Medium review burden because benchmark repositories may include executable tasks, pinned repositories, test harnesses, scripts, or dependency installation.
- Do not run benchmark code until Source Reviewer and Risk Auditor inspect repository contents and license.

## Ingestion Decision

Candidate only. Reference-only until reviewed.

## Next Action

Source Reviewer should inspect README, license, task format, executable scripts, dependency behavior, and whether results can inform skill validation policy without copying benchmark content.
