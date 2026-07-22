---
type: Skill
title: Codebase Structural Map
description: Use when an unfamiliar or large repository needs a derived structural index of files, symbols, dependencies, routes, tests, or domains before architecture review, onboarding, or change analysis.
tags: [skill, software-engineering, code-intelligence, graph, indexing, architecture, onboarding, privacy, verification, okf]
timestamp: 2026-07-22T00:00:00-03:00
okf_version: "0.2"
source_status: distilled-reviewed
source_name: Architectonic synthesis of reviewed Code Review Graph, Codebase Memory MCP, Understand Anything, and Graphify boundaries
source_url: https://github.com/architectonic/skills/blob/main/sources/reviewed/2026-07-22-code-intelligence-cluster.md
source_revision: code-review-graph@6ce25b4e53f9df397f5136e86a59e17c02a610fe; codebase-memory-mcp@7d6cdb23ef5ca2fd51f5d5b7509b33e112ef15f3; understand-anything@6ae71878beb50226a1e4b7e2f52ac6468c86f74b
license: Apache-2.0
source_license_status: all-reviewed-sources-mit
source_content_copied: false
domain: software-engineering
artifact_kind: skill
target_surfaces: [skills, workframe, architectonic]
risk_level: medium
requires_review: true
review_status: source_reviewed_utility_evaluation_pending
---

# Codebase Structural Map

## Trigger

Use when an unfamiliar or large repository needs a derived structural index of files, symbols, dependencies, routes, tests, or domains before architecture review, onboarding, or change analysis.

Skip graph construction when the repository is small, the question is local, ordinary source search is sufficient, the language is unsupported, the environment forbids installation or indexing, or the expected graph cost exceeds the likely benefit.

## Purpose

Create or refresh a bounded, reproducible structural map that accelerates source discovery without replacing source files, tests, configuration, history, architecture records, or human-reviewed project knowledge.

## Inputs

- Repository root and exact scope.
- Current commit or revision.
- User question or downstream task.
- Existing graph/index engine, version, configuration, and store when available.
- Languages, generated code, vendored code, submodules, worktrees, and monorepo boundaries.
- Secret, private-data, memory, artifact, and large-directory exclusions.
- Approved output directory and retention policy.
- Local compute, storage, model, token, and time budget.
- Authorization for installation, config writes, watchers, hooks, UI, model calls, or cross-repository indexing, if any.

## Procedure

1. **State the need.** Explain what the structural map must help decide and why ordinary source inspection is insufficient.
2. **Inspect before selecting a tool.** Read repository instructions, language manifests, workspace files, existing indexes, ignore files, architecture documents, and current graph metadata.
3. **Choose the least powerful sufficient path.** Prefer, in order:
   - an existing fresh approved index;
   - an existing approved engine with a bounded refresh;
   - deterministic local parsing or source-search-derived mapping;
   - LLM-assisted summaries only when needed and approved;
   - no graph when source inspection is cheaper or safer.
4. **Declare engine boundaries.** Record the engine, exact version or revision, installation source, execution mode, model provider if any, persistent store, network behavior, and files/configuration it may write.
5. **Review exclusions.** Exclude secrets, credentials, private memory, personal data, generated outputs, dependency/vendor trees, binaries, caches, large irrelevant assets, and unrelated repositories. Record intentional exceptions.
6. **Separate installation from analysis.** Installing a binary or package, running a remote installer, editing MCP or agent configuration, adding symlinks, starting a server, enabling a dashboard, or changing execution policy requires explicit approval and rollback evidence.
7. **Separate persistence from analysis.** Auto-indexing, background watchers, post-commit hooks, CI integration, cross-repository stores, and durable ADR or knowledge writes require separate approval.
8. **Bind scope and output.** Resolve the actual repository/worktree root and approved output location. Do not redirect writes from a worktree to the main checkout, user home, global cache, or another repository without disclosure and approval.
9. **Build or refresh.** Index only the approved scope. Preserve the source commit, configuration hash, exclusions, parser coverage, skipped files, errors, timing, and output artifacts.
10. **Classify evidence.** Distinguish:
    - parser facts such as file, symbol, import, route, and direct call edges;
    - heuristic edges such as inferred call, data-flow, or framework relationships;
    - semantic similarity and communities;
    - LLM-generated summaries, domains, flows, and explanations.
11. **Sample-verify.** Check representative entry points, modules, routes, tests, callers, dynamic loading, generated code, configuration-driven links, and known cross-package or cross-service paths against actual source.
12. **Measure freshness.** Compare the index revision with the working tree and requested diff. Mark stale sections and refresh only when justified.
13. **Publish as derived evidence.** Store the map separately from canonical architecture, memory, ontology, and decisions. Label tool, revision, source commit, confidence, exclusions, and known blind spots.
14. **Define cleanup.** Record how to stop servers/watchers, remove hooks/config, uninstall the engine, retain or delete graph data, and restore changed files.

## Output Contract

Return or record:

1. question and expected value;
2. repository scope and source commit;
3. engine or no-engine decision;
4. installation and execution provenance;
5. exclusions and private-data boundary;
6. output/store location and retention;
7. parser and language coverage;
8. generated artifacts;
9. evidence classes and confidence;
10. sample-verification results;
11. freshness status and blind spots;
12. persistent processes or mutations;
13. cleanup and rollback instructions.

## Verification

- The map answers a stated repository question rather than merely producing a visualization.
- Repository root, worktree behavior, source revision, and output location are explicit.
- Exclusions protect secrets, private knowledge, generated assets, dependencies, and irrelevant files.
- Installation, configuration, hooks, watchers, UI, model calls, and cross-repository indexing were separately authorized.
- Tool and artifact revisions are recoverable.
- Representative nodes and relationships were checked against actual source and tests.
- Parser facts, heuristics, semantic edges, and LLM summaries are clearly distinguished.
- Stale indexes are not treated as current.
- Generated graph outputs do not overwrite canonical architecture, memory, ontology, or decisions.
- Cleanup and rollback are documented.

## Failure Modes

- Building a graph because a graph tool is available rather than because it helps a decision.
- Running a remote shell or PowerShell installer without review.
- Allowing an installer to modify every detected coding agent by default.
- Indexing secrets, private memory, generated outputs, or unrelated repositories.
- Redirecting graph writes from a worktree to the main checkout silently.
- Enabling auto-index, watchers, hooks, UI, or CI integration during a read-only request.
- Treating semantic similarity, communities, inferred domains, or risk scores as source truth.
- Repeating upstream benchmark claims as expected local performance.
- Persisting source-derived data indefinitely without retention policy.
- Committing large generated graph artifacts blindly.
- Using a graph to avoid reading the source that supports a consequential conclusion.

## Provenance Boundary

This is an original first-party procedure distilled from reviewed code-intelligence systems and Architectonic graph/source hierarchy doctrine. No upstream skill body, installer, binary, source index, graph output, benchmark result, configuration, or model-generated summary was copied.