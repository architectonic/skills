---
name: okf-pipeline-pattern
description: Build deterministic OKF (Open Knowledge Format) pipelines that extract structured data from sources, produce knowledge bundles, enrich them through agent-guided grounding, and optionally sync back. Use when building reproducible knowledge extraction workflows from databases, filesystems, git repos, or APIs. Covers connector contracts, producer/enrichment loops, provenance, and MCP exposure.
tags: [skill-management, okf, knowledge-format, pipeline, connector, provenance, extraction]
type: Reference
---

# OKF Pipeline Pattern

Deterministic connectors produce OKF bundles. Agents enrich them. Sync is explicit.

## When to use

- Building reproducible knowledge extraction from structured sources
- You need deterministic, auditable data pipeline steps
- You want to expose knowledge tools via MCP
- You need provenance tracking from source to knowledge artifact

## Core Pattern (from xSAVIKx/okf-skills)

```text
Structured source
→ deterministic connector produce
→ OKF bundle
→ agent-guided grounded enrichment
→ optional ingest/sync back to source
→ visual graph rendering
→ MCP-exposed command surface
```

## Connector Contract

Every connector should:

1. Expose a `schema` subcommand describing inputs/outputs
2. Be deterministic: same source → same OKF bundle
3. Preserve provenance: extractor version, source path, timestamp
4. Separate read-only produce from mutating ingest --sync
5. Fail loudly on missing credentials or unreachable sources

## Producer Types

| Source Family | Examples | Risk Level |
|---|---|---|
| Databases | SQLite, MySQL, PostgreSQL, BigQuery | High (credentials) |
| Filesystem | Directory trees, file metadata | Medium (access scope) |
| Git | Repo metadata, history, refs | Medium (repo access) |
| APIs | REST endpoints, structured responses | Medium-High (auth, rate limits) |

## Enrichment Rules

- Producers are deterministic and low-risk
- Enrichment is agent-guided and non-deterministic
- Enrichment must be grounded in evidence from the source
- Never fabricate facts not derivable from the OKF bundle + source
- Track enrichment provenance separately from extraction provenance

## Sync Policy

- `produce` = read-only, safe to automate
- `ingest --sync` = mutating, requires explicit review
- Never sync without human approval for production sources
- Log every sync operation with before/after state

## MCP Exposure

When exposing OKF tools via MCP:

- Discover installed skills on PATH or explicit skills directory
- Gate tool-level permissions by connector risk level
- Expose schema subcommands so agents can discover capabilities
- Never expose sync tools without explicit enablement

## Anti-Patterns

- Do not treat OKF production as a black-box LLM operation (deterministic is the point)
- Do not enrich without grounding evidence
- Do not sync without human review
- Do not expose all connectors as MCP tools without permission gating
- Do not mix extraction provenance with enrichment provenance
