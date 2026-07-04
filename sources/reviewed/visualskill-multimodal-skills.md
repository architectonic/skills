---
type: Source Profile
title: VISUALSKILL Multimodal Skills for Computer-Use Agents
description: Reviewed source profile for hierarchical multimodal GUI/computer-use skill artifacts with on-demand topic and figure retrieval.
tags: [source-profile, skills, multimodal, computer-use, gui, mcp, reviewed, reference-only]
okf_version: "0.2"
source_url: https://arxiv.org/abs/2606.18448
source_name: "VISUALSKILL: Multimodal Skills for Computer-Use Agents"
source_author: Ziyan Jiang; Li An; Yujian Liu; Jiabao Ji; Qiucheng Wu; Jacob Andreas; Yang Zhang; Shiyu Chang
source_repository: https://github.com/XMHZZ2018/VisualSkills
source_commit: unavailable; repository returned 404 through GitHub connector in this pass
license: repository unavailable through GitHub connector; code, figures, datasets, and paper reuse terms not verified
runtime_targets: [computer-use-agents, claude-code, mcp, gui-automation, multimodal-agents]
skill_format: hierarchical multimodal skill with central index, per-topic files, and figure retrieval
risk_level: medium
ingestion_status: reviewed-reference-only
reviewed_at: 2026-07-03
reviewed_by: Source Reviewer
---

# VISUALSKILL Multimodal Skills for Computer-Use Agents

## Review Decision

Accepted as a reviewed reference-only source profile.

Do not normalize this source directly into a packaged skill yet. The arXiv record is useful evidence that GUI/computer-use skills may need multimodal artifacts, but the claimed reproduction repository was not accessible through the GitHub connector during this pass and redistribution rights for code, figures, datasets, screenshots, and paper artifacts were not verified.

## Provenance

- Paper: https://arxiv.org/abs/2606.18448
- Claimed code/reproduction repository: https://github.com/XMHZZ2018/VisualSkills
- Repository inspection result: `GitHub.get_repo` returned `404 Not Found` for `XMHZZ2018/VisualSkills` in this pass.
- Initial arXiv date recorded by the candidate and public arXiv metadata: 2026-06-16.
- The arXiv record states that the code is available at the claimed GitHub repository, but repository availability could not be confirmed through the connector.

## License

License status remains incomplete.

- The repository was unavailable through the connector, so repository license, package metadata, figure license, benchmark license, and dataset terms could not be verified.
- Therefore this profile remains summarized/reference-only.
- Do not copy paper text, code, figures, screenshots, UI examples, benchmark artifacts, MCP tool implementation, or result tables into local package artifacts.

## Evidence Summary

The source proposes a multimodal skill format for computer-use agents. The locally relevant idea is that GUI workflows are not fully captured by text-only procedures because agents must identify interface elements and verify visual state after actions.

Operationally relevant signals:

- The paper describes a hierarchical skill artifact organized around a central index and per-topic files.
- The paper describes a `load_topic` MCP tool that retrieves topic-specific text and figures on demand.
- The reported benchmark context includes CUA-World and OSExpert-Eval.
- The reported evaluation compares no-skill, matched text-only skill, and multimodal VISUALSKILL conditions.
- The result is useful as design evidence, not as a directly importable artifact.

## Usefulness

This source is useful because the local catalog is currently text-oriented and may underrepresent skills where visual state recognition is part of the procedure.

Acceptable local uses now:

- reference-only source profile;
- design input for future multimodal skill-format doctrine;
- caution that GUI/computer-use procedures may need screenshots, state cards, UI-region references, or visual verification checks;
- future Critic input when checking whether local skill formats handle non-textual evidence.

Unacceptable local uses now:

- copying the claimed repository content or paper artifacts;
- reproducing figures or screenshots;
- treating the reported scores as locally validated for `architectonic-skills`;
- installing or running MCP/topic-loading code without a separate repository, license, and sandbox review;
- normalizing a multimodal skill artifact before the local package has a safe asset policy.

## Security and Operational Review Notes

Risk level: medium.

Risk areas:

- MCP retrieval tools can become hidden context-expansion or prompt-injection channels if topics and figures are untrusted;
- multimodal artifacts may include screenshots, UI captures, copyrighted figures, or private interface data;
- visual examples can overfit agents to stale UI layouts;
- topic-loading must be bounded, inspectable, and provenance-preserving;
- repository unavailability blocks code/license verification.

## Ingestion Decision

Status: reviewed-reference-only.

No normalization item is created from this pass. A future Critic or Normalizer may design a local multimodal-skill asset policy after reviewing additional available, licensed sources and defining safe handling for screenshots, figures, captions, visual state cards, and MCP topic retrieval.
