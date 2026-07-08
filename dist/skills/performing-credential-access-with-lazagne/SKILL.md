---
name: performing-credential-access-with-lazagne
description: Review-gated defensive assessment wrapper for LaZagne credential-access risk. Use only for authorized security planning, evidence boundaries, detection mapping, and remediation.
tags: [agent-skill, okf, lazagne, credential-access, password-stores, endpoint-security, incident-response, security, review-gated]
license: Apache-2.0
type: Playbook
title: Performing Credential Access with LaZagne
domain: security-offensive
risk_level: high
requires_review: true
source_family: anthropic-cybersecurity-skills
source_license: Apache-2.0
source_status: blocked-pending-redaction
---

# Performing Credential Access with LaZagne

This package-facing entry is blocked pending redaction and safety review.

LaZagne-style credential-access workflows can recover saved passwords and secrets from browsers, application stores, operating-system credential stores, local files, Wi-Fi profiles, databases, mail clients, and related endpoint artifacts. This repository must not expose a default executable procedure for harvesting, validating, reusing, or prioritizing credentials. Treat the upstream technique as reference-only unless an approved defensive assessment workspace has written scope, evidence-handling rules, and human review controls.

## Allowed use in this repository

- Record authorization requirements, scope boundaries, and rules of engagement.
- Plan defensive assessment scope and evidence-retention boundaries.
- Map credential-store exposure to detections, hardening controls, and remediation.
- Preserve provenance, risk classification, review status, and package-safety rationale.
- Help reviewers decide whether a future defensive-only workflow is safe to publish.

## Disallowed use in this repository

- Do not provide copyable live-operation commands or tool execution steps.
- Do not include instructions for extracting, dumping, parsing, validating, spraying, cracking, reusing, or prioritizing recovered credentials.
- Do not request, paste, store, transform, summarize, or enrich recovered secrets, cookies, hashes, tokens, keys, or credential artifacts.
- Do not perform live host, tenant, domain, network, account, or credential actions from this skill.
- Do not package this entry as publication-ready until a reviewer replaces it with a defensive-only workflow.

## Safe reviewer checklist

1. Confirm written authorization, scope, asset boundaries, and evidence-retention rules.
2. Confirm the task is defensive validation, detection engineering, incident-response scoping, or remediation planning.
3. Keep procedural credential-access detail out of the package-facing skill.
4. Move any operational references to a controlled, non-default review artifact if they are retained at all.
5. Verify that the final skill teaches defensive planning, detection, evidence handling, and remediation rather than execution.
6. Require explicit human approval before any installer, catalog, or publisher surface presents this as usable automation.

## Defensive review prompts

- Which endpoint credential stores are in scope for defensive monitoring and hardening?
- Which EDR, file-access, process, module-load, browser-store, credential-vault, or identity-control signals should be inspected?
- Which controls reduce exposure from saved credentials, browser secrets, cached tokens, local admin reach, stale sessions, and weak endpoint hygiene?
- What remediation evidence can be collected without exposing or reproducing secrets?

## Status

Risk decision: high risk, requires review, blocked pending redaction.
