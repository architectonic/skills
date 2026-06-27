---
name: marketplace-skill-triage
description: Triage skills from public marketplaces and aggregators using evidence-based
  scoring rather than popularity alone. Use when evaluating candidate skills from
  skills.sh, awesome lists, GitHub marketplaces, or arXiv-backed skill research. Covers
  license checks, duplicate-intent detection, executable-surface analysis, maintainer
  verification, and evaluation-evidence scoring.
tags:
- business
- skill-management
- triage
- marketplace
- quality
- provenance
- okf
type: Playbook
title: Marketplace Skill Triage
domain: business
risk_level: medium
requires_review: true
source_family: agent-skills-standard
source_status: adapted
---

# Marketplace Skill Triage

Popularity is not quality. Score candidates on evidence, not stars.

## When to use

- Evaluating a candidate skill from a public marketplace or aggregator
- Deciding whether to clone, profile, summarize, or block a skill source
- Periodic review of the skill catalog for stale or redundant entries
- Building a source-scoring policy for automated ingestion

## Core Pattern (from agent-skills-data-driven-analysis-2026)

```text
candidate skill
→ license and provenance check
→ duplicate-intent check
→ executable-surface check
→ adoption and maintainer check
→ evaluation evidence check
→ import as profile, summary, or block
```

## Scoring Dimensions

### 1. License and Provenance
- Clear license file (MIT, Apache-2.0, CC-BY, etc.)
- Identifiable maintainer or organization
- Repository age > 30 days (avoid fly-by-night)
- Attribution for third-party content

### 2. Duplicate-Intent Check
- Search existing catalog for same capability
- Prefer the more specific, better-maintained entry
- Flag near-duplicates for merge consideration

### 3. Executable-Surface Analysis
- Does the skill contain shell commands? (medium risk)
- Does it install packages? (high risk)
- Does it access credentials or accounts? (critical risk)
- Does it mutate external systems? (critical risk)
- Does it use browser automation? (high risk)
- Does it register MCP tools? (high risk)

### 4. Adoption and Maintainer Signals
- Stars, forks, recent commits
- Issue response time
- Release cadence
- Maintainer identity (individual vs org vs abandoned)

### 5. Evaluation Evidence
- Does the skill report benchmarks or test results?
- Is there a paper or technical report backing the approach?
- Are claims specific and falsifiable?

## Scoring Rubric

| Dimension | Strong (2) | Weak (1) | Missing (0) |
|---|---|---|---|
| License | Clear OSI-approved | Ambiguous | None |
| Provenance | Org/known author | Individual, active | Anonymous |
| Duplicate | Unique capability | Partial overlap | Exact duplicate |
| Executable | Read-only text | Scripts, no mutation | External mutation |
| Adoption | >100 stars, active | Some activity | Abandoned |
| Evaluation | Benchmarks/paper | Anecdotal claims | No evidence |

**Score ≥ 8**: Candidate for distillation
**Score 5-7**: Profile and summarize only
**Score < 4**: Block or reference-only

## Anti-Patterns

- Do not treat star count as a quality signal by itself
- Do not import skills with unclear licenses
- Do not skip executable-surface review for "just text" skills (they may reference scripts)
- Do not let marketplace aggregators become trusted authorities without independent review
- Do not import from abandoned repositories without extra scrutiny (hijack risk)

## Workframe Position

This triage gate runs before any skill enters the catalog. Workframe should require a minimum triage score before promoting a candidate to `profiled` status.
