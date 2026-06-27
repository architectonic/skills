---
name: Knowledge Ops — SOP/Runbook Authoring and KB Hygiene
description: Author, validate, and clean up company SOPs and internal runbooks. 5W2H
  completeness checks, cross-link and orphan-page validation across wikis, KB ingestion
  + hygiene reporting, runbook step verification (named owner, expected duration,
  observable success signal, rollback path, escalation contact). Pairs Ishikawa's
  5W2H method, Gawande's Checklist Manifesto, ISO 9001, ITIL v4, and Google SRE Workbook
  runbook discipline.
version: 1.0.0
source: claude-skills/business-operations/knowledge-ops (MIT)
author: claude-code-skills (distilled by Agent-Memory-Ops-Kit)
tags:
- agent-operations
- productivity
- bizops
- sop
- runbook
- knowledge-management
- kb
- 5w2h
- wiki
- ops-documentation
- okf
type: Playbook
title: Knowledge Ops — SOP/Runbook Authoring and KB Hygiene
domain: agent-operations
risk_level: medium
requires_review: true
source_family: amok-native
source_status: adapted
---

# Knowledge Ops — SOP/Runbook Authoring and KB Hygiene

Company SOP + internal runbook authoring, 5W2H completeness validation, and KB hygiene reporting for Head-of-Ops / Knowledge-Manager / TPM-Internal personas.

## Purpose

An ops organization three years in accumulates a sprawl: 600 Notion pages, 200 Confluence runbooks, three Obsidian vaults, a `Drive/SOPs/` folder, and a Slack #ops-questions channel that exists because nobody can find the canonical doc. Predictable failure modes:

1. **No owner** — 40% of SOPs name "the team" instead of a person.
2. **No last-reviewed date** — years-old SOPs reference sunset tools.
3. **Vague success signals** — "verify the service is up" is not observable.
4. **No rollback path** — runbooks tell you how to send the alert, not retract it.
5. **Orphan pages** — half the KB has no inbound links.
6. **Glossary drift** — "CSM" means different things in different docs.
7. **Happy-path-only SOPs** — no coverage for the 30% case where things break.

This skill answers: **"Which 20 docs do I fix first, and what specifically is wrong with each?"** — with deterministic logic, not intuition.

## When to use

- Authoring a new SOP for a cross-functional process (procurement intake, vendor offboarding, incident-comms cascade, employee onboarding).
- Validating an existing runbook before it goes into rotation (every step must have: named owner, expected duration, observable success signal, observable failure signal, rollback path, escalation contact).
- Ingesting a multi-document KB export (Notion zip, Confluence space export, Obsidian vault) and surfacing what's broken: orphan pages, stale pages (no edit > 12 months), glossary drift, missing-owner pages.
- Onboarding a new ops hire by generating the SOPs they need in week 1.
- Wiki cleanup sprints — quarterly hygiene work.

## 5W2H Completeness Checklist

Every SOP step must answer:

| Dimension | Question | Failure mode if missing |
|-----------|----------|------------------------|
| **Who** | Named owner (not "the team") | No accountability |
| **What** | Concrete action, not vague | Operator guesses |
| **When** | Trigger condition + deadline | Step runs at wrong time |
| **Where** | System / tool / location | Operator can't find it |
| **Why** | Purpose of this step | Step gets skipped as "unnecessary" |
| **How** | Exact procedure (copy-pasteable) | Inconsistent execution |
| **How Much** | Expected duration + success signal | No way to verify completion |

## Runbook Step Verification

Every runbook step must have:
- **Named owner**: A person, not a team
- **Expected duration**: P50 estimate in minutes
- **Observable success signal**: What "done" looks like (not "verify it works")
- **Observable failure signal**: What "broken" looks like
- **Rollback path**: How to undo this step if it goes wrong
- **Escalation contact**: Who to call if rollback fails

## KB Hygiene Audit

When auditing a wiki/knowledge base, check for:

1. **Orphan pages**: No inbound links from other pages
2. **Stale pages**: No edits in > 12 months
3. **Missing owner**: No named maintainer
4. **Glossary drift**: Same term defined differently across docs
5. **Happy-path-only**: No error handling or exception branches
6. **Broken links**: Internal links pointing to deleted/moved pages
7. **Duplicate content**: Same process documented in multiple places with drift

## Workflow

1. **Intake**: Capture the SOP/runbook as structured text with 5W2H fields per step.
2. **Validate**: Score each step against the 5W2H checklist. Flag missing dimensions.
3. **Cross-link**: Map inbound/outbound links. Identify orphans.
4. **Prioritize**: Rank docs by impact (criticality × staleness × orphan status).
5. **Fix**: Rewrite the top 20 docs with complete 5W2H fields and rollback paths.

## Source

Distilled from `claude-skills/business-operations/skills/knowledge-ops/SKILL.md` (claude-code-skills, MIT).
Adapted for Hermes Agent — removed Claude Code-specific `/cs:` command references.
