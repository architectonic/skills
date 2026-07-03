---
type: Source Profile
title: Skill Usage in Realistic Settings
description: Reviewed source profile for realistic skill retrieval, selection, and refinement benchmarking in large agent skill libraries.
tags: [source-profile, skills, evaluation, retrieval, refinement, benchmark, reviewed, reference-only]
okf_version: "0.2"
source_url: https://arxiv.org/abs/2604.04323
source_name: How Well Do Agentic Skills Work in the Wild: Benchmarking LLM Skill Usage in Realistic Settings
source_author: Yujian Liu; Jiabao Ji; Li An; Tommi Jaakkola; Yang Zhang; Shiyu Chang
source_repository: https://github.com/UCSB-NLP-Chang/Skill-Usage
source_commit: 03446d16f7b659ccc93ac5bd512f62e9b7fabb45
license: repository license file not found in this pass; arXiv/paper and dataset reuse terms not verified
runtime_targets: [claude-code, terminal-bench, harbor, skill-retrieval, skill-refinement, skill-evaluation]
skill_format: benchmark-and-evaluation-framework
risk_level: medium
ingestion_status: reviewed-reference-only
reviewed_at: 2026-07-03
reviewed_by: Source Reviewer
---

# Skill Usage in Realistic Settings

## Review Decision

Accepted as a reviewed reference-only source profile.

Do not normalize this source directly into a packaged skill yet. The durable local value is a Critic and catalog-quality check: skill libraries should be evaluated by retrieval quality, selection behavior, task fit, and refinement outcomes rather than by raw skill count.

## Provenance

- Paper: https://arxiv.org/abs/2604.04323
- Code/reproduction repository: https://github.com/UCSB-NLP-Chang/Skill-Usage
- Repository inspected commit: `03446d16f7b659ccc93ac5bd512f62e9b7fabb45`
- Initial arXiv date recorded by the candidate and public arXiv metadata: 2026-04-06.
- The repository README identifies itself as code and data for the paper and links to the arXiv record and Hugging Face dataset.

## License

License status remains incomplete.

- A repository `LICENSE` or `LICENSE.md` file was not found during this pass.
- The repository README links to a Hugging Face dataset, but dataset terms were not separately verified here.
- Therefore this profile remains summarized/reference-only.
- Do not copy code, data, benchmark tasks, prompts, result tables, figures, or paper text into local package artifacts until license and attribution are separately verified.

## Evidence Summary

The source studies skill utility under progressively more realistic conditions. The locally relevant finding is that skill benefits become fragile when an agent must retrieve from a large noisy skill pool and adapt partially relevant skills.

Operationally relevant signals:

- The paper evaluates retrieval from a 34k real-world skill collection rather than only hand-curated skills.
- The repository README describes a framework for evaluating skill utility from hand-curated skills through noisy-pool retrieval.
- The README lists settings for force-loaded, curated, distractor, no-skill, retrieved, and retrieved-with-refinement evaluations.
- The repository includes scripts for retrieval, query-specific refinement, query-agnostic refinement, result aggregation, and skill-usage analysis.
- The README says experiments cover SkillsBench and Terminal-Bench 2.0 with Claude Opus 4.6, Kimi K2.5, and Qwen3.5-397B.

## Usefulness

This source is useful because the local catalog currently tracks skill counts and risk counts, but does not yet measure whether a future agent can retrieve and apply the right skill.

Acceptable local uses now:

- reference-only source profile;
- Critic input for library-quality evaluation;
- future catalog-quality rubric for retrieval and applicability;
- future evaluation-playbook seed after license and reproduction requirements are reviewed;
- caution against treating `catalog_skill_count` as a value metric by itself.

Unacceptable local uses now:

- copying the benchmark implementation, datasets, tasks, tables, or paper text;
- treating the reported improvements as locally validated for `architectonic-skills`;
- normalizing a new evaluation workflow before license, dataset, and execution-safety review;
- publishing this as endorsed package content;
- running repository scripts blindly because the setup requires Docker, Harbor, API keys, Hugging Face downloads, and local or cloud model execution.

## Security and Operational Review Notes

Risk level: medium.

Risk areas:

- reproduction requires local environment setup, Docker, dependencies, external downloads, and model/API access;
- downloaded skill corpora and search indexes should be treated as untrusted input until separately scanned;
- benchmark harnesses may execute tasks in containers and should not be run outside a controlled sandbox;
- the repository is useful as evidence for evaluation design, not as an installable skill source.

## Ingestion Decision

Status: reviewed-reference-only.

Create a Critic queue item to evaluate whether the local catalog should add a quality metric or report that samples retrieval/selectability across `dist/skills/`. The next step should be a local, small, non-executing catalog-quality rubric, not a benchmark reproduction run.

## Follow-Up Queue

Critic should consume `critic-skill-retrieval-quality-20260703` after remaining Source Reviewer pressure is reduced or if raw catalog-count optimization reappears.