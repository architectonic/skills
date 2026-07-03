---
type: Source Candidate
title: Context-Aware Agent Skill Security Analysis
author_or_org: Florian Holzbauer, David Schmidt, Gabriel Gegenhuber, Sebastian Schrittwieser, Johanna Ullrich
source_name: Context Matters: Repository-Aware Security Analysis of the Agent Skill Ecosystem
source_url: https://arxiv.org/abs/2603.16572
review_date: 2026-07-03
runtime_targets: [claude-code, openclaw, agent-skills, skill-security]
skill_format: empirical security analysis
capabilities: [skill-risk-review, repository-context-review, malicious-skill-detection, abandoned-repository-risk]
risk_level: high
ingestion_status: candidate
license: unknown
source_status: summarized
okf_version: "0.2"
---

# Context-Aware Agent Skill Security Analysis

## Why it matters

This source is relevant to the repository's risk gates. It argues that skill safety review should inspect repository context, not only the standalone `SKILL.md` or description text.

The arXiv abstract reports a large empirical analysis of 238,180 unique skills from distribution platforms and GitHub, and says repository-aware analysis sharply reduces suspicious classifications compared with isolated scanners while still surfacing real attack vectors such as abandoned-repository hijacking.

## Evidence captured

- arXiv record: https://arxiv.org/abs/2603.16572
- Initial submission: 2026-03-17; revised: 2026-06-01.
- Venue note on arXiv: AgentSkills '26 Workshop, ACM Conference on AI and Agentic Systems, Best Paper Award.
- Key risk claim: isolated scanner reports can overestimate maliciousness without repository context.
- Key operational risk: abandoned repository hijacking is an agent-skill ecosystem attack vector.

## Review notes

The source should remain candidate/reference-only until Source Reviewer or Risk Auditor verifies:

1. license and reuse rights;
2. whether the paper has code/data links worth cataloging;
3. what concrete checklist changes should be added to `Skill Safety Review`;
4. whether `sources/reviewed/` should include a formal reviewed profile;
5. whether future candidate review must include repository ownership, freshness, and abandonment checks.

## Candidate extraction

Potential reusable capability:

```text
Review agent skills with repository context: compare the skill file, surrounding project, maintainer activity, dependency surface, and abandonment risk before classifying or trusting the skill.
```

Potential normalized artifact type: `Risk Auditor` workflow or update to an existing security-review skill after review.

## Status

Candidate only. Do not normalize, package, or publish until provenance, license, and safety review are complete.
