---
type: Source Profile
title: Repository-Context Agent Skill Security
description: Reviewed source profile for repository-aware security analysis of agent skills and abandoned-repository hijack risk.
tags: [source-profile, skills, security, repository-context, supply-chain, reviewed, reference-only]
okf_version: "0.2"
source_url: https://arxiv.org/abs/2603.16572
source_name: Context Matters: Repository-Aware Security Analysis of the Agent Skill Ecosystem
source_author: Florian Holzbauer; David Schmidt; Gabriel Gegenhuber; Sebastian Schrittwieser; Johanna Ullrich
source_repository: https://github.com/holzsec/repository-context-agentskills
license: arXiv paper license visible through arXiv; code repository license not verified in this pass
runtime_targets: [claude-code, openclaw, agent-skills, skill-security, skill-marketplaces]
skill_format: empirical-security-analysis-and-reproduction-bundle
risk_level: high
ingestion_status: reviewed-reference-only
reviewed_at: 2026-07-03
reviewed_by: Source Reviewer
---

# Repository-Context Agent Skill Security

## Review Decision

Accepted as a reviewed reference-only source profile.

Do not normalize this source directly into a packaged skill. The durable local value is a Risk Auditor checklist improvement: third-party skill review should inspect repository context, repository maturity, ownership/freshness, code/README alignment, marketplace references, and abandoned-repository hijack risk before classifying or trusting a skill.

## Provenance

- Paper: https://arxiv.org/abs/2603.16572
- Code/reproduction bundle: https://github.com/holzsec/repository-context-agentskills
- Initial arXiv submission: 2026-03-17.
- Revised arXiv version: 2026-06-01.
- Venue note: AgentSkills '26 Workshop, ACM Conference on AI and Agentic Systems.
- The GitHub repository identifies itself as the code and data-artifact bundle accompanying the paper.

## License

License status remains incomplete.

- The arXiv record exposes a paper license link, but this pass did not verify redistribution terms for copied paper text.
- The code repository was inspected as a public GitHub source, but a repository license was not verified in this pass.
- Therefore this profile remains summarized/reference-only.
- Do not copy code, data, figures, prompts, tables, or paper text into local package artifacts until license and attribution are separately verified.

## Evidence Summary

The paper reports a large empirical security analysis of agent skills across marketplaces and GitHub. The reviewed claim most relevant to this repository is not the exact scanner rate, but the review method: scanner output should be treated as a signal requiring repository context, not as ground truth.

Operationally relevant findings:

- Existing marketplace scanners may classify high percentages of skills as malicious when inspecting skill files in isolation.
- Repository-aware analysis compares the skill description with surrounding repository documentation, code, and metadata.
- The paper reports that contextual analysis reduces the suspicious set sharply and helps separate likely false positives from genuinely suspicious repositories.
- The paper identifies abandoned-repository hijacking as a real agent-skill ecosystem attack vector.
- The accompanying repository includes RQ1 dataset collection, RQ2 malicious-classification analysis, and RQ3 repository-context scoring scripts.

## Usefulness

This source is useful because the local aggregator is beginning to ingest public skill candidates. A pure file-level review is insufficient for this repository's risk gate.

Acceptable local uses now:

- reference-only source profile;
- risk-gate input for third-party skill review;
- checklist source for repository-context review;
- future Critic input for evaluating scanner false positives;
- future Source Reviewer rubric for abandoned repository and marketplace-reference checks.

Unacceptable local uses now:

- copying reproduction code or datasets into this repository;
- treating the paper's scoring model as locally validated;
- treating GitHub stars, marketplace presence, or scanner pass/fail as sufficient safety evidence;
- normalizing a new skill from this source before the Risk Auditor translates it into a narrow local checklist;
- publishing this as endorsed package content.

## Security Review Notes

Risk level: high.

Risk areas this source adds to the local review gate:

- marketplace entries may reference repositories that have moved, disappeared, become private, or been hijacked;
- abandoned repositories can become a supply-chain attack surface;
- a skill can look suspicious in isolation but be expected behavior inside a legitimate security or automation repository;
- a skill can look benign in isolation while the repository context suggests unrelated or suspicious behavior;
- repository metadata is useful but must not become a popularity shortcut;
- external datasets and reproduction scripts may require local execution, large downloads, or credentialed APIs and should not be run blindly.

## Ingestion Decision

Status: reviewed-reference-only.

Create a Risk Auditor queue item to decide whether `Skill Safety Review` or adjacent risk doctrine should add a repository-context checklist. The checklist should be local and concise, not copied from the paper.

## Follow-Up Queue

Risk Auditor should consume `risk-repository-context-skill-review-20260703` before any Normalizer turns this source into a procedure.