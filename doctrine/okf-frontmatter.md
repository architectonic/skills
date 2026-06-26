---
type: Standard
title: OKF Frontmatter for Skills
description: Metadata rules for runtime-neutral skill concepts in an OKF-compatible skill bundle.
tags: [skills, okf, frontmatter, metadata, standard]
timestamp: 2026-06-26T00:00:00-03:00
okf_version: "0.1"
source_status: distilled
source_name: Agent Memory Ops Kit OKF frontmatter standard
risk_level: low
---

# OKF Frontmatter for Skills

Skill documents should use OKF-compatible Markdown with YAML frontmatter.

## Required Field

OKF requires every non-reserved Markdown concept document to include a non-empty `type` field.

For individual skills:

```yaml
type: Skill
```

## Recommended Fields

```yaml
title: Short human-readable title
description: Trigger-oriented one-sentence summary
tags: [category, topic]
timestamp: 2026-06-26T00:00:00-03:00
```

## Recommended Skill Extensions

```yaml
source_status: native | adapted | distilled | summarized | reference-only | blocked
source_name: Upstream source name or local synthesis
source_url: https://example.com/source
source_license: MIT
risk_level: low | medium | high | blocked
requires_review: true | false
runtime_targets: [claude, codex, cursor, hermes, generic]
```

## Description Rule

Prefer trigger-oriented descriptions.

Use:

```text
Use when reviewing a codebase for architecture drift.
```

Avoid:

```text
This skill reviews architecture.
```

## Risk Levels

```text
low     = reading, reasoning, documentation, checklists
medium  = edits local files, generates code, runs tests, uses local tools
high    = shell, installs, network, browser automation, account access, external systems, production mutation
blocked = unclear license, unsafe behavior, private data, or unverifiable provenance
```

## Anti-Patterns

Avoid:

```text
missing type field
procedure content hidden in frontmatter
unclear source provenance
missing risk level for mutating skills
runtime-specific metadata treated as canonical source
```
