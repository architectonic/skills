---
name: Analyzing Email Headers for Phishing Investigation
description: Review suspicious email headers for phishing indicators under authorized incident-response controls.
tags: [forensics, email-analysis, phishing, spf, dkim, dmarc, header-analysis, security-defensive, incident-response]
license: Apache-2.0
type: Playbook
domain: forensics
risk_level: high
requires_review: true
source_status: existing-package-skill-risk-reviewed
review_gate: authorized-incident-response-only
---

# Analyzing Email Headers for Phishing Investigation

## Safety Boundary

Use this skill only for authorized incident response, abuse-desk triage, legal/compliance review, or defensive mailbox investigation where the reviewer has permission to inspect the message and its metadata.

Do not use this skill to access, extract, publish, submit, or enrich private mailbox content unless the case owner has approved the exact evidence handling path. Treat message bodies, attachments, recipients, internal relay names, authentication results, source IPs, and user identifiers as sensitive evidence.

External reputation checks, third-party submissions, and API-backed enrichment must remain outside the package-facing default workflow unless a separate review approves data minimization, terms, credentials, retention, and disclosure risk.

## When to Use

- Investigating a suspected phishing message or business email compromise attempt.
- Validating whether a visible sender is aligned with the authenticated sender.
- Reviewing SPF, DKIM, DMARC, ARC, Return-Path, Reply-To, Message-ID, and Received-chain evidence.
- Producing a defensive report that separates authentication failures, routing anomalies, sender-domain issues, and content indicators.

## Required Authorization Checklist

Before analysis, confirm:

- The message is in scope for the investigation.
- Evidence handling rules are known for the mailbox, tenant, case, or client.
- Private content is minimized before being shared or copied.
- Attachments and links are not opened or submitted without explicit approval.
- Any external enrichment service has been approved for the data being sent.

## Review Workflow

### 1. Preserve Evidence Without Expanding Exposure

Work from a case-approved export or case-approved header view. Record where the evidence came from, who authorized access, and whether body or attachment content was reviewed.

Preferred package-facing evidence scope:

- Full raw headers.
- Authentication-Results fields.
- Envelope sender and visible sender fields.
- Message-ID, Date, Return-Path, Reply-To.
- Received-chain metadata needed to reconstruct routing.

Avoid unnecessary package-facing collection of:

- Full mailbox folders.
- Unrelated messages.
- Attachment contents.
- Message bodies where header-only review is sufficient.
- Personal contact lists or unrelated recipient data.

### 2. Reconstruct the Delivery Chain

Read `Received` headers from earliest handoff to latest recipient-side handoff. Identify:

- Apparent origin.
- Relay sequence.
- Boundary between external infrastructure and recipient infrastructure.
- Missing, malformed, duplicated, or internally inconsistent hops.
- Time anomalies that may indicate tampering, forwarding, or delayed delivery.

Treat self-reported client headers and display names as low-trust. Prefer server-added routing and authentication headers.

### 3. Validate Authentication and Alignment

Review these fields as a set, not in isolation:

- SPF result and envelope sender alignment.
- DKIM signature presence, selector, signing domain, and validation result.
- DMARC disposition and alignment.
- ARC results where forwarding may affect authentication.
- Return-Path and Reply-To mismatch.
- From display-name impersonation.

A pass on SPF or DKIM does not prove the message is benign. It may indicate legitimate infrastructure abuse, compromised accounts, forwarding, or authorized bulk-mail service use.

### 4. Review Sender and Infrastructure Signals

Classify infrastructure findings without leaking sensitive details:

- New, lookalike, or typo-squatted domains.
- Mismatched visible sender, reply path, and envelope sender.
- Unexpected sending service or relay path.
- Suspicious Message-ID format or sender infrastructure mismatch.
- Internal relay names or tenant identifiers that should be redacted in reports.

Use generic descriptions when reporting to broader audiences. Preserve raw values only in restricted case evidence.

### 5. Review Body and Attachment Indicators Only When Approved

If header evidence is insufficient and the case owner approves content review, inspect body and attachment indicators defensively:

- Visible link text versus actual destination.
- Attachment names, types, and hashes.
- Requests for credentials, payments, MFA codes, wire transfers, or account recovery.
- Brand impersonation, urgency language, and reply-channel manipulation.

Do not open links, detonate attachments, or submit sensitive content to public or third-party systems from the package-facing workflow.

### 6. Produce a Minimal Defensive Report

A safe report should include:

- Case identifier.
- Scope and authorization note.
- Message metadata summary.
- Authentication assessment.
- Delivery-chain assessment.
- Sender-domain and infrastructure assessment.
- Content or attachment indicators only if approved.
- Evidence sensitivity classification.
- Recommended containment, user notification, tenant rule review, and detection follow-up.

## Classification Guidance

| Finding | Interpretation |
|---|---|
| SPF fail with visible-domain impersonation | Strong spoofing indicator. |
| DKIM absent or misaligned | Suspicious when a legitimate sender normally signs. |
| DMARC fail or no enforcement | Raises impersonation risk. |
| Reply-To mismatch | Common BEC and credential-harvest signal. |
| Recently created lookalike domain | Strong phishing indicator. |
| Authentication passes but content is malicious | Possible compromised account or authorized service abuse. |
| Attachment hash matches known malware | Escalate to malware handling workflow. |

## Output Format

```text
Email Header Analysis Report

Scope and authorization:
- Case:
- Reviewer:
- Evidence source:
- Handling restrictions:

Header summary:
- Visible From:
- Envelope sender / Return-Path:
- Reply-To:
- Message-ID:
- Date:

Authentication:
- SPF:
- DKIM:
- DMARC:
- ARC / forwarding context:

Delivery chain:
- Earliest observed hop:
- Recipient-side boundary:
- Routing anomalies:

Indicators:
- Sender/domain:
- Infrastructure:
- Content/attachment indicators, if approved:

Assessment:
- Risk level:
- Confidence:
- Rationale:

Recommended action:
- Containment:
- User guidance:
- Detection or mail-rule follow-up:
- Evidence retention notes:
```

## Review Notes

This package-facing version intentionally omits executable mailbox extraction, DNS/reputation commands, API-key examples, public submission workflows, attachment extraction scripts, and raw private-data examples. Those steps require a separate approved forensic runbook and case-specific authorization.