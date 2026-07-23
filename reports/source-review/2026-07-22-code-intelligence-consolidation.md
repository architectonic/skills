---
type: SourceReviewReport
title: Code Intelligence Skill Consolidation
date: 2026-07-22
status: validation_pending
branch: agent/code-intelligence-consolidation
sources: [Code Review Graph, Codebase Memory MCP, Understand Anything]
tags: [skills, code-intelligence, graph, impact-analysis, lifecycle, privacy, validation]
okf_version: "0.2"
---

# Code Intelligence Skill Consolidation

## Decision

Distill a tool-neutral structural-map procedure and a source-verified change-impact review procedure. Keep graph engines optional and environment-specific. Retain existing package entries only within their actual scopes.

## Source evidence

### Code Review Graph

- reviewed revision: `6ce25b4e53f9df397f5136e86a59e17c02a610fe`;
- license: MIT;
- license blob: `83c1ad6884340e94ff27816b4191ea6a23139cb4`;
- README blob: `48188036da3adaf8cba68566656e1e3624976af4`;
- installer/config implementation blob: `7e4365284d1ccef3bb9edababd761f3364636e66`.

Useful for deterministic structural mapping, incremental freshness, and blast-radius selection. Installation writes MCP and agent configuration, and optional hooks, watchers, CI comments, and merge gates require separate authorization.

### Codebase Memory MCP

- reviewed revision: `7d6cdb23ef5ca2fd51f5d5b7509b33e112ef15f3`;
- license: MIT;
- license blob: `0b95352746a97a8cf2d1f3ba568bc7bb5e514d1f`;
- README blob: `bb4919ed58bd61ee78d051d5fe5b16c802855afd`.

Useful as a persistent local binary/MCP structural engine. Remote installers, binary provenance, auto-indexing, watchers, cache retention, localhost UI, cross-repository indexing, and ADR writes require environment review.

### Understand Anything

- current repository: `Egonex-AI/Understand-Anything`;
- original bookmark owner: `Lum1104`;
- reviewed revision: `6ae71878beb50226a1e4b7e2f52ac6468c86f74b`;
- license: MIT;
- license blob: `5df102e8a2e29cdfb881ae7ec5040f2766564680`;
- README blob: `04efe8311e3cf56d088ac4c4f3da8378784205d2`;
- main skill blob: `f13012e0e5a7648670b40d9f58343a72c0e96f79`.

Useful for explanatory graphs, tours, domain extraction, diff views, and dashboards. Its workflow can install dependencies, write project data/configuration, redirect worktree output to the main checkout, enable hooks, consume substantial model tokens, and generate inferred summaries. Those behaviors remain explicit review boundaries.

## First-party working source

Added:

1. `skills/codebase-structural-map.md`
2. `skills/change-impact-review.md`

Both:

- are engine-neutral;
- work with an approved fresh index or ordinary source search;
- record repository revision, tool revision, scope, exclusions, output, freshness, and blind spots;
- distinguish parser facts, heuristics, semantic edges, and LLM-generated summaries;
- verify consequential claims against source, configuration, history, tests, or runtime evidence;
- separate installation, hooks, watchers, UI, CI comments, merge gates, and canonical writes from analysis;
- remain outside `core/manifest.json` pending utility evaluation.

## Catalog architecture

Added bounded decision clusters under `operations/catalog-decisions/*.json`.

Updated `scripts/apply_catalog_decisions.py` to:

- merge the original decision file and sorted cluster files;
- reject duplicate decisions across files;
- expose every contributing file in the generated catalog and install manifest;
- preserve the existing lifecycle and installation schema.

All catalog workflows now trigger on clustered decision files and run the central validator.

## Package decisions

| Entry | Lifecycle | Install | Risk | Scope |
|---|---|---|---|---|
| `Graphify Onboarding` | reviewed | conditional | medium | Derived graph onboarding, not canonical truth |
| `monorepo-navigator` | reviewed | conditional | high | Monorepo impact, CI, migration, history, cache, and publication |
| `codebase-design` | reviewed | conditional | low | Optional deep-module doctrine, not mandatory vocabulary |

Total deep catalog decisions after this batch: 16.

## Boundaries

- No upstream installer, binary, package, MCP server, graph, dashboard, source index, benchmark output, model call, hook, watcher, CI comment, ADR, or configuration was executed or copied.
- No repository source was indexed.
- No imported package body was edited.
- No external source was promoted into the reviewed core.
- No npm publication was attempted.

## Acceptance tests

| Test | Expected |
|---|---|
| Sixteen deep catalog decisions are applied | Pass in PR validation |
| Cluster decision file appears in the install manifest | Pass in PR validation |
| Duplicate decisions across files fail validation | Pass by processor design |
| Graphify remains derived-not-canonical and review gated | Pass in PR validation |
| Monorepo navigation is high-risk and conditional | Pass in PR validation |
| Codebase design becomes low-risk optional doctrine | Pass in PR validation |
| Two code-intelligence skills have pinned source revisions | Pass in PR validation |
| Graph evidence requires source verification | Pass in PR validation |
| Install/config/hook/watcher/CI mutations remain separately gated | Pass in PR validation |
| Prior design, video, SEO, and classification decisions remain intact | Pass in PR validation |

## Next justified action

After validation and merge:

1. evaluate the two procedures on small, monorepo, dynamic-framework, stale-index, and false-positive fixtures;
2. continue with memory/living-knowledge sources or BMAD investigation as the next skills cluster;
3. keep runtime installation and Workframe adapters for the later Workframe pass;
4. continue classification cleanup independently in bounded semantic batches.
