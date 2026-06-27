---
name: trace2skill
description: Distill trajectory-local lessons into transferable agent skills via parallel
  patch consolidation.
tags:
- agent-operations
- research
- skill-evolution
- trajectory-learning
- agent-skills
- skill-creation
- inductive-reasoning
- okf
type: Playbook
title: Trace2Skill
domain: agent-operations
risk_level: medium
requires_review: true
source_family: agent-skills-standard
source_status: adapted
---

# Trace2Skill

## Overview

Trace2Skill consolidates broad execution trajectories into unified skill directories through inductive reasoning over agent experience. Addresses two key limitations:
- Manual skill authoring doesn't scale
- Skills from parametric knowledge alone miss critical operational pitfalls

Key innovation: analyzes many traces **in parallel** and consolidates recurring lessons into **one portable skill directory**.

## Three-Stage Pipeline

### Stage 1: Trajectory Generation
- ReAct-style harness
- Fixed agent runs with initial skill S0, producing trajectories with query, reasoning/tool-use history, outcome
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

## Experimental Results

### Spreadsheet Domain
- Skills evolved from Qwen3.5-35B trajectories improve Qwen3.5-122B by up to 57.65 pp
- Cross-family: Gemma-4 and GPT-5.5 both benefit from Qwen3.5-authored skills

### Math Reasoning
- +Error signal transfers cleanly between 122B and 35B
- Improves both held-out DAPO and OOD AIME 2026

### Visual QA (DocVQA)
- Only 50 examples needed
- +Combined: +0.2534 ANLS / +22.25 Acc for 122B user

## Key Insights

1. **Parallel vs Sequential**: Parallel is 20x faster (3min vs 60min) with better quality
2. **Consolidated vs Retrieval Memory**: One consolidated skill outperforms ReasoningBank episodic retrieval
3. **Agentic vs Single-Call Analysis**: Only 12.1% agreement; LLM-only attributes parse errors as root cause 57% vs 14% for agentic

## Learned SoPs (from 323 patches)
- Formula recalculation & write-back verification (55.1%)
- Tool selection: openpyxl over pandas.to_excel() (54.8%)
- Explicit read-back verification (42.7%)

## Verifier-Guided Evolution (Long-Context EDA)
- Verifier-guided skill evolution for long-context EDA agents
- Builds on Trace2Skill with formal verification steps
