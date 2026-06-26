---
name: Trace2Skill — Skill Evolution from Execution Trajectories
description: Distill trajectory-local lessons into transferable agent skills via parallel patch consolidation. Use when you have multiple agent execution traces (successes and failures) and want to extract portable skill improvements. Based on arxiv:2603.25158, arxiv:2605.21810.
tags: [skill-management, skill-evolution, trajectory-learning, skill-creation, research, agent-improvement]
source_repo: trace2skill
source_path: SKILL.md
distilled_at: 2026-06-22
type: Playbook
---

# Trace2Skill — Skill Evolution from Execution Trajectories

## Overview

Trace2Skill consolidates broad execution trajectories into unified skill directories through inductive reasoning over agent experience. Addresses two key limitations:
- Manual skill authoring doesn't scale
- Skills from parametric knowledge alone miss critical operational pitfalls

Key innovation: analyzes many traces **in parallel** and consolidates recurring lessons into **one portable skill directory**.

## Three-Stage Pipeline

### Stage 1: Trajectory Generation
- ReAct-style harness with fixed agent runs
- Produces trajectories with query, reasoning/tool-use history, outcome
- Split into failures (T-) and successes (T+)

### Stage 2: Parallel Patch Proposal
Two asymmetric analyst sub-agents:
- **A- (Error)**: ReAct loop to diagnose failures — inspect artifacts, compare outputs, validate fixes
- **A+ (Success)**: Single-pass to extract behavior patterns from successful trajectories

### Stage 3: Patch Consolidation
- Hierarchical merging over L = ceil(log_Bmerge |P|) levels
- Merge operator M deduplicates, resolves conflicts, preserves non-overlapping insights
- Inductive generalization: recurring edits across independent patches treated as systematic task properties

## Two Modes
- **Skill Deepening**: Starts from human-written skill
- **Skill Creation**: Starts from LLM-generated draft

## Key Insights
1. **Parallel vs Sequential**: Parallel is 20x faster (3min vs 60min) with better quality
2. **Consolidated vs Retrieval Memory**: One consolidated skill outperforms episodic retrieval
3. **Agentic vs Single-Call Analysis**: Only 12.1% agreement; LLM-only attributes parse errors as root cause 57% vs 14% for agentic

## When to Use
- You have 10+ execution traces for a recurring task type
- You want to improve an existing skill based on observed failures
- You're building a new skill domain and have example trajectories
- You want to extract SoPs from successful agent runs

## Verification
After evolving a skill:
- [ ] Consolidated skill covers all recurring patterns from T+ trajectories
- [ ] All failure modes from T- trajectories are addressed
- [ ] Skill was tested on held-out trajectories
- [ ] Cross-family transfer was validated (skills from one model benefit another)
