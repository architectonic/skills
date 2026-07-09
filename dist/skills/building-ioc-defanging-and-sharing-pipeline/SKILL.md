---
name: Building IOC Defanging and Sharing Pipeline
description: Review-gated defensive guidance for handling, defanging, and sharing indicators of compromise without exposing active malicious indicators, credentials, or automated external submission paths.
tags: [security-defensive, incident-response, ioc, defanging, threat-intelligence, governance, stix, taxii, misp, review-gated]
license: Apache-2.0
type: Playbook
domain: security-defensive
risk_level: high
requires_review: true
source_status: package_risk_reviewed
reviewed_at: 2026-07-09
reviewed_by: Skills Value Operator
---

# Building IOC Defanging and Sharing Pipeline

## Purpose

Use this skill to design or review a defensive IOC handling pipeline for authorized security operations. It is intentionally review-gated because IOC extraction, refanging, STIX/TAXII/MISP integration, API-key usage, and external threat-intelligence sharing can expose malicious indicators, leak private incident evidence, or mutate external systems.

This package-facing version is a governance wrapper. It does not provide executable submission code, live MISP/TAXII calls, API-key examples, automated feed distribution, or operational refanging routines.

## Allowed Use

Use this skill when you need to:

- define policy for safe IOC handling and defanging;
- review whether IOC material is authorized, shareable, and correctly labeled;
- design approval gates before publishing indicators to partners, MISP, TAXII, SIEM, SOAR, or email channels;
- document defensive handling requirements for reports, tickets, and analyst handoffs;
- verify that internal pipelines avoid accidental activation, leakage, or unaudited external mutation.

Do not use this skill to harvest, activate, test, submit, or distribute indicators without explicit authorization and human approval.

## Risk Classification

High-risk surfaces requiring review:

- IOC extraction from incident reports, mailbox data, tickets, logs, malware reports, or third-party feeds;
- refanging or normalizing defanged malicious URLs, domains, IPs, email addresses, and hashes;
- STIX bundle generation from unreviewed indicators;
- MISP, TAXII, SIEM, SOAR, email, chat, or feed distribution;
- API keys, passwords, tokens, connector credentials, or service accounts;
- external submissions that can create, enrich, block, quarantine, alert, or publish indicators;
- handling private, customer, partner, embargoed, or leaked threat-intelligence material.

## Safe Design Principles

1. **Preserve authorization.** Only process IOC data from approved sources and within the scope of a documented defensive investigation.
2. **Keep indicators inert by default.** Human-facing outputs should be defanged unless a reviewer explicitly approves machine-readable export.
3. **Separate analysis from publication.** Extraction, review, enrichment, and sharing should be separate stages with audit records between them.
4. **Minimize private evidence.** Strip message bodies, user identifiers, internal hostnames, customer names, and nonessential incident context before sharing.
5. **Require explicit TLP and audience controls.** Every shared indicator set should include traffic-light protocol, distribution scope, confidence, source, and expiry metadata.
6. **Prefer dry-run previews.** Analysts should review proposed indicator records before any external system receives them.
7. **Log decisions, not secrets.** Audit records should identify approvers, sources, timestamps, and destinations without storing API keys or sensitive raw payloads.

## Review Checklist

Before any IOC sharing pipeline is approved, confirm:

- the data source is authorized and documented;
- all indicators are relevant to a defensive investigation;
- false positives and known-good infrastructure have been removed;
- private or regulated data has been redacted;
- TLP, confidence, retention, and expiration are set;
- intended recipients and external systems are approved;
- API keys and connector credentials are stored outside skill content and logs;
- a human reviewer has approved the exact payload and destination;
- rollback or takedown procedures exist for erroneous submissions.

## Recommended Pipeline Shape

A safe IOC pipeline should be staged as follows:

1. **Intake:** collect only authorized incident evidence or trusted feed data.
2. **Sanitize:** remove private context and normalize records in an internal workspace.
3. **Defang for review:** produce inert analyst-facing indicators for human inspection.
4. **Classify:** assign type, source, confidence, TLP, expiry, and distribution limits.
5. **Approve:** require human approval before any machine-readable or external publication.
6. **Export:** generate controlled output for approved destinations only.
7. **Audit:** record source, reviewer, destination, and decision metadata.
8. **Monitor:** track false positives, expiry, revocation, and partner feedback.

## Blocked Package-Facing Content

The following are intentionally omitted from this package-facing skill:

- executable IOC extractors that refang or activate indicators;
- STIX bundle generation snippets for malicious indicators;
- MISP or TAXII client code;
- API-key, username, password, or token examples;
- authenticated external submission examples;
- automated distribution to partners, email, chat, SIEM, SOAR, or blocklists;
- sample malicious domains, URLs, or hashes presented as operational payloads.

Use internal, reviewed runbooks for implementation details when the environment, authorization, data handling policy, and destination controls are known.

## Acceptance Criteria

A use of this skill is acceptable only when:

- the request is defensive and authorized;
- indicator material is handled as potentially sensitive evidence;
- no secrets or live connector details are embedded in skill content;
- external publication is gated by explicit human review;
- outputs remain inert unless a separate approved implementation runbook requires machine-readable export;
- all sharing decisions are auditable.

## References

- CISA guidance on the operational value and handling of indicators of compromise
- OASIS STIX 2.1 specification
- OASIS TAXII 2.1 specification
- MISP documentation for information sharing governance
