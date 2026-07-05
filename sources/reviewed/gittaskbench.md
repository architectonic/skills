---
type: Source Profile
title: GitTaskBench
source_name: QuantaAlpha/GitTaskBench
source_url: https://github.com/QuantaAlpha/GitTaskBench
organization: QuantaAlpha
reviewed_at: 2026-07-05T06:13:56-03:00
reviewed_by: Source Reviewer
license: not_found_in_direct_connector_review
runtime_targets: [benchmark, code-agent-evaluation, repository-level-agent-tasks]
skill_format: benchmark-and-evaluation-harness
risk_level: medium
ingestion_status: reference-only-blocked-from-normalization
review_boundary: metadata_and_repository_file_review_no_clone_no_execution_no_content_copy
status: reviewed
---

# GitTaskBench Source Profile

## Summary

`QuantaAlpha/GitTaskBench` is a repository-level benchmark and tooling suite for evaluating code agents on real-world tasks that require using existing GitHub repositories. The source is relevant to the skills corpus because it can inform validation doctrine: task setup, success criteria, execution-completion rate, task pass rate, repository-context use, and benchmark-style acceptance criteria.

## Directly inspected evidence

- `README.md` presents GitTaskBench as a benchmark for code agents solving real-world tasks through repository leveraging and links to an arXiv paper and leaderboard.
- `README.md` reports 54 representative tasks across seven domains and describes repository-level task construction.
- `README.md` documents integrations for OpenHands, SWE-Agent, and Aider, plus `gittaskbench grade` and `gittaskbench eval` commands.
- `setup.py` declares package name `gittaskbench`, version `0.1.0`, console entry point `gittaskbench=gittaskbench.cli:main`, and a broad dependency set.
- `requirements.txt` includes pinned CUDA/PyTorch, image/audio/scientific packages, and a direct GitHub archive dependency for OpenAI CLIP.
- Direct fetch of repository `LICENSE` returned `404 Not Found` during this review.

## Usefulness

Potentially useful as a reference source for:

- skill validation gates;
- acceptance criteria design;
- repository-context evaluation;
- benchmark failure taxonomy around setup, dependencies, task outputs, and tests;
- measuring whether agent procedures improve task completion or pass-rate outcomes.

## Boundary decision

Keep this source `reference-only` and blocked from normalization for now.

Reasons:

- No repository `LICENSE` file was found by direct connector fetch, so redistribution and adaptation boundaries are unclear.
- The repository is a benchmark/tooling suite, not a compact reusable skill.
- Safe reuse does not require copying tasks, ground truth, prompts, reports, or benchmark content.
- Runtime use would require local installation, package execution, heavy pinned dependencies, GPU/CUDA packages, framework-specific batch runners, and task/evaluation commands.
- The dependency surface includes a direct GitHub archive dependency and should not be recommended or run inside the scheduler.

## Allowed future use

Allowed:

- cite as a reference-only benchmark source;
- distill a generic validation principle only after license and attribution are clarified;
- use its public README-level structure to inform internal acceptance-criteria thinking without copying benchmark content.

Not allowed in the scheduler:

- clone the repository;
- execute `pip install`, `gittaskbench`, shell runners, OpenHands, SWE-Agent, or Aider batch scripts;
- copy task definitions, ground truth, reports, prompts, images, datasets, or benchmark code;
- normalize a GitTaskBench-derived skill until license, risk, usefulness, and redistribution boundaries are cleared.

## Review outcome

The review queue item `review-gittaskbench-20260705` is complete. No normalization queue item was created. No risk item was created because the blocking issue is already sufficient: license is missing and execution is unnecessary for the current scheduler role.
