---
name: Procurement Optimizer — Spend Categorization and Supplier Rationalization
description: Run annual SaaS audits, category-level spend reviews, and supplier rationalization.
  Categorize spend (UNSPSC-aligned with Pareto breakdown), purchasing-cycle analysis
  (bottleneck categories per Theory of Constraints), and risk-balanced supplier consolidation
  that refuses single-source recommendations for tier-1 categories without a documented
  break-glass plan.
version: 1.0.0
source: claude-skills/business-operations/procurement-optimizer (MIT)
author: claude-code-skills (distilled by Agent-Memory-Ops-Kit)
tags:
- business
- productivity
- bizops
- procurement
- spend-categorization
- supplier-consolidation
- unspsc
- saas-audit
- purchasing-cycle
- okf
type: Playbook
title: Procurement Optimizer — Spend Categorization and Supplier Rationalization
domain: business
risk_level: medium
requires_review: true
source_family: amok-native
source_status: adapted
---

# Procurement Optimizer — Spend Categorization and Supplier Rationalization

Annual category review for Head of Procurement / Head of BizOps / VP Finance. Categorize spend, find the Pareto-20% of categories driving 80% of cost, surface purchasing-cycle bottlenecks, and produce a **risk-balanced** supplier-consolidation plan.

## Purpose

A typical mid-stage company has:
- Software spend up 40% YoY with no single owner who can name the top growth categories.
- 3 monitoring tools, 2 expense platforms, 4 email-marketing tools — duplicate-function clusters.
- Purchasing cycle where some categories close in 5 days and others take 90.
- Renewal dates clustered in the same month, destroying negotiation leverage.

## When to use

- Annual SaaS audit and category-level spend review.
- Category owner wants to know which 5 categories drove this year's spend growth.
- Finance flags that software spend is up 40% YoY and needs a Pareto by category.
- BizOps suspects duplicate-function tools and needs a defensible consolidation plan.
- Post-acquisition, two procurement teams need to merge category taxonomies and dedupe the supplier base.

## When NOT to use

- Scoring or auditing an individual vendor → use vendor-management.
- Financial close, monthly reporting, or P&L analysis → use finance skills.
- Drafting or negotiating contract terms → use legal/contract skills.
- Building outbound sales proposals → use business development skills.

## Workflow

1. **Intake spend**: Collect line items with `{supplier, description, category_hint, annual_spend, frequency, currency}`. Include prior-year spend for YoY analysis.

2. **Categorize and find the Pareto**: Categorize spend along UNSPSC-aligned taxonomy. Identify the 20% of categories driving 80% of cost.

3. **Analyze purchasing cycle**: Compute cycle time per category. Identify bottleneck categories (Goldratt's Theory of Constraints).

4. **Consolidate suppliers**: Produce a risk-balanced consolidation plan. **Never recommend single-source for tier-1 categories without a documented break-glass plan.**

5. **Stagger renewals**: Recommend renewal date distribution to avoid clustering and maintain negotiation leverage.

## Risk-Balanced Consolidation Rules

| Rule | Rationale |
|------|-----------|
| Never single-source tier-1 without break-glass plan | Business continuity risk |
| Always maintain 2+ vendors for critical categories | Negotiation leverage + failover |
| Consolidate tier-3 first | Lowest risk, fastest savings |
| Stagger renewal dates across quarters | Avoid budget spikes + maintain leverage |
| Document consolidation rationale | Audit trail for future reviews |

## Source

Distilled from `claude-skills/business-operations/skills/procurement-optimizer/SKILL.md` (claude-code-skills, MIT).
Adapted for Hermes Agent — removed Claude Code-specific tool references.
