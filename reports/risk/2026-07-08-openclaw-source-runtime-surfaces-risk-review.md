# OpenClaw Source Runtime Surfaces Risk Review — 2026-07-08

## Board ticket

- Ticket: `skills-risk-review-openclaw-source-runtime-surfaces-001`
- Role: `Risk Auditor`
- Inspected ref: `main`
- Inspected SHA before first content write: `5c9593ee6fc2e2c9542f610fbf74605fd2eb460c`
- Mode: source-profile risk review only

## Inputs reviewed

- `operations/heartbeat.md`
- `operations/board.json`
- `operations/gates.md`
- `operations/value-ledger.json`
- `operations/daily/2026-07-08/status.json`
- `operations/daily/2026-07-08/queues.json`
- `operations/daily/2026-07-08/report.md`
- `operations/log.md`
- `dist/catalog.json`
- `dist/catalog.md`
- `dist/install-manifest.json`
- `reports/review/2026-07-08-manual-source-review.md`
- `sources/profiles/2026-07-08/openclaw-openclaw.json`

`operations/action-runs/discover-skill-sources/latest.json` was checked and remains absent on the default branch.

## Boundaries

- No OpenClaw repository clone occurred.
- No OpenClaw code, commands, setup steps, configuration snippets, browser workflows, cron workflows, channel setup flows, account setup flows, gateway setup flows, daemon setup flows, or implementation content was copied.
- No candidate code was executed.
- No skill normalization, catalog edit, package action, npm publication, or registry publication occurred.
- Review used only the existing internal source profile and prior source-review report.

## Risk classification

| Surface | Risk | Decision |
|---|---:|---|
| Real messaging/account/channel integrations | High | Block operational channel/account setup details from package-facing Skills material. |
| Gateway exposure and remote access surfaces | High | Block gateway setup and remote-access operational detail. Abstract only as a security-boundary review pattern. |
| Browser/canvas/nodes/cron tools | High | Block executable browser automation, cron execution, and node/tool orchestration detail. |
| Host tool access in main session | High | Block host-tool enablement and command snippets. Abstract only as least-privilege/sandbox review guidance. |
| DM pairing, allowlist, and sandbox policy configuration | High | Allow only non-operational policy checklist language; no concrete account/channel mutation flow. |
| Daemon/onboarding install flow | High | Block install/onboarding flow detail from normalized package content. |

## Allowed abstraction boundary

Future OpenClaw-derived package-facing material may only cover original, source-attributed, non-operational review patterns:

- how to identify account/channel/browser/cron/gateway/host-tool surfaces in an agent runtime;
- how to separate source profiles from normalized installable skills;
- how to write a risk gate before normalizing runtime material;
- how to require least privilege, sandbox defaults, explicit user confirmation, and review-before-execution for agent runtime surfaces;
- how to record watch/quarantine decisions when safe abstraction is not possible.

Future package-facing material must not include:

- command snippets;
- account setup or channel mutation steps;
- browser automation instructions;
- cron execution recipes;
- gateway setup or remote-access setup;
- daemon/onboarding installation detail;
- implementation code or copied examples;
- operational instructions that would enable use of OpenClaw itself.

## Decision

`conditional_allow_abstract_safety_patterns_only`.

OpenClaw may remain a reviewed high-risk source profile. It may support a future original skill only if that skill is framed as a generic high-risk agent-runtime surface review checklist and avoids operational setup, implementation, commands, account/browser/cron/gateway details, or copied source content.

## Queue changes

Closed:

- `risk-review-openclaw-source-runtime-surfaces-20260708`

Left open and now eligible as the next lower-priority board path:

- `normalize-vercel-ai-sdk-source-profile-20260708`
- `skills-normalize-vercel-ai-sdk-profile-001`

No OpenClaw normalization queue was opened. A future OpenClaw abstraction ticket should be created only after the Vercel AI SDK normalization/catalog path or if the board explicitly prioritizes generic high-risk agent-runtime safety guidance.

## Acceptance tests

| Test | Result | Evidence |
|---|---|---|
| Classifies account/browser/cron/gateway/host-tool risk surfaces | Pass | All listed OpenClaw runtime surfaces remain high-risk and require review-gated abstraction only. |
| Defines allowed abstraction boundaries for any future OpenClaw-derived skill | Pass | Allowed boundary is limited to generic, original, source-attributed review/checklist patterns. |
| Blocks command snippets, account setup, browser automation, cron execution, and operational channel mutation detail unless explicitly safe | Pass | The blocked boundary explicitly excludes commands, setup flows, browser/cron/gateway/account/channel operational detail, and implementation content. |
| Updates board and queues with either normalization, watch, or quarantine state | Pass | Risk queue is closed. OpenClaw remains source-profile/watch-only for now; Vercel AI SDK normalization remains the next eligible board ticket. |

## Value delta

The high-risk OpenClaw source-runtime blocker is now resolved without normalizing or copying OpenClaw material. The repository has a safe boundary for any future OpenClaw-derived work and can proceed to the lower-risk Vercel AI SDK normalization ticket.

## Next action

Normalizer should consume `skills-normalize-vercel-ai-sdk-profile-001` / `normalize-vercel-ai-sdk-source-profile-20260708` and create only original provider/tool/sandbox guidance from the reviewed Vercel AI SDK source profile. Any later OpenClaw-derived work must remain generic high-risk runtime-surface safety guidance and must not include operational OpenClaw details.
