---
name: market-research-methodology
title: Market Research Methodology
description: 'Upstream market research: market sizing, survey/sampling design, and
  segmentation. The discipline is **method + assumptions**: a TAM is never a single
  number, a survey is never powered only in aggregate, and a segment is never a demographic
  slice.'
type: Playbook
domain: research
tags:
- research
- okf
risk_level: medium
requires_review: false
---

# Market Research Methodology

Upstream market research: market sizing, survey/sampling design, and segmentation. The discipline is **method + assumptions**: a TAM is never a single number, a survey is never powered only in aggregate, and a segment is never a demographic slice.

## Core Tools

1. **Market Sizer** — Computes TAM/SAM/SOM by both top-down and bottoms-up methods side-by-side, reports divergence, flags failed triangulation
2. **Sample Size Planner** — Survey sample size with finite-population correction and per-segment minimums
3. **Segmentation Scorer** — Scores candidate segments against Kotler's 5 criteria with substantiality + accessibility gates

## Workflow

1. **Write the brief** — Objective, decision this informs, sizing approach, sampling plan, assumptions register
2. **Size the market** — Both top-down AND bottoms-up. Reconcile the delta before quoting anything
3. **Plan the survey** — Fund per-segment floors, not just the overall n
4. **Score the segments** — Drop segments failing substantiality/accessibility gates
5. **Assemble evidence pack** — Every number carries its method + assumptions + confidence

## Forcing Questions (one at a time)

1. **"Is your TAM top-down or bottoms-up — computed both ways?"** → Both; reconcile the delta. Canon: Bessemer / a16z market-sizing.
2. **"What decision will this market size drive — at what precision?"** → Size to the decision's tolerance, not spurious precision.
3. **"What's your margin of error and confidence — per segment?"** → Power each reported segment, not only the total. Canon: Cochran; AAPOR.
4. **"Are survey questions free of leading/double-barreled wording?"** → Pre-test wording. Canon: Schuman & Presser; Dillman.
5. **"Do segments pass measurable/substantial/accessible/actionable?"** → Drop those that fail. Canon: Kotler.

## Anti-Patterns

- **A single TAM number with no method** — Always triangulate
- **Spurious precision** — "$3.7142B" implies confidence you don't have
- **Powering only the total** — Each reported segment needs its own sample floor
- **Leading survey questions** — Pre-test wording against bias literature
- **Demographic slices as segments** — Must be substantial AND accessible

## Distinct From

| Neighbor | Difference |
|---|---|
| `marketing-skill/campaign-analytics` | That measures deployed spend; this is upstream methodology |
| `marketing-skill/marketing-demand-acquisition` | That runs acquisition; this builds the evidence |
| `commercial/pricing-strategist` | That sets price; this sizes the market |
| `product-research` | That studies users; this studies the market |
