---
name: performing-initial-access-with-evilginx3
description: Review-gated defensive assessment wrapper for EvilGinx3 adversary-in-the-middle phishing and session-capture risk. Use only for authorized security planning, detection mapping, and remediation.
tags: [agent-skill, okf, evilginx, phishing, adversary-in-the-middle, session-theft, mfa-bypass, identity-security, security, review-gated]
license: Apache-2.0
type: Playbook
title: Performing Initial Access with EvilGinx3
domain: security-offensive
risk_level: high
requires_review: true
source_family: anthropic-cybersecurity-skills
source_license: Apache-2.0
source_status: blocked-pending-redaction
---

# Performing Initial Access with EvilGinx3

This package-facing entry is blocked pending redaction and safety review.

Adversary-in-the-middle phishing workflows can capture credentials, session cookies, authentication material, and MFA-bypassing session state. This repository must not expose a default executable procedure for phishing infrastructure, lure generation, session capture, token replay, account takeover, or post-access activity. Treat the upstream technique as reference-only unless an approved defensive assessment workspace has written scope, legal authorization, notification rules, and human review controls.

## Allowed use in this repository

- Record authorization requirements, scope boundaries, notification rules, and rules of engagement.
- Plan defensive assessment scope for identity controls, phishing resilience, and session-security monitoring.
- Map AiTM and session-replay risk to detections, controls, and remediation.
- Preserve provenance, risk classification, review status, and package-safety rationale.
- Help reviewers decide whether a future defensive-only workflow is safe to publish.

## Disallowed use in this repository

- Do not provide copyable live-operation commands, configuration steps, lure setup, delivery guidance, or session-replay instructions.
- Do not include instructions for creating phishing infrastructure, generating lures, capturing credentials, capturing cookies, bypassing MFA, importing cookies, or hijacking sessions.
- Do not request, paste, store, transform, summarize, or enrich credentials, cookies, tokens, authentication material, or captured session data.
- Do not perform live domain, tenant, mailbox, cloud-account, browser, phishing, or network actions from this skill.
- Do not package this entry as publication-ready until a reviewer replaces it with a defensive-only workflow.

## Safe reviewer checklist

1. Confirm written authorization, scope, notification requirements, and evidence-retention rules.
2. Confirm the task is defensive validation, detection engineering, identity-control review, incident-response scoping, or remediation planning.
3. Keep procedural phishing, lure, token-capture, and session-replay detail out of the package-facing skill.
4. Move any operational references to a controlled, non-default review artifact if they are retained at all.
5. Verify that the final skill teaches defensive planning, detection, evidence handling, and remediation rather than execution.
6. Require explicit human approval before any installer, catalog, or publisher surface presents this as usable automation.

## Defensive review prompts

- Which identity providers, tenants, and session controls are in scope for defensive review?
- Which controls reduce AiTM impact: phishing-resistant MFA, device binding, conditional access, token protection, impossible-travel checks, and session revocation?
- Which logs, certificate-transparency signals, domain-monitoring events, proxy indicators, and authentication anomalies should be reviewed?
- What remediation evidence can be collected without exposing or reproducing credentials, cookies, tokens, or captured sessions?

## Status

Risk decision: high risk, requires review, blocked pending redaction.
