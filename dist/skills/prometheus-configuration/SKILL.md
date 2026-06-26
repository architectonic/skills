---
name: prometheus-configuration
description: Set up Prometheus for comprehensive metric collection, storage, and monitoring. Use when implementing metrics collection, setting up monitoring infrastructure, configuring recording rules, or designing alert rules.
type: Metric
---

# Prometheus Configuration

> Source: SWE-Skills-Bench — `skills/prometheus-configuration/SKILL.md`

Complete guide to Prometheus setup, metric collection, scrape configuration, and recording rules.

## When to Use

- Setting up Prometheus monitoring
- Configuring metric scraping
- Creating recording rules and alert rules
- Implementing service discovery
- Designing monitoring infrastructure

## Installation

### Docker Compose

```yaml
services:
  prometheus:
    image: prom/prometheus:latest
    ports: ["9090:9090"]
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus-data:/prometheus
    command:
      - "--config.file=/etc/prometheus/prometheus.yml"
      - "--storage.tsdb.retention.time=30d"
```

### Kubernetes (Helm)

```bash
helm install prometheus prometheus-community/kube-prometheus-stack \
  --namespace monitoring --create-namespace \
  --set prometheus.prometheusSpec.retention=30d
```

## Core Configuration

```yaml
global:
  scrape_interval: 15s
  evaluation_interval: 15s
  external_labels:
    cluster: "production"

alerting:
  alertmanagers:
    - static_configs: [{targets: ["alertmanager:9093"]}]

rule_files:
  - /etc/prometheus/rules/*.yml

scrape_configs:
  - job_name: "prometheus"
    static_configs: [{targets: ["localhost:9090"]}]

  - job_name: "my-app"
    static_configs: [{targets: ["app1:9090"]}]
    metrics_path: "/metrics"
```

## Service Discovery Patterns

### Kubernetes Pods

```yaml
- job_name: "kubernetes-pods"
  kubernetes_sd_configs: [{role: pod}]
  relabel_configs:
    - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
      action: keep
      regex: true
    - source_labels: [__meta_kubernetes_namespace]
      target_label: namespace
    - source_labels: [__meta_kubernetes_pod_name]
      target_label: pod
```

### File-based Service Discovery

```yaml
- job_name: "file-sd"
  file_sd_configs:
    - files: ["/etc/prometheus/targets/*.json"]
      refresh_interval: 5m
```

## Recording Rules

```yaml
# /etc/prometheus/rules/recording_rules.yml
groups:
  - name: api_metrics
    interval: 15s
    rules:
      - record: job:http_requests:rate5m
        expr: sum by (job) (rate(http_requests_total[5m]))
      - record: job:http_requests_error_rate:ratio
        expr: job:http_requests_errors:rate5m / job:http_requests:rate5m
      - record: job:http_request_duration:p95
        expr: histogram_quantile(0.95,
          sum by (job, le) (rate(http_request_duration_seconds_bucket[5m])))
```

## Alert Rules

```yaml
groups:
  - name: availability
    rules:
      - alert: ServiceDown
        expr: up == 0
        for: 1m
        labels: {severity: critical}
        annotations:
          summary: "Service {{ $labels.instance }} is down"

      - alert: HighErrorRate
        expr: job:http_requests_error_rate:ratio > 0.05
        for: 5m
        labels: {severity: warning}
        annotations:
          summary: "Error rate {{ $value | humanizePercentage }} exceeds 5%"

      - alert: HighLatency
        expr: job:http_request_duration:p95 > 1
        for: 5m
        labels: {severity: warning}
```

## Validation

```bash
promtool check config prometheus.yml
promtool check rules /etc/prometheus/rules/*.yml
```

## Best Practices

1. Use consistent metric naming (prefix_name_unit)
2. Set appropriate scrape intervals (15-60s typical)
3. Use recording rules for expensive queries
4. Implement high availability (multiple Prometheus instances)
5. Configure retention based on storage capacity
6. Use relabeling for metric cleanup
7. Monitor Prometheus itself
8. Use Thanos/Cortex for long-term storage
9. Document custom metrics
10. Set `for:` duration on alerts to avoid flapping
