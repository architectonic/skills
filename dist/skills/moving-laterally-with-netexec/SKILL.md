---
name: moving-laterally-with-netexec
description: Review-gated defensive assessment wrapper for NetExec lateral-movement and credential-abuse risk. Use only for authorized network security planning, detection mapping, evidence boundaries, and remediation.
tags: [agent-skill, okf, netexec, lateral-movement, active-directory, credential-access, smb, identity-security, security, review-gated]
license: Apache-2.0
type: Playbook
title: Moving Laterally with NetExec
domain: security-offensive
risk_level: high
requires_review: true
source_family: anthropic-cybersecurity-skills
source_license: Apache-2.0
source_status: blocked-pending-redaction
---

# Moving Laterally with NetExec

This package-facing entry is blocked pending redaction and safety review.

NetExec-style workflows can validate credentials at scale, enumerate domain and host access, perform password spraying, execute commands remotely, dump credential material, and support lateral movement. This repository must not expose a default executable procedure for authentication abuse, remote execution, credential dumping, password spraying, pass-the-hash, ticket abuse, or follow-on movement. Treat the upstream technique as reference-only unless an approved defensive assessment workspace has written scope, lockout-safety rules, evidence-handling boundaries, and human review controls.

## Allowed use in this repository

- Record authorization requirements, network/domain scope, account-safety limits, lockout constraints, and rules of engagement.
- Plan defensive assessment scope for remote-service exposure, credential hygiene, identity controls, and lateral-movement monitoring.
- Map NetExec-related risk to detections, controls, and remediation.
- Preserve provenance, risk classification, review status, and package-safety rationale.
- Help reviewers decide whether a future defensive-only workflow is safe to publish.

## Disallowed use in this repository

- Do not provide copyable live-operation commands, password-spraying steps, pass-the-hash guidance, command-execution procedures, credential-dumping instructions, or lateral-movement workflows.
- Do not include instructions for validating harvested credentials, finding administrative access, dumping SAM/LSA/NTDS material, collecting attack-path data for abuse, or pivoting across hosts.
- Do not request, paste, store, transform, summarize, or enrich credentials, hashes, tickets, account secrets, dumped databases, or recovered credential artifacts.
- Do not perform live domain, network, host, service, account, remote-execution, or credential actions from this skill.
- Do not package this entry as publication-ready until a reviewer replaces it with a defensive-only workflow.

## Safe reviewer checklist

1. Confirm written authorization, network/domain scope, rate limits, lockout policy, and evidence-retention rules.
2. Confirm the task is defensive validation, detection engineering, incident-response scoping, identity-control review, or remediation planning.
3. Keep procedural credential abuse, remote execution, password spraying, dumping, and lateral-movement detail out of the package-facing skill.
4. Move any operational references to a controlled, non-default review artifact if they are retained at all.
5. Verify that the final skill teaches defensive planning, detection, evidence handling, and remediation rather than execution.
6. Require explicit human approval before any installer, catalog, or publisher surface presents this as usable automation.

## Defensive review prompts

- Which remote-service protocols, hosts, admin paths, and identity scopes are authorized for defensive review?
- Which controls reduce lateral-movement risk: local-admin minimization, credential guard, LAPS/gMSA, SMB hardening, network segmentation, MFA-resistant admin workflows, and tiered administration?
- Which logs, EDR events, remote-service events, authentication patterns, lockout signals, and credential-dumping indicators should be inspected?
- What remediation evidence can be collected without exposing or reproducing credentials, hashes, tickets, dumped secrets, or command-execution artifacts?

## Status

Risk decision: high risk, requires review, blocked pending redaction.
