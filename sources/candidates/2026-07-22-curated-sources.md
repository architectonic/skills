---
type: Source Candidate Batch
title: Curated Skill Sources — 2026-07-22
description: High-signal source candidates from the July bookmark audit, deduplicated against the current package-facing registry.
tags: [skills, discovery, candidates, provenance, design, media, seo, research, code-graphs]
review_date: 2026-07-22
risk_level: medium
ingestion_status: candidate
source_status: summarized
okf_version: "0.2"
---

# Curated Skill Sources — 2026-07-22

## Boundary

This batch records source and routing evidence only. It does not authorize installation, copy third-party content, execute repository code, grant credentials, or promote any source into the reviewed core.

Each candidate still requires exact-revision capture, license review, hidden-script and dependency inspection, semantic deduplication, safety review, and a with/without-skill utility evaluation.

## Deduplication finding

The July audit found that discovery and classification are separate problems:

- `ai-seo` is already package-facing but needed risk and target-surface classification.
- the HyperFrames family is already package-facing but was buried in `uncategorized` with weak risk metadata;
- several apparently new capabilities overlap existing `frontend-design`, `canvas-design`, `litreview`, `github-deep-research`, `media-use`, `benchmark`, and agent-operation skills;
- external source names cannot be treated as unique capability identities.

Do not create a second skill merely because the upstream repository or slug differs. Compare trigger, inputs, procedure, verification, dependencies, side effects, and measured task delta.

## Review-next sources

| Source | Candidate artifacts | Likely surfaces | Dedupe status | Initial risk | Next review |
|---|---|---|---|---|---|
| `remotion-dev/skills` | programmatic-video framework skill(s) | skills, workframe, click-blue | not found as an exact source | medium/high | inspect exact skills, revision, license, renderer and dependency scope |
| `JakubAntalik/transitions.dev` | transition design; transition polish | skills, design-system | capability gap appears distinct | low/medium | inspect reduced-motion, framework assumptions, and visual verification |
| `Leonxlnx/taste-skill` | design audit, redesign, brand-kit, visual direction | skills, design-system, click-blue | overlaps existing frontend/design skills | medium | compare procedures and measured output against local design doctrine |
| `Nutlope/hallmark` | anti-template interface audit and redesign | skills, design-system, click-blue | overlaps design audit candidates | medium | inspect license, scripts, rubric, and distinctness |
| `tushaarmehtaa/tushar-skills` | deploy check, auth wiring, SEO readiness, GTM launch, anti-slop | skills, workframe, click-blue | mixed; per-skill semantic review required | medium/high | split by capability and review executable/auth/deploy surfaces separately |
| `StarTrail-org/PixelRAG` | visual retrieval; pixelbrowse | skills, workframe, design-system | related to VISUALSKILL source candidate, not identical | medium/high | inspect models, indexing, document privacy, evaluation, and runtime cost |
| `SeanJ1ang/design-judge-skills` | evidence-based design evaluation and award workflow | skills, design-system, click-blue | design evaluation appears distinct | medium | inspect exact source revision, shared datasets, license, and current-rule lookup |
| `every-app/open-seo` | SEO skills, MCP connector, self-hosted application | skills, workframe, click-blue | `ai-seo` already exists; other artifacts unresolved | high | represent as one source with multiple artifacts; review provider credentials and external data |
| `heygen-com/hyperframes` | video skill suite, CLI, media adapters, runtime | skills, workframe, click-blue, design-system | seven package entries already exist | medium/high | review imported bodies and runtime dependencies before any promotion |
| `mvanhorn/last30days-skill` | recent multi-source research | skills, architectonic, click-blue | overlaps research skills but adds explicit recency/source resolution | medium/high | inspect provider terms, API/scraping behavior, and date-window verification |
| `bradautomates/claude-video` | frame-and-transcript grounded video review | skills, workframe, click-blue | distinct from generic media-use | medium/high | inspect extraction tools, private-video handling, dependencies, and benchmarks |
| `tirth8205/code-review-graph` | graph build; delta review; PR review | skills, workframe, architectonic | overlaps architecture review but adds persistent structural graph | medium/high | inspect repository indexing, language coverage, persistence, and review delta |
| `DeusData/codebase-memory-mcp` | persistent code graph MCP | workframe, architectonic, skills reference | connector/runtime, not a flat skill | high | review filesystem authority, MCP tools, persistence, and repository isolation |
| `bmad-code-org/BMAD-METHOD` | investigation, adaptive routing, PRD and UX workflows | skills, architectonic, workframe | extensive overlap with existing doctrine and workflows | medium/high | extract only bounded distinct procedures; reject framework duplication |
| `killaislop.com` | design quality and anti-template principles | skills, design-system | overlaps Hallmark, Taste, and anti-slop entries | low/medium | verify canonical source/license and retain only measurable distinct procedure |

## Registry and discovery sources

| Source | Role | Boundary |
|---|---|---|
| `skills.sh` | skill-source discovery | metadata sampling only; no bulk mirror |
| `integrations.sh` | connector and protocol discovery | registry presence is not trust or compatibility |
| `webmcp.com` | WebMCP capability discovery | review browser permissions, tool declarations, and origin boundaries |

## Promotion requirements

A candidate may advance only when all applicable gates pass:

1. canonical upstream source and exact revision recorded;
2. license and redistribution status recorded;
3. source tree inspected for scripts, hooks, binaries, install steps, external calls, and hidden instructions;
4. credential, browser, filesystem, network, execution, publication, and external-mutation scope declared;
5. semantic duplicate and supersession check completed;
6. representative task executed with and without the candidate;
7. outcome, token cost, runtime cost, and new failure modes recorded;
8. package-facing wording adapted to local authority and privacy boundaries;
9. human review completed for high-risk or externally mutating capabilities.

## Next bounded batch

Review in this order:

1. Transitions and Hallmark/Taste as design-quality candidates;
2. Remotion and existing HyperFrames entries as programmatic-video candidates;
3. OpenSEO as a multi-artifact source rather than a flat skill;
4. Last30Days and Claude Video as evidence-grounding candidates;
5. Code Review Graph and Codebase Memory as graph/runtime candidates.
