---
type: Critic Report
title: Offensive Identity Cloud Risk Triage
status: complete
date: 2026-07-07
role: Critic
scheduled_role: Source Reviewer
selected_role: Critic
inspected_ref: main
inspected_sha: 81a4e02f457cd86eec8518e0d4dcd93bbd33d14b
model_requirement_status: model_setting_unverified
---

# Offensive Identity Cloud Risk Triage

## Decision

Selected **Critic** instead of the 08:00 cadence **Source Reviewer** because the only open concrete queue item was `metadata-backfill-uncategorized-and-unspecified-risk-20260707`, and the project quality gate treats uncategorized/unspecified package-facing skills as standing maintenance material.

## Directly inspected files

- `dist/skills/assessing-vector-and-embedding-weaknesses/SKILL.md`
- `dist/skills/attacking-entra-id-with-roadtools/SKILL.md`
- `dist/skills/attacking-oauth-with-device-code-phishing/SKILL.md`
- `dist/skills/auditing-entra-id-with-aadinternals/SKILL.md`
- `dist/skills/auditing-foundry-smart-contract-security/SKILL.md`

## Risk finding

Three inspected package-facing entries should not receive routine metadata backfill before explicit risk review:

- `attacking-entra-id-with-roadtools`
- `attacking-oauth-with-device-code-phishing`
- `auditing-entra-id-with-aadinternals`

Reason: these files contain live-offensive identity/cloud procedures involving tenant enumeration, token acquisition/exchange, phishing, and federation-backdoor or Golden SAML validation. They include authorization warnings, but their procedure surfaces are materially higher risk than ordinary defensive audit or package metadata cleanup. They should be review-gated and classified by Risk Auditor before any package/publication endorsement.

## Lower-risk follow-up candidates

Two inspected files appear suitable for a later bounded metadata backfill batch after this risk gate is handled:

- `assessing-vector-and-embedding-weaknesses`: likely `domain: security-defensive` or `cloud-security`, `risk_level: medium`, `requires_review: true` because it tests RAG/vector leakage and poisoning in authorized environments.
- `auditing-foundry-smart-contract-security`: likely `domain: security-defensive` or `software-engineering`, `risk_level: medium`, `requires_review: false` or `true` depending on package policy for financial smart-contract audit procedures.

## Queue action

Created a high-priority Risk Auditor queue item: `risk-review-offensive-identity-cloud-skills-20260707`.

## Boundary

No third-party content was copied. No repository was cloned. No commands from the inspected skills were executed. No skill body was rewritten in this pass.
