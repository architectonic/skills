# Manual Discovery Source Review — 2026-07-08

## Board ticket

- Ticket: `skills-source-review-batch-001`
- Role: `Source Reviewer`
- Inspected ref: `main`
- Inspected SHA before first content write: `7cc1606cb14137314ab354d83769f62fe709875a`
- Mode: metadata/license/risk review only

## Boundaries

- No repository was cloned.
- No candidate code was executed.
- No third-party implementation content was copied.
- No skill was normalized.
- No catalog/package/publication action was attempted.
- Candidate repository reads were limited to public metadata, README/license excerpts, and repository metadata.

## Files and sources reviewed

### Internal Skills files

- `operations/heartbeat.md`
- `operations/board.json`
- `operations/gates.md`
- `operations/value-ledger.json`
- `operations/daily/2026-07-08/status.json`
- `operations/daily/2026-07-08/queues.json`
- `operations/daily/2026-07-08/report.md`
- `operations/log.md`
- `dist/catalog.json`
- `dist/install-manifest.json`
- `reports/discovery/2026-07-08-manual.md`
- `reports/discovery/2026-07-08-manual.json`
- `sources/candidates/2026-07-08-manual.json`

### Public candidate files

- `modelcontextprotocol/servers` `README.md`
- `modelcontextprotocol/servers` `LICENSE`
- `vercel/ai` `packages/ai/README.md`
- `vercel/ai` `LICENSE`
- `QuantaAlpha/GitTaskBench` `README.md`
- `QuantaAlpha/GitTaskBench` `LICENSE` fetch result: `404 Not Found`
- `openclaw/openclaw` `README.md`
- `openclaw/openclaw` `LICENSE`

## Candidate decisions

| Candidate | Decision | License status | Usefulness | Risk | Boundary |
|---|---|---|---:|---:|---|
| `modelcontextprotocol/servers` | `source_profile_created_review_gated` | usable with attribution/license tracking | high | medium | Do not copy server code or executable snippets; use only boundary/safety patterns in future original normalization. |
| `vercel/ai` | `source_profile_created_review_gated` | usable with attribution/license tracking | high | medium | Do not copy examples or implementation; future original guidance may cover provider abstraction and sandbox/tool safety. |
| `QuantaAlpha/GitTaskBench` | `watch_note_created_license_blocked` | blocked: `LICENSE` not found by direct fetch | medium | medium | Do not normalize, package, copy, or derive dataset/task content until license is verified. |
| `openclaw/openclaw` | `source_profile_created_high_risk_review_required` | usable with attribution/license tracking | high | high | No normalization until a dedicated high-risk source review approves safe abstraction boundaries. |

## Evidence summary

- `modelcontextprotocol/servers` README explicitly describes reference implementations and warns they are educational examples rather than production-ready solutions. Its LICENSE records an MIT-to-Apache-2.0 transition and CC-BY-4.0 documentation boundary.
- `vercel/ai` package README describes the AI SDK as a provider-agnostic TypeScript toolkit for AI-powered applications and agents, and its LICENSE is Apache-2.0.
- `QuantaAlpha/GitTaskBench` README describes a benchmark/tooling suite with task definitions, repository code bases, ground truth, test scripts, and reports. Direct `LICENSE` fetch returned `404 Not Found`, so redistribution remains blocked.
- `openclaw/openclaw` LICENSE is MIT, but README describes real messaging channels, local-first gateway, multi-agent routing, browser/canvas/nodes/cron tools, pairing defaults, and sandbox defaults. This creates a high-risk account/browser/cron/runtime surface.

## Artifacts created

- `reports/review/2026-07-08-manual-source-review.md`
- `reports/review/2026-07-08-manual-source-review.json`
- `sources/profiles/2026-07-08/modelcontextprotocol-servers.json`
- `sources/profiles/2026-07-08/vercel-ai.json`
- `sources/profiles/2026-07-08/openclaw-openclaw.json`
- `sources/watch/2026-07-08-gittaskbench-license-blocked.json`

## Queue changes

Created:

- `risk-review-openclaw-source-runtime-surfaces-20260708`
- `normalize-vercel-ai-sdk-source-profile-20260708`

Closed:

- `source-review-manual-discovery-20260708`

## Acceptance tests

| Test | Result | Evidence |
|---|---|---|
| Verifies license/redistribution boundary for each `review_next` candidate | Pass | Directly fetched license files for MCP servers, Vercel AI SDK, and OpenClaw; GitTaskBench stayed watch/license-blocked after `LICENSE` 404. |
| Classifies safety/runtime surface, including OpenClaw high-risk messaging/browser/cron/account surfaces | Pass | OpenClaw is high risk due to real messaging/account/channel integrations, browser/canvas/nodes/cron tools, gateway exposure, host tool access, and sandbox policy surfaces. |
| Creates source profiles, skip/watch notes, risk items, or normalization queues only when justified | Pass | Created three source profiles, one watch note, one high-risk review queue, and one bounded Vercel normalization queue. |
| Does not copy third-party content, clone repositories, execute code, publish, or package candidates | Pass | Review was metadata-only; no clone, execution, implementation copy, normalization, package, catalog, npm, or publication action occurred. |

## Value delta

The discovery fallback output is now actionable: three candidates have reviewed source profiles, one candidate is explicitly license-blocked on watch, OpenClaw is safety-gated before normalization, and Vercel AI SDK has a bounded original-normalization path.

## Next action

Risk Auditor should consume `skills-risk-review-openclaw-source-runtime-surfaces-001` before any OpenClaw-derived normalization or package-facing endorsement. If risk review is deferred, Normalizer may consume `skills-normalize-vercel-ai-sdk-profile-001` only for original guidance based on the reviewed source profile and without copying third-party examples or implementation content.
