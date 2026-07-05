---
type: Operations Fallback
title: Manual Discovery Review Fallback
description: Connector-safe fallback when the scheduled discovery/review GitHub Action has not produced today's reports.
tags: [skills, discovery, review, fallback, scheduler]
okf_version: "0.2"
status: active
---

# Manual Discovery Review Fallback

## Purpose

The primary path is `.github/workflows/discover-skill-sources.yml`, which runs `scripts/discover_skill_sources.py` and `scripts/review_discovery_candidates.py`.

If the workflow has not produced today's `reports/discovery/`, `reports/review/`, or `sources/candidates/` artifacts, the Skills Loop Operator may perform a connector/manual fallback rather than producing another status-only pass.

## Allowed fallback

The operator may create a small metadata-only fallback report under:

- `reports/discovery/YYYY-MM-DD-manual.md`
- `reports/discovery/YYYY-MM-DD-manual.json`
- `reports/review/YYYY-MM-DD-manual.md`
- `reports/review/YYYY-MM-DD-manual.json`
- `sources/candidates/YYYY-MM-DD-manual.json`

The fallback may use public web/GitHub search results as metadata only.

## Required fields

Each candidate record should include:

- `name`
- `url`
- `source`
- `description`
- `license` if visible
- `stars` or adoption signal if visible
- `last_activity` if visible
- `risk_level`
- `decision`: `review_next`, `watch`, or `skip_or_low_priority`
- `reason`
- `review_boundary`: `metadata_only_no_content_copy_no_code_execution`

## Boundaries

Do not clone repositories.
Do not execute candidate code.
Do not copy third-party content.
Do not normalize a skill until license, usefulness, risk, security/runtime surface, and redistribution boundaries are reviewed.
Do not treat discovery as value unless it creates review-next candidates, skip notes, source profiles, risk items, or normalization queue items.

## Scheduler behavior

If no current review artifact exists and the cadence role is Radar or Source Reviewer, prefer this fallback over a status-only run.

If no reliable public source metadata can be gathered, record the exact query/source blocker and stop. Do not invent candidates.
