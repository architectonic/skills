---
name: skill-revision
description: Revise agent skills using execution traces, verifier feedback, and utility
  gates. Use when improving cold-start LLM-authored skills, when a skill fails in
  production, or when evidence-based skill improvement is needed. Covers trace-conditioned
  diagnosis, principle-memory retrieval, anchored editing, and utility-gated promotion.
tags:
- agent-operations
- skill-management
- skill-revision
- trace-conditioned
- verifier
- self-improvement
- okf
type: Playbook
title: skill-revision
domain: agent-operations
risk_level: medium
requires_review: true
source_family: agent-skills-standard
source_status: adapted
---

# skill-revision

Revise agent skills using execution traces, verifier feedback, and utility gates.

## When to use

- A skill fails in production and needs evidence-based improvement
- A cold-start skill was generated one-shot and needs grounding
- Execution traces show recurring failure patterns
- A proposed skill edit needs verification before promotion

## Core Pattern (from SkillRevise)

```text
initial skill
→ execution attempt
→ trace and verifier evidence
→ diagnosis
→ principle-memory retrieval
→ anchored revision
→ re-execution
→ utility-gated selection
→ promote or reject
```

## Workflow

### 1. Collect Evidence
- Run the skill against a bounded task
- Capture execution trace (actions, outputs, errors)
- Record verifier pass/fail signals
- Note where the skill diverged from expected behavior

### 2. Diagnose
- Classify failure mode: missing step, wrong order, wrong tool, missing guardrail, scope mismatch
- Identify whether the failure is in the skill's text, its assumptions, or its preconditions
- Separate fixable defects from fundamental design flaws

### 3. Retrieve Principles
- Search memory for similar past failures and fixes
- Identify reusable repair patterns (e.g., "always validate URL before fetching", "require confirmation before destructive action")
- Record the principle that explains why the fix works

### 4. Apply Anchored Revision
- Edit only the specific section of the skill that caused the failure
- Preserve all unchanged sections verbatim
- Add a revision note explaining what changed and why
- Keep the diff reviewable

### 5. Re-execute and Gate
- Run the revised skill against the same task
- Run against a held-out task (transfer check)
- Apply utility gate: promote only if net positive with no material regressions
- Record the outcome as a receipt

## Required Receipts

Each revision cycle must preserve:
- Original skill text
- Changed skill text (diff-visible)
- Execution evidence (trace excerpt or summary)
- Verifier signals (before and after)
- Rejected candidate(s) and reasons lost
- Promotion decision with rationale

## Promotion Criteria

Promote revised skill only if:
- The fix addresses the root cause, not just the symptom
- No regressions on previously-passing cases
- The revision is minimal (not a full rewrite)
- Transfer check passes on at least one held-out task
- Failure-mode classification is documented

## Anti-patterns

- Rewriting the entire skill instead of anchoring to the failure point
- Promoting because the new version "looks better" without execution evidence
- Ignoring regressions on previously-passing cases
- Skipping held-out transfer checks
- Revising based on a single flaky execution

## Sources

- HKUST-KnowComp/skillrevise — trace-conditioned skill revision framework
- evaluator-optimizer-self-improvement-loop.md — bounded loop pattern
- skill-distillation.md — contrastive induction and paired verification
