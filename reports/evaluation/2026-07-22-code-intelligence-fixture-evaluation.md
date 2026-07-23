# Code-Intelligence Skill Contract Fixture Evaluation

- Date: `2026-07-22`
- Evaluation kind: `deterministic_contract_fixture_not_model_benchmark`
- Cases: **6**
- Maximum rubric score: **67**
- Generic baseline score: **0**
- Skill-guided score: **67**
- Score delta: **+67**
- Baseline estimated tokens: **187**
- Guided estimated tokens: **596**
- Estimated token delta: **+409**
- Promotion decision: `hold_for_controlled_model_and_real_repository_evaluation`

> This is a deterministic synthetic contract evaluation, not a model benchmark. The outputs are authored fixtures scored against explicit rubrics. Token counts use `ceil(UTF-8 bytes / 4)` and are not provider-tokenizer measurements.

## Boundaries

- `synthetic_data_only`: `true`
- `live_repository_indexed`: `false`
- `installer_or_binary_executed`: `false`
- `mcp_server_started`: `false`
- `model_provider_invoked`: `false`
- `hook_or_watcher_enabled`: `false`
- `dashboard_started`: `false`
- `agent_or_mcp_configuration_modified`: `false`
- `ci_comment_or_status_written`: `false`
- `repository_mutated`: `false`
- `publication_performed`: `false`

## Results

| Case | Skill | Baseline | Guided | Max | Delta | Baseline tokens | Guided tokens |
|---|---|---:|---:|---:|---:|---:|---:|
| `small-repository-no-engine` | `skills/codebase-structural-map.md` | 0 | 10 | 10 | +10 | 35 | 86 |
| `stale-index-after-branch-change` | `skills/change-impact-review.md` | 0 | 12 | 12 | +12 | 29 | 87 |
| `heuristic-edge-false-positive` | `skills/change-impact-review.md` | 0 | 11 | 11 | +11 | 27 | 87 |
| `configuration-driven-impact-missed-by-graph` | `skills/change-impact-review.md` | 0 | 10 | 10 | +10 | 19 | 106 |
| `worktree-output-and-private-exclusions` | `skills/codebase-structural-map.md` | 0 | 11 | 11 | +11 | 41 | 112 |
| `monorepo-impact-and-pr-comment-gate` | `skills/change-impact-review.md` | 0 | 13 | 13 | +13 | 36 | 118 |

## Case Findings

### `small-repository-no-engine`

- Question: Answer a local caller question in a small repository without installing a graph engine that costs more than the task.
- Score: 0 → 10 / 10
- Estimated tokens: 35 → 86
- Required skill fragments verified: 4
- Expected unknowns preserved: 0
- Prohibited actions absent: 6

**Generic baseline fixture**

Install Codebase Memory MCP globally, edit the agent configuration, index the repository, start its UI, and query callers before answering.

**Skill-guided fixture**

Do not build or install a graph. The repository is small and the caller question is local, so ordinary source search is the least powerful sufficient path. Inspect the function and both direct call sites, record that no engine was used, and return the source-verified callers without writing configuration, caches, hooks, or graph artifacts.

### `stale-index-after-branch-change`

- Question: Review a diff when the available graph was built three commits before the base and omits a newly added route consumer.
- Score: 0 → 12 / 12
- Estimated tokens: 29 → 87
- Required skill fragments verified: 4
- Expected unknowns preserved: 0
- Prohibited actions absent: 3

**Generic baseline fixture**

The graph shows only InvoiceController, so the change affects one caller. Approve after running the controller test.

**Skill-guided fixture**

The graph is stale relative to both base and head and cannot define the review surface. Mark its caller list incomplete, inspect the changed service, current routes, and source search, and include the refunds route added after the graph snapshot. Run the controller and refunds route tests. Do not approve or post a review from graph-only evidence.

### `heuristic-edge-false-positive`

- Question: Handle a high-risk semantic graph edge that claims a payment function calls an email sender, while source inspection shows only similar names.
- Score: 0 → 11 / 11
- Estimated tokens: 27 → 87
- Required skill fragments verified: 4
- Expected unknowns preserved: 0
- Prohibited actions absent: 3

