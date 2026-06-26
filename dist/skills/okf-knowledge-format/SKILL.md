---
name: OKF Knowledge Format
description: Reference for OKF-compatible YAML frontmatter, source status values, risk levels, preferred types, and repository fields. Use when creating new OKF-compatible entries or reviewing existing ones.
tags: [skill-management, okf, format, reference, frontmatter, standards]
---

# OKF Knowledge Format

## Purpose

Reference document for OKF-compatible Markdown formatting used in AOMK. Every durable knowledge file should follow these conventions for interoperability: readable by humans, GitHub, search tools, and coding agents without conversion.

## Required Field

Every OKF-compatible file must include:

```yaml
---
type: Playbook
---
```

## Recommended Fields

```yaml
---
title: Human-readable title
description: One-sentence summary
tags: [topic, capability]
timestamp: 2026-06-20T00:00:00-03:00
---
```

## Provenance Fields

For cataloged or adapted public sources, include:

```yaml
---
source_name: AMOK OKF Profile
source_url: https://example.com/repo
source_license: MIT
source_status: summarized
reviewed_at: 2026-06-20
risk_level: low
runtime_targets: [codex, cursor, claude-code, hermes]
capabilities: [read-files, edit-files, run-tests]
requires_review: false
---
```

## Type Values

Use one of these preferred types:

| Type | Use For |
|------|---------|
| `Skill` | A compact reusable procedure triggered by a recognizable task type |
| `Playbook` | A multi-step operational loop or process pattern |
| `Workflow` | A command-like lifecycle flow with defined stages |
| `Runbook` | A standard operating procedure for agent sessions |
| `Source Profile` | A description of an upstream source repository |
| `Catalog Index` | A routing table or catalog |
| `Security Review` | A checklist for security-sensitive changes |
| `Decision` | A chosen direction with reason and consequence |
| `Memory Model` | A model for what belongs in project memory |
| `Ontology` | Core entity model for classifying agent knowledge |
| `Authority Model` | Source hierarchy and conflict resolution rules |
| `Policy` | A governance rule, boundary, or ingestion constraint |

Unknown types are allowed, but prefer these unless a source needs a more specific class.

## Source Status Values

Use exactly one of:

| Status | Meaning |
|--------|---------|
| `native` | Written for this repository |
| `summarized` | Derived from public source behavior without copying substantial content |
| `adapted` | Rewritten from a compatible public source |
| `verbatim` | Copied under compatible terms, with explicit attribution |
| `reference-only` | Cataloged for discovery; not ingested |

Progressive flow: `candidate` → `cataloged` → `normalized` → `audited`. Terminal states: `blocked` or `reference-only`.

## Risk Levels

| Level | Indicators |
|-------|------------|
| `low` | Pure reading, reasoning, documentation, or checklist behavior |
| `medium` | Edits local files, generates code, runs tests, or uses local tools |
| `high` | Runs shell commands, installs packages, uses network, browser automation, MCP servers, account access, or external-system mutation |
| `blocked` | Unclear license, unsafe behavior, private data, or unverifiable provenance |

## Naming Conventions

- File names: lowercase, hyphens between words (e.g., `skill-quality-gate.md`)
- Tags: lowercase, no spaces (e.g., `[agent-skill, okf, ingestion]`)
- Titles: Title Case, concise

## Anti-Patterns

- Don't omit `type` from frontmatter — it's the minimum OKF requirement
- Don't use undocumented type values without reason
- Don't leave `source_status` blank on adapted/verbatim entries
- Don't forget `risk_level` on entries that execute code or mutate systems
