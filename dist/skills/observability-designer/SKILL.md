---
name: Observability Designer — Production Observability Strategy
description: Design production-ready observability strategies combining metrics, logs, and traces. SLI/SLO design, golden-signals monitoring, alert optimization, dashboard generation. Use when adding observability to a new service, refactoring noisy alerting, or designing an SLO program before scaling production load. Complements slo-architect (which handles error-budget math).
version: 1.0.0
source: claude-skills/engineering/observability-designer (MIT)
author: Claude Skills Team (distilled by Agent-Memory-Ops-Kit)
tags: [devops, engineering, observability, monitoring, sli, slo, alerting, dashboard, metrics, traces]
type: Metric
---

# Observability Designer — Production Observability Strategy

Design comprehensive observability strategies for production systems including SLI/SLO frameworks, alerting optimization, and dashboard design.

## When NOT to use

→ **slo-architect**: For SLO/SLI design with error-budget math, multi-window burn-rate alerting thresholds, and SLO review gates. This skill handles dashboard design and alert-noise reduction; slo-architect handles the error-budget math.

## The Three Pillars of Observability

### Metrics
- **Golden Signals**: Latency, traffic, errors, and saturation
- **RED Method**: Rate, Errors, Duration (for request-driven services)
- **USE Method**: Utilization, Saturation, Errors (for resource monitoring)
- **Business Metrics**: Revenue, user engagement, feature adoption

### Logs
- Structured JSON logging with correlation IDs
- Log levels: ERROR (actionable), WARN (investigate), INFO (significant events), DEBUG (development only)
- Never log PII, credentials, or tokens

### Traces
- Distributed tracing with OpenTelemetry
- Span naming: `service.operation` (e.g., `payments.charge`)
- Context propagation across service boundaries
- Sampling: head-based for errors, tail-based for latency analysis

## SLI/SLO Framework Design

### Service Level Indicators (SLI)

Choose measurable signals that indicate service health:

| Service type | Primary SLI | Secondary SLI |
|-------------|------------|---------------|
| API | Request latency (P99) | Error rate |
| Database | Query latency (P95) | Connection pool utilization |
| Queue | Consumer lag | Processing latency |
| Storage | Read/write latency | Availability |

### Service Level Objectives (SLO)

Set reliability targets based on user experience:

| SLO | Availability | Use case |
|-----|-------------|----------|
| 99.9% | 8.76h downtime/year | Standard SaaS |
| 99.95% | 4.38h downtime/year | Business-critical |
| 99.99% | 52.6min downtime/year | Mission-critical |

### Error Budget Management

Error budget = 1 - SLO (e.g., 99.9% SLO = 0.1% error budget)

- Track budget consumption rate (burn rate)
- Multi-window burn rate alerts: fast-burn (1h window) and slow-burn (6h+ window)
- When budget is exhausted: freeze non-critical deployments, focus on reliability

## Alert Optimization Principles

1. **Every alert must be actionable** — if nobody responds, delete the alert
2. **Alert on symptoms, not causes** — "high error rate" not "CPU at 90%"
3. **Use multi-window burn rates** — prevents alert flapping
4. **Deduplicate** — one alert per incident, not one per affected service
5. **Severity must match response** — P1 = page now, P3 = ticket for next sprint

## Dashboard Design

### Layout Principles

1. **Golden signals first** — latency, traffic, errors, saturation at the top
2. **Drill-down hierarchy** → overview → service → endpoint → instance
3. **Red/yellow/green thresholds** — visual SLO compliance at a glance
4. **Correlation panels** — metrics + logs + traces side by side

### Essential Panels

| Panel | Purpose | Data source |
|-------|---------|-------------|
| Request rate | Traffic volume | Metrics |
| Error rate (%) | Health signal | Metrics |
| Latency (P50/P95/P99) | Performance | Metrics |
| Saturation | Resource pressure | Metrics |
| SLO compliance | Reliability status | Metrics + SLO config |
| Top error types | Debugging | Logs |
| Active incidents | Operational awareness | Alerting |

## Workflow

1. **Identify service type** → API / database / queue / storage / batch
2. **Define SLIs** → Choose 2-4 measurable signals
3. **Set SLOs** → Based on user expectations and business requirements
4. **Design dashboards** → Golden signals + drill-down + SLO compliance
5. **Configure alerts** → Multi-window burn rates + symptom-based thresholds
6. **Iterate** → After one on-call rotation, measure actionable-alert ratio. Re-run optimization if ratio didn't improve.

## Source

Distilled from `claude-skills/engineering/skills/observability-designer/SKILL.md` (Claude Skills Team, MIT).
Adapted for Hermes Agent — removed Claude Code-specific tool references.
