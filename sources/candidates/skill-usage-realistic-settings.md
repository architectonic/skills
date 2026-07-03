---
type: Source Candidate
title: Skill Usage in Realistic Settings
author_or_org: UCSB NLP Chang Lab / Yujian Liu, Jiabao Ji, Li An, Tommi Jaakkola, Yang Zhang, Shiyu Chang
source_name: How Well Do Agentic Skills Work in the Wild: Benchmarking LLM Skill Usage in Realistic Settings
source_url: https://arxiv.org/abs/2604.04323
review_date: 2026-07-03
runtime_targets: [claude-code, terminal-bench, skill-retrieval, skill-refinement]
skill_format: benchmark and retrieval/refinement framework
capabilities: [skill-retrieval, skill-selection, skill-refinement, skill-evaluation]
risk_level: medium
ingestion_status: candidate
license: unknown
source_status: summarized
okf_version: "0.2"
---

# Skill Usage in Realistic Settings

## Why it matters

This source is directly relevant to the `skills` repository because it tests whether large skill collections help agents under realistic retrieval and selection conditions, not only curated benchmark settings.

The paper reports that skill benefits are fragile when agents must retrieve from noisy collections and adapt partially relevant skills. It also reports that query-specific refinement can recover some lost performance when the retrieved skills are already reasonably relevant.

## Evidence captured

- arXiv record: https://arxiv.org/abs/2604.04323
- Paper date: 2026-04-06.
- Claimed code link from the arXiv record: https://github.com/UCSB-NLP-Chang/Skill-Usage
- Reported corpus: 34k+ real-world skills collected from open-source repositories and skill aggregation surfaces.
- Reported lesson: retrieval quality, selection behavior, and refinement matter as much as raw skill count.

## Review notes

The source should remain candidate/reference-only until Source Reviewer verifies:

1. repository availability and license;
2. whether code/data can be reused or only cited;
3. whether evaluation setup maps to Architectonic's `dist/skills` catalog;
4. whether catalog metadata should add retrieval/refinement fields;
5. whether this implies a Critic queue item for low-value or hard-to-retrieve skills.

## Candidate extraction

Potential reusable capability:

```text
Evaluate and improve a skill library by measuring retrieval quality, selection quality, and task-specific refinement rather than treating catalog size as value.
```

Potential normalized artifact type: `Workflow`, `Evaluation Playbook`, or `Critic` procedure after review.

## Status

Candidate only. Do not normalize, package, or publish until provenance, license, and safety review are complete.
