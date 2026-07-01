---
type: Operating Instructions
title: Skills Daily Ledger
description: Shared daily state and queue contract for the skills aggregator project operator.
tags: [skills, daily-ledger, queues, scheduler, loop-engineering]
okf_version: "0.2"
status: active
---

# Skills Daily Ledger

## Purpose

The daily ledger is the shared state object for the `skills` aggregator loop.

It lives under:

```text
operations/daily/YYYY-MM-DD/
```

The project operator reads and updates it on every scheduled run.

## Required Daily Files

Each operating day should eventually contain:

```text
status.json
queues.json
report.md
radar.md
review-plan.md
normalization-plan.md
catalog-plan.md
publication-plan.md
critic.md
```

## `status.json`

Machine-readable daily state. Start from:

```text
operations/daily/status-template.json
```

## `queues.json`

Machine-readable work queues. Start from:

```text
operations/daily/queues-template.json
```

## Role Write Rules

- Reporter updates `report.md` and `status.json`.
- Radar updates `radar.md`, `sources/candidates/`, and `queues.discovery` / `queues.review`.
- Source Reviewer updates `review-plan.md`, source profiles, and `queues.review` / `queues.normalization` / `queues.risk`.
- Normalizer updates skill/source files and `queues.normalization` / `queues.catalog`.
- Cataloger updates catalog artifacts, reports, `status.json`, and `queues.catalog`.
- Risk Auditor updates review notes and `queues.risk`.
- Packager updates installability notes and `queues.packaging`.
- Publisher updates `publication-plan.md` and `queues.publication`.
- Critic updates `critic.md` and may add concrete queue items.

## Queue Item Shape

```json
{
  "id": "short-stable-id",
  "priority": 1,
  "role": "Radar",
  "target": "URL or path",
  "source_url": "https://example.com/source",
  "reason": "Why this matters",
  "action": "Concrete next action",
  "risk_level": "low|medium|high|unknown",
  "status": "open",
  "created_by": "Reporter",
  "created_at": "YYYY-MM-DDTHH:MM:SS-03:00"
}
```

Valid statuses:

```text
open
in-progress
blocked
done
skipped
```

## Anti-Noise Rule

Do not create extra daily files unless a recurring role needs them. Put temporary thoughts into the relevant daily role file or queue item.
