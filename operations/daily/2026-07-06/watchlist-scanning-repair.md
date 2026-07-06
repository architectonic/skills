---
type: Operations Report
title: Watched Source Scanning Repair
description: Durable note for adding constant scanning of known high-signal upstream skill sources.
tags: [skills, operations, discovery, watchlist, radar]
okf_version: "0.2"
status: active
---

# Watched Source Scanning Repair

## Trigger

Operator feedback identified a gap: high-signal sources already reviewed or distilled can still add new skills later. Example: `mattpocock/skills` now exposes a `teach` skill path, so broad one-time discovery is not enough.

## Repair

Added a repo-controlled watchlist and wired the deterministic discovery/review producer to it.

Changed surfaces:

- `operations/source-watchlist.json`
- `scripts/discover_skill_sources.py`
- `scripts/review_discovery_candidates.py`
- `.github/workflows/discover-skill-sources.yml`
- `sources/candidates/mattpocock-teach.md`
- `operations/daily/2026-07-06/queues.json`
- `operations/daily/2026-07-06/status.json`

## Watchlist behavior

The discovery producer now checks known high-signal upstream sources from `operations/source-watchlist.json`, starting with:

- `mattpocock/skills`
- `skills.sh`

The review producer now treats watched repository paths and registry watch candidates as metadata-only triage inputs. The workflow handoff now records watched-repository and registry candidate counts.

## New review queue

Created `review-mattpocock-teach-delta-20260706` for Source Reviewer.

The reviewer should inspect license, changelog, the `teach` boundary, asset/component reuse pattern, invocation surface, overlap with existing Architectonic skills, and whether this should become a source profile, skip/watch note, risk item, or original normalization queue.

## Boundary

No upstream prose, examples, assets, templates, or code were copied. No repository was cloned. No candidate code was executed.
