---
type: Discovery Repair Report
title: Discovery Handoff Repair 2026-07-08
description: Board-ticket evidence for restoring deterministic Skills discovery handoff production.
tags: [skills, discovery, handoff, github-actions, repair]
okf_version: "0.2"
status: active
---

# Discovery Handoff Repair — 2026-07-08

## Board ticket

- Ticket: `skills-restore-discovery-handoff-001`
- Role: Tool Builder
- Value type: `discovery_pipeline_repair`
- Decision: deterministic producer exists, but the canonical handoff file is absent; queue connector-safe manual fallback and leave GitHub Action producer verification as the repair path.

## Direct evidence inspected

- `operations/heartbeat.md` requires each Skills heartbeat to fetch the board, gates, daily state, log, discovery handoff if present, catalog surfaces, and relevant ticket inputs before selecting a board ticket.
- `operations/board.json` marks `skills-restore-discovery-handoff-001` as the highest-priority ready ticket and requires the run to explain why the latest discovery handoff is absent, create or queue a deterministic repair path, avoid mirroring third-party content, and update board/daily state with the next source-review action.
- `operations/gates.md` makes `operations/board.json` the board of record and says useful Skills work must restore/repair discovery, review a source/candidate, normalize a useful skill, remove a risk blocker, improve package-facing metadata, verify catalog/install parity, or verify installable/published surfaces.
- `operations/action-runs/discover-skill-sources/README.md` states the canonical handoff file is `operations/action-runs/discover-skill-sources/latest.json`.
- `operations/action-runs/discover-skill-sources/latest.json` returned `404 Not Found` on the default branch during this run.
- `.github/workflows/discover-skill-sources.yml` exists and is scheduled hourly at minute 23. It runs `scripts/discover_skill_sources.py`, then `scripts/review_discovery_candidates.py`, then writes `operations/action-runs/discover-skill-sources/latest.json`, and commits `reports/discovery`, `reports/review`, `sources/candidates`, and `operations/action-runs/discover-skill-sources` when they differ.
- `scripts/discover_skill_sources.py` is metadata-only by design and does not ingest third-party content.
- `scripts/review_discovery_candidates.py` is metadata-only triage and does not clone repositories, execute candidate code, copy third-party content, or create skills directly.
- Today's daily state already records the missing handoff as an open blocker.

## Why the latest handoff is absent

The repository contains the intended producer workflow and scripts, but the canonical handoff file is absent from the default branch. From connector-visible repository state, this means no successful producer commit has landed that includes `operations/action-runs/discover-skill-sources/latest.json`.

The connector-visible evidence is insufficient to prove whether the hourly Action failed before writing, failed during commit/push, has not run since the workflow was introduced, or was blocked by Actions/runtime configuration. The repair path should therefore avoid pretending discovery is active and should create a bounded fallback that produces metadata-only candidates until an Action run can be inspected or successfully commits the canonical handoff.

## Repair path queued

Queue `skills-manual-discovery-fallback-001` as the next discovery value ticket.

The fallback ticket must:

1. use public web/GitHub metadata only;
2. record at least three real public candidate sources or record exact searches/blockers if fewer are found;
3. write `reports/discovery/2026-07-08-manual.md`, `reports/discovery/2026-07-08-manual.json`, and `sources/candidates/2026-07-08-manual.json` when candidates are found;
4. classify candidates as `review_next`, `watch`, or `skip_or_low_priority`;
5. not clone, execute, copy, import, normalize, publish, or package any candidate content;
6. preserve the current risk gate for `dist/skills/auditing-mcp-servers-for-tool-poisoning/SKILL.md`.

Queue `skills-action-handoff-producer-verification-001` as a blocked CI/local-agent repair ticket.

The verification ticket should be promoted only when a tool surface can inspect GitHub Actions runs/logs or execute the discovery scripts in a safe local/CI context. Its goal is to prove whether the scheduled workflow is failing in discovery, review, handoff write, commit, pull/rebase, or push.

## Acceptance tests

- Explains why latest discovery handoff is absent: **pass**. The canonical `latest.json` is absent from default branch while producer workflow/scripts exist; connector-visible state cannot prove the exact runtime failure mode.
- Creates or queues a deterministic repair path: **pass**. Queues a manual metadata-only fallback plus a blocked producer-verification ticket.
- Does not mirror third-party content: **pass**. This report contains only repository metadata and operational decisions.
- Updates board and daily state with next source-review action: **pass pending commit**. Board/daily updates in this heartbeat mark this ticket done, add the fallback ticket, and record the next action.

## Publication/risk state

Package/publication endorsement remains blocked. Discovery is not considered healthy until either the fallback creates reviewable candidate metadata or the GitHub Action commits a fresh `latest.json`. The open MCP tool-poisoning/SSRF risk ticket remains a package-facing safety gate and must still be resolved before catalog/package endorsement.
