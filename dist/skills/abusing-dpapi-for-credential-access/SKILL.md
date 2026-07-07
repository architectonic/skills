---
name: abusing-dpapi-for-credential-access
description: Review-gated defensive assessment wrapper for DPAPI credential-access risk. Use only for authorized Windows security planning, evidence boundaries, detection mapping, and remediation.
tags: [agent-skill, okf, dpapi, credential-access, windows, active-directory, security, review-gated]
license: Apache-2.0
type: Playbook
title: Abusing DPAPI for Credential Access
domain: security-offensive
risk_level: high
requires_review: true
source_family: anthropic-cybersecurity-skills
source_license: Apache-2.0
source_status: blocked-pending-redaction
---

# Abusing DPAPI for Credential Access

This package-facing entry is blocked pending redaction and safety review.

DPAPI credential-access procedures can recover protected secrets from Windows users, browsers, credential vaults, and domain backup-key paths. This repository must not expose a default executable procedure for that capability. Treat the upstream technique as reference-only unless an approved engagement workspace has written scope, evidence handling, and review controls.

## Allowed use in this repository

- Record authorization requirements and rules of engagement.
- Plan defensive assessment scope and evidence-handling boundaries.
- Map DPAPI-related findings to controls, detections, and remediation.
- Preserve provenance, risk classification, and review status.
- Help reviewers decide whether a future defensive-only workflow is safe to publish.

## Disallowed use in this repository

- Do not provide copyable live-operation commands.
- Do not include instructions for decrypting, extracting, harvesting, or reusing credentials, browser secrets, cookies, vault records, private keys, or domain backup keys.
- Do not request, paste, store, transform, or summarize recovered secrets or credential artifacts.
- Do not perform live host, domain, tenant, or network actions from this skill.
- Do not package this entry as publication-ready until a reviewer replaces it with a defensive-only workflow.

## Safe reviewer checklist

1. Confirm written authorization, scope, and evidence-retention rules.
2. Confirm the task is defensive validation, detection engineering, incident-response scoping, or remediation planning.
3. Keep procedural credential-access detail out of the package-facing skill.
4. Move any operational references to a controlled, non-default review artifact if they are retained at all.
5. Verify that the final skill teaches defensive planning, detection, evidence handling, and remediation rather than execution.
6. Require explicit human approval before any installer, catalog, or publisher surface presents this as usable automation.

## Defensive review prompts

- What DPAPI-protected asset classes are in scope for defensive monitoring?
- Which logs, EDR events, file-access signals, or identity-control events should be inspected?
- Which controls reduce exposure from stored credentials, browser secrets, local admin reach, domain backup-key access, and stale saved sessions?
- What remediation evidence can be collected without exposing or reproducing secrets?

## Status

Risk decision: high risk, requires review, blocked pending redaction.
