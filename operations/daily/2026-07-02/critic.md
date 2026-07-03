---
type: Report
title: Skills Critic Checkpoint 2026-07-02
description: Critic findings and evidence-aware validation criteria for the skills aggregator.
tags: [skills, critic, validation, pruning, catalog-quality]
okf_version: "0.2"
status: active
---

# Critic Checkpoint — 2026-07-02

## Role Boundary

This pass consumed `maintenance-swe-skills-bench-validation-policy-20260702` as Critic work.

No benchmark tasks, skill documents, prompts, tests, scripts, datasets, Docker images, or paper text were copied. `sources/reviewed/swe-skills-bench.md` remains the provenance boundary and stays `reviewed-reference-only`.

## Evidence-Aware Skill Validation Criteria

Future Critic, Cataloger, and Normalizer passes should treat skill inclusion as a claim that needs evidence, not as a default good.

A skill should be promoted, retained, or packaged only when at least one of these is true:

```text
1. It prevents a recurring observed failure in this repository or a tracked operator run.
2. It is tied to concrete acceptance criteria for a repository class, runtime, tool surface, or workflow.
3. It has a clear verification step that can be executed without unsafe credentials or uncontrolled external effects.
4. It records a source profile, review state, risk level, and known runtime target.
5. It is intentionally marked reference-only, requires-review, or candidate when evidence is incomplete.
```

## Demotion / Pruning Criteria

A skill should be demoted, queued for review, or removed when any of these apply:

```text
1. It gives generic advice that a competent base model should already know.
2. It lacks a specific trigger, input boundary, procedure, verification method, or failure mode.
3. It assumes a stale runtime, stale API, stale package layout, or version-specific behavior without naming that dependency.
4. It can worsen task outcomes when applied to the wrong runtime, repository type, or version.
5. It requires shell, filesystem, network, browser, credential, account, or state-changing actions without a risk gate.
6. It is present in dist/skills but missing or inconsistent across catalog.json, catalog.md, install-manifest.json, and reports.
7. It duplicates another skill without adding a narrower trigger, safer boundary, or clearer verification rule.
```

## Version-Mismatch Rule

Skills that depend on external tools, runtimes, frameworks, MCP servers, package formats, or hosted APIs must name the target surface and must not be treated as universal.

When the target surface is unknown or moving, mark the entry as:

```text
requires_review: true
risk_level: medium|high
source_status: candidate|reference-only|distilled
```

Do not package or publish such entries as endorsed until the catalog and review state make that boundary visible.

## Catalog Health Findings

Catalog drift remains the highest operational blocker:

```text
dist/catalog.md:   1173 skills, 2 high-risk entries
dist/catalog.json: 1170 skills, 1 high-risk entry
```

The local MCP security skill is not yet reflected across generated catalog/install/report surfaces. Packager and Publisher should stay blocked until a Cataloger pass executes the catalog builder through checkout or CI and verifies generated-surface parity.

## Queue Decision

`maintenance-swe-skills-bench-validation-policy-20260702` is complete as Critic work.

No new queue item was created because the next concrete action is already represented by blocked Cataloger items:

```text
catalog-mcp-security-skill-20260702
catalog-reconcile-dist-catalog-surfaces-20260702
```

## Next Action

Run Cataloger from a checkout or CI-backed workflow, execute `npm run build:catalog`, then verify `dist/catalog.json`, `dist/catalog.md`, `dist/install-manifest.json`, and reports agree before Packager or Publisher resumes.
