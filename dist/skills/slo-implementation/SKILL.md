---
name: SLO Implementation
description: Define and implement Service Level Indicators (SLIs) and Service Level Objectives (SLOs) with error budgets and alerting. Use when establishing reliability targets, implementing SRE practices, or measuring service performance.
source: SWE-Skills-Bench (SWE-Skills-Bench/skills/slo-implementation/SKILL.md)
license: MIT
tags: [devops, slo, sli, sre, reliability, error-budget, prometheus, alerting]
type: Playbook
---

# SLO Implementation

Framework for defining and implementing Service Level Indicators (SLIs), Service Level Objectives (SLOs), and error budgets.

## When to Use

- Define service reliability targets
- Measure user-perceived reliability
- Implement error budgets
- Create SLO-based alerts
- Track reliability goals

## SLI/SLO/SLA Hierarchy

```
SLA (Service Level Agreement) — Contract with customers
  ↓
SLO (Service Level Objective) — Internal reliability target
  ↓
SLI (Service Level Indicator) — Actual measurement
```

## Defining SLIs

### Availability SLI

```promql
sum(rate(http_requests_total{status!~"5.."}[28d]))
/
sum(rate(http_requests_total[28d]))
```

### Latency SLI

```promql
sum(rate(http_request_duration_seconds_bucket{le="0.5"}[28d]))
/
sum(rate(http_request_duration_seconds_count[28d]))
```

### Durability SLI

```
sum(storage_writes_successful_total) / sum(storage_writes_total)
```

## Setting SLO Targets

| SLO %  | Downtime/Month | Downtime/Year |
|--------|----------------|---------------|
| 99%    | 7.2 hours      | 3.65 days     |
| 99.9%  | 43.2 minutes   | 8.76 hours    |
| 99.95% | 21.6 minutes   | 4.38 hours    |
| 99.99% | 4.32 minutes   | 52.56 minutes |

## Error Budget

```
Error Budget = 1 - SLO Target

Example: SLO 99.9% → Error Budget 0.1% = 43.2 min/month
```

### Error Budget Policy

```yaml
error_budget_policy:
  - remaining_budget: 100%
    action: Normal development velocity
  - remaining_budget: 50%
    action: Consider postponing risky changes
  - remaining_budget: 10%
    action: Freeze non-critical changes
  - remaining_budget: 0%
    action: Feature freeze, focus on reliability
```

## Prometheus Recording Rules

```yaml
groups:
  - name: sli_rules
    interval: 30s
    rules:
      - record: sli:http_availability:ratio
        expr: |
          sum(rate(http_requests_total{status!~"5.."}[28d]))
          / sum(rate(http_requests_total[28d]))

      - record: sli:http_latency:ratio
        expr: |
          sum(rate(http_request_duration_seconds_bucket{le="0.5"}[28d]))
          / sum(rate(http_request_duration_seconds_count[28d]))

  - name: slo_rules
    interval: 5m
    rules:
      - record: slo:http_availability:error_budget_remaining
        expr: (sli:http_availability:ratio - 0.999) / (1 - 0.999) * 100
```

## SLO Alerting Rules (Multi-Window Burn Rate)

```yaml
groups:
  - name: slo_alerts
    rules:
      # Fast burn: 14.4x rate
      - alert: SLOErrorBudgetBurnFast
        expr: |
          slo:http_availability:burn_rate_1h > 14.4
          and slo:http_availability:burn_rate_5m > 14.4
        for: 2m
        labels:
          severity: critical

      # Slow burn: 6x rate
      - alert: SLOErrorBudgetBurnSlow
        expr: |
          slo:http_availability:burn_rate_6h > 6
          and slo:http_availability:burn_rate_30m > 6
        for: 15m
        labels:
          severity: warning
```

## SLO Dashboard Queries

```promql
# Current SLO compliance
sli:http_availability:ratio * 100

# Error budget remaining
slo:http_availability:error_budget_remaining

# Days until budget exhausted
(slo:http_availability:error_budget_remaining / 100) * 28
/ (1 - sli:http_availability:ratio) * (1 - 0.999)
```

## SLO Review Process

- **Weekly**: Current compliance, error budget status, trend analysis
- **Monthly**: SLO achievement, error budget usage, incident postmortems
- **Quarterly**: SLO relevance, target adjustments, process improvements

## Best Practices

1. Start with user-facing services
2. Use multiple SLIs (availability, latency, etc.)
3. Set achievable SLOs (don't aim for 100%)
4. Implement multi-window alerts to reduce noise
5. Track error budget consistently
6. Review SLOs regularly
7. Document SLO decisions
8. Align with business goals
9. Automate SLO reporting
10. Use SLOs for prioritization
