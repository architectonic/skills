---
type: Skill
title: Change Impact Review
description: Use when reviewing a working-tree diff, commit, or pull request and the agent must identify affected behavior, callers, dependents, tests, routes, data flows, and operational risk without treating graph output as proof.
tags: [skill, software-engineering, code-review, impact-analysis, graph, diff, pull-request, tests, verification, okf]
timestamp: 2026-07-22T00:00:00-03:00
okf_version: "0.2"
source_status: distilled-reviewed
source_name: Architectonic synthesis of reviewed Code Review Graph, Codebase Memory MCP, Understand Anything, and local review doctrine
source_url: https://github.com/architectonic/skills/blob/main/sources/reviewed/2026-07-22-code-intelligence-cluster.md
source_revision: code-review-graph@6ce25b4e53f9df397f5136e86a59e17c02a610fe; codebase-memory-mcp@7d6cdb23ef5ca2fd51f5d5b7509b33e112ef15f3; understand-anything@6ae71878beb50226a1e4b7e2f52ac6468c86f74b
license: Apache-2.0
source_license_status: all-reviewed-sources-mit
source_content_copied: false
domain: software-engineering
artifact_kind: skill
target_surfaces: [skills, workframe]
risk_level: medium
requires_review: false
review_status: source_reviewed_utility_evaluation_pending
---

# Change Impact Review

## Trigger

Use when reviewing a working-tree diff, commit, or pull request and the agent must identify affected behavior, callers, dependents, tests, routes, data flows, and operational risk without treating graph output as proof.

Use ordinary source search when no approved fresh graph exists. Do not install or refresh a graph engine merely to satisfy the form of the workflow when the diff is small and directly inspectable.

## Purpose

Select the smallest sufficient review surface, trace plausible impact beyond changed lines, and convert derived graph evidence into source-verified findings with explicit confidence and test implications.

## Inputs

- Diff, commit range, or pull request under review.
- Base and head revisions.
- Repository instructions and architecture constraints.
- Existing tests, CI results, issue/PR context, and acceptance criteria.
- Approved structural graph or index, including engine/version, source commit, freshness, exclusions, and coverage.
- Source-search, history, blame, and runtime/configuration tools available.
- Authorization for comments, status checks, merge gates, labels, or other repository mutations.

## Procedure

1. **Resolve the review target.** Record base, head, changed files, uncommitted state, generated files, renames, deletions, and whether the diff is complete.
2. **Read intent before impact.** Inspect the issue, PR body, specification, tests, and changed source to understand the intended behavior and acceptance criteria.
3. **Check graph suitability.** Use graph evidence only when the index covers the relevant languages and paths and is fresh enough for the base/head state. Record stale or excluded regions.
4. **Identify changed symbols and contracts.** Determine modified interfaces, schemas, routes, commands, configuration keys, events, data models, permissions, dependencies, and persisted formats.
5. **Generate an impact hypothesis.** Use graph queries or source search to identify likely callers, dependents, implementations, tests, consumers, routes, data flows, and cross-package or cross-service edges.
6. **Verify in source.** Inspect every consequential relationship in actual code, manifests, configuration, generated artifacts, history, or tests. Mark graph-only edges as unverified and do not report them as defects.
7. **Look beyond static edges.** Check dynamic imports, dependency injection, reflection, framework registration, configuration-driven routing, templates, generated code, database migrations, feature flags, message channels, and external APIs that a static graph may miss.
8. **Inspect negative impact.** Consider deleted behavior, broken fallbacks, error paths, cancellation, retries, permissions, privacy, concurrency, caching, compatibility, rollback, and observability.
9. **Map test obligations.** Identify existing tests that should exercise the change, tests likely affected, missing coverage, and the minimum relevant commands. Do not assume graph-linked tests are sufficient.
10. **Evaluate operational scope.** Check deployment, migration, data, environment, secret, performance, cost, external-service, and release implications when the changed contract reaches them.
11. **Separate findings from questions.** A finding needs evidence, impact, and a correction criterion. Uncertain relationships become questions or follow-up checks.
12. **Run bounded verification.** Execute the smallest relevant build, typecheck, lint, tests, static checks, or reproduction allowed by the environment. Record what was not run.
13. **Write only with authorization.** Posting a PR comment, review, status, label, sticky summary, or merge gate is a separate repository mutation. Prepare the review first and publish only when explicitly requested.

## Output Contract

Return:

1. review target and intended behavior;
2. graph/index provenance and freshness, or no-engine decision;
3. changed contracts and symbols;
4. source-verified impact surface;
5. dynamic/configuration relationships checked;
6. findings with severity, evidence, impact, and correction criterion;
7. questions and unverified graph hypotheses;
8. affected and missing tests;
9. commands and results;
10. operational and migration implications;
11. residual uncertainty;
12. publication status.

## Verification

- Base/head and changed-file scope are explicit.
- The review begins from intended behavior and actual changed source.
- Graph coverage, freshness, exclusions, and engine revision are disclosed.
- Every reported impact or defect is supported by source, configuration, history, test, or runtime evidence.
- Static-analysis blind spots were considered.
- Findings are separated from hypotheses and questions.
- Tests are selected from behavior and contracts, not only graph proximity.
- Repository comments, statuses, labels, gates, or merges were not mutated without authorization.
- The final review states what was not inspected or executed.

## Failure Modes

- Treating a high graph risk score as a defect.
- Reporting an inferred caller without reading the call site.
- Using a stale graph after significant branch or working-tree changes.
- Ignoring excluded files, unsupported languages, generated code, configuration, or runtime registration.
- Reviewing only changed lines and missing contract consumers.
- Running the entire repository test suite when a smaller verified set is sufficient.
- Assuming linked tests prove behavioral coverage.
- Posting a public PR comment containing sensitive paths, data, or speculative findings.
- Enabling CI comments or merge gates during a read-only review.
- Converting uncertainty into confident severity labels.

## Provenance Boundary

This is an original first-party procedure distilled from reviewed change-impact systems and Architectonic source-grounding doctrine. No upstream skill body, graph query, benchmark output, repository data, PR comment, or generated review was copied.