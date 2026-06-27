---
name: channel-economics
title: Channel Economics
description: 'Analyze and rebalance direct vs. partner-led channel economics. Answers
  three questions at the quarterly channel review:'
type: Playbook
domain: business
tags:
- business
- okf
risk_level: low
requires_review: false
source_family: agent-skills-standard
source_status: adapted
---

# Channel Economics

Analyze and rebalance direct vs. partner-led channel economics. Answers three questions at the quarterly channel review:

1. **What does each channel actually cost to serve, fully loaded?** (headcount, partner discount, MDF, enablement time, support load, overhead)
2. **What is each channel's ROI under three lenses?** (cash year-1, LTV-adjusted, marginal — next dollar)
3. **What is the optimal channel mix subject to constraints?** (min direct floor, max partner ceiling, CAC sensitivity)

Outputs per-channel verdicts (DOUBLE-DOWN / MAINTAIN / DEFUND / EXIT), sensitivity-tested mix recommendation, and diminishing-returns inflection point.

## Workflow

1. **Intake channel data** — Per channel: deal count, ARR, avg deal size, gross margin %, CAC, sales-cycle days, retention, expansion, partner discount %, all attributable costs
2. **Compute cost-to-serve** — Fully-loaded per deal AND per $ ARR, with hidden-cost surfacing
3. **Compute ROI** — 3-lens ROI (Cash / LTV / Marginal) with verdicts and diminishing-returns inflection
4. **Optimize channel mix** — Constrained optimization with sensitivity scenarios
5. **Decide** — Skill recommends; human commits

## Forcing Questions (one at a time)

1. **"What's your fully-loaded cost-to-serve per channel?"** → Load channel-manager headcount, MDF, enablement time, overhead. Canon: Kaplan & Cooper (ABC).
2. **"What is the retention differential between direct and partner-sourced customers?"** → Instrument per-channel retention BEFORE computing ROI. Canon: Skok (SaaS Metrics 2.0).
3. **"What share of 'channel-sourced' pipeline did your team actually originate?"** → Influence ≠ source. Canon: SiriusDecisions / Forrester.
4. **"What is the marginal ROI of the next dollar in partner vs. direct?"** → Compute diminishing-returns on both. Canon: Tomasz Tunguz.
5. **"What's your MDF-to-attributable-pipeline ratio?"** → Target <5:1. Canon: Jay McBain (Canalys).
6. **"Is channel-mix dogma blocking a profitable segment?"** → Mix should follow segment math. Canon: MIT Sloan.
7. **"Is overhead allocation consistent across channels?"** → Same methodology, both channels. Canon: Horngren.

## Anti-Patterns

- **"Influenced" ≠ "sourced"** — Loading influenced deals as partner revenue inflates partner ROI and direct CAC simultaneously
- **Inconsistent overhead allocation** — The #1 anti-pattern in channel economics
- **Ignoring enablement time** — Every hour your AE co-sells with a partner is a direct cost charged to partner channel
- **MDF without ROI tracking** — MDF without attributable pipeline ROI is partner-discount theatre
- **Channel-mix dogma** — "We're partner-first" blocks profitable segments
- **No retention differential** — Partner-sourced customers often churn differently; ignoring it overstates LTV by 30-50%

## Distinct From

| Neighbor | Difference |
|---|---|
| `partnerships-architect` | Designs partner program structure; this quantifies whether it pays for itself |
| `revenue-operations` | Owns funnel mechanics; this loads channel-level economic outcome |
| `financial-analysis` | Historical close; this is forward-looking decision support |
| `deal-desk` | Per-deal discount; this operates quarterly |
| `pricing-strategist` | Sets price; this analyzes economics across channels at that price |
