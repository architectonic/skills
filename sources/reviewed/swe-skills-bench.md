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
ingestion_status: reviewed-reference-only
reviewed_at: 2026-07-02
---

# SWE-Skills-Bench

## What It Is

SWE-Skills-Bench is a public benchmark repository and paper for testing whether injected skill documents improve software-engineering agent performance on real repository tasks.

The repository README describes 49 real-world software-engineering tasks paired with curated skill documents. The arXiv record describes the benchmark as requirement-driven and designed to isolate the marginal utility of agent skills in real-world software engineering.

## Review Decision

Accepted as `reviewed-reference-only`.

This source should inform local validation doctrine, catalog pruning criteria, and future benchmark-backed skill evaluation. It should not be copied into local skills, bundled into `dist/skills`, or run automatically by the connector-only aggregator.

## Provenance

- Repository: https://github.com/GeniusHTX/SWE-Skills-Bench
- Paper: https://arxiv.org/abs/2603.15401
- Repository owner: GeniusHTX
- Repository status at review: public, not archived
- Default branch at review: `main`
- Review date: 2026-07-02

## License

The repository declares MIT in the README and includes a top-level MIT `LICENSE` file with copyright assigned to Yi Zhang.

MIT licensing permits reuse under its terms, but this local review still defaults to reference-only because benchmark tasks, skill documents, evaluation scripts, third-party repositories, Docker images, and agent-run traces carry separate operational and review burdens.

## Evidence Summary

- The README states the benchmark contains 49 real-world software-engineering tasks paired with curated skill documents.
- The repository exposes a Hugging Face loading path and a full evaluation framework.
- The full evaluation framework requires Python, Docker, Claude Code CLI inside the container image, and an Anthropic API key.
- The configuration file defines task repositories, pinned commits, Docker images, resource limits, network mode, test commands, and evaluation thresholds.
- The lifecycle code validates task files, starts Docker containers, copies local skills into `/home/dev/.claude/skills` when enabled, clones configured repositories, runs Claude Code, preserves or cleans containers, and writes reports.
- The arXiv abstract reports that many evaluated skills yield little or no pass-rate improvement, while specialized skills can help and version-mismatched guidance can degrade outcomes.

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

The main local lesson is negative as much as positive: skill inclusion should not be treated as inherently useful. Skills need task-context fit, evidence, and validation against real acceptance criteria.

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

Do not run benchmark scripts without an isolated environment, explicit credentials policy, Docker image review, and cost controls.

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

`review-swe-skills-bench-20260702` is complete.

Create or keep downstream work only as maintenance/critic work after catalog drift is resolved: derive local skill-validation criteria from the benchmark's evaluation pattern without copying benchmark content.
