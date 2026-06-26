---
name: Orchestrate Batch Refactor
description: Plan and execute large refactor efforts with parallel multi-agent analysis. Use when refactoring many files, splitting workstreams, or coordinating sub-agents for batch code changes.
tags: [agent-operations, refactoring, multi-agent, batch, code-quality]
source: terminal-skills (terminalskills.io)
license: Apache-2.0
distilled: 2026-06-22
type: Playbook
---

# Orchestrate Batch Refactor

## Overview

Run high-throughput refactors safely: analyze scope in parallel, synthesize a single plan, then execute independent work packets with sub-agents.

## When to Use Parallelization

- Use for medium/large scope touching many files or subsystems
- Skip multi-agent execution for tiny edits or highly coupled single-file work

## Core Workflow

1. **Define scope and success criteria.**
   - List target paths/modules and non-goals
   - State behavior constraints (e.g., preserve external behavior)

2. **Run parallel analysis first.**
   - Split target scope into analysis lanes
   - Spawn `explorer` sub-agents in parallel to analyze each lane
   - Ask each agent for: intent map, coupling risks, candidate work packets, required validations

3. **Build one dependency-aware plan.**
   - Merge explorer output into a single work graph
   - Create work packets with clear file ownership and validation commands
   - Sequence packets by dependency level; run only independent packets in parallel

4. **Execute with worker agents.**
   - Spawn one `worker` per independent packet
   - Assign explicit ownership (files/responsibility)
   - Instruct every worker they are not alone in the codebase and must ignore unrelated edits

5. **Integrate and verify.**
   - Review packet outputs, resolve overlaps, run validation gates
   - Run targeted tests per packet, then broader suite for integrated scope

6. **Report and close.**
   - Summarize packet outcomes, key refactors, conflicts resolved, residual risks

## Work Packet Rules

- One owner per file per execution wave
- No parallel edits on overlapping file sets
- Keep packet goals narrow and measurable
- Include explicit done criteria and required checks
- Prefer behavior-preserving refactors unless user explicitly requests behavior change

## Planning Contract

Every packet must include:
1. Packet ID and objective
2. Owned files
3. Dependencies (none or packet IDs)
4. Risks and invariants to preserve
5. Required checks
6. Integration notes for main thread

## Safety Guardrails

- Do not start worker execution before plan synthesis is complete
- Do not parallelize across unresolved dependencies
- Do not claim completion if any required packet check fails
- Stop and re-plan when packet boundaries cause repeated merge conflicts

## Validation Strategy

Run in order:
1. Packet-level checks (fast and scoped)
2. Cross-packet integration checks
3. Full project safety checks when scope is broad

Prefer fast feedback loops, but never skip required behavior checks.
