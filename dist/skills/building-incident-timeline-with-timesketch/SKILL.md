---
name: Building Incident Timeline with Timesketch
description: Govern defensive forensic timeline planning with Timesketch without exposing private evidence, credentials, deployment commands, API mutation snippets, or executable ingestion workflows.
tags: [agent-skill, okf, timesketch, timeline-analysis, forensic-timeline, dfir, incident-investigation, collaborative-forensics, security, governance]
license: Apache-2.0
type: Playbook
domain: forensics
risk_level: high
requires_review: true
source_status: risk_reviewed
reviewed_at: 2026-07-09
review_ticket: skills-risk-review-ir-dashboard-timesketch-001
---

# Building Incident Timeline with Timesketch

## Purpose

Use this skill to plan and review defensive forensic timeline work with Timesketch-style workflows while protecting private evidence, credentials, and investigation records.

This skill is high risk because forensic timelines can contain disk-image artifacts, event logs, browser history, cloud logs, usernames, IP addresses, file paths, email artifacts, regulated data, and investigation annotations. Automation can also upload evidence, create sketches, tag events, or mutate investigation records. Those surfaces require explicit authorization and review.

## Use When

- A DFIR team needs a safe timeline-analysis plan.
- A reviewer needs to classify Timesketch, Plaso, log, or evidence-ingestion workflows.
- An agent or package needs to preserve forensic workflow value without shipping executable ingestion or mutation steps.
- An investigation needs evidence-handling, chain-of-custody, retention, and access-control requirements.

## Do Not Use For

- Deploying Timesketch, OpenSearch, PostgreSQL, Redis, Celery, Plaso, Dissect, or related services.
- Ingesting disk images, event logs, browser histories, cloud logs, email data, or endpoint artifacts.
- Uploading Sigma rules or running automated analyzers against real evidence.
- Connecting to an API with credentials.
- Creating, tagging, annotating, mutating, exporting, or deleting investigation records.
- Processing private, regulated, customer, employee, or leaked data without explicit legal and incident authorization.

## Required Review Gate

Before any implementation or evidence handling, confirm:

1. Written authorization covers the systems, accounts, data sources, and time range.
2. Evidence collection follows chain-of-custody requirements.
3. Private and regulated data handling is approved.
4. Access is limited to named investigators.
5. Deployment and ingestion happen in an isolated, approved environment.
6. API credentials and service accounts are handled outside package content.
7. Timeline exports, stories, screenshots, and annotations have retention and disclosure rules.
8. Any mutation of investigation records is reviewed and logged.
9. Synthetic data is used for testing and templates.

## Safe Timeline Model

Use this skill to define the investigation plan, not to execute collection or ingestion.

| Phase | Safe Package-Facing Guidance | Review Boundary |
|---|---|---|
| Scope | define systems, accounts, timeframe, evidence classes | requires authorization |
| Evidence plan | list approved source categories | no private sample evidence |
| Timeline schema | define normalized fields | avoid real usernames, IPs, paths, or hashes |
| Access model | named roles and permissions | no credentials in package |
| Analysis plan | questions and hypotheses | no executable searches against real evidence |
| Annotation policy | allowed tags and note standards | mutation requires case-owner approval |
| Reporting | export rules and redaction | legal/comms review may be required |

## Evidence Classification

| Evidence Class | Examples | Default Handling |
|---|---|---|
| Endpoint artifacts | disk images, filesystem metadata, registry hives | restricted evidence store only |
| Authentication logs | Windows event logs, identity-provider logs | investigator-only unless aggregated |
| Browser artifacts | history, downloads, cookies, cache metadata | high privacy sensitivity |
| Cloud logs | API audit logs, storage access logs | scope by tenant/account/time range |
| Network logs | proxy, firewall, DNS, flow logs | redact user and internal host details in reports |
| Investigation records | tags, annotations, stories, saved searches | mutation must be attributable and reversible where possible |

## Safe Workflow

1. Document authorization and scope.
2. Define evidence source categories without collecting evidence in this package step.
3. Define the target timeline schema.
4. Define redaction and access rules.
5. Define reviewer-approved tags and annotation vocabulary.
6. Define retention and export controls.
7. Validate the plan with synthetic events.
8. Hand off implementation to an authorized DFIR operator with approved tooling.
9. Log every ingestion, search, tag, annotation, export, and deletion in the case record.

## Timeline Schema Template

```text
case_name:
authorized_by:
scope_start:
scope_end:
systems_in_scope:
accounts_in_scope:
evidence_categories:
excluded_sources:
timeline_fields:
sensitive_fields:
redaction_rules:
allowed_tags:
annotation_policy:
access_roles:
retention_period:
export_policy:
reviewer:
approval_date:
```

## Safe Analysis Questions

- What is the first known malicious or suspicious event?
- Which systems fall within the approved scope?
- Which event classes support or refute the incident hypothesis?
- What gaps exist in the evidence timeline?
- Which findings require corroboration before escalation?
- Which artifacts must be excluded from reports due to privacy or legal constraints?

## Redaction Rules

- Replace usernames with role labels unless identity is required for the investigation.
- Replace hostnames with asset categories in broad summaries.
- Remove browser history details from non-investigator reports.
- Remove raw paths, URLs, emails, and command lines unless approved.
- Keep raw evidence in the evidence store, not in reusable package examples.
- Never include credentials, tokens, cookies, service passwords, or private keys.

## Implementation Boundary

This package-facing skill must not include:

- deployment commands;
- ingestion commands;
- live API client code;
- credential placeholders;
- real evidence examples;
- analyzer execution;
- tag or annotation mutation code;
- export automation;
- service configuration instructions that create external state.

Those tasks require a separate authorized DFIR implementation plan outside this skill.

## Acceptance Checklist

- [ ] The skill is marked `risk_level: high`.
- [ ] The skill is marked `requires_review: true`.
- [ ] Deployment and ingestion commands have been removed or replaced with planning guidance.
- [ ] Credential placeholders and API mutation snippets have been removed.
- [ ] Private evidence examples have been removed or generalized.
- [ ] Safe forensic governance and timeline-planning guidance remains useful.
- [ ] Catalog refresh is queued after metadata changes.

## Output Format

```text
TIMESKETCH TIMELINE REVIEW RESULT

Risk: high
Requires review: true

Approved safe use:
- timeline scope planning
- evidence classification
- access and retention planning
- redaction policy
- synthetic-data schema design

Blocked from package-facing use:
- service deployment
- evidence ingestion
- credentialed API use
- analyzer execution
- investigation-record mutation
- private evidence examples

Next gate:
- catalog parity refresh after this risk review
```
