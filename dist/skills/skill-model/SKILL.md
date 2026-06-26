---
name: Skill Model
description: OKF-compatible frontmatter schema and template for agent skills. Use when creating new skills, validating skill frontmatter, or designing skill metadata fields.
tags: [skill-management, skill-management, schema, okf, frontmatter, template]
---

# Skill Model

Defines the reusable OKF-compatible structure for agent skills.

A skill is a compact procedure triggered by a recognizable task type. It tells an agent what to do differently, how to verify success, and what failure modes to avoid.

## Required Frontmatter

```yaml
---
type: Playbook
title: Skill Name
description: One sentence explaining what the skill helps an agent do.
tags: [agent-skill]
timestamp: 2026-06-20T00:00:00-03:00
---
```

## Recommended Frontmatter

```yaml
source_name: Upstream repo or author name
source_url: https://example.com/source
source_license: MIT
source_status: summarized
risk_level: low
runtime_targets: [claude-code, codex, cursor, hermes]
capabilities: [read-files, edit-files, run-tests]
requires_review: false
```

## Source Status Values

| Value | Meaning |
|-------|---------|
| `native` | Created for this repo |
| `summarized` | Derived from public source without copying substantial text |
| `adapted` | Rewritten for this repo from a compatible source |
| `verbatim` | Copied from compatible source; requires explicit license note |
| `reference-only` | Cataloged but not ingested |

## Risk Levels

| Level | Meaning |
|-------|---------|
| `low` | Cognitive guardrail or reference; no external mutation |
| `medium` | Reads files, runs tests, or modifies local project files |
| `high` | Mutates external systems, installs packages, accesses network, or handles secrets |

## Skill Template

```md
---
type: Reference
title: Skill Name
description: One sentence explaining what the skill helps an agent do.
tags: [agent-skill]
timestamp: 2026-06-20T00:00:00-03:00
source_name: Native
source_url: null
source_license: Native repository license
source_status: native
risk_level: low
runtime_targets: [codex, cursor, claude-code, hermes]
capabilities: []
requires_review: false
---

# Skill Name

## Trigger

Use when...

## Purpose

This skill prevents...

## Inputs

- Required input 1
- Required input 2

## Procedure

1. Step one.
2. Step two.
3. Step three.

## Verification

Success means...

## Failure Modes

- Failure mode 1
- Failure mode 2

## Security Notes

- Mark any filesystem mutation, command execution, network access, browser automation, account access, package installation, or MCP/tool usage.

## Source Notes

- Source:
- License:
- Normalization notes:
```

## Skill Quality Test

A good skill is:
- short enough to load into context;
- specific enough to change behavior;
- reusable across projects;
- verifiable;
- source-grounded;
- security-labeled;
- not a vague principle disguised as a procedure.

## Bad Skill Signs

- It repeats general advice.
- It has no trigger.
- It cannot be verified.
- It contains private project context.
- It tries to solve too many workflows at once.
- It hides risky tool use.
- It copies third-party material without license review.

## Verify

- Every skill has required frontmatter fields.
- `source_status` is one of the five valid values.
- `risk_level` is explicitly set.
- Capabilities list matches actual tool use in the procedure.
