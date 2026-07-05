---
type: Operations Contract
title: Scheduler Online Scout Contract
description: Contract requiring the scheduled Skills operator to scan online sources and produce durable candidate review artifacts.
tags: [skills, scheduler, scout, discovery, review, online-scan]
okf_version: "0.2"
status: active
---

# Scheduler Online Scout Contract

## Purpose

The Skills scheduler exists to find complementary external skill sources for the Architectonic skills mega-repo, vet them safely, and convert only suitable candidates into source profiles, skip notes, risk items, or normalization queues.

It should not merely report that the repository is healthy.

The preferred producer is `.github/workflows/discover-skill-sources.yml`, which runs `scripts/discover_skill_sources.py` and `scripts/review_discovery_candidates.py`.

If that workflow has not produced current artifacts, the scheduled Skills operator should perform scheduler-side online scouting and write metadata-only fallback artifacts.

## Required artifact set

A useful scout pass creates or verifies at least one of:

- `reports/discovery/YYYY-MM-DD.md`
- `reports/discovery/YYYY-MM-DD.json`
- `reports/review/YYYY-MM-DD.md`
- `reports/review/YYYY-MM-DD.json`
- `sources/candidates/YYYY-MM-DD.json`
- source profile under `sources/`
- skip note under `sources/` or `reports/review/`
- normalization queue item
- risk queue item

## Online scout surfaces

The scheduler should search current public web and GitHub signals for:

- new or recently updated GitHub repositories for AI agents, MCP servers, Claude skills, Cursor rules, Codex instructions, OpenAI agents, Vercel AI SDK agents, workflow runners, harnesses, memory systems, evaluator loops, browser tools, and agent runtimes;
- public roundup posts, launch posts, HN discussions, blogs, and documentation pages that mention GitHub repositories or reusable skill patterns;
- official examples from Anthropic, OpenAI, Cursor, Vercel, MCP, GitHub, and comparable tool ecosystems.

The scheduler should favor candidates that are complementary to the existing mega-repo: capabilities, workflows, safety policies, memory patterns, evaluation harnesses, installer patterns, MCP connectors, and practical agent operating loops.

## Required candidate fields

Each candidate record should include:

- `name`
- `url`
- `source_family`
- `description`
- `observed_at_utc`
- `license` when visible
- `stars`, `forks`, or adoption signal when visible
- `last_activity` when visible
- `complementarity`
- `risk_level`
- `decision`: `review_next`, `watch`, or `skip_or_low_priority`
- `reason`
- `review_boundary`: `metadata_only_no_content_copy_no_code_execution`

## Minimum usefulness threshold

A scheduler fallback scout pass is useful if it records at least three real public candidate sources or creates at least one source profile, skip note, risk item, or normalization queue item.

If fewer than three real candidates can be found, do not invent. Record exact searches and blockers.

## Boundaries

Do not clone repositories.
Do not execute candidate code.
Do not copy third-party content.
Do not import private, leaked, unlicensed, or executable material without explicit risk review.
Do not turn a candidate into a skill until license, usefulness, risk, security/runtime surface, and redistribution boundaries are reviewed.

## Scheduler behavior

If no current discovery/review artifact exists and the cadence role is Radar or Source Reviewer, the scheduler should:

1. search public web and GitHub signals;
2. record metadata-only candidates;
3. classify candidates as `review_next`, `watch`, or `skip_or_low_priority`;
4. write discovery/review/source-candidate artifacts;
5. update today's status, queues, and log with candidate counts and resulting commit SHA.
