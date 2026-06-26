---
name: Vendor Management — Scorecard, SLA Tracking, and Third-Party Risk
description: Review, score, and audit third-party SaaS/vendor relationships. Run vendor scorecards with industry tuning, track SLA compliance with credit-claim flags, classify third-party risk across 4 risk vectors, prepare tier-1 vendor reviews, and audit the SaaS portfolio. Produces KEEP / REVIEW / REPLACE recommendations with deterministic scoring.
version: 1.0.0
source: claude-skills/business-operations/vendor-management (MIT)
author: claude-code-skills (distilled by Agent-Memory-Ops-Kit)
tags: [productivity, bizops, vendor, sla, third-party-risk, vendor-management, saas-management, tprm]
type: Playbook
---

# Vendor Management — Scorecard, SLA Tracking, and Third-Party Risk

Operational third-party performance review. Score vendors on multi-dimensional criteria, track SLA compliance against contractual targets, classify third-party risk, and recommend KEEP / REVIEW / REPLACE actions.

## Purpose

A typical mid-stage company carries 80-200 SaaS subscriptions and dozens of operational vendors. Most are reviewed only at renewal — which is too late. This skill enables **quarterly or rolling vendor performance reviews** with deterministic scoring so the renewal decision is already half-made before the contract comes due.

## When to use

- Quarterly vendor scorecard preparation for leadership.
- Tier-1 vendor (identity provider, data warehouse) has recurring incidents — quantify the SLA gap.
- CISO needs third-party risk classification of the SaaS portfolio for audit.
- Renewal is 60-90 days out and you need a defensible KEEP / REVIEW / REPLACE recommendation.
- Post-acquisition vendor deduplication.

## When NOT to use

- Negotiating new contract terms → use legal/contract skills.
- Writing outbound proposals or RFP responses → use business development skills.
- Categorizing software spend or finding duplicate SaaS → use procurement-optimizer.
- Designing internal system SLOs → use SLO/SLI skills.

## Vendor Criticality Tiers

| Tier | Definition | Review frequency |
|------|-----------|-----------------|
| **Tier 1** | Business stops if down | Quarterly |
| **Tier 2** | Important but workaround exists | Semi-annually |
| **Tier 3** | Nice-to-have | Annually |

## Vendor Scorecard Dimensions

Score each vendor 0-100 across:

1. **Uptime** (25%): Actual uptime vs. contractual SLA
2. **Support responsiveness** (25%): P90 ticket response time vs. contractual target
3. **Security posture** (25%): Certifications held (SOC2, ISO27001, HIPAA, PCI-DSS, FedRAMP)
4. **Incident history** (25%): Count and severity of incidents in last 12 months

## Third-Party Risk Vectors

| Vector | What to assess | Red flags |
|--------|---------------|-----------|
| **Operational** | Uptime history, incident frequency | >3 incidents/year for tier-1 |
| **Security** | Certifications, breach history, data handling | No SOC2 for data-processing vendors |
| **Financial** | Vendor financial health, funding stage | Pre-revenue vendor for tier-1 dependency |
| **Concentration** | Single-source risk, switching cost | No alternative for tier-1 category |

## Recommendation Framework

| Score | Recommendation | Action |
|-------|---------------|--------|
| 80–100 | **KEEP** | Continue relationship, monitor |
| 60–79 | **REVIEW** | Investigate gaps, set improvement plan |
| < 60 | **REPLACE** | Initiate RFP for alternative |

## Workflow

1. **Intake**: Collect vendor catalog with name, category, annual_spend, contract_end_date, criticality, uptime_pct, support_response_hours_p90, incident_count_last_12m, security_certs, renewal_terms.
2. **Score**: Compute 0-100 score per vendor across the 4 dimensions.
3. **Classify risk**: Assess each vendor across the 4 risk vectors.
4. **Recommend**: KEEP / REVIEW / REPLACE with specific findings.
5. **Plan**: For REVIEW vendors, set 90-day improvement plan with measurable targets.

## Source

Distilled from `claude-skills/business-operations/skills/vendor-management/SKILL.md` (claude-code-skills, MIT).
Adapted for Hermes Agent — removed Claude Code-specific tool references.
