---
name: performance-engineer
title: Performance Engineer
description: '1. **Establish Baseline**: Measure current performance with real user
  monitoring 2. **Identify Bottlenecks**: Use profiling, distributed tracing, and
  load testing 3. **Prioritize Optimizations**: Based on user impact, business value,
  and effort'
type: Playbook
domain: software-engineering
tags:
- software-engineering
- okf
risk_level: medium
requires_review: true
---

# Performance Engineer

## When to Use
- Diagnosing performance bottlenecks in backend, frontend, or infrastructure
- Designing load tests, capacity plans, or scalability strategies
- Setting up observability and performance monitoring
- Optimizing latency, throughput, or resource efficiency
- Implementing caching architectures
- Establishing performance budgets and regression detection

## When NOT to Use
- Feature development with no performance goals
- No access to metrics, traces, or profiling data
- Quick, non-technical summary is the only requirement

## Performance Engineering Workflow

1. **Establish Baseline**: Measure current performance with real user monitoring
2. **Identify Bottlenecks**: Use profiling, distributed tracing, and load testing
3. **Prioritize Optimizations**: Based on user impact, business value, and effort
4. **Implement Changes**: With proper testing and validation procedures
5. **Set Guardrails**: Performance budgets, monitoring, and alerting
6. **Validate Improvements**: Through comprehensive testing and user experience measurement
7. **Plan for Scalability**: With appropriate caching and architectural improvements

## Observability Stack

### Distributed Tracing
- **OpenTelemetry**: Vendor-neutral instrumentation, propagation, and collection
- **Jaeger / Tempo**: Trace visualization and analysis
- **Key headers**: `traceparent`, `tracestate` (W3C Trace Context)

### Metrics & Monitoring
- **Prometheus**: Time-series metrics, alerting rules, service discovery
- **Grafana**: Dashboards, alerting, multi-source data fusion
- **RED Metrics**: Rate, Errors, Duration (for services)
- **USE Metrics**: Utilization, Saturation, Errors (for resources)

### Real User Monitoring (RUM)
- **Core Web Vitals**: LCP (Largest Contentful Paint), FID (First Input Delay), CLS (Cumulative Layout Shift)
- **Synthetic Monitoring**: Automated uptime checks, API testing, user journey simulation

## Load Testing

### Tools by Use Case
| Tool | Best For |
|---|---|
| k6 | Modern load testing, scripting in JS, CI/CD integration |
| Locust | Python-based, distributed, programmable |
| Gatling | High-throughput, Scala-based, detailed reports |
| JMeter | Mature, GUI-based, extensive plugin ecosystem |
| Artillery | Quick API load tests, YAML configuration |

### Load Testing Strategy
1. **Smoke Test**: 1-2 VUs, verify script works
2. **Load Test**: Expected traffic levels, find baseline
3. **Stress Test**: Beyond expected capacity, find breaking point
4. **Soak Test**: Sustained load over hours, find memory leaks
5. **Spike Test**: Sudden traffic surge, test auto-scaling

## Multi-Tier Caching

### Cache Layers (fastest → slowest)
1. **Browser Cache**: HTTP cache headers, service workers
2. **CDN Cache**: CloudFlare, CloudFront, edge computing
3. **API Gateway Cache**: Rate limiting, response caching
4. **Application Cache**: In-memory (computed values, session data)
5. **Distributed Cache**: Redis, Memcached, Hazelcast
6. **Database Cache**: Query result cache, connection pooling, buffer pool

### Cache Invalidation Strategies
- **TTL-based**: Time-to-live expiration (simple, eventual consistency)
- **Event-driven**: Invalidate on data write (more consistent)
- **Write-through**: Write to cache and DB simultaneously
- **Write-behind**: Write to cache, async write to DB (fast, risk of loss)
- **Cache-aside**: Application manages cache reads/writes

### Stampede Prevention
- **Locking**: Only one request recomputes when cache expires
- **Early recomputation**: Refresh TTL before expiration
- **Probabilistic early expiration**: Randomized TTL jitter

## Frontend Performance

### Core Web Vitals Optimization
- **LCP**: Optimize largest image/font, use preload, reduce server response time
- **FID**: Minimize main thread work, break up long tasks (>50ms)
- **CLS**: Set dimensions for images/videos, avoid dynamic content injection

### Resource Optimization
- Image optimization (WebP, AVIF, responsive images, lazy loading)
- JavaScript bundle splitting, tree shaking, code splitting
- CSS optimization (critical CSS, eliminate render-blocking)
- HTTP/2, HTTP/3, resource hints (preload, prefetch, preconnect)

## Backend Performance

### API Optimization
- Response time optimization (< 200ms target for APIs)
- Pagination (cursor-based for large datasets)
- Bulk operations (reduce round trips)
- Async processing (background jobs, message queues)

### Database Performance
- Query optimization (EXPLAIN ANALYZE, index tuning)
- Connection pooling (PgBouncer, ProxySQL)
- Read replicas for read-heavy workloads
- Partitioning for large tables

### Concurrency
- Thread pool tuning
- Async/await patterns
- Lock-free data structures where possible
- Backpressure mechanisms

## Cloud & Infrastructure Performance

### Auto-Scaling
- HPA (Horizontal Pod Autoscaler) for Kubernetes
- VPA (Vertical Pod Autoscaler) for right-sizing
- Cluster Autoscaler for node scaling
- Custom metrics for application-specific scaling

### Serverless
- Cold start optimization (keep warm, reduce package size)
- Memory allocation tuning (CPU scales with memory)
- Provisioned concurrency for latency-sensitive functions

### Container Optimization
- Docker image optimization (multi-stage builds, distroless)
- Kubernetes resource limits and requests
- Pod disruption budgets for availability

## Performance Budgets

### Setting Budgets
- **Timing budgets**: Max response time per endpoint (e.g., p95 < 200ms)
- **Resource budgets**: Max CPU/memory per service
- **Bundle budgets**: Max JS/CSS bundle size
- **Request budgets**: Max number of API calls per page load

### CI/CD Integration
- Automated performance testing in CI pipeline
- Deployment blocking on budget violations
- Trend analysis and regression detection
- Lighthouse CI for frontend budgets

## SRE Practices

### SLI/SLO Framework
- **SLI** (Service Level Indicator): What you measure (e.g., request latency)
- **SLO** (Service Level Objective): Target value (e.g., p99 < 500ms)
- **Error Budget**: Acceptable failure rate (e.g., 0.1% over 30 days)

### Alerting
- Symptom-based alerting (on SLO burn rate, not on causes)
- Multi-window burn rate alerts (short window + long window)
- Alert fatigue reduction (group related alerts, actionable only)

## Anti-Patterns
- Optimizing without measuring (premature optimization)
- Ignoring the 90/10 rule (focus on the 10% causing 90% of latency)
- Caching everything (cache invalidation complexity)
- Load testing in production without safeguards
- Setting performance budgets without team buy-in

## Related Skills
- `software-development/performance-optimization.md` — algorithmic improvements
- `devops/slo-implementation.md` — SLI/SLO/Prometheus recording rules
- `devops/cache-strategy.md` — caching patterns
- `devops/rate-limiter.md` — API rate limiting
- `devops/error-monitoring.md` — error log analysis
