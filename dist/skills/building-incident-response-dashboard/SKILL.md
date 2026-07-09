---
name: Building Incident Response Dashboard
description: Design defensive incident-response dashboard governance without exposing live incident data, IOCs, credentials, or SIEM mutation snippets.
tags: [agent-skill, okf, soc, dashboard, incident-response, situational-awareness, metrics, security, governance]
license: Apache-2.0
type: Metric
domain: security-defensive
risk_level: high
requires_review: true
source_status: risk_reviewed
reviewed_at: 2026-07-09
review_ticket: skills-risk-review-ir-dashboard-timesketch-001
---

# Building Incident Response Dashboard

## Purpose

Use this skill to design or review incident-response dashboard requirements, data boundaries, ownership, and operational safeguards. It is a defensive governance wrapper for active-incident dashboards.

This skill is high risk because active IR dashboards can expose live incident data, internal hosts, affected identities, IOCs, analyst assignments, containment state, and operational response steps. Dashboard automation can also mutate SIEM lookup tables, tickets, or incident records. Those surfaces require explicit human review before implementation or installation.

## Use When

- An IR team needs a safe dashboard specification for active incident coordination.
- SOC leadership needs status, workload, and response-progress reporting.
- A team needs to decide which incident data may be shown to which audience.
- A package, installer, or agent needs to classify an IR dashboard skill before publication.

## Do Not Use For

- Building or executing live SIEM searches.
- Publishing real IOCs, hostnames, identities, case numbers, or containment status.
- Writing or updating lookup tables, tickets, cases, dashboards, or incident records.
- Creating scheduled searches, SOAR playbooks, alert actions, or account/device mutation.
- Handling customer, employee, patient, legal, or regulated incident evidence without an approved evidence-handling process.

## Required Review Gate

Before implementation, a reviewer must confirm:

1. The organization owns or is authorized to process the incident data.
2. Data fields are classified by sensitivity and audience.
3. IOC, host, user, asset, and case identifiers are redacted or scoped to authorized viewers.
4. Dashboard refresh behavior is read-only unless a separate change-control approval exists.
5. Any SIEM, SOAR, ticketing, endpoint, cloud, or identity mutation is out of scope for this skill.
6. Logging, retention, export, and screenshot policies are defined.
7. Executive views aggregate sensitive data instead of exposing raw evidence.

## Safe Dashboard Model

Design dashboards as read-only views over pre-approved data products.

Recommended dashboard sections:

| Section | Safe Content | Review Notes |
|---|---|---|
| Incident summary | phase, severity band, owner role, last update time | avoid raw case IDs in broad-audience views |
| Scope summary | aggregate affected system counts | do not expose hostnames unless viewer is authorized |
| Containment progress | percentage and milestone state | avoid showing live containment commands or response actions |
| IOC summary | counts by IOC type | do not publish raw indicators outside the approved response group |
| Timeline | major response milestones | omit private evidence and personal data |
| Workload | assigned team/queue counts | avoid naming analysts in executive views |
| Business impact | service-level impact and recovery estimate | avoid unverified legal or breach conclusions |

## Data Classification

Classify every field before it appears in the dashboard.

| Data Class | Examples | Default Handling |
|---|---|---|
| Public summary | status category, high-level impact | allowed in executive view after review |
| Internal operational | queue counts, phase, response SLA | restricted to internal stakeholders |
| Sensitive incident data | hostnames, usernames, IPs, hashes, domains, ticket IDs | restricted to incident team |
| Private evidence | logs, emails, browser history, screenshots, endpoint artifacts | excluded from dashboards unless explicitly approved |
| Mutation controls | isolation state, blocklists, ticket writes, lookup writes | excluded from this skill |

## Safe Workflow

1. Define the dashboard audience.
2. Define allowed questions for that audience.
3. Map questions to aggregate metrics.
4. Classify each source field.
5. Remove raw sensitive values from broad views.
6. Require reviewer approval for any dashboard that shows live incident data.
7. Use read-only service accounts and least-privilege dashboard permissions.
8. Record the approved data sources, refresh cadence, owner, and retention period.
9. Test with synthetic data before connecting to any production data source.
10. Keep generated dashboards out of package publication until review is complete.

## Dashboard Requirements Template

```text
Dashboard name:
Incident type:
Audience:
Owner:
Data sources:
Refresh cadence:
Allowed fields:
Excluded fields:
Sensitive-field handling:
Reviewer:
Approval date:
Retention:
Export/screenshot policy:
Read-only guarantee:
Known limitations:
```

## Safe Metrics

Prefer aggregate metrics that support coordination without exposing unnecessary evidence.

- incident phase
- severity band
- time since detection
- containment percentage
- affected-system count by category
- unresolved task count by queue
- handoff status
- mean time to acknowledge
- mean time to contain
- recovery milestone status

## Redaction Rules

- Replace exact hostnames with asset categories unless exact names are required.
- Replace usernames with team or role labels for management views.
- Replace exact IOCs with counts by type for non-technical audiences.
- Remove email addresses, file paths, URLs, screenshots, and raw event payloads.
- Avoid embedding live case numbers in reusable templates.
- Never include credentials, tokens, cookies, secrets, or private keys.

## Implementation Boundary

This package-facing skill must not include:

- executable SIEM queries against live data;
- scheduled-search configuration;
- lookup-table writes;
- SOAR actions;
- endpoint isolation;
- identity or account changes;
- firewall, DNS, or blocklist mutation;
- ticket or incident-record mutation;
- raw IOCs or private evidence examples.

Those tasks require a separate authorized implementation plan outside this skill.

## Acceptance Checklist

- [ ] The skill is marked `risk_level: high`.
- [ ] The skill is marked `requires_review: true`.
- [ ] Raw SIEM query snippets have been removed or replaced with requirements language.
- [ ] Raw IOC, host, user, and case examples have been removed or generalized.
- [ ] Lookup-write and scheduled-search instructions have been removed or review-gated.
- [ ] Safe dashboard guidance remains useful for defensive IR planning.
- [ ] Catalog refresh is queued after metadata changes.

## Output Format

```text
IR DASHBOARD REVIEW RESULT

Risk: high
Requires review: true

Approved safe use:
- read-only dashboard requirements
- aggregate metrics
- audience and field classification
- redaction and retention policy

Blocked from package-facing use:
- live SIEM queries
- raw incident data
- IOC publication
- lookup writes
- scheduled searches
- SOAR or account/device mutation

Next gate:
- catalog parity refresh after this risk review
```
