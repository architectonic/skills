---
type: Action Handoff
title: Discover Skill Sources Action Handoff
description: Observable handoff from GitHub Actions to the ChatGPT Skills scheduler.
tags: [skills, github-actions, scheduler, discovery, review, handoff]
okf_version: "0.2"
status: active
---

# Discover Skill Sources Action Handoff

`latest.json` in this directory is written by `.github/workflows/discover-skill-sources.yml` on every workflow attempt.

The GitHub Action owns deterministic recurring production:

- discover public candidate sources;
- run metadata-only review;
- commit `reports/discovery/*`, `reports/review/*`, and `sources/candidates/*`;
- commit this handoff file so the ChatGPT scheduler can inspect the latest action state.

The ChatGPT scheduler owns review judgment, normalization planning, risk handling, and bounded fallback:

- read this handoff before assuming the workflow did or did not run;
- if review-next candidates exist, prioritize Source Reviewer;
- if artifacts are missing or stale, diagnose or repair the producer;
- if the action surface is unavailable or repeatedly fails, use the scheduler online scout contract to produce a bounded metadata-only fallback;
- do not copy third-party content, clone repositories, execute candidate code, or normalize a skill without license, usefulness, and risk review.
