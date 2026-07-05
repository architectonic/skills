---
type: Source Profile
title: SWE-Skills-Bench
description: Reviewed reference-only benchmark source for evaluating whether injected software-engineering skill documents improve agent outcomes.
tags: [source-profile, skills, benchmark, software-engineering, evaluation, reference-only]
okf_version: "0.2"
source_url: https://github.com/GeniusHTX/SWE-Skills-Bench
source_name: SWE-Skills-Bench
source_author: GeniusHTX / Yi Zhang and paper coauthors
license: MIT
runtime_targets: [agent-skills, software-engineering-agents, benchmark-evaluation]
skill_format: benchmark-corpus
risk_level: medium
ingestion_status: reviewed-reference-only-validation-doctrine-candidate
reviewed_at: 2026-07-05T10:14:55-03:00
reviewed_by: Source Reviewer
review_boundary: metadata_and_repository_file_review_no_clone_no_execution_no_content_copy
status: reviewed
---

# SWE-Skills-Bench

## What It Is

SWE-Skills-Bench is a public benchmark repository and paper for testing whether injected skill documents improve software-engineering agent performance on real repository tasks.

The repository README describes 49 real-world software-engineering tasks paired with curated skill documents. It frames the benchmark question as whether giving an agent a skill document actually helps.

## Current Review Decision

Accepted as `reviewed-reference-only-validation-doctrine-candidate`.

This source should inform local validation doctrine, catalog pruning criteria, and future benchmark-backed skill evaluation. It should not be copied into local skills, bundled into `dist/skills`, or run automatically by the connector-only aggregator.

The 2026-07-05 review closes queue item `review-swe-skills-bench-20260705-0711` as a refreshed source review rather than a new normalization path.

## Provenance

- Repository: https://github.com/GeniusHTX/SWE-Skills-Bench
- Paper: https://arxiv.org/abs/2603.15401
- Repository owner: GeniusHTX
- Repository status at review: public, not archived
- Default branch at review: `main`
- Review date: 2026-07-05

## Directly Inspected Evidence

- Repository metadata was read through the GitHub connector.
- `README.md` describes the project as a benchmark dataset for evaluating whether injected skill documents improve agent performance on real-world software-engineering tasks.
- `README.md` states the dataset contains 49 tasks and lists domains including TDD workflow, security review, MCP server builder, CI analysis, Python packaging, GitOps, observability, performance optimization, RAG, and LLM evaluation.
- `README.md` documents two use paths: loading a HuggingFace dataset or running a full Docker-based evaluation framework.
- `README.md` documents full-evaluation prerequisites: Python, Docker, Claude Code CLI inside the container image, and an Anthropic API key.
- `README.md` describes experiment/control commands with `--use-skill` and `--no-use-skill`, plus post-processing scripts for pass-rate comparison, failed-test extraction, token analysis, and duration analysis.
- `LICENSE` is present and is MIT, copyright Yi Zhang, 2026.
- `requirements.txt` lists the harness dependency surface: `pyyaml`, `docker`, `python-dotenv`, `click`, and `rich`.
- `config/benchmark_config.yaml` shows task execution is container-oriented, may use Docker images, can use network mode `bridge` for setup, and includes resource limits and build/test commands.

## Usefulness

Useful for the local skills aggregator because it gives a concrete evidence model for:

```text
skill usefulness evaluation
skill regression detection
version-mismatch warnings
acceptance-criteria-linked verification
catalog pruning and demotion decisions
benchmark-informed critic checks
```

The main local lesson is negative as much as positive: skill inclusion should not be treated as inherently useful. Skills need task-context fit, experiment/control comparison, cost visibility, runtime safety, and validation against real acceptance criteria.

The reusable procedure learned is not an upstream skill. It is a review boundary for future local doctrine: a normalized skill should eventually be judged by whether it improves task outcomes compared with a no-skill baseline, while also tracking failed tests, token cost, wall-clock duration, and environment assumptions.

## Risks

Medium risk.

Observed risk surfaces:

```text
Docker container creation and execution
network access during environment setup
third-party repository cloning at pinned commits
external Docker images
local skill copying into agent runtime directories
Anthropic API key usage
Claude Code autonomous execution inside containers
unit-test and build-command execution
benchmark task prompts and skill documents that should not be blindly imported
```

Do not run benchmark scripts without an isolated environment, explicit credentials policy, Docker image review, dependency review, network policy, and cost controls.

## Ingestion Boundary

Allowed locally:

```text
reference-only source profile
summary of benchmark purpose
validation-policy lessons
critic queue items for evidence-backed skill pruning
future benchmark runner design notes after separate risk review
```

Blocked locally:

```text
copying benchmark task prompts
copying skill documents
copying test code or repository fixtures
running Docker images from this automation pass
using API keys in benchmark execution
normalizing benchmark skills as local skills without separate source review
publishing benchmark-derived claims as local validation without reproducing or citing evidence
```

## Queue Decision

`review-swe-skills-bench-20260705-0711` is complete.

No normalization queue item was created. No risk queue item was created because the scheduler boundary already blocks the execution and credential surfaces for this source. Future work, if needed, should be critic/maintenance work that derives internal validation criteria from the benchmark's evaluation pattern without copying benchmark content.