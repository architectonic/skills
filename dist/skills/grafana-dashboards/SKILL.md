---
name: grafana-dashboards
description: Create and manage production Grafana dashboards for real-time visualization of system and application metrics. Use when building monitoring dashboards, visualizing metrics, or creating operational observability interfaces.
type: Metric
---

# Grafana Dashboards

> Source: SWE-Skills-Bench — `skills/grafana-dashboards/SKILL.md`

Design effective Grafana dashboards for monitoring applications, infrastructure, and business metrics.

## When to Use

- Visualizing Prometheus metrics
- Creating custom dashboards
- Implementing SLO dashboards
- Monitoring infrastructure
- Tracking business KPIs

## Design Principles

### Information Hierarchy

```
┌─────────────────────────────────────┐
│  Critical Metrics (Big Numbers)     │  ← Top: at-a-glance status
├─────────────────────────────────────┤
│  Key Trends (Time Series)           │  ← Middle: temporal patterns
├─────────────────────────────────────┤
│  Detailed Metrics (Tables/Heatmaps) │  ← Bottom: drill-down
└─────────────────────────────────────┘
```

### RED Method (Services)

- **Rate** — Requests per second
- **Errors** — Error rate
- **Duration** — Latency/response time

### USE Method (Resources)

- **Utilization** — % time resource is busy
- **Saturation** — Queue length/wait time
- **Errors** — Error count

## Panel Types

### Stat Panel (Single Value with Thresholds)

```json
{
  "type": "stat",
  "title": "Error Rate %",
  "fieldConfig": {
    "defaults": {
      "thresholds": {
        "steps": [
          {"value": 0, "color": "green"},
          {"value": 2, "color": "yellow"},
          {"value": 5, "color": "red"}
        ]
      }
    }
  }
}
```

### Time Series Graph

```json
{
  "type": "graph",
  "title": "P95 Latency",
  "targets": [{
    "expr": "histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket[5m])) by (le, service))"
  }]
}
```

### Heatmap (Latency Distribution)

```json
{
  "type": "heatmap",
  "title": "Latency Heatmap",
  "targets": [{
    "expr": "sum(rate(http_request_duration_seconds_bucket[5m])) by (le)",
    "format": "heatmap"
  }]
}
```

## Dashboard Variables

```json
{
  "templating": {
    "list": [
      {
        "name": "namespace",
        "type": "query",
        "query": "label_values(kube_pod_info, namespace)"
      },
      {
        "name": "service",
        "type": "query",
        "query": "label_values(kube_service_info{namespace=\"$namespace\"}, service)",
        "multi": true
      }
    ]
  }
}
```

Use in queries: `http_requests_total{namespace="$namespace", service=~"$service"}`

## Common Dashboard Patterns

**API Monitoring:** Request rate, error rate %, P50/P95/P99 latency, active connections

**Infrastructure:** CPU/memory/disk per node, pod count by namespace, node status

**Database:** QPS, connection pool, query latency percentiles, replication lag, slow queries

## Dashboard Provisioning as Code

```yaml
# dashboards.yml
apiVersion: 1
providers:
  - name: "default"
    folder: "General"
    type: file
    disableDeletion: false
    options:
      path: /etc/grafana/dashboards
```

### Terraform

```hcl
resource "grafana_dashboard" "api" {
  config_json = file("${path.module}/dashboards/api-monitoring.json")
}
```

## Best Practices

1. Start with Grafana community dashboard templates
2. Use consistent naming for panels and variables
3. Group related metrics in rows
4. Default time range: Last 6 hours
5. Use variables for namespace/service filtering
6. Add panel descriptions for context
7. Configure units correctly (bytes, seconds, percent)
8. Set meaningful thresholds for color coding
9. Use consistent colors across dashboards
10. Test dashboards with different time ranges
