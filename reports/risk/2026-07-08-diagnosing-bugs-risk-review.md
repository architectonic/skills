# Diagnosing Bugs Risk Review — 2026-07-08

## Board ticket

- Ticket: `skills-risk-review-diagnosing-bugs-001`
- Role: Risk Auditor
- Input skill: `dist/skills/diagnosing-bugs/SKILL.md`
- Decision: `allow_with_review_gate`

## Reviewed source

Direct default-branch review found the original package-facing skill listed these feedback-loop options:

- failing tests;
- HTTP script against a running dev server;
- CLI fixture invocation;
- headless browser script with Playwright/Puppeteer, DOM, console, and network assertions;
- captured trace replay from real request, payload, or event log;
- throwaway harness;
- property/fuzz loop;
- bisection harness;
- differential loop;
- HITL bash script.

## Risk classification

| Surface | Risk | Decision |
|---|---:|---|
| Unit/integration/e2e failing tests | Low | Allowed. |
| HTTP-level reproduction | Medium | Allowed only against authorized dev/staging targets with no credential leakage. |
| CLI fixture loop | Low | Allowed when fixtures are synthetic or sanitized. |
| Throwaway harness | Medium | Allowed when bounded and non-mutating by default. |
| Property/fuzz loop | Medium | Review-gated for runtime limits, input bounds, and no external side effects. |
| Bisection harness | Medium | Review-gated when it boots services, mutates data, or depends on external systems. |
| Differential loop | Low/medium | Allowed when using sanitized fixtures; review-gated if real payloads are used. |
| Browser/headless automation | High | Review-gated; package-facing operational browser/session instructions removed. |
| DOM/console/network capture | High | Review-gated; capture outputs must be minimized and redacted. |
| Captured trace replay | High | Review-gated; real request/payload/event-log material must be sanitized before persistence or sharing. |
| Human-in-the-loop scripts | Medium/high | Review-gated for stop conditions, visibility, and no hidden mutation. |

## Changes made

`dist/skills/diagnosing-bugs/SKILL.md` was converted into a medium-risk, requires-review, repository-owner-authorized diagnostic playbook.

Added metadata:

- `domain: software-engineering`
- `risk_level: medium`
- `requires_review: true`
- `review_gate: repository-owner-authorized-diagnostics-only`
- `source_status: reviewed-metadata-only`
- review notes describing browser/headless, trace replay, fixture, fuzz, bisection, and HITL risk.

Package-facing content was rewritten to:

- preserve safe diagnostic value;
- classify browser/headless automation as high-risk;
- classify trace replay and capture artifacts as sensitive;
- require authorization, data minimization, redaction, retention limits, and cleanup;
- avoid executable browser/session/trace-capture snippets;
- avoid operational commands, account/session setup, API-key usage, and capture instructions.

## Acceptance tests

| Test | Result | Evidence |
|---|---|---|
| Browser/headless automation, trace replay, fixture, bisection, fuzz, and HITL surfaces are classified | Pass | Risk table and skill frontmatter/body classify each surface and require review where needed. |
| Safe diagnostic guidance is preserved | Pass | Feedback-loop hierarchy, cause isolation, bisection, differential comparison, fix/verify, and regression-test guidance remain. |
| Operational browser/session/trace-capture snippets are review-gated or removed if package-facing unsafe | Pass | No Playwright/Puppeteer commands, browser-session setup, trace-capture steps, real-payload replay commands, or credential/API-key usage remain. |
| Catalog refresh remains blocked until review completes | Pass | This report closes the risk review and unblocks catalog parity as the next board ticket; no catalog publication was attempted in this pass. |

## Boundaries preserved

- No browser session opened.
- No trace tooling executed.
- No repository cloned.
- No online discovery used.
- No third-party content copied.
- No generated catalog surface hand-edited.
- No package, npm, registry, or publication action attempted.

## Outcome

The risk blocker is removed. `Diagnosing Bugs` can remain package-facing only as a review-gated diagnostic playbook. Catalog parity after metadata-backfill batch 002 is now the next required board ticket.
