---
type: Source Index
title: Skills Source Profiles
description: Source profile structure for public agent skills, loops, workflows, runbooks, MCP procedures, and runtime documentation.
tags: [skills, sources, provenance, license, review, aggregator]
okf_version: "0.2"
status: active
---

# Skills Source Profiles

## Purpose

This directory stores reviewed or candidate source profiles for public skill and loop material.

A source profile records provenance and review status. It is not a mirror of the source.

## Suggested Layout

```text
sources/
  candidates/
  reviewed/
  blocked/
```

## Minimum Source Profile

```md
---
type: Source Profile
title: Source Name
description: One sentence explaining why this source matters.
tags: [source-profile, skills]
okf_version: "0.2"
source_url: https://example.com/source
source_name: Source Name
source_author: Author or Organization
license: UNKNOWN
runtime_targets: [claude, codex, cursor, mcp]
skill_format: UNKNOWN
risk_level: unknown
ingestion_status: candidate
reviewed_at: YYYY-MM-DD
---

# Source Name

## What It Is

## Why It Matters

## Provenance

## License

## Runtime Targets

## Candidate Capabilities

## Risks

## Ingestion Decision

## Next Action
```

## Ingestion Statuses

```text
candidate
reviewed
reference-only
summarized
normalized
blocked
stale
```

## Rule

Do not copy substantial source content into this repository unless license, attribution, usefulness, and security review all permit it.
