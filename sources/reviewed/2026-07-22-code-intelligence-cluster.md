---
type: SourceReview
title: Code Intelligence and Change Impact Cluster Review
date: 2026-07-22
status: reviewed_for_distillation
sources: [Code Review Graph, Codebase Memory MCP, Understand Anything]
tags: [skills, code-intelligence, knowledge-graph, impact-analysis, mcp, source-review, provenance, privacy]
okf_version: "0.2"
---

# Code Intelligence and Change Impact Cluster Review

## Decision

Distill two tool-neutral first-party procedures:

1. `skills/codebase-structural-map.md` — create or refresh a derived structural index with explicit scope, exclusions, freshness, provenance, and validation;
2. `skills/change-impact-review.md` — review a diff or pull request using graph evidence when available, then verify every consequential claim against actual source and tests.

Do not vendor or execute any of the three upstream systems as part of this skills review. They are alternative runtimes with different cost, persistence, mutation, and trust profiles. Installing one is a later environment decision, not an implicit consequence of adopting the procedures.

## Code Review Graph

- Repository: https://github.com/tirth8205/code-review-graph
- Reviewed revision: `6ce25b4e53f9df397f5136e86a59e17c02a610fe`
- License: MIT
- License blob: `83c1ad6884340e94ff27816b4191ea6a23139cb4`
- Reviewed README blob: `48188036da3adaf8cba68566656e1e3624976af4`
- Reviewed installation/configuration implementation blob: `7e4365284d1ccef3bb9edababd761f3364636e66`
- Decision: reference and optionally evaluate as a local structural engine; do not make it mandatory.

### Retain

- Tree-sitter-derived structure and dependency relationships.
- Incremental freshness tied to changed files and commit state.
- Blast-radius analysis as a way to choose which source and tests deserve inspection.
- Local-first indexing and an explicit graph database.
- Reproducible benchmark configuration and pinned upstream snapshots as the correct standard for performance claims.
- Dry-run and symmetric uninstall concepts for integration changes.

### Correct or constrain

- Installation writes MCP configuration, hooks, skills, and platform instructions across several coding agents. This requires explicit target-platform approval and a before/after configuration diff.
- Watch mode, commit hooks, and CI comments are persistent automation, not part of a read-only graph query.
- The GitHub Action can write pull-request comments and optionally fail a merge gate. Those permissions require separate repository approval.
- Token-reduction and impact-quality metrics remain upstream benchmark claims, not guaranteed results for an arbitrary repository.
- A parser edge or risk score is evidence for inspection, not proof that a behavior or defect exists.

## Codebase Memory MCP

- Repository: https://github.com/DeusData/codebase-memory-mcp
- Reviewed revision: `7d6cdb23ef5ca2fd51f5d5b7509b33e112ef15f3`
- License: MIT
- License blob: `0b95352746a97a8cf2d1f3ba568bc7bb5e514d1f`
- Reviewed README blob: `bb4919ed58bd61ee78d051d5fe5b16c802855afd`
- Decision: reference and optionally evaluate as a local binary/MCP structural engine; do not run a remote installer or binary without artifact review.

### Retain

- Persistent structural graph and explicit local store.
- Architecture, route, symbol, call, data-flow, change-impact, and cross-repository queries.
- Separation of headless server and optional visualization UI.
- Automatic update notifications without automatic replacement.
- Local processing as a desirable deployment property.

### Correct or constrain

- The tool explicitly reads source and writes agent configuration.
- Recommended one-line shell and PowerShell installers are executable supply-chain actions. Download, inspect, checksum/signature-verify, pin, and run through an approved installation route instead.
- Automatic indexing and background watchers create persistent resource use and may scan a project merely because an MCP session connects.
- The store under the user cache can persist source-derived symbols, routes, names, and cross-repository relationships beyond the active session.
- The optional localhost UI expands the listening surface and must bind, authenticate, and expose data according to the environment policy.
- ADR management writes durable architectural records and must not bypass the repository's canonical decision process.
- Bundled embeddings and semantic edges are derived signals, not canonical architecture.

## Understand Anything

- Current repository: https://github.com/Egonex-AI/Understand-Anything
- Original bookmark owner: `Lum1104`; repository now resolves to the Egonex organization and credits the original author.
- Reviewed revision: `6ae71878beb50226a1e4b7e2f52ac6468c86f74b`
- License: MIT
- License blob: `5df102e8a2e29cdfb881ae7ec5040f2766564680`
- Reviewed README blob: `04efe8311e3cf56d088ac4c4f3da8378784205d2`
- Reviewed `understand` skill blob: `f13012e0e5a7648670b40d9f58343a72c0e96f79`
- Decision: reference for graph-assisted onboarding and domain explanation; do not vendor the multi-agent skill wholesale.

