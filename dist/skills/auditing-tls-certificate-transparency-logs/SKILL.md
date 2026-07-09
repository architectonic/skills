---
name: Auditing TLS Certificate Transparency Logs
description: Review-gated defensive guidance for monitoring Certificate Transparency signals for owned domains without reconnaissance or external-mutation automation.
tags: [agent-skill, okf, certificate-transparency, ct-logs, tls-monitoring, brand-protection, defensive-security, incident-response]
license: Apache-2.0
type: Playbook
domain: security-defensive
risk_level: high
requires_review: true
source_status: package-facing-risk-reviewed
review_status: authorized-owned-domain-use-only
---

# Auditing TLS Certificate Transparency Logs

## Safety boundary

Use this skill only for authorized monitoring of domains, brands, subsidiaries, or infrastructure that the operator is permitted to assess. Treat CT-derived hostnames, typosquat candidates, DNS observations, and alert payloads as sensitive security intelligence.

This skill is not a reconnaissance playbook. It must not be used to enumerate third-party attack surfaces, probe services, bypass rate limits, submit abuse reports, trigger revocation, mutate blocklists, or notify external parties without a separate incident-response approval path.

## When to use

- Monitor owned domains for unexpected certificate issuance.
- Review whether known certificate issuers and certificate lifecycles align with an approved inventory.
- Triage certificate changes that may indicate shadow IT, misconfiguration, or brand-abuse risk.
- Produce internal compliance or security-monitoring evidence.

## Review requirements

Before using CT-derived data in an operational workflow, confirm:

1. The monitored domain set is explicitly owned, contracted, or otherwise authorized.
2. Public CT data collection respects service terms, rate limits, and internal data-handling policy.
3. Alert destinations, ticketing systems, and SIEM integrations are approved for sensitive security findings.
4. External escalation such as revocation requests, abuse reports, takedowns, or customer notifications follows an incident-response process.
5. Findings are corroborated before action; CT appearance alone is not proof of compromise or misuse.

## Safe workflow

### 1. Define authorized scope

Create a written scope containing owned root domains, approved subsidiaries, and approved brand variants. Exclude unrelated lookalikes or third-party domains unless legal, brand-protection, or incident-response approval explicitly covers them.

### 2. Establish a baseline

Build an internal inventory of expected certificate issuers, covered hostnames, renewal patterns, wildcard use, and expiration windows. Keep the baseline tied to asset ownership so that unexpected findings can be routed to the correct owner.

### 3. Review new observations defensively

For each new observation, classify it without taking external action:

- expected renewal;
- new approved service;
- unknown internal service;
- possible unauthorized issuance;
- possible brand-abuse or phishing indicator;
- false positive requiring no action.

Do not treat CT-derived subdomains as permission to scan, access, claim, or test services. Any validation beyond passive review must be separately authorized.

### 4. Corroborate before escalation

Corroborate suspicious certificates with approved internal sources such as asset inventory, certificate management records, DNS ownership records, change tickets, and incident-response intake. Keep evidence minimal and redact sensitive identifiers when sharing outside the response team.

### 5. Route through approved response channels

Escalate only through approved channels. External actions such as certificate revocation requests, registrar/hosting abuse reports, anti-phishing notices, customer messaging, blocklists, or enforcement tickets require human approval and traceable authorization.

## Allowed outputs

- Internal certificate inventory summary.
- Authorized issuer drift report.
- New hostname review queue.
- Certificate expiration and lifecycle report.
- Evidence packet for internal incident-response review.

## Blocked package-facing content

This package-facing skill intentionally omits:

- direct CT API polling instructions, endpoints, or scheduler cadence;
- DNS-resolution procedures for newly discovered hostnames;
- typosquat generation algorithms;
- takeover triage procedures;
- SMTP, webhook, PagerDuty, or SIEM configuration snippets;
- revocation, abuse-report, blocklist, takedown, or notification automation;
- CT-log consistency-proof implementation details.

Those may be appropriate only inside a separate, authorized internal runbook with legal, incident-response, and operational approvals.

## Acceptance checklist

- Scope is limited to authorized assets.
- No third-party probing or service access occurs from CT observations alone.
- Alert routing is approved before sensitive findings are transmitted.
- External actions require explicit human approval.
- The workflow produces reviewable defensive evidence, not reconnaissance instructions.
