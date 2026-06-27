---
name: product-research-methodology
title: Product Research Methodology
description: 'Product/user research as operational discipline: choosing the right
  method, sizing it honestly, and synthesizing findings into governed insights. Core
  rule: **method must match the goal**, and **an insight requires recurrence across
  independent participants**.'
type: Playbook
domain: research
tags:
- research
- okf
risk_level: medium
requires_review: true
---

# Product Research Methodology

Product/user research as operational discipline: choosing the right method, sizing it honestly, and synthesizing findings into governed insights. Core rule: **method must match the goal**, and **an insight requires recurrence across independent participants**.

## Core Tools

1. **Study Designer** — Maps (research goal × product stage) to appropriate method and plan skeleton
2. **Saturation Planner** — Method-based sample guidance with explicit confidence label (Nielsen 5/segment, Guest ~12 thematic, evaluative coverage)
3. **Insight Synthesizer** — Clusters coded observations, counts distinct participants, flags singletons as ANECDOTE

## Workflow

1. **Frame the study** — Research questions, method rationale, participant criteria, analysis plan, repository tagging scheme
2. **Pick the method** — Match goal (discovery/evaluative/validation) to stage (concept/prototype/beta/live)
3. **Size it** — Method-based n with stated confidence. Never claim prevalence from small-n usability tests
4. **Synthesize** — Code observations, cluster by tag, require ≥3 independent sources for INSIGHT
5. **File in repository** — Tag to atomic schema at synthesis time with evidence and confidence

## Forcing Questions (one at a time)

1. **"Generative (discover problems) or evaluative (test a solution)?"** → Name it first; the method follows. Canon: Rohrer (NN/g).
2. **"What's your sample size and saturation rationale — at what confidence?"** → Method-based n (5/segment usability; ~12 thematic). Canon: Nielsen; Guest et al.
3. **"How many independent participants support each insight?"** → Require ≥3 sources; flag singletons. Canon: atomic research / Braun & Clarke.
4. **"Are tasks framed as outcomes (jobs) or feature reactions?"** → Frame around job-to-be-done and recent real behavior. Canon: Christensen JTBD; Portigal.
5. **"Where does this land in the repository, and how is it tagged?"** → Tag to atomic schema at synthesis time. Canon: Tomer Sharon Polaris.

## Anti-Patterns

- **Mismatching method to goal** — Usability tests can't discover unmet needs; interviews can't measure task success
- **Reporting usability problems as percentages** — Small-n tests surface problems, not population rates
- **Promoting an anecdote to an insight** — One participant is a signal to probe, not a finding
- **Framing questions as feature reactions** — Probe the job and recent behavior, not hypothetical opinions
- **Synthesizing without a repository scheme** — Tag at synthesis time or insights rot unfindable

## Distinct From

| Neighbor | Difference |
|---|---|
| `product-team/ux-researcher-designer` | That produces artifacts; this is method + repository discipline |
| `product-team/product-discovery` | That plans discovery sprints; this designs and synthesizes research |
| `product-team/experiment-designer` | That runs live A/B; this runs qualitative/evaluative research |
| `market-research` | That studies the market; this studies users |
