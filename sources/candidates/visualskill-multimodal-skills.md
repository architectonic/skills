---
type: Source Candidate
title: VISUALSKILL Multimodal Skills for Computer-Use Agents
source_url: https://arxiv.org/abs/2606.18448
source_name: VISUALSKILL: Multimodal Skills for Computer-Use Agents
author_or_org: Ziyan Jiang, Li An, Yujian Liu, Jiabao Ji, Qiucheng Wu, Jacob Andreas, Yang Zhang, Shiyu Chang
review_date: 2026-07-03
runtime_targets: [computer-use-agents, claude-code, mcp]
skill_format: hierarchical multimodal skill with topic files and figures
capabilities: [computer-use, gui-navigation, multimodal-skill-artifacts, skill-loading]
risk_level: medium
ingestion_status: candidate
license: unknown
source_status: summarized
okf_version: "0.2"
---

# VISUALSKILL Multimodal Skills for Computer-Use Agents

## Why it matters

This is a current research candidate for multimodal agent skills. It argues that GUI/computer-use skills should not be text-only artifacts because visual figures can help agents identify interface elements and verify workflow state.

The paper describes a hierarchical skill format organized around a central index and per-topic files. A `load_topic` MCP tool retrieves topic-specific text and figures on demand.

## Evidence captured

- arXiv record: https://arxiv.org/abs/2606.18448
- Paper date: 2026-06-16.
- Claimed code link from the arXiv record: https://github.com/XMHZZ2018/VisualSkills
- Claimed benchmark context: CUA-World and OSExpert-Eval.
- Claimed result: VISUALSKILL improves over a no-skill baseline and over a matched text-only skill in the reported setup.

## Review notes

The source should remain candidate/reference-only until Source Reviewer verifies:

1. repository availability and license;
2. whether figures or UI captures can be redistributed;
3. whether the `load_topic` MCP pattern creates safe, bounded retrieval behavior;
4. whether the approach generalizes beyond the paper's applications;
5. whether a distilled internal skill should teach multimodal skill design, not copy the paper artifact.

## Candidate extraction

Potential reusable capability:

```text
Design hierarchical multimodal agent skills for GUI/computer-use workflows where visual state recognition matters.
```

Potential normalized artifact type: `Workflow` or `Skill` after license and safety review.

## Status

Candidate only. Do not normalize, package, or publish until provenance, license, and safety review are complete.
