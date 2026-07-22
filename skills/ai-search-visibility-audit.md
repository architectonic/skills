---
type: Skill
title: AI Search Visibility Audit
description: Use when auditing whether a brand, page, product, or topic appears accurately and citeably in current AI-assisted search and answer surfaces without relying on stale platform statistics or unsupported optimization claims.
tags: [skill, seo, ai-search, aeo, geo, citations, visibility, current-sources, structured-data, evidence, verification, okf]
timestamp: 2026-07-22T00:00:00-03:00
okf_version: "0.2"
source_status: distilled-reviewed
source_name: Architectonic replacement for the reviewed packaged ai-seo reference, informed by OpenSEO evidence boundaries
source_url: https://github.com/architectonic/skills/blob/main/sources/reviewed/2026-07-22-seo-evidence-cluster.md
source_revision: packaged-ai-seo@62339de9a8c7ff51f3e8ff682e4c5e80a3dbc89d; open-seo@95e95d48cb88e60e1277422254e59c59b3e7e2e2
license: Apache-2.0
source_license_status: local-replacement; open-seo-mit
source_content_copied: false
domain: research
artifact_kind: skill
target_surfaces: [skills, click-blue, workframe]
risk_level: medium
requires_review: false
review_status: source_reviewed_utility_evaluation_pending
---

# AI Search Visibility Audit

## Trigger

Use when auditing whether a brand, page, product, or topic appears accurately and citeably in current AI-assisted search and answer surfaces without relying on stale platform statistics or unsupported optimization claims.

This is an observational and content-quality audit. It cannot guarantee citation, ranking, inclusion, or traffic impact.

## Purpose

Measure current visibility across explicitly named search or answer surfaces, identify the sources and page characteristics those surfaces actually use, and produce bounded content, entity, evidence, and indexing recommendations.

## Inputs

- Brand, entity, site, product, page set, or topic in scope.
- Priority audiences, markets, languages, and user questions.
- Current site pages, structured data, authorship, evidence, and indexing controls.
- Approved access to current search/answer surfaces.
- Current official crawler, indexing, robots, and structured-data documentation.
- Search Console, analytics, referral, citation, or server-log evidence when available.
- Competitor or comparison set when requested.

## Procedure

1. **Name the surfaces.** Record the exact products, modes, regions, languages, account state, and date tested. Do not generalize one product's behavior to all AI search.
2. **Define representative questions.** Build a bounded set covering definitions, category discovery, comparisons, alternatives, use cases, trust questions, pricing, implementation, and brand-specific queries as relevant.
3. **Capture observations.** For each question record the answer, cited URLs, cited domains, source types, presence or absence of the target, factual accuracy, freshness, and uncertainty. Preserve screenshots or recoverable notes where allowed.
4. **Separate observation from inference.** A citation is observed. The reason it was selected is usually an inference unless supported by official documentation or controlled testing.
5. **Inspect cited pages.** Compare page type, directness, evidence, authorship, dates, entity clarity, structured data, internal links, accessibility, and content extractability. Do not copy the cited page.
6. **Check first-party search foundations.** Inspect indexing, canonical, robots, crawlability, page status, metadata, structured data, Search Console evidence, and ordinary SERP performance. AI visibility does not replace technical and traditional search foundations.
7. **Verify crawler controls currently.** Use official, current documentation for relevant crawlers and user agents. Record documentation date and product scope. Do not rely on memorized crawler names or assume one control affects every product.
8. **Audit content extractability.** Check whether key claims are direct, self-contained, sourced, dated, attributable, and understandable outside surrounding marketing prose.
9. **Audit entity and evidence quality.** Check organization/product identity, authorship, credentials, contact and policy pages, primary-source data, citations, definitions, comparison criteria, and consistency across owned and authoritative third-party sources.
10. **Check third-party presence carefully.** Record authoritative reviews, directories, communities, documentation, datasets, and publications only when current evidence shows they matter for the tested questions. Do not manufacture mentions or manipulate communities.
11. **Propose bounded improvements.** Prioritize factual corrections, stronger primary evidence, clearer answer structure, current dates, authorship, schema fixes, crawl/index repairs, comparison transparency, and genuinely useful assets.
12. **Define measurement.** Establish a repeatable query set, collection cadence, evidence format, and success criteria. Treat referral traffic and citations as separate metrics.

## Output Contract

Start with:

- tested surfaces and date;
- current visibility summary;
- factual or brand-representation risks;
- strongest cited source types;
- highest-confidence improvements;
- major unknowns.

Then provide:

| Query | Surface/mode | Target present | Citation/source | Answer accuracy | Evidence type | Observation | Inference | Confidence |
|---|---|---:|---|---|---|---|---|---|

Add sections for technical/indexing findings, content extractability, entity/evidence quality, current official crawler controls, and a repeatable measurement plan.

## Verification

- Every platform claim is tied to a named product, mode, region, date, or current official source.
- Static prevalence, click-loss, citation-multiplier, or optimization-gain statistics are not repeated without recoverable current evidence.
- Observed citations are separated from hypotheses about selection.
- The audit includes ordinary indexing, canonical, crawlability, and SERP foundations.
- Current official crawler documentation was checked when crawler controls are discussed.
- Recommendations improve user-facing truth and evidence rather than merely formatting text for machines.
- No community manipulation, fabricated third-party mention, automated posting, review solicitation, or crawler-rule mutation occurred without explicit authorization.
- The measurement plan is reproducible and does not promise causal attribution it cannot establish.

## Failure Modes

- Treating all AI assistants, answer modes, or search products as one system.
- Reusing old percentages or crawler lists from an undated reference.
- Claiming a content change caused citation from one observation.
- Optimizing for extraction while making content worse for humans.
- Publishing unsupported statistics, expert quotations, awards, or credentials.
- Recommending Wikipedia, Reddit, reviews, or community posts as manipulation targets.
- Blocking or allowing crawlers without understanding the current product-specific effect.
- Ignoring traditional search, indexing, and technical foundations.
- Promising citation, ranking, traffic, or conversion results.

## Provenance Boundary

This is an original first-party procedure that supersedes the packaged `ai-seo` reference. It preserves no static platform statistics from that body and copies no OpenSEO skill content or provider response.