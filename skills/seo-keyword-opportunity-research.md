---
type: Skill
title: SEO Keyword Opportunity Research
description: Use when converting seed topics, existing rankings, Search Console queries, customer problems, or competitor terms into a prioritized, evidence-backed keyword opportunity set.
tags: [skill, seo, keywords, search-console, serp, intent, local-seo, prioritization, evidence, verification, okf]
timestamp: 2026-07-22T00:00:00-03:00
okf_version: "0.2"
source_status: distilled-reviewed
source_name: Architectonic synthesis of reviewed OpenSEO keyword research workflow
source_url: https://github.com/architectonic/skills/blob/main/sources/reviewed/2026-07-22-seo-evidence-cluster.md
source_revision: open-seo@95e95d48cb88e60e1277422254e59c59b3e7e2e2; keyword-research@4bdfc40dd4a27756f3abbc291b7b1bfe1176699c
license: Apache-2.0
source_license_status: open-seo-mit
source_content_copied: false
domain: research
artifact_kind: skill
target_surfaces: [skills, click-blue, workframe]
risk_level: medium
requires_review: false
review_status: source_reviewed_utility_evaluation_pending
---

# SEO Keyword Opportunity Research

## Trigger

Use when converting seed topics, existing rankings, Search Console queries, customer problems, or competitor terms into a prioritized, evidence-backed keyword opportunity set.

Do not use this skill to assign several terms to pages; use `seo-keyword-page-mapping` after opportunity research.

## Purpose

Identify search demand that fits the business and can plausibly be served, while separating first-party evidence, provider estimates, observed SERPs, and analyst inference.

## Inputs

- SEO project context.
- One or more seed topics, products, pages, competitors, or customer problems.
- Market, country, language, city, or service area when material.
- Search Console or equivalent first-party query data when available.
- Existing ranking, keyword, content, and conversion data.
- Approved keyword, SERP, local-search, and domain-data providers.
- Budget or credit constraint for provider calls.

## Procedure

1. **State the research question.** Define the product, audience, market, funnel stage, and decision the keyword set must support.
2. **Start with first-party demand.** When available, inspect real queries, pages, impressions, clicks, CTR, position, and conversions. Identify near-ranking, high-impression, declining, and converting terms before broad discovery.
3. **Normalize seeds.** Reduce the brief to a small set of distinct research angles: problem, category, use case, comparison, alternative, job-to-be-done, local service, and existing-page opportunity.
4. **Discover candidates.** Use an approved provider or current search evidence in bounded batches. Record provider, market, language, date, and query parameters.
5. **Hydrate known terms.** Add available volume, difficulty, CPC, trend, intent, current rank, page, and SERP feature data. Mark absent values `unknown`.
6. **Inspect SERP intent.** For top or ambiguous terms, inspect current result types, ranking pages, dominant intent, freshness, local-pack presence, and whether the user can produce the required page type.
7. **Handle local search separately.** Use location-specific organic and Maps/local-pack evidence. Do not transfer national metrics directly to local conclusions.
8. **Filter.** Remove duplicates, off-product terms, wrong geography/language, misleading branded terms, unsupported page types, irrelevant intent, and opportunities that require capabilities the business does not have.
9. **Prioritize.** Score practical opportunity using business fit, intent, first-party evidence, competitive plausibility, page readiness, conversion path, demand signal, and evidence confidence. Volume alone is not priority.
10. **Present before mutation.** Return a shortlist and evidence table. Saving keywords, adding tags, creating trackers, or changing project state requires explicit confirmation.

## Output Contract

Start with:

- best opportunity theme;
- terms to target now;
- terms requiring SERP or business validation;
- first-party quick wins;
- local or market caveats.

Then provide:

| Keyword | Intent | Market | First-party signal | Provider metrics | SERP evidence | Business fit | Priority | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|---|

End with one recommended next action: page mapping, content brief, competitor research, local validation, save/tag proposal, or no action.

## Verification

- The actual market, language, geography, provider, and collection date are recorded.
- First-party query evidence is distinguished from third-party estimates.
- Unknown metrics remain unknown.
- SERP intent was inspected when it could change the decision.
- Local and organic evidence are not conflated.
- Priority reflects business and intent fit, not only search volume.
- No keywords, tags, trackers, briefs, pages, or outreach actions were written without confirmation.
- The shortlist can be traced to evidence rows.

## Failure Modes

- Starting from broad provider suggestions while ignoring queries the site already earns.
- Treating provider volume, difficulty, CPC, or traffic as exact facts.
- Inferring intent from keyword wording without inspecting current SERPs.
- Mixing countries, languages, devices, or local areas in one score.
- Selecting keywords because they are large rather than useful.
- Recommending terms requiring a page, product, location, or authority the user cannot support.
- Saving or tagging data as part of read-only research.
- Returning hundreds of rows without a decision-oriented shortlist.

## Provenance Boundary

This is an original first-party procedure distilled from reviewed OpenSEO keyword-research patterns. It is provider-neutral and copies no OpenSEO skill body, tool response, or keyword data.