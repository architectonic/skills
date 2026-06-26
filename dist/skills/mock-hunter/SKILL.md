---
name: mock-hunter
description: Audit a live web page to identify mock data, hardcoded values, LLM-generated metrics, and broken endpoints. Uses browser automation to trace visible values through network and DOM to their source.
type: Metric
---

# MockHunter — Live Page Reality Check

## Overview

MockHunter audits a live web page and tells you, for every visible value, whether it is real, mocked, LLM-generated, hardcoded, broken, or unknown. Built for vibe-coded apps (Lovable, Bolt, v0, Replit, AI Studio, Cursor Composer) where the UI may look complete but the data layer often is not.

## When to Use This Skill

- Auditing an AI-generated UI to find out which values are actually wired up
- Reviewing a contractor or teammate's deliverable before sign-off
- Before showing a vibe-coded MVP to a customer or investor
- A dashboard "looks too clean" — every metric uniformly round, all timestamps clustered, no variance

## How It Works

### Phase 1: Setup & Smart Questions

1. Ask for the target URL
2. Auto-detect the stack from the URL (`*.lovable.app`, `*.bolt.new`, `*.v0.app`, `*.replit.app`, `aistudio.google.com`, otherwise Custom)
3. Ask 3-5 targeted questions: auth mode, DB access, suspicions, page goal
4. Confirm the audit plan, ownership/permission, target environment, and allowed action classes

### Phase 2: Navigate & Catalog

1. Navigate to the target URL
2. Handle auth per chosen mode
3. Wait for network idle (max 10s)
4. Take full-page screenshot, capture accessibility snapshot
5. Inventory every: heading, button, link, input, card, badge, stat, table cell, empty state, image
6. Capture initial console errors and network requests

### Phase 3: Test Interactivity

1. For every tab: click (after user approval), snapshot, scroll to bottom, re-catalog
2. For every button: click only user-approved, non-destructive controls
3. For every form: identify required fields; submit throwaway data only with explicit user approval
4. Record per-element behavior

### Phase 4: Trace Provenance

For every visible value, run this decision tree:

```
Did any network request return this value?
├── YES — found in a response:
│   ├── Status 4xx/5xx → BROKEN
│   ├── Endpoint matches /ai|openai|generate|llm|chat → LLM
│   ├── Response shape matches mock library (faker, MSW, mockoon) → MOCK
│   ├── Uniformity flags trigger → MOCK or LLM (review)
│   └── No DB → UNKNOWN (best-guess)
└── NO — value not in any network response:
    ├── String literal in DOM source → HARDCODED
    └── Computed from Math.random / Date.now / faker → MOCK
```

### Phase 5: Report

Produce a markdown report with verdicts per visible value: `REAL`, `MOCK`, `LLM`, `HARDCODED`, `BROKEN`, or `UNKNOWN`.

## Output Format

```markdown
# MockHunter Report: [URL]

## Summary
- Total values audited: X
- REAL: X | MOCK: X | LLM: X | HARDCODED: X | BROKEN: X | UNKNOWN: X

## Findings

### [Section Name]
| Value | Location | Verdict | Evidence |
|-------|----------|---------|----------|
| "42 users" | Hero section | HARDCODED | String literal in DOM |
| "98%" | Stats card | MOCK | Matches faker pattern |
| Table data | Dashboard | REAL | Returned from /api/data |

## Recommendations
- [Priority] Description of what to fix
```

## Safety Rules

- Default to observation-only until the user confirms ownership
- Identify a safe test account or environment before any interaction
- Get explicit approval before any click, submit, or authenticated action that can mutate state
- Skip destructive or ambiguous controls rather than relying on label regex alone

## Limitations

- Requires browser automation (Playwright or equivalent)
- Cannot trace values from WebSocket connections without additional tooling
- DB verification requires read-only DB access
- Some values may be classified as UNKNOWN without DB access or source code
