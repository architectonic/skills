---
name: Systematic Performance Profiling
description: Systematic performance profiling for Node.js, Python, and Go applications. Identifies CPU, memory, and I/O bottlenecks, generates flamegraphs, analyzes bundle sizes, optimizes database queries, runs load tests.
tags: [software-development, performance, profiling, flamegraph, node, python, go, load-testing]
type: Playbook
---

# Performance Profiler

**Tier:** POWERFUL
**Category:** Engineering
**Domain:** Performance Engineering

Systematic performance profiling for Node.js, Python, and Go applications. Identifies CPU, memory, and I/O bottlenecks; generates flamegraphs; analyzes bundle sizes; detects memory leaks; and runs load tests with k6 and Artillery. Always measures before and after.

## Source

Distilled from claude-skills (`.gemini/skills/performance-profiler`), MIT license.

## When to Use

- App is slow and you don't know where the bottleneck is
- P99 latency exceeds SLA before a release
- Memory usage grows over time (suspected leak)
- Bundle size increased after adding dependencies
- Preparing for a traffic spike (load test before launch)
- Database queries taking >100ms

## Golden Rule: Measure First

```bash
# Establish baseline BEFORE any optimization
# Record: P50, P95, P99 latency | RPS | error rate | memory usage

# Wrong: "I think the N+1 query is slow, let me fix it"
# Right: Profile → confirm bottleneck → fix → measure again → verify improvement
```

## Core Capabilities

- **CPU profiling** — flamegraphs for Node.js, py-spy for Python, pprof for Go
- **Memory profiling** — heap snapshots, leak detection, GC pressure
- **Bundle analysis** — webpack-bundle-analyzer, Next.js bundle analyzer
- **Database optimization** — EXPLAIN ANALYZE, slow query log, N+1 detection
- **Load testing** — k6 scripts, Artillery scenarios, ramp-up patterns
- **Before/after measurement** — establish baseline, profile, optimize, verify

## Quick Start

```bash
# Analyze a project for performance risk indicators
python3 scripts/performance_profiler.py /path/to/project

# JSON output for CI integration
python3 scripts/performance_profiler.py /path/to/project --json

# Custom large-file threshold
python3 scripts/performance_profiler.py /path/to/project --large-file-threshold-kb 256
```

## Node.js Profiling

→ See references for details on:
- CPU: `0x`, `clinic flame`, `--inspect` + Chrome DevTools
- Memory: `--inspect` + Heap Snapshots, `clinic heap`
- Load testing: k6 ramp-up patterns, Artillery scenarios

## Python Profiling

→ See references for details on:
- CPU: `py-spy record`, `cProfile`, `line_profiler`
- Memory: `tracemalloc`, `objgraph`, `memory_profiler`
- Load testing: Locust, k6 as external runner

## Go Profiling

→ See references for details on:
- CPU: `pprof` tool, `runtime/pprof` package
- Memory: `pprof -inuse_space`, `pprof -alloc_space`
- Load testing: `vegeta`, `k6` as external runner

## Optimization Playbook (from references)

1. **Database first** — N+1 queries, missing indexes, slow joins
2. **Bundle size** — code splitting, tree shaking, dynamic imports
3. **API calls** — batching, caching, connection pooling
4. **Node.js** — event loop blocking, memory leaks, GC pressure
5. **Load test** — verify improvements hold under load

## Cross-References

- Related: `software-development/performance-optimization` — broader performance patterns
- Related: `devops/slo-architect` — SLA/SLO context for performance targets
- Related: `software-development/python-performance-optimization` — Python-specific deep dive
