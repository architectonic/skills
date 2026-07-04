---
type: Critic Report
title: Skill Retrieval Quality Rubric
summary: Non-executing local rubric for judging whether the skills catalog is retrievable, selectable, and useful rather than merely large.
tags: [skills, critic, catalog-quality, retrieval, selectability, evaluation]
okf_version: "0.2"
status: active
---

# Skill Retrieval Quality Rubric

## Trigger

Use this rubric when catalog size, discovery volume, or package publication pressure risks becoming a substitute for actual skill usefulness.

This report consumes `critic-skill-retrieval-quality-20260703` and uses the reviewed reference-only source profile `sources/reviewed/skill-usage-realistic-settings.md` as input. It does not run, copy, reproduce, or import the external benchmark.

## Decision

Raw skill count is not a sufficient value metric for `architectonic-skills`.

The catalog is useful only if a future agent can:

1. identify the right skill for a concrete task;
2. reject irrelevant or risky skills;
3. choose between near-duplicate skills;
4. understand when a skill requires human review or restricted execution;
5. apply the selected skill without needing hidden project context;
6. verify that the skill changed behavior or prevented a known failure mode.

## Non-Executing Sample Rubric

For a small local sample, select 10-20 skills from `dist/catalog.json` without executing external tasks. Include:

- 3 high-risk or review-sensitive entries when available;
- 3 `uncategorized` entries;
- 3 highly central or broadly named entries;
- 1-3 recently added or recently touched entries.

Score each sampled skill from 0 to 3 across the following dimensions:

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Retrieval fit | Title/tags do not reveal when to use it | Discoverable only by exact title | Discoverable by likely task words | Clearly discoverable by task, domain, and failure mode |
| Selectability | Too vague to choose over alternatives | Some signal but overlaps heavily | Clear enough to choose in common cases | Distinct, narrow trigger and obvious alternatives/rejections |
| Applicability | Procedure is missing or generic | Procedure needs substantial inference | Procedure can guide a normal run | Procedure is compact, ordered, and directly usable |
| Verification | No success check | Weak or subjective check | Concrete check exists | Check catches common false positives or regressions |
| Risk clarity | Unsafe surfaces hidden | Risk present but vague | Risk named | Risk, required review, and allowed/blocked actions are explicit |
| Source/provenance clarity | Source unknown where it matters | Partial source context | Clear enough for internal use | Clear source, license/reuse posture, and confidence boundary |

Total score bands:

```text
0-6    slop / remove or rewrite
7-11   weak / keep only if strategically important
12-15  usable / acceptable catalog entry
16-18  strong / good retrieval and application target
```

## Local Catalog Quality Metrics

Future Reporter or Critic passes should track these beside raw catalog count:

```text
sample_size
sample_strong_count
sample_usable_count
sample_weak_count
sample_slop_count
uncategorized_sample_failures
requires_review_clarity_failures
near_duplicate_conflicts
missing_verification_count
missing_failure_modes_count
```

These are lightweight quality signals. They do not prove benchmark performance.

## Acceptance Rules

A sampled skill should be marked for repair when:

- the title is too generic to retrieve from a large catalog;
- the trigger does not state a concrete task condition;
- the procedure merely says to be careful or thorough;
- verification is absent or circular;
- failure modes are missing;
- risk level is unspecified while the procedure touches shell, filesystem, credentials, account actions, network, browser automation, MCP/tools, or production mutation;
- the skill overlaps another skill without a clear distinction.

## Blocked Actions

Do not perform any of the following from this Critic pass:

- run the external benchmark repository;
- download benchmark datasets;
- copy benchmark tasks, prompts, tables, figures, or code;
- claim local measured improvement;
- promote the reviewed source to packaged skill content;
- change `skills/` or `dist/skills/` without a concrete normalization/catalog queue item.

## Follow-Up Queue Recommendation

No immediate normalization is justified from this pass.

The next useful Critic or Cataloger follow-up is a small local sampling report under a future daily ledger, for example:

```text
critic-sample-catalog-retrievability-YYYYMMDD
```

That future item should sample local catalog entries only, write repair queue items for weak/slop entries, and avoid external benchmark execution until license and sandbox requirements are separately reviewed.

## Run Result

`critic-skill-retrieval-quality-20260703` is complete as a local non-executing rubric. Review, risk, normalization, catalog, packaging, and publication queues can remain clear unless a future sampled catalog-quality pass creates concrete repair work.
