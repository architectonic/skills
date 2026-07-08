---
name: performing-kerberoasting-attack
description: Review-gated defensive assessment wrapper for Kerberoasting risk. Use only for authorized Active Directory security planning, detection mapping, evidence boundaries, and remediation.
tags: [agent-skill, okf, kerberoasting, active-directory, credential-access, kerberos, identity-security, security, review-gated]
license: Apache-2.0
type: Playbook
title: Performing Kerberoasting Attack
domain: security-offensive
risk_level: high
requires_review: true
source_family: anthropic-cybersecurity-skills
source_license: Apache-2.0
source_status: blocked-pending-redaction
---

# Performing Kerberoasting Attack

This package-facing entry is blocked pending redaction and safety review.

Kerberoasting workflows can request service tickets, extract crackable material, and enable offline password recovery against Active Directory service accounts. This repository must not expose a default executable procedure for ticket extraction, hash formatting, cracking, credential validation, or follow-on privilege escalation. Treat the upstream technique as reference-only unless an approved defensive assessment workspace has written scope, evidence-handling rules, and human review controls.

## Allowed use in this repository

- Record authorization requirements, domain-scope boundaries, account classes, and rules of engagement.
- Plan defensive assessment scope for service-account hygiene, Kerberos telemetry, password policy, and privilege review.
- Map Kerberoasting exposure to detections, controls, and remediation.
- Preserve provenance, risk classification, review status, and package-safety rationale.
- Help reviewers decide whether a future defensive-only workflow is safe to publish.

## Disallowed use in this repository

- Do not provide copyable live-operation commands, ticket-request procedures, hash-extraction steps, cracking guidance, or credential-validation workflows.
- Do not include instructions for requesting tickets for abuse, extracting crackable material, tuning cracking jobs, validating recovered credentials, or using recovered access.
- Do not request, paste, store, transform, summarize, or enrich tickets, hashes, passwords, account secrets, or recovered credential artifacts.
- Do not perform live domain, directory, identity-provider, host, network, account, or credential actions from this skill.
- Do not package this entry as publication-ready until a reviewer replaces it with a defensive-only workflow.

## Safe reviewer checklist

1. Confirm written authorization, Active Directory scope, account classes, and evidence-retention rules.
2. Confirm the task is defensive validation, detection engineering, identity-control review, incident-response scoping, or remediation planning.
3. Keep procedural ticket extraction, cracking, credential-validation, and privilege-escalation detail out of the package-facing skill.
4. Move any operational references to a controlled, non-default review artifact if they are retained at all.
5. Verify that the final skill teaches defensive planning, detection, evidence handling, and remediation rather than execution.
6. Require explicit human approval before any installer, catalog, or publisher surface presents this as usable automation.

## Defensive review prompts

- Which service accounts, SPN-bearing accounts, and privilege tiers are in scope for defensive review?
- Which logs, identity events, Kerberos service-ticket patterns, encryption-type signals, and honeypot-account alerts should be inspected?
- Which controls reduce exposure: strong service-account passwords, gMSA adoption, least privilege, RC4 reduction, account rotation, and SPN hygiene?
- What remediation evidence can be collected without exposing or reproducing tickets, hashes, passwords, or recovered credentials?

## Status

Risk decision: high risk, requires review, blocked pending redaction.
