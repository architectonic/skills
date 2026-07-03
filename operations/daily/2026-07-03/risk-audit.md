---
type: Risk Audit
title: Skills Risk Auditor Checkpoint
description: Daily Risk Auditor checkpoints for package safety and repository-context review gates.
tags: [skills, aggregator, risk-audit, package-health, source-review, repository-context]
okf_version: "0.2"
status: active
risk_level: medium
reviewed_at: 2026-07-03T19:12:32-03:00
---

# Skills Risk Auditor Checkpoint

## 16:13 Checkpoint

### Role Decision

Selected role: Risk Auditor.

Scheduled role: Risk Auditor.

Reason: catalog parity is restored, package surfaces are coherent, and `queues.risk` is empty. The only justified Risk Auditor action in this pass is to verify that no safety gate currently blocks resumed Source Reviewer/Radar work and to persist a checkpoint.

### Inspected Ref

- Repository: `architectonic/skills`
- Inspected ref: `main`
- Inspected SHA: `923dc9a8b2dcb2e4cebc8e5e37237a06b765c38c`

### Gate Check

- `queues.risk`: empty.
- `queues.review`: empty.
- `queues.normalization`: empty.
- `queues.catalog`: no open item; stale catalog blocker is closed as done.
- `dist/catalog.json` and `dist/catalog.md`: both report 1173 skills, 2 high-risk entries, 409 medium-risk entries, and 759 unspecified-risk entries.
- `package.json`: `architectonic-skills` version `0.1.3`.
- `dist/install-manifest.json`: points at `README.md`, `dist/catalog.json`, `dist/catalog.md`, and `dist/install-manifest.json`.

### High-Risk Surface Review

The two high-risk surfaces remain acceptable only under explicit review gates:

1. `skills/mcp-external-tool-security-review.md`
   - Status: local defensive skill.
   - Risk: high.
   - Requires review: true.
   - Decision: keep available as a defensive checklist; do not treat MCP server compliance as trust.

2. `sources/reviewed/agent-skill-security-research.md`
   - Status: reviewed reference-only risk-audited source profile.
   - Risk: high.
   - License: unresolved for redistribution.
   - Decision: keep reference-only; do not copy paper text, datasets, scanner prompts, payload examples, exploit examples, or repository code.

### Decision

No risk queue item was consumed because none was open.

No new skill, source profile, catalog surface, package metadata, or publication artifact was changed.

The safety gate does not currently block resumed Radar or Source Reviewer work. Broad normalization remains inappropriate until a reviewed source creates a concrete normalization queue item.

## 19:12 Repository Context Gate

### Role Decision

Selected role: Risk Auditor.

Scheduled role: Packager.

Override reason: `queues.risk` had open priority-1 item `risk-repository-context-skill-review-20260703`; review and safety gates outrank packaging endorsement.

### Inspected Ref

- Repository: `architectonic/skills`
- Inspected ref: `main`
- Inspected SHA: `cdf4e10243df5905483dd4db0866db3a73285486`

### Queue Item Consumed

- `risk-repository-context-skill-review-20260703`

### Source Reviewed

- `sources/reviewed/repository-context-agent-skill-security.md`

### Decision

The reviewed source should improve local ingestion doctrine, not become a packaged skill. The durable value is a compact repository-context review gate that Source Reviewer, Risk Auditor, Normalizer, Packager, and Publisher can apply before trusting third-party skill candidates.

Updated `doctrine/ingestion-policy.md` with a Repository Context Gate requiring repository owner, URL, inspected commit or release, freshness, license evidence, README/docs/code alignment, marketplace-reference validity, abandonment/transfer/private-state checks, scanner-warning interpretation, and blind-execution risk review.

No third-party code, paper text, datasets, figures, scanner prompts, or reproduction artifacts were copied.

### Gate Result

- `queues.risk`: the repository-context item may be closed as done.
- `queues.review`: two candidate reviews remain open.
- `queues.normalization`: still empty.
- `queues.catalog`: no open package/catalog drift item.
- `skills/`: unchanged.
- `dist/`: unchanged.
- `package.json`: unchanged, `architectonic-skills` version `0.1.3`.

### Next Action

Source Reviewer should consume `review-skill-usage-20260703` next. Keep `skill-usage-realistic-settings` and `visualskill-multimodal-skills` reference-only until repository context, license, provenance, and safety implications are verified.
