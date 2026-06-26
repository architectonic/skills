---
name: SaaS Revenue Operations
description: Analyze sales pipeline health, revenue forecasting accuracy, and go-to-market efficiency metrics for SaaS revenue optimization.
tags: [productivity, revenue, saas, pipeline, forecast, gtm, revops]
type: Metric
---

# Revenue Operations

Analyze sales pipeline health, revenue forecasting accuracy, and go-to-market efficiency metrics for SaaS revenue optimization.

## Source

Distilled from claude-skills (`.gemini/skills/revenue-operations`), MIT license.

## When to Use

- Analyzing sales pipeline coverage and health
- Tracking forecast accuracy with MAPE
- Calculating GTM efficiency metrics (Magic Number, LTV:CAC, Burn Multiple, Rule of 40)
- Preparing weekly pipeline reviews or quarterly business reviews
- Evaluating go-to-market performance and unit economics

## Core Metrics

### Pipeline Metrics

- **Pipeline Coverage Ratio** — Total pipeline value / quota target (healthy: 3-4x)
- **Stage Conversion Rates** — Stage-to-stage progression rates
- **Sales Velocity** — (Opportunities x Avg Deal Size x Win Rate) / Avg Sales Cycle
- **Deal Aging** — Flags deals exceeding 2x average cycle time per stage
- **Concentration Risk** — Warns when >40% of pipeline is in a single deal
- **Coverage Gap Analysis** — Identifies quarters with insufficient pipeline

### Forecast Accuracy

- **MAPE** — mean(|actual - forecast| / |actual|) x 100
- **Forecast Bias** — Over-forecasting (positive) vs under-forecasting (negative) tendency
- **Weighted Accuracy** — MAPE weighted by deal value for materiality

| Rating | MAPE Range | Interpretation |
|--------|-----------|----------------|
| Excellent | <10% | Highly predictable, data-driven process |
| Good | 10-15% | Reliable forecasting with minor variance |
| Fair | 15-25% | Needs process improvement |
| Poor | >25% | Significant forecasting methodology gaps |

### GTM Efficiency

| Metric | Formula | Target |
|--------|---------|--------|
| Magic Number | Net New ARR / Prior Period S&M Spend | >0.75 |
| LTV:CAC | (ARPA x Gross Margin / Churn Rate) / CAC | >3:1 |
| CAC Payback | CAC / (ARPA x Gross Margin) months | <18 months |
| Burn Multiple | Net Burn / Net New ARR | <2x |
| Rule of 40 | Revenue Growth % + FCF Margin % | >40% |
| Net Dollar Retention | (Begin ARR + Expansion - Contraction - Churn) / Begin ARR | >110% |

## Workflows

### Weekly Pipeline Review

1. Verify pipeline export is current and all required fields (stage, value, close_date, owner) are populated.
2. Calculate pipeline metrics (coverage, conversion, velocity, aging, concentration).
3. Review key indicators: coverage ratio >3x, aging deals, concentration risk, stage distribution.
4. Document findings.
5. Action items: address aging deals, redistribute concentration, fill coverage gaps.

### Forecast Accuracy Review (Monthly/Quarterly)

1. Verify all forecast periods have corresponding actuals.
2. Calculate MAPE, bias, and trend.
3. Analyze patterns: improving/declining accuracy, high-bias reps/segments, systematic over/under-forecasting.
4. Document findings.
5. Improvement actions: coach high-bias reps, adjust methodology, improve data hygiene.

### GTM Efficiency Audit (Quarterly/Board Prep)

1. Verify revenue, cost, and customer figures reconcile with finance.
2. Calculate all GTM efficiency metrics.
3. Benchmark against targets (Magic Number >0.75, LTV:CAC >3:1, etc.).
4. Document findings.
5. Strategic decisions: adjust spend allocation, optimize channels, improve retention.

### Quarterly Business Review (Combined)

1. Run pipeline analyzer for forward-looking coverage
2. Run forecast tracker for backward-looking accuracy
3. Run GTM calculator for efficiency benchmarks
4. Cross-reference pipeline health with forecast accuracy
5. Align GTM efficiency metrics with growth targets

## Cross-References

- Related: `productivity/saas-metrics-coach` — broader SaaS financial health
- Related: `productivity/business-finance-fundamentals` — unit economics fundamentals
- Related: `productivity/product-analytics` — product metrics and cohort analysis
