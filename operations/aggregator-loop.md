---
type: Operating Instructions
title: Skills Aggregator Loop
description: Role-based, ledger-driven operating model for discovering, reviewing, normalizing, cataloging, packaging, and publishing reusable agent skills and loops.
tags: [skills, aggregator, loop-engineering, project-operator, queues, scheduler, web-discovery]
okf_version: "0.2"
status: active
---

# Skills Aggregator Loop

## Purpose

The `skills` repository is an installable skill bundle and a living aggregator for public agent skills, loops, workflows, runbooks, source profiles, and reusable procedures.

The aggregator should improve through one recurring project operator that selects specialized roles through a shared daily ledger and queues.

Canonical loop:

```text
Observe
-> Plan
-> Act
-> Evaluate
-> Repair / Learn
-> Persist memory
-> Repeat
```

## Operating Pattern

```text
single project-operator scheduler
many roles
shared daily ledger
queued + scheduled execution
```

The operator reads durable state, selects one role, acts within that role boundary, updates status and queues, and stops cleanly.

Time defines when work may happen. Queues decide whether useful work exists.

## Scope

The aggregator may discover and catalog:

```text
public agent skill directories
Claude / Codex / Cursor / Goose / OpenCode / Amp / Aider / Roo / Cline-style skill or rule systems
MCP server procedures
slash-command workflows
agent loop patterns
playbooks and runbooks
repository maintenance loops
official runtime documentation
benchmark or evaluation repositories for skills
public marketplaces and registries with clear provenance
```

It must not ingest private content, leaked material, secrets, raw prompt dumps, unlicensed mirrors, or instructions that bypass review.

## Core Roles

### Reporter

Owns daily memory.

Writes:

```text
operations/daily/YYYY-MM-DD/report.md
operations/daily/YYYY-MM-DD/status.json
```

### Radar

Owns discovery.

Searches public web, GitHub, official docs, credible posts, repositories, and release notes for new skill and loop sources.

Writes or updates:

```text
operations/daily/YYYY-MM-DD/radar.md
operations/daily/YYYY-MM-DD/queues.json
sources/candidates/
```

### Source Reviewer

Owns provenance, license, adoption, usefulness, and safety review.

Consumes:

```text
queues.review
```

Writes or updates source profiles and review status.

### Normalizer

Owns conversion from accepted source behavior into OKF-compatible skills, playbooks, workflows, runbooks, or reference-only source profiles.

Consumes:

```text
queues.normalization
```

Writes under:

```text
skills/
dist/skills/
sources/
```

as appropriate.

### Cataloger

Owns machine-readable and human-readable catalog surfaces.

Runs or requests:

```bash
npm run build:catalog
```

Updates:

```text
dist/catalog.json
dist/catalog.md
dist/install-manifest.json
reports/
operations/daily/YYYY-MM-DD/status.json
```

### Risk Auditor

Owns safety review.

Checks for:

```text
prompt injection
hidden instructions
shell or filesystem abuse
credential or context exfiltration
network fetch or execute behavior
account-flow risk
state-changing external actions
license or attribution risk
private or leaked material
```

### Packager

Owns installability.

Checks package files, dist layout, catalog manifests, npx install surfaces, README/install instructions, and review flags for high-risk skills.

### Publisher

Owns future website/export preparation.

Prepares public-facing catalogs, summaries, pages, and install/download metadata after source review and catalog validation.

### Critic

Owns entropy control.

Finds duplication, stale sources, low-value skills, overbroad procedures, broken indexes, unused reports, and process drift.

## Queues

Primary queues:

```text
discovery
review
normalization
catalog
risk
packaging
publication
maintenance
critic
```

Queue items should be concrete and small.

A good queue item names:

```text
source or file
why it matters
role owner
next action
risk level
status
```

## Priority Rule

Review and safety outrank growth.

If there are unreviewed candidates, missing license data, high-risk imports, broken catalog manifests, or stale package surfaces, prioritize review, risk, catalog, and packaging before broad discovery.

Discovery is valuable only when it feeds reviewable source profiles or queue items.

## Default Ingestion Stance

```text
reference-only first
summarize by default
copy rarely
normalize only if useful
package only if safe
publish only if provenance is clear
```

## Evidence Rule

Do not claim a source is useful, safe, adopted, maintained, or installable unless the repository or public source supports that claim.

When evidence is insufficient, mark the item as candidate, partial, blocked, or needs-review.

## Quality Gate (2026-07-07)

Any skill added to or updated under `dist/skills/` must pass the `authoring-agent-skills` checklist (`dist/skills/authoring-agent-skills/SKILL.md`) before its queue item closes:

```text
description = what + when, third person, trigger terms present
name lowercase-hyphen, action-oriented
frontmatter carries domain and risk_level (no new uncategorized/unspecified entries)
body < 500 lines, references one level deep
```

The Critic should treat the existing uncategorized-domain and unspecified-risk backlogs as standing maintenance queue material: batch metadata backfill outranks new discovery when those counts grow.

## Stopping Conditions (2026-07-07)

Each operator run is bounded: one role, one queue item (or one small batch of the same kind). Cap repair retries at two per run; after the cap, record a blocker in the ledger and stop rather than looping. An empty relevant queue is a valid no-op run — record it honestly and exit. Never let a run rewrite state it did not inspect this run.

## Distribution Rule

Any change that modifies `dist/skills/` or install-facing metadata should be followed by a catalog refresh or a queue item for Cataloger.

Current catalog builder:

```bash
npm run build:catalog
```

## Success Metrics

Track in the daily ledger:

- candidate sources discovered;
- sources reviewed;
- sources blocked;
- normalized skills added;
- skills updated;
- catalog skill count;
- domain counts;
- risk counts;
- high-risk or requires-review count;
- package/catalog build status;
- publication/export readiness;
- duplicate or stale entries found;
- unresolved blockers.

## Anti-Patterns

Avoid:

- blind mirroring;
- copying third-party content without license review;
- adding generic tips as skills;
- treating popularity as validation;
- packaging high-risk skills without review flags;
- mixing private project memory into public skills;
- creating reports that do not update queues or catalog state;
- many separate scheduled tasks fighting over the same repo.
