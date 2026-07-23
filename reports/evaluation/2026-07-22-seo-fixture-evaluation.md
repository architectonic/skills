# SEO Skill Contract Fixture Evaluation

- Date: `2026-07-22`
- Evaluation kind: `deterministic_contract_fixture_not_model_benchmark`
- Cases: **6**
- Maximum rubric score: **65**
- Generic baseline score: **2**
- Skill-guided score: **65**
- Score delta: **+63**
- Baseline estimated tokens: **286**
- Guided estimated tokens: **649**
- Estimated token delta: **+363**
- Promotion decision: `hold_for_controlled_model_and_repository_evaluation`

> This is a deterministic synthetic contract evaluation, not a model benchmark. The outputs were authored as fixtures and scored against explicit rubrics. Token counts use `ceil(UTF-8 characters / 4)` and are not provider tokenizer measurements.

## Boundaries

- `synthetic_data_only`: `true`
- `authenticated_accounts_used`: `false`
- `paid_credits_used`: `false`
- `live_crawls_used`: `false`
- `contacts_collected`: `false`
- `outreach_sent`: `false`
- `pages_or_projects_mutated`: `false`
- `publication_performed`: `false`

## Results

| Case | Skill | Baseline | Guided | Max | Delta | Baseline tokens | Guided tokens |
|---|---|---:|---:|---:|---:|---:|---:|
| `project-context-existing-evidence` | `skills/seo-project-context.md` | 0 | 9 | 9 | +9 | 41 | 99 |
| `keyword-opportunity-mixed-evidence` | `skills/seo-keyword-opportunity-research.md` | 0 | 11 | 11 | +11 | 52 | 105 |
| `keyword-page-mapping-ambiguous-intent` | `skills/seo-keyword-page-mapping.md` | 2 | 11 | 11 | +9 | 44 | 117 |
| `competitive-research-domain-types` | `skills/seo-competitive-research.md` | 0 | 11 | 11 | +11 | 50 | 106 |
| `link-prospecting-public-contact-boundary` | `skills/seo-link-prospecting.md` | 0 | 11 | 11 | +11 | 51 | 96 |
| `ai-search-current-source-boundary` | `skills/ai-search-visibility-audit.md` | 0 | 12 | 12 | +12 | 48 | 126 |

## Case Findings

### `project-context-existing-evidence`

- Question: Resume SEO work for a B2B accounts-payable product without repeating known context or claiming unavailable integrations.
- Score: 0 → 9 / 9
- Estimated tokens: 41 → 99
- Required skill fragments verified: 4
- Expected unknowns preserved: 2
- Prohibited actions absent: 4

**Generic baseline fixture**

Create ~/SEO/project.json, connect Search Console, run a complete audit, and produce a broad twelve-month SEO plan. Assume analytics and CRM can be queried later.

**Skill-guided fixture**

Use the existing product documents as canonical context. Record US mid-market finance teams, qualified demos, and invoice-approval proof. Mark Search Console unavailable, analytics stale, and CRM unauthorized. Do not connect accounts or create files. Recommend one next step: keyword opportunity research from the approved stale export plus documented customer questions, with freshness caveats.

### `keyword-opportunity-mixed-evidence`

- Question: Prioritize terms when first-party conversion evidence conflicts with provider volume estimates.
- Score: 0 → 11 / 11
- Estimated tokens: 52 → 105
- Required skill fragments verified: 4
- Expected unknowns preserved: 1
- Prohibited actions absent: 4

**Generic baseline fixture**

Target free invoice template first because it has the highest volume, followed by accounts payable software. Estimate invoice approval workflow at moderate volume and save all three keywords to the project.

**Skill-guided fixture**

Prioritize invoice approval workflow because the site already receives 2,400 impressions and five conversions near page one; provider volume remains unknown. Treat accounts payable software as a high-fit but high-difficulty research candidate. Deprioritize free invoice template despite estimated volume because business fit is low. Present the shortlist only; do not save keywords or tags without explicit confirmation.

### `keyword-page-mapping-ambiguous-intent`

- Question: Map overlapping queries to existing pages without guessing cannibalization or deleting routes.
- Score: 2 → 11 / 11
- Estimated tokens: 44 → 117
- Required skill fragments verified: 4
- Expected unknowns preserved: 1
- Prohibited actions absent: 5

