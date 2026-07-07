---
name: auditing-entra-id-with-aadinternals
description: Review-gated defensive assessment wrapper for AADInternals-based Entra ID security validation. Use only for authorized identity-security planning, evidence boundaries, detection design, and remediation mapping.
tags: [agent-skill, okf, aadinternals, entra-id, azure-ad, cloud-identity, security, review-gated]
license: Apache-2.0
type: Playbook
domain: security-offensive
risk_level: high
requires_review: true
source_family: public-security-tooling
source_license: Apache-2.0
source_status: blocked-pending-redaction
---

# Auditing Entra ID with AADInternals

This package-facing entry is blocked pending redaction and safety review.

AADInternals includes capabilities that can affect live cloud identity environments. This repository must not expose a default executable procedure for that capability. Treat the upstream tool as reference-only unless an approved engagement workspace has written scope, evidence handling, and review controls.

## Allowed use in this repository

- Record authorization requirements.
- Plan defensive assessment scope.
- Map findings to controls, detections, and remediation.
- Preserve provenance and review status.

## Disallowed use in this repository

- Do not provide copyable live-operation commands.
- Do not request, paste, store, or transform credentials, session material, tenant exports, or identity artifacts.
- Do not perform live tenant actions from this skill.
- Do not package this entry as publication-ready until a reviewer replaces it with a defensive-only workflow.

## Safe reviewer checklist

1. Confirm written authorization and scope.
2. Confirm the task is defensive validation or remediation planning.
3. Keep procedural detail out of the package-facing skill.
4. Move any operational references to a controlled, non-default review artifact if they are retained at all.
5. Verify that the final skill teaches defensive planning, evidence handling, and remediation rather than execution.

## Status

Risk decision: high risk, requires review, blocked pending redaction.
