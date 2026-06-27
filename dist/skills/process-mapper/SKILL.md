---
name: Process Mapper — BPMN Documentation and Bottleneck Analysis
description: Document end-to-end business processes in BPMN-style notation, measure
  cycle times by stage, surface where work spends most of its time waiting vs. being
  worked, and quantify the gap between processing time and total elapsed time. Pairs
  Lean / Six Sigma / Theory-of-Constraints with deterministic analysis to produce
  a process map, ranked bottleneck list, and cycle-time analysis (P50, P90, value-add
  ratio, Little's Law throughput).
version: 1.0.0
source: claude-skills/business-operations/process-mapper (MIT)
author: claude-code-skills (distilled by Agent-Memory-Ops-Kit)
tags:
- agent-operations
- productivity
- bizops
- process
- bpmn
- bottleneck
- cycle-time
- lean
- six-sigma
- value-stream
- okf
type: Playbook
title: Process Mapper — BPMN Documentation and Bottleneck Analysis
domain: agent-operations
risk_level: medium
requires_review: true
source_family: amok-native
source_status: adapted
---

# Process Mapper — BPMN Documentation and Bottleneck Analysis

BPMN-style business process documentation, bottleneck detection, and cycle-time analysis for internal-operations leaders.

## Purpose

Internal-operations work suffers from three recurring failure modes:

1. **Implicit process** — steps exist only in tribal knowledge, handoffs drop, onboarding takes weeks.
2. **Invisible waiting** — most elapsed time is queue/wait/approval, not actual work; teams optimize the wrong stage.
3. **Local optimization** — Goldratt's Theory of Constraints is ignored; resources added to non-constraint stages gain nothing.

This skill produces a documented process map, identifies where work waits, and points to the constraint by name.

## When to use

- Documenting a new business process (procurement, onboarding, incident handoff, expense reimbursement, customer onboarding).
- An existing process is "too slow" but nobody can name the bottleneck.
- Cycle time is being measured but value-add ratio is not.
- Cross-functional handoffs are dropping work and root cause is unclear.

## Process Stage Types

Every stage in a process map must be classified as:

| Type | Description | Optimization approach |
|------|-------------|----------------------|
| **value-add** | Directly transforms the work product | Optimize for speed |
| **wait** | Work sits in a queue, awaiting approval or resource | Eliminate or parallelize |
| **rework** | Work loops back due to defects or rejection | Root-cause the defect source |

## Cycle-Time Health Bands

| VA% (value-add ratio) | Verdict | Meaning |
|----------------------|---------|---------|
| > 25% | HEALTHY | Most time is spent on real work |
| 10–25% | TYPICAL | Normal for cross-functional processes |
| < 10% | WASTE-HEAVY | Most time is waiting — constraint is the queue |

## Workflow

1. **Intake**: Capture the process as structured data with one entry per stage: `name`, `owner`, `type` (value-add | wait | rework), `duration_minutes_p50`, `duration_minutes_p90`.

2. **Map stages**: Produce an ASCII swim-lane diagram separated by owner so cross-functional handoffs become visible.

3. **Measure cycle time**: Compute total P50, total P90, value-add ratio (VA%), and Little's-Law throughput estimate.

4. **Detect bottlenecks**: Rank by severity (CRITICAL / HIGH / MEDIUM) with root-cause hypothesis and one recommended action per finding.

5. **Recommend**: Pair the bottleneck list with the cycle-time verdict. Recommend a single constraint-focused intervention per Goldratt's "subordinate everything to the constraint" rule. Don't recommend optimization of a non-constraint stage.

## Theory of Constraints — Five Focusing Steps

1. **Identify** the constraint (the stage that limits throughput).
2. **Exploit** the constraint (maximize its utilization before adding capacity).
3. **Subordinate** everything else to the constraint (don't optimize non-constraints).
4. **Elevate** the constraint (add capacity only after steps 1–3 are complete).
5. **Repeat** — the constraint will move; don't let inertia become the new constraint.

## Source

Distilled from `claude-skills/business-operations/skills/process-mapper/SKILL.md` (claude-code-skills, MIT).
Adapted for Hermes Agent — removed Claude Code-specific tool references.
