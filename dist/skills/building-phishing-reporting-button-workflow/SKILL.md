---
name: Building Phishing Reporting Button Workflow
description: Govern phishing reporting-button programs without exposing package-facing mailbox mutation, external-submission, or private-data automation.
tags: [security-defensive, phishing-reporting, email-security, incident-response, security-awareness, outlook, microsoft-365, soar, governance, high-risk, requires-review]
license: Apache-2.0
type: Playbook
domain: security-defensive
risk_level: high
requires_review: true
source_status: package_risk_reviewed
review_status: governance_wrapper_only
---

# Building Phishing Reporting Button Workflow

## Purpose

Use this skill to plan and review a phishing-reporting-button program at a governance level. It is intentionally a high-risk defensive wrapper: it does not provide package-facing instructions for configuring tenant-wide email controls, monitoring user-submitted mailboxes, extracting indicators from private messages, submitting content to third-party analysis services, mutating inboxes, blocking domains, or notifying reporters automatically.

## Risk classification

This workflow is high risk because a real implementation can touch:

- Microsoft 365, Google Workspace, or similar email-suite administrative configuration.
- Dedicated reporting mailboxes containing user-submitted messages and potentially private data.
- Security orchestration systems that monitor mailbox content or trigger automated response actions.
- URLs, attachments, sender data, headers, and other indicators extracted from reported messages.
- External reputation, sandbox, or scanning services that may receive sensitive message artifacts.
- Inbox retraction, message movement, sender/domain blocking, reporter notifications, and user metrics.

Any deployment, automation, connector setup, mailbox monitoring, third-party submission, or remediation action requires explicit human review, tenant authorization, privacy/legal approval where applicable, and environment-specific change control.

## Safe use

Use this playbook only to:

- Define the review checklist for a phishing-reporting program.
- Identify required approvals and owners.
- Separate user-report intake, triage, analyst review, remediation, and communications responsibilities.
- Document what must be redacted before logs, reports, or examples leave the authorized environment.
- Decide which actions must remain human-approved instead of automatic.
- Define non-sensitive success metrics for program governance.

Do not use this skill to configure a live email tenant, connect to a mailbox, submit message contents to external services, mutate user inboxes, block domains, or send user notifications.

## Governance checklist

### 1. Program scope

- Identify the mail platform, reporting mechanism, SOC owner, privacy owner, legal/compliance reviewer, and change-control process.
- Define which mailbox artifacts may be collected and which must be redacted or excluded.
- Confirm data retention, access controls, audit logging, and incident-classification boundaries.

### 2. Intake controls

- Treat reported messages as potentially sensitive user data.
- Restrict access to authorized analysts and approved automation accounts.
- Document how test submissions differ from production reports.
- Keep sample data synthetic unless the review explicitly authorizes real-message handling.

### 3. Triage controls

- Require review before extracting or sharing indicators derived from user messages.
- Require review before sending URLs, attachments, or headers to any external reputation or sandbox service.
- Record which services are approved, what data they receive, and whether submissions are public, private, or shared with a community feed.

### 4. Response controls

- Human-review inbox retraction, message movement, domain blocking, sender blocking, and reporter notifications unless a formally approved automation policy exists.
- Require rollback and audit evidence for every mailbox or domain mutation.
- Keep simulation-credit and reporter-feedback logic separate from threat-remediation logic.

### 5. Metrics controls

- Prefer aggregate metrics that do not expose individual user behavior unless HR, legal, and privacy review explicitly permits named reporting.
- Avoid publishing message contents, reporter identities, recipient lists, or raw indicators outside approved channels.

## Review artifacts to produce

A safe implementation plan should produce:

- Approved scope and data-handling policy.
- Threat-model notes for mailbox monitoring and third-party submissions.
- Human-approval matrix for remediation and notification actions.
- Redaction rules for examples, reports, tickets, and metrics.
- Rollback and audit requirements for mailbox or domain mutations.
- A test plan using synthetic messages and non-production accounts.

## Explicitly blocked from package-facing guidance

This package copy intentionally omits:

- Tenant-admin setup commands or step-by-step console instructions.
- SOAR mailbox-monitoring connector details.
- IOC extraction code for user-submitted messages.
- VirusTotal, URLScan, sandbox, or reputation-service submission code.
- Automated inbox retraction, message movement, sender/domain blocking, or reporter-notification workflows.
- Real incident identifiers, personal data placeholders, message contents, headers, URLs, attachments, or escalation contacts.

## Acceptance criteria

A downstream implementation is not cleared by this skill unless reviewers confirm:

- The environment owner authorized the mail-platform and SOAR scope.
- Privacy/legal handling for reported messages is documented.
- External submissions are approved and classified as public/private/shared.
- Automated mutations have explicit approval, audit logging, and rollback.
- Test evidence uses synthetic or approved sanitized data.

This skill is for defensive governance only. It is not a deployment guide, automation recipe, external-submission workflow, or remediation runbook.
