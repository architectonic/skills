---
type: Normalization Plan
title: MCP External Tool Security Review Normalization
summary: Normalizer pass converting the local MCP risk audit into a compact OKF-compatible skill without copying MCP documentation.
tags: [skills, aggregator, normalizer, mcp, external-tools, security]
okf_version: "0.2"
status: active
risk_level: high
created_at: 2026-07-02T12:01:27-03:00
---

# MCP External Tool Security Review Normalization

## Role Decision

Selected role: Normalizer.

Reason: the scheduled Publisher slot had no publication queue, while `normalize-mcp-external-tool-security-checklist-20260702` was open, high priority, and explicitly approved by the Risk Auditor as the safe next step. Queue pressure and safety-gated normalization outweighed an empty publication pass.

## Queue Item Consumed

`normalize-mcp-external-tool-security-checklist-20260702`

Target: `operations/daily/2026-07-02/risk-audit.md`

## Normalization Decision

Created a local OKF-compatible skill:

```text
skills/mcp-external-tool-security-review.md
```

The skill is distilled from the local Risk Auditor checklist and references MCP as a reviewed source profile. It does not copy MCP documentation, does not endorse third-party MCP servers, and remains marked high risk / requires review.

## Verification

- Trigger exists.
- Inputs exist.
- Procedure exists.
- Verification exists.
- Failure modes exist.
- Source profile link is preserved.
- Risk level remains high.
- `requires_review: true` is set.
- No third-party documentation was copied.

## Queue Follow-Up

Created catalog queue item:

```text
catalog-mcp-security-skill-20260702
```

Cataloger should rebuild or reconcile catalog surfaces after this new skill is included, preferably together with the existing catalog drift reconciliation item.
