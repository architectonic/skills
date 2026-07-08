---
name: Browser Trace
description: Review-gated guidance for collecting and inspecting browser automation traces in authorized debugging contexts. Use only for read-only defensive investigation of owned or explicitly authorized browser sessions; do not use for account/session surveillance, credential capture, or unapproved browser attachment.
tags: [software-development, debugging, browser, cdp, tracing, automation, observability, security-review]
domain: software-engineering
risk_level: high
requires_review: true
review_gate: authorized-read-only-browser-debugging-only
source: mxyhi/ok-skills (MIT)
source_status: distilled-reviewed
distilled: 2026-06-22
type: Playbook
---

# Browser Trace

Browser Trace is a review-gated defensive debugging playbook for inspecting browser automation failures from traces that were collected from owned or explicitly authorized sessions.

The safe package-facing use case is narrow: a reviewer may use already-approved trace artifacts to understand navigation failures, JavaScript errors, network failures, DOM state, or timing issues in a controlled debugging environment. This skill must not be used to attach to another user's live browser, inspect private sessions, collect credentials, bypass account controls, or monitor activity without authorization.

## Review Gate

Before using this skill, confirm all of the following:

1. The browser session, test environment, account, and data are owned by the operator or explicitly authorized by the owner.
2. The trace capture plan is read-only and does not drive pages, submit forms, mutate accounts, bypass authentication, or change remote state.
3. The data classification is known before screenshots, DOM snapshots, console logs, network metadata, or runtime traces are collected.
4. Secrets, cookies, bearer tokens, session identifiers, personal data, and proprietary page contents are either absent, minimized, or redacted before sharing.
5. Any remote-browser provider credentials are handled outside the skill text and are never pasted into prompts, logs, reports, or shared artifacts.
6. Retention is bounded: trace artifacts are stored only as long as needed for the debugging task and are deleted or archived according to the project policy.

If any item is uncertain, stop and perform a security/privacy review before collecting or analyzing trace data.

## Allowed Uses

Use this skill for defensive debugging when the operator is authorized to inspect the browser session:

- diagnose failed browser automation runs;
- correlate page navigation, console errors, network failures, and DOM state;
- inspect screenshots or DOM snapshots that are known to be safe to store;
- summarize trace artifacts for a bug report or regression investigation;
- identify whether failures come from selectors, timing, navigation, server responses, client-side exceptions, or test-environment instability.

## Disallowed Uses

Do not use this skill for:

- attaching to a live browser session without explicit authorization;
- monitoring a human user's browsing activity;
- capturing credentials, cookies, session tokens, private messages, payment information, or personal data;
- using browser traces to bypass access controls or account protections;
- collecting screenshots or DOM dumps from third-party accounts without permission;
- publishing raw trace artifacts that may contain secrets, proprietary content, or personal data;
- running command snippets copied from package-facing documentation against production sessions without review.

## Safe Workflow

1. **Scope the trace.** Define the authorized target, owner, purpose, expected data sensitivity, and retention limit.
2. **Collect minimally.** Capture only the domains and time window needed for the debugging question. Avoid broad runtime or DOM collection when network or console metadata is enough.
3. **Separate raw and shareable artifacts.** Keep raw traces in a restricted workspace. Create a separate redacted summary for tickets, reports, or agent context.
4. **Inspect locally or in a controlled environment.** Do not upload raw traces to external tools unless the data owner has approved that transfer.
5. **Redact before reuse.** Remove secrets, cookies, authorization headers, user identifiers, sensitive DOM content, and private screenshots before using trace output as model context.
6. **Delete or archive deliberately.** Apply the retention plan after the debugging task is complete.

## Trace Review Checklist

When reviewing a trace, look for:

- page load and navigation sequence;
- failed requests, status codes, retries, and timing gaps;
- client-side exceptions and console errors;
- selector or DOM-state mismatch at the failure point;
- modal, dialog, redirect, or cross-origin transitions;
- test-environment instability such as blocked resources, throttling, or session expiry;
- evidence that raw artifacts contain secrets or private data that must be redacted.

## Redaction Requirements

Before trace data leaves the restricted debugging context, remove or mask:

- cookies, tokens, API keys, authorization headers, and session identifiers;
- email addresses, names, account IDs, payment data, and private messages;
- screenshots containing private or proprietary content;
- DOM sections containing user data, hidden tokens, or proprietary application state;
- raw network bodies unless they are necessary and approved for the review.

Prefer summaries over raw artifacts. A good report states the failure, the observed evidence, the affected page or request class, and the recommended fix without exposing sensitive trace content.

## Output Format

A safe Browser Trace report should include:

- authorization scope and data classification;
- trace time window and environment;
- failure summary;
- relevant navigation, network, console, and DOM observations;
- redactions applied;
- likely root cause;
- recommended next debugging or code action;
- retention/deletion status for raw artifacts.

## Package Boundary

This skill intentionally does not include browser-launch commands, debugger-port setup, remote-provider setup, API-key handling, capture scripts, or raw query commands. Those details are environment-specific and may expose browser sessions, credentials, private DOM data, or sensitive trace artifacts if reused without review.

Operational capture instructions belong in a private, project-authorized runbook with explicit owner approval, credential handling, data-retention rules, and redaction requirements.
