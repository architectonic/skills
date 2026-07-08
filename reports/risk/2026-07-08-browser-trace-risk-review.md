# Browser Trace Risk Review — 2026-07-08

## Ticket

- Board ticket: `skills-risk-review-browser-trace-001`
- Role: Risk Auditor
- Input skill: `dist/skills/browser-trace/SKILL.md`
- Trigger: metadata backfill found browser/CDP session attachment, screenshots, DOM dumps, Browserbase API key mention, local debugger command snippets, and raw network/console/runtime trace capture.

## Decision

`conditional_allow_review_gated_read_only_defensive_debugging`

Browser Trace can remain package-facing only as high-risk, review-gated, read-only defensive debugging guidance for owned or explicitly authorized browser sessions.

The package-facing skill must not include executable browser-launch, debugger-port, remote-provider, API-key, capture-script, raw trace-query, or browser-attachment snippets. Those details belong only in private project runbooks with explicit authorization, credential handling, data retention, and redaction controls.

## Risk classification

| Surface | Classification | Package-facing decision |
|---|---|---|
| Browser/CDP session attachment | High | Allowed only as conceptual read-only defensive debugging scope; no attach commands or debugger-port instructions. |
| Screenshots and DOM dumps | High | Allowed only with data classification, minimization, redaction, and retention guidance. |
| Browserbase/API-key handling | High | Removed from package-facing instructions; credentials must remain outside skill text and model context. |
| Raw network/console/runtime traces | High | Allowed only as reviewed artifacts; raw bodies, tokens, cookies, headers, and identifiers require redaction. |
| Filesystem trace layout and query commands | Medium/high | Removed as reusable operational detail; summaries and review checklist retained. |
| Browser automation mutation | High | Explicitly disallowed. Skill is read-only debugging guidance only. |

## Changes made

Updated `dist/skills/browser-trace/SKILL.md` to:

- add `domain: software-engineering`;
- add `risk_level: high`;
- add `requires_review: true`;
- add `review_gate: authorized-read-only-browser-debugging-only`;
- add `source_status: distilled-reviewed`;
- remove local Chrome debugger launch commands;
- remove tracer/capture/query command snippets;
- remove remote-provider/API-key operational handling detail;
- preserve defensive debugging value through authorization, minimization, redaction, review checklist, and safe report format.

## Acceptance tests

| Test | Result | Evidence |
|---|---|---|
| Classifies browser/CDP/session/API-key/DOM/screenshot/filesystem trace surfaces | Pass | This report classifies all listed surfaces, and the skill now has `risk_level: high` and `requires_review: true`. |
| Defines whether Browser Trace can remain package-facing as a read-only defensive debugging skill | Pass | Decision is `conditional_allow_review_gated_read_only_defensive_debugging`. |
| Redacts or gates command snippets and API-key/browser-session handling if needed | Pass | Package-facing launch/capture/query commands and API-key/provider setup details were removed; review gate and credential-handling boundaries were added. |
| Keeps catalog/package/publication endorsement blocked until review and catalog parity are complete | Pass | This review closes the high-risk blocker but opens catalog parity as the next gate. No package, npm, registry, or publication action was attempted. |

## Boundaries preserved

- No online discovery was performed.
- No repository was cloned.
- No browser session was opened or attached.
- No trace tooling was executed.
- No third-party content was copied.
- No generated catalog surface was hand-edited.
- No package, npm, registry, or publication action was attempted.

## Next gate

`skills-catalog-refresh-after-metadata-backfill-001` should be unblocked and consumed next to verify catalog/install-manifest parity after package-facing metadata changes to Autonomy Loop, Autoresearch Loop, and Browser Trace.