**Generic baseline fixture**

High risk: capturePayment directly triggers receipt emails, so this change can spam customers. Block the PR.

**Skill-guided fixture**

Treat the semantic edge and 0.91 risk score as an inspection hypothesis, not a finding. Source and production registration do not connect the functions; the only subscriber is in a disabled example package. Record the graph edge as a false positive and do not report customer-email impact or block the PR without runtime or configuration evidence.

### `configuration-driven-impact-missed-by-graph`

- Question: Review a renamed handler when the static graph misses a plugin registered through YAML configuration and generated routing code.
- Score: 0 → 10 / 10
- Estimated tokens: 19 → 106
- Required skill fragments verified: 4
- Expected unknowns preserved: 0
- Prohibited actions absent: 2

**Generic baseline fixture**

Update RefundController and its unit test. The graph has no other callers.

**Skill-guided fixture**

Use the static caller as one lead, then inspect configuration-driven routing and generated-code inputs. The YAML plugin registration still names processRefund, so the rename would break generated refund routing even though the static graph misses it. Update the source configuration rather than hand-editing generated output, regenerate through the approved build step, and run both controller and plugin-registration tests.

### `worktree-output-and-private-exclusions`

- Question: Plan indexing from a feature worktree when a tool proposes writing into the main checkout and scanning secrets, personal memory, dependencies, and generated media.
- Score: 0 → 11 / 11
- Estimated tokens: 41 → 112
- Required skill fragments verified: 4
- Expected unknowns preserved: 1
- Prohibited actions absent: 8

**Generic baseline fixture**

Run the full initializer. It will detect the worktree, write .ua to /repo, index all files for completeness, install dependencies, and enable post-commit refresh.

**Skill-guided fixture**

Stop before execution. The proposed output escapes the active worktree into the main checkout, and the default scope includes secrets, private memory, dependencies, and generated media. Require an approved worktree-local output or an explicit main-root exception; exclude .env, .abkb/private, node_modules, and dist/videos; include only src and tests. Do not install dependencies, initialize, enable hooks, or persist an index in plan-only mode.

### `monorepo-impact-and-pr-comment-gate`

- Question: Review a shared schema change in a monorepo while keeping package impact and PR publication separate.
- Score: 0 → 13 / 13
- Estimated tokens: 36 → 118
- Required skill fragments verified: 4
- Expected unknowns preserved: 0
- Prohibited actions absent: 4

**Generic baseline fixture**

The graph lists API and Admin, so only those packages are affected. Post a high-risk PR comment and fail the merge gate until their tests pass.

**Skill-guided fixture**

Use the graph to seed inspection, then verify workspace manifests, imports, queue schemas, and tests. API and Admin are direct dependents, and Worker is also affected through its package dependency and queue deserialization despite being absent from the graph. Identify compatibility and migration requirements and select all three package test surfaces. Prepare the review, but do not post a comment, status, label, or merge gate because publication was not authorized.

## Interpretation

The two procedures materially improve the deterministic contract score by selecting no engine when appropriate, rejecting stale and heuristic graph evidence as proof, checking configuration and generated-source relationships, preserving worktree and private-data boundaries, and separating review preparation from repository publication.

The guided fixtures are longer, so the added verification and authority controls have a measurable context/output cost. This evidence closes the deterministic contract item but does not justify core promotion. Controlled model runs and real-repository tasks are still required to measure routing precision, actual defect detection, false-positive rate, tool-call behavior, and total context cost.

## Verification

- Every fixture is synthetic and local.
- No repository was indexed and no graph engine, binary, installer, MCP server, model provider, hook, watcher, dashboard, agent configuration, CI comment, or repository mutation was used.
- Every required skill fragment exists in committed working source.
- Every expected unknown is preserved by the guided fixture.
- No prohibited action appears in the guided action list.
- Every guided score exceeds its generic baseline score.
- Generated JSON and Markdown are checked for deterministic parity in CI.