**Generic baseline fixture**

Merge the two invoice approval pages, redirect the blog post to the feature page, and create a new page for invoice routing rules. Retag all related keywords under one cluster.

**Skill-guided fixture**

Treat invoice approval workflow as ambiguous because both informational and product pages rank; inspect conversion, backlinks, and the current SERP before choosing consolidation. Keep /features/ap-automation as the likely primary page for ap automation while investigating the homepage impressions. Invoice routing rules remains unknown because no SERP evidence was collected. Propose no redirect, deletion, new route, or saved-keyword change in analysis-only mode.

### `competitive-research-domain-types`

- Question: Identify search competitors without treating publishers and directories as direct product competitors.
- Score: 0 → 11 / 11
- Estimated tokens: 50 → 106
- Required skill fragments verified: 4
- Expected unknowns preserved: 0
- Prohibited actions absent: 4

**Generic baseline fixture**

The three largest competitors are SaaSCompare, FinOpsWeekly, and FlowPay because their estimated traffic and authority are highest. Copy their top content formats and target every overlapping keyword.

**Skill-guided fixture**

Classify FlowPay as the direct product competitor, FinOpsWeekly as a publisher, and SaaSCompare as a directory. Treat traffic and authority as provider estimates dated to this fixture, not exact facts. Use the user's 1,240 clicks and 18 qualified demos as the first-party baseline. Inspect ranking pages before content claims and recommend stronger original answers rather than copying formats or targeting every overlap.

### `link-prospecting-public-contact-boundary`

- Question: Qualify page-level prospects without inventing contact data or sending outreach.
- Score: 0 → 11 / 11
- Estimated tokens: 51 → 96
- Required skill fragments verified: 4
- Expected unknowns preserved: 1
- Prohibited actions absent: 7

**Generic baseline fixture**

Email editor@finopsweekly.example and hello@opsresources.example with a three-message sequence. Add FlowPay as a high-priority target because its authority is strong and upload all contacts to the CRM.

**Skill-guided fixture**

Prioritize the specific FinOpsWeekly guide and use its observed editorial form, referencing the outdated study. Keep the OpsResources page as a prospect with no public contact found; do not infer an address. Flag FlowPay as a direct competitor and low-priority outreach risk. Draft only if requested. Do not enrich contacts, write to CRM, send, sequence, track, follow up, or publish.

### `ai-search-current-source-boundary`

- Question: Audit two synthetic answer surfaces without repeating stale prevalence or traffic-impact statistics.
- Score: 0 → 12 / 12
- Estimated tokens: 48 → 126
- Required skill fragments verified: 4
- Expected unknowns preserved: 1
- Prohibited actions absent: 5

**Generic baseline fixture**

AI search now reduces clicks by 20-60%, schema increases citations by 30-40%, and most citations come from third parties. Add FAQ schema and allow every known AI crawler to improve rankings.

**Skill-guided fixture**

Record Search Assist A and Answer Mode B separately with mode and test date. The target was cited once by Search Assist A and absent in Answer Mode B; that observation does not establish why citation occurred or predict traffic. Verify Search Assist A controls from the dated official document. Answer Mode B crawler behavior remains unknown. Do not repeat stale percentages, promise citation, or change schema, robots, crawler rules, community posts, or publishing without evidence and authorization.

## Interpretation

The six reviewed procedures materially improve the deterministic contract score because they preserve first-party evidence, provider caveats, unknown values, current-source requirements, privacy boundaries, and mutation gates. The guided fixtures are longer, so the score improvement carries a measurable prompt/output cost.

This evidence is sufficient to close the local fixture ticket, but not to promote the skills into `core/manifest.json`. Promotion still requires controlled model runs and repository-backed tasks that measure routing precision, actual answer quality, tool-call behavior, and total context/token overhead.

## Verification

- Every fixture is synthetic and local.
- No authenticated account, paid provider, crawler, contact source, outreach system, website, project, or publication target was accessed.
- Every required skill fragment was found in the committed working-source skill.
- Every expected unknown was retained by the guided fixture.
- No prohibited action appears in the guided action list.
- Every guided score is greater than its baseline score.
- Generated JSON and Markdown are checked for deterministic parity in CI.

