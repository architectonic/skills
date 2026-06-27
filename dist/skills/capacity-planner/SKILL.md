---
name: Capacity Planner — Ops Team Sizing with Erlang-C Queueing Theory
description: Size ops capacity for teams that handle queued work (Support, CX, CS,
  BizOps, IT ops, Finance ops). Erlang-C queueing math, P90 demand sizing, shrinkage-adjusted
  FTE, manager-trigger thresholds, and quarterly hiring sequence with ramp + attrition.
  Produces capacity sizing at multiple utilization levels, per-member utilization
  health, and a 12-month hiring plan.
version: 1.0.0
source: claude-skills/business-operations/capacity-planner (MIT)
author: claude-code-skills (distilled by Agent-Memory-Ops-Kit)
tags:
- software-engineering
- productivity
- bizops
- capacity
- headcount
- utilization
- queueing-theory
- ops-planning
- workforce
- okf
type: Playbook
title: Capacity Planner — Ops Team Sizing with Erlang-C Queueing Theory
domain: software-engineering
risk_level: medium
requires_review: true
source_family: amok-native
source_status: adapted
---

# Capacity Planner — Ops Team Sizing with Erlang-C Queueing Theory

Sizing tool for **ops teams that handle queued work** — Support, CX, Customer Success, BizOps, IT ops, Finance ops. Built on Erlang-C queueing theory, Little's Law, and the operational-leadership canon (Fournier, Larson, Cleveland, Reinertsen).

## Purpose

You are an ops leader sized 15 → 35 with no idea how the 35-person org will actually behave at peak load. Or you are at 88% utilization and SLA is starting to slip. Or you have a hiring budget approved and need to sequence it across four quarters without burning out the existing team. This skill answers those questions with arithmetic, not vibes.

It produces three artifacts:

1. **Capacity sizing** at 70/80/90% utilization against P50/P90/P99 demand, with P(SLA breach) at each point and a SAFE/WATCH/AT_RISK/CRITICAL risk band.
2. **Utilization health** at the per-member traffic-light level plus a team verdict (HEALTHY/SQUEEZED/OVERLOADED/UNBALANCED).
3. **12-month quarterly hiring plan** accounting for ramp curves, attrition, QoQ demand growth, and span-of-control manager triggers.

## When to use

- **Annual ops capacity planning** (October-November for the following fiscal year).
- Sustained team utilization is above 80%.
- Team is growing >50% in 12 months.
- SLA is slipping and you need to quantify the gap.
- Hiring budget approved but sequence is unclear.

## NOT for

- Engineering capacity (DORA + cycle time) → use engineering capacity planning.
- Strategic 3-year workforce planning → use HR/strategic planning.
- System reliability SLO design → use SLO/SLI skills.

## Key Concepts

### Erlang-C Model

The Erlang-C formula calculates the probability that an arriving request must wait in queue (i.e., all agents are busy):

```
P(wait) = (A^N / N!) * (N / (N - A)) / [Σ(k=0 to N-1) A^k/k! + (A^N/N!) * (N/(N-A))]
```

Where:
- **A** = offered load (arrival rate × average handle time)
- **N** = number of agents

This gives you the probability of SLA breach at any given staffing level.

### Utilization Risk Bands

| Utilization | Risk Band | Meaning |
|------------|-----------|---------|
| < 70% | SAFE | Room for demand spikes |
| 70–80% | WATCH | Healthy but monitor |
| 80–90% | AT RISK | SLA degradation likely at P90+ |
| > 90% | CRITICAL | SLA breaches imminent |

### Little's Law

```
L = λW
```
- **L** = average number of items in the system
- **λ** = arrival rate
- **W** = average time in the system

Throughput = (agents × utilization) / average handle time

## Workflow

1. **Intake demand profile**: Arrival rate (requests/day), average handle time, current team size, SLA target (e.g., 80% of requests answered in 20 seconds).
2. **Size capacity**: Compute agents needed at P50, P90, P99 demand for 70/80/90% utilization.
3. **Assess health**: Score each current member's utilization. Flag OVERLOADED individuals.
4. **Build hiring plan**: Sequence hires across quarters accounting for ramp (new hire reaches full productivity in 2-3 months), attrition (industry average 10-15% annually), and manager span-of-control triggers (new manager needed when team exceeds 8-10 direct reports).

## Source

Distilled from `claude-skills/business-operations/skills/capacity-planner/SKILL.md` (claude-code-skills, MIT).
Adapted for Hermes Agent — removed Claude Code-specific tool references.