### Retain

- Structural graph plus guided onboarding and impact-oriented views.
- Explicit disclosure that full initialization can consume substantial model tokens.
- Incremental refresh and a recorded source commit.
- Separate structural, business-domain, onboarding, diff, explanation, dashboard, and knowledge-vault modes.
- Scoped exclusions and a project-owned data directory.

### Correct or constrain

- The main workflow installs dependencies when its build output is absent, creates `.ua/` or legacy data directories, writes configuration, creates intermediate and temporary files, and can enable post-commit updates.
- Worktree detection may redirect output from the active worktree to the main repository root. That behavior must be explicit and approved; it can cross the requested write boundary.
- The installer clones into the user's home directory and creates agent-platform symlinks; remote shell and PowerShell one-liners must not be executed without review.
- LLM-generated summaries, domains, flows, lessons, tags, and inferred relationships are not equivalent to parser facts.
- Full-repository multi-agent analysis can expose private source to the configured model provider and consume material tokens or cost.
- Automatic hooks, dashboard launch, language/config persistence, cleanup, and deletion are separate mutations.
- Generated graph and onboarding artifacts must not overwrite canonical architecture, project memory, ontology, or decisions.

## Runtime selection

Do not install all three by default.

Choose based on the task and environment:

- **Code Review Graph** — focused local structural map, affected-source selection, and PR/diff review.
- **Codebase Memory MCP** — broad static-binary structural and semantic MCP service with persistent local graph and optional cross-repository/UI features.
- **Understand Anything** — multi-agent explanatory graph, dashboard, tours, domain extraction, and onboarding artifacts with higher model and artifact footprint.
- **No engine** — small repositories, one-off changes, unsupported languages, strict no-install environments, or tasks where ordinary source search and tests are sufficient.

Selection must consider source sensitivity, parser coverage, installation provenance, config mutation, persistent storage, hooks/watchers, model provider, token/cost budget, UI exposure, and uninstall/rollback.

## Existing package decisions

### `Graphify Onboarding`

Lifecycle: reviewed, conditional.

Retain its strongest rule: generated graph output is a derived discovery aid, not canonical truth. Ignore rules, source hierarchy, private-data review, and source verification remain required. Generalize its routing so the procedure does not imply one mandatory Graphify runtime.

### `monorepo-navigator`

Lifecycle: reviewed, conditional, high risk.

Retain for monorepo tooling, selective builds, package impact, migration, and coordinated publishing. It includes executable analysis, CI, remote cache, history rewriting, and publication guidance; none is authorized by an ordinary navigation request. Its absolute tool recommendations and bundled-script assumptions are advisory, not universal truth.

### `codebase-design`

Lifecycle: reviewed, conditional.

Retain as module/interface design doctrine. It is conceptually distinct from source indexing and impact analysis. The imported body prescribes exact vocabulary and universal design rules, so use it only when that deep-module model is explicitly desired rather than as the default architecture language.

## First-party procedures

Create:

1. `skills/codebase-structural-map.md`
2. `skills/change-impact-review.md`

They must:

- use an existing approved engine when available, but remain usable with ordinary source search;
- record tool, version/revision, repository commit, scope, excludes, output location, and freshness;
- treat graph nodes, edges, communities, semantic similarity, summaries, and risk scores as derived evidence;
- verify consequential claims in source, configuration, history, and tests;
- prohibit silent installation, config mutation, hooks, watchers, CI comments, merge gates, dashboards, cross-repository indexing, ADR writes, or publication;
- protect secrets, generated assets, vendored code, private memory, and irrelevant large directories through reviewed exclusions;
- keep generated artifacts separate from canonical repository knowledge.

## Promotion gates

1. unfamiliar small repository where no graph engine is installed;
2. existing Code Review Graph index with a stale commit;
3. Codebase Memory project with auto-watch disabled;
4. Understand Anything graph containing LLM-generated domain claims;
5. a diff whose graph misses a dynamic or configuration relationship;
6. a monorepo change with package and runtime impact;
7. a private repository with secrets and memory directories requiring exclusion;
8. a false-positive graph edge that must not become a review finding;
9. a PR-comment request where write permission remains separately gated;
10. a cost/token comparison showing when not to build a graph.

## Boundary

No upstream executable, installer, skill body, graph database, benchmark output, source index, dashboard, model call, MCP configuration, hook, watcher, CI comment, ADR, or repository artifact was copied or executed. Existing imported package bodies remain unchanged. Catalog decisions alter routing and installation guidance only.