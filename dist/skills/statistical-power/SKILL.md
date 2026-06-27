---
name: Statistical Power & Sample Size
description: Sample-size and statistical power calculations for planning studies.
  Use whenever someone asks "how many subjects/samples/replicates do I need", wants
  an a priori power analysis, a minimum detectable effect (MDE), a power curve, or
  needs to justify a sample size for a grant, IRB protocol, or pre-registration. Covers
  closed-form power for t-tests, ANOVA, proportions, correlations, chi-square, and
  regression, plus simulation-based (Monte Carlo) power for designs with no formula.
source: K-Dense-AI/scientific-agent-skills (MIT)
distilled: 2026-06-23
type: Playbook
title: Statistical Power & Sample Size
domain: research
tags:
- research
- okf
risk_level: medium
requires_review: true
source_family: agent-skills-standard
source_status: adapted
---

# Statistical Power & Sample Size

## Overview

Power analysis answers: **how large a sample do you need to reliably detect an effect of a given size?** Four quantities are locked: sample size (n), effect size, significance level (α), and power (1 − β). Fix any three, the fourth is determined.

## When to Use

- Determining required sample size before collecting data (a priori power analysis)
- Finding the minimum detectable effect (MDE) for a fixed sample size
- Producing power curves for a grant or protocol
- Justifying sample size for IRB, grant, or pre-registration
- Powering designs without textbook formulas (mixed models, logistic regression, cluster-randomized trials) via simulation

## The One Decision That Drives Everything: Effect Size

**Do not invent a number.** Use in order of preference:
1. **Minimally important effect** (SESOI) — smallest effect that would change a decision
2. **Pilot/prior-study estimate** — but shrink it (published effects are inflated)
3. **Convention** (Cohen's small/medium/large) — only as last resort, say so explicitly

**Run a sensitivity analysis:** report how required n changes across a plausible range of effect sizes.

**Avoid post-hoc ("observed") power** — it's circular and uninformative.

## Closed-Form Quick Recipes

```python
# Using statsmodels:
from statsmodels.stats.power import TTestIndPower, TTestPower, FTestAnovaPower, NormalIndPower

# Two independent means: n per group for d=0.5, 80% power
analysis = TTestIndPower()
n = analysis.solve_power(effect_size=0.5, power=0.80, alpha=0.05)
# → ~64 per group

# Paired t-test
analysis = TTestPower()
n = analysis.solve_power(effect_size=0.5, power=0.80, alpha=0.05)

# One-way ANOVA (k groups)
analysis = FTestAnovaPower()
n = analysis.solve_power(effect_size=0.25, k_groups=4, power=0.80, alpha=0.05)

# Two proportions
analysis = NormalIndPower()
n = analysis.solve_power(effect_size=0.15, power=0.80, alpha=0.05)  # effect_size = |p1 - p2|
```

## Simulation-Based Power (No Formula)

For logistic/Poisson regression, mixed models, cluster-randomized trials, survival, interactions:

```python
# 1. Simulate dataset from assumed truth
# 2. Analyze with the exact test/model you plan to use
# 3. Repeat ≥1000 times (5000-10000 for stable estimates)
# Power = fraction of replicates where test is significant
```

## Adjustments People Forget

- **Multiple comparisons:** Power at corrected α (e.g. α/m for Bonferroni)
- **Attrition/dropout:** `n_enroll = ceil(n_analyzed / (1 − dropout_rate))`
- **Clustering:** Inflate by design effect `DEFF = 1 + (m − 1)·ICC`
- **Unequal allocation:** Pass ratio parameter

## Reporting Template

```
A priori power analysis was conducted to determine the sample size needed to detect
a [between-group difference of Cohen's d = 0.50], which we considered the smallest
effect of clinical interest. With α = .05 (two-sided) and power = .80, a two-sample
t-test requires n = 64 per group (128 total; computed with statsmodels 0.14).
Allowing for 20% attrition, we will enrol 160 participants. A sensitivity analysis
showed required n ranges from 45 to 105 per group across plausible effects
d = 0.40–0.60 (Figure X).
```

## Common Pitfalls

1. Inventing the effect size or copying an inflated pilot estimate
2. Reporting a single n instead of a sensitivity range/power curve
3. Post-hoc/observed power (circular)
4. Ignoring clustering (pseudoreplication)
5. Forgetting dropout
6. Confusing α with power, or one-sided with two-sided
7. Powering only the primary endpoint while reporting underpowered secondaries
8. Using a t-test formula for a model you won't actually fit

## Attribution

From K-Dense-AI/scientific-agent-skills (MIT), authored by K-Dense Inc.
