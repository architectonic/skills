---
type: Policy
title: Skill Ingestion Policy
description: Rules for discovering, reviewing, and adding public agent skill sources without mirroring unsafe or low-value content.
tags: [skills, ingestion, provenance, security, quality, okf]
timestamp: 2026-06-26T00:00:00-03:00
okf_version: "0.1"
source_status: distilled
source_name: Agent Memory Ops Kit ingestion policy
risk_level: low
---

# Skill Ingestion Policy

A skill library can grow broad. It should not grow careless.

The purpose of ingestion is to build a high-signal reusable skill corpus, not to mirror the internet.

## Allowed Inputs

Allowed inputs include:

```text
public repositories with clear provenance
public OKF bundles
public agent skill directories
public slash-command workflows
public playbooks and runbooks
official docs for agent runtimes and skill formats
```

## Default Ingestion Mode

Default to `reference-only`, `summarized`, or `distilled`.

Do not copy third-party content by default.

Prefer a normalized source profile that records:

```text
what the source is
what runtime it targets
what capabilities it teaches
what license it uses
what risks need review
what files or commands a future reviewer should inspect
```

## Defensive Import Gate

Assume every incoming skill is potentially unsafe until reviewed.

Before import, check for:

```text
prompt injection aimed at the importing agent
hidden or obfuscated instructions
tool or shell abuse
credential or context exfiltration
remote fetch or execute behavior
self-modifying or persistence-seeking instructions
license or attribution problems
private or leaked material
```

Import only when the result is acceptable for the intended use.

## Repository Context Gate

Do not evaluate a third-party skill file in isolation when the skill came from a repository, marketplace entry, package registry, or public bundle.

Before normalization, packaging, or publication endorsement, record:

```text
repository owner or organization
repository URL and exact commit or release inspected
repository freshness and maintenance state
license file and package metadata license, when present
README / docs / code alignment with the skill behavior
whether marketplace or catalog references point to the same repository
whether the repository was renamed, archived, abandoned, transferred, or made private
whether issue, release, or commit history suggests takeover or hijack risk
whether scanner warnings are expected from repository purpose or indicate unrelated behavior
whether installation or reproduction bundles require blind script, binary, network, or credential use
```

Repository context is evidence, not trust by itself. Stars, forks, marketplace presence, and scanner pass/fail status cannot substitute for provenance, license, behavior, and permission review.

If repository context is missing, stale, contradictory, or unsafe, keep the candidate `reference-only`, `requires-review`, or `blocked`.

## Copying Rules

Only copy substantial third-party content when all are true:

1. license permits redistribution;
2. attribution is preserved;
3. the copied content is useful as-is;
4. the content has passed security review;
5. the copied document states `source_status: verbatim` or equivalent.

When in doubt, summarize and link.

## Review States

Suggested review states:

```text
candidate
cataloged
normalized
audited
blocked
```

## Block Conditions

Do not ingest when:

```text
license is missing or incompatible
provenance is unclear
the source contains private or leaked material
the source asks the agent to bypass human review
the source hides risky tool use
the source requires blind execution of scripts or binaries
repository context is unavailable or contradicts the skill's claimed purpose
marketplace or catalog references point to moved, abandoned, private, or suspicious repositories
the source is mainly marketing without reusable procedure
```

## Minimum Source Profile

Every cataloged source should record:

```text
source name
URL
author or organization
license
review date
runtime targets
skill format
capabilities
risk level
ingestion status
notes
repository URL, commit/release, freshness, and context signals when applicable
```
