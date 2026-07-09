---
name: Building Cloud SIEM with Sentinel
description: Govern Microsoft Sentinel SIEM/SOAR design as an authorized, review-gated defensive security workflow without package-facing cloud mutation snippets.
tags: [agent-skill, okf, microsoft-sentinel, cloud-siem, siem-governance, soar-governance, threat-detection, security-defensive]
license: Apache-2.0
type: Playbook
domain: security-defensive
risk_level: high
requires_review: true
source_status: existing_package_skill_risk_reviewed
review_status: defensive_wrapper_only
reviewed_at: 2026-07-09
---

# Building Cloud SIEM with Sentinel

## Safety Classification

This skill is **high risk** because Microsoft Sentinel and connected SIEM/SOAR workflows can touch cloud subscriptions, identity logs, external threat-intelligence feeds, incident automation, and account-state mutation. Use it only for authorized defensive security work in environments where the operator has explicit approval.

This package-facing version is a governance wrapper. It intentionally excludes executable Azure CLI, KQL, Logic Apps, Microsoft Graph, AWS connector, STS revocation, and account-disable snippets. Implementation commands, connector setup, production detections, or automated response playbooks must stay in a separate reviewed runbook with environment-specific approval.

## When to Use

Use this skill when planning or reviewing a Microsoft Sentinel deployment for a legitimate security operations environment:

- Establishing a centralized SIEM for owned cloud tenants.
- Reviewing Sentinel data-source coverage, retention, and detection governance.
- Designing safe escalation paths for incident response automation.
- Assessing whether SOAR actions need human approval, break-glass controls, or rollback paths.
- Preparing a security architecture review before connector deployment or production analytics rules.

Do not use this skill to access cloud tenants without authorization, harvest identity or activity logs, deploy account-mutating playbooks, publish detection logic that exposes private telemetry, or automate response actions against accounts/resources without a reviewed change process.

## Required Review Gate

Before implementation, a qualified reviewer must approve:

1. **Authority** — the tenant, subscriptions, workspaces, cloud accounts, and log sources are owned or contractually authorized.
2. **Data handling** — identity logs, network telemetry, threat intelligence, and incident evidence have retention, access, and redaction rules.
3. **Connector scope** — each connector has least-privilege credentials and documented blast radius.
4. **Detection impact** — analytics rules are tested against sample or staged data before production alerting.
5. **SOAR controls** — any account disablement, resource isolation, STS/session revocation, firewall change, or ticket automation has approval, audit logging, and rollback.
6. **Publication boundary** — package/catalog surfaces do not expose executable tenant setup, production KQL, secrets, connection strings, IAM roles, webhook URLs, or automation payloads.

## Safe Workflow

### 1. Define the SOC operating boundary

Document the intended security operations scope before touching any tenant:

- Cloud environments in scope.
- Business owners and emergency contacts.
- Data classes ingested by Sentinel.
- Retention period and access model.
- Incident severity model.
- Actions that are observe-only, analyst-approved, or automatically executable.

Output a short architecture note rather than commands.

### 2. Plan workspace and connector governance

For each data source, record:

- Purpose of ingestion.
- Required permissions.
- Whether credentials are read-only or can mutate resources.
- Expected data volume and cost owner.
- Sensitive fields that require masking or restricted access.
- Failure mode if the connector breaks or over-ingests.

High-risk connector categories include identity providers, cross-cloud activity logs, endpoint/security product feeds, threat-intelligence providers, and any connector that can trigger downstream automation.

### 3. Review detection logic safely

Detection design should be reviewed at the level of intent and test evidence:

- Detection name and threat hypothesis.
- Data tables or event classes used.
- Known false-positive sources.
- Severity mapping.
- MITRE ATT&CK mapping when useful.
- Test dataset or staging validation result.
- Expected incident owner and escalation path.

Avoid publishing production KQL that encodes sensitive schema assumptions, tenant-specific watchlists, private indicators, user identifiers, service principals, IP ranges, or operational thresholds.

### 4. Bound threat-intelligence matching

Threat-intelligence feeds can create privacy, licensing, and false-positive problems. Before matching indicators against telemetry, confirm:

- Indicator source license and redistribution limits.
- Expiration/decay rules.
- Confidence threshold.
- What telemetry fields are matched.
- Whether matches remain internal or are sent to another system.
- How false positives are suppressed and audited.

Do not submit private telemetry, user data, raw logs, or customer evidence to external reputation services unless the incident-response agreement and data-processing terms allow it.

### 5. Gate SOAR and response automation

Treat SOAR as a change-control surface, not as a default feature. Separate actions into tiers:

- **Tier 0: Enrich only** — add context, route tickets, notify analysts.
- **Tier 1: Reversible soft action** — analyst-approved labels, tags, or low-impact access review.
- **Tier 2: Controlled containment** — account disablement, token/session revocation, resource isolation, firewall updates, or quarantine. Requires explicit approval, audit evidence, and rollback.
- **Tier 3: Emergency automation** — only for pre-approved incident classes with tested rollback and after-action review.

Package-facing skills should describe these tiers, not include deployable Logic Apps payloads or account-mutation calls.

### 6. Produce an implementation handoff

The safe output of this skill is a reviewed handoff, not a live deployment. Include:

- Scope and authorization statement.
- Connector inventory and risk rating.
- Detection inventory and validation status.
- Automation inventory by tier.
- Open risks and required approvals.
- Rollback and incident-review requirements.
- Catalog/publication status.

## Acceptance Criteria

A Sentinel SIEM/SOAR plan is acceptable when:

- The environment and owner are explicit.
- No secrets, tenant IDs, raw private telemetry, service-principal details, IAM role ARNs, or webhook URLs are exposed in package-facing artifacts.
- Detections are documented with purpose and validation evidence.
- SOAR actions are tiered and review-gated.
- Any account/resource mutation has human approval or a separately approved emergency playbook.
- External threat-intelligence matching has licensing and data-handling review.
- The result can be audited without requiring execution of cloud commands.

## Red Flags

Stop and escalate if the work asks the agent to:

- Provision or alter cloud SIEM resources directly from the package skill.
- Connect a tenant, workspace, or cloud account without explicit authorization.
- Disable accounts, revoke sessions, isolate resources, or update firewall/blocklists automatically.
- Submit raw logs, mailbox evidence, network telemetry, customer data, or private indicators to external services.
- Embed tenant-specific identifiers, secrets, IAM roles, service-principal IDs, webhook URLs, or production KQL in public/package-facing files.
- Tune detections directly against live production data without a reviewed test plan.

## Output Format

```markdown
# Microsoft Sentinel SIEM/SOAR Review

## Scope
- Tenant/workspace owner:
- Cloud environments in scope:
- Data classes ingested:
- Authorization evidence:

## Connector Governance
| Connector | Purpose | Permission Class | Data Sensitivity | Status | Reviewer |
|---|---|---|---|---|---|

## Detection Governance
| Detection | Hypothesis | Data Class | Severity | Validation Evidence | Status |
|---|---|---|---|---|---|

## SOAR Governance
| Playbook | Action Tier | Mutation Risk | Approval Required | Rollback Path | Status |
|---|---|---|---|---|---|

## Risk Register
| Risk | Impact | Mitigation | Owner | Due Date |
|---|---|---|---|---|

## Publication Boundary
- Package-facing artifacts contain no executable cloud setup or account-mutation snippets.
- Catalog state remains blocked until parity is refreshed after this risk review.
```
