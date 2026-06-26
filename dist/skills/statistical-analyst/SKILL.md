---
name: statistical-analyst
description: Run hypothesis tests, analyze A/B experiment results, calculate sample sizes, and interpret statistical significance with effect sizes. Use when you need to validate whether observed differences are real, size an experiment correctly before launch, or interpret test results with confidence. Triggers on: A/B test, hypothesis test, statistical significance, p-value, confidence interval, sample size, effect size, experiment design, chi-square, t-test, z-test.
tags: [data-science, statistics, ab-testing, hypothesis-testing, experiment-design]
type: Playbook
---

# Statistical Analyst

Expert statistician and data scientist. Help teams make decisions grounded in statistical evidence — not gut feel. Distinguish signal from noise, size experiments correctly before they start, and interpret results with full context: significance, effect size, power, and practical impact.

Treat "statistically significant" and "practically significant" as separate questions and always answer both.

## Entry Points

### Mode 1 — Analyze Experiment Results (A/B Test)
Use when an experiment has already run and you have result data.

1. **Clarify** — Confirm metric type (conversion rate, mean, count), sample sizes, and observed values
2. **Choose test** — Proportions → Z-test; Continuous means → t-test; Categorical → Chi-square
3. **Run** — Execute statistical test (use Python scripts or manual calculation)
4. **Interpret** — Report p-value, confidence interval, effect size (Cohen's d / Cohen's h / Cramér's V)
5. **Decide** — Ship / hold / extend using the decision framework below

### Mode 2 — Size an Experiment (Pre-Launch)
Use before launching a test to ensure it will be conclusive.

1. **Define** — Baseline rate, minimum detectable effect (MDE), significance level (α), power (1−β)
2. **Calculate** — Compute required N per variant
3. **Sanity-check** — Confirm traffic volume can deliver N within acceptable time window
4. **Document** — Lock the stopping rule before launch to prevent p-hacking

### Mode 3 — Interpret Existing Numbers
Use when someone shares a result and asks "is this significant?" or "what does this mean?"

1. Ask for: sample sizes, observed values, baseline, and what decision depends on the result
2. Run the appropriate test
3. Report using the Bottom Line → What → Why → How to Act structure
4. Flag any validity threats (peeking, multiple comparisons, SUTVA violations)

## Test Selection Guide

| Scenario | Metric | Test |
|---|---|---|
| A/B conversion rate (clicked/not) | Proportion | Z-test for two proportions |
| A/B revenue, load time, session length | Continuous mean | Two-sample t-test (Welch's) |
| A/B/C/n multi-variant with categories | Categorical counts | Chi-square |
| Single sample vs. known value | Mean vs. constant | One-sample t-test |
| Non-normal data, small n | Rank-based | Mann-Whitney U (flag for human) |

**When NOT to use these tests:**
- n < 30 per group without checking normality
- Metrics with heavy tails (e.g. revenue with whales) — consider log transform or trimmed mean first
- Sequential / peeking scenarios — use sequential testing or SPRT instead
- Clustered data (e.g. users within countries) — standard tests assume independence

## Decision Framework (Post-Experiment)

| p-value | Effect Size | Practical Impact | Decision |
|---|---|---|---|
| < α | Large / Medium | Meaningful | Ship |
| < α | Small | Negligible | Hold — statistically significant but not worth the complexity |
| ≥ α | — | — | Extend (if underpowered) or Kill |
| < α | Any | Negative UX | Kill regardless |

**Always ask:** "If this effect were exactly as measured, would the business care?" If no — don't ship on significance alone.

## Effect Size Reference

Effect sizes translate statistical results into practical language:

**Cohen's d (means):**
| d | Interpretation |
|---|---|
| < 0.2 | Negligible |
| 0.2–0.5 | Small |
| 0.5–0.8 | Medium |
| > 0.8 | Large |

**Cohen's h (proportions):**
| h | Interpretation |
|---|---|
| < 0.2 | Negligible |
| 0.2–0.5 | Small |
| 0.5–0.8 | Medium |
| > 0.8 | Large |

**Cramér's V (chi-square):**
| V | Interpretation |
|---|---|
| < 0.1 | Negligible |
| 0.1–0.3 | Small |
| 0.3–0.5 | Medium |
| > 0.5 | Large |

## Proactive Risk Triggers

Surface these unprompted when you spot the signals:

- **Peeking / early stopping** — Running a test and checking results daily inflates false positive rate. Ask: "Did you look at results before the planned end date?"
- **Multiple comparisons** — Testing 10 metrics at α=0.05 gives ~40% chance of at least one false positive. Flag when > 3 metrics are being evaluated.
- **Underpowered test** — If n is below the required sample size, a non-significant result tells you nothing. Always check power retroactively.
- **SUTVA violations** — If users in control and treatment can interact (e.g. social features, shared inventory), the independence assumption breaks.
- **Simpson's Paradox** — An aggregate result can reverse when segmented. Flag when segment-level results are available.
- **Novelty effect** — Significant early results in UX tests often decay. Flag for post-novelty re-measurement.

## Output Artifacts

| Request | Deliverable |
|---|---|
| "Did our test win?" | Significance report: p-value, CI, effect size, verdict, caveats |
| "How big should our test be?" | Sample size report with power/MDE tradeoff table |
| "What's the confidence interval for X?" | CI report with margin of error and interpretation |
| "Is this difference real?" | Hypothesis test with plain-English conclusion |
| "How long should we run this?" | Duration estimate = (required N per variant) / (daily traffic per variant) |
| "We tested 5 things — what's significant?" | Multiple comparison analysis with Bonferroni-adjusted thresholds |

## Quality Loop

Tag every finding with confidence:

- 🟢 **Verified** — Test assumptions met, sufficient n, no validity threats
- 🟡 **Likely** — Minor assumption violations; interpret directionally
- 🔴 **Inconclusive** — Underpowered, peeking, or data integrity issue; do not act

## Communication Standard

Structure all results as:

**Bottom Line** — One sentence: "Treatment increased conversion by 1.2pp (95% CI: 0.4–2.0pp). Result is statistically significant (p=0.003) with a small effect (h=0.18). Recommend shipping."

**What** — The numbers: observed rates/means, difference, p-value, CI, effect size

**Why It Matters** — Business translation: what does the effect size mean in revenue, users, or decisions?

**How to Act** — Ship / hold / extend / kill with specific rationale

## Python Helper Scripts

Use Python with `scipy` and `statsmodels` for calculations:

```python
# Z-test for two proportions
from statsmodels.stats.proportion import proportions_ztest
count = np.array([250, 310])  # successes
nobs = np.array([5000, 5000])  # total
stat, pval = proportions_ztest(count, nobs)

# Two-sample t-test
from scipy import stats
t_stat, pval = stats.ttest_ind_from_stats(
    mean1=42.3, std1=18.1, nobs1=800,
    mean2=46.1, std2=19.4, nobs2=820,
    equal_var=False  # Welch's t-test
)

# Sample size for proportion test
from statsmodels.stats.power import NormalIndPower
analysis = NormalIndPower()
n = analysis.solve_power(effect_size=0.2, alpha=0.05, power=0.80, ratio=1.0)
```

## Source Attribution

Derived from `claude-skills/engineering/statistical-analyst` (MIT license, Alireza Rezvani / claude-skills project). Adapted for Hermes Agent by removing Claude-specific references and tool invocations.
