---
type: Skill
title: SEO Keyword-to-Page Mapping
description: Use when grouping keywords by search intent and ranking-page evidence, mapping each cluster to an existing or proposed page, and identifying cannibalization or consolidation risk.
tags: [skill, seo, keywords, clustering, page-mapping, intent, serp, cannibalization, content-architecture, verification, okf]
timestamp: 2026-07-22T00:00:00-03:00
okf_version: "0.2"
source_status: distilled-reviewed
source_name: Architectonic synthesis of reviewed OpenSEO keyword clustering workflow
source_url: https://github.com/architectonic/skills/blob/main/sources/reviewed/2026-07-22-seo-evidence-cluster.md
source_revision: open-seo@95e95d48cb88e60e1277422254e59c59b3e7e2e2; keyword-clustering@0fbadf7564b3127dd9f87f4fd14f7e17c9bc4b39
license: Apache-2.0
source_license_status: open-seo-mit
source_content_copied: false
domain: business
artifact_kind: skill
target_surfaces: [skills, click-blue, workframe]
risk_level: medium
requires_review: false
review_status: source_reviewed_utility_evaluation_pending
---

# SEO Keyword-to-Page Mapping

## Trigger

Use when grouping keywords by search intent and ranking-page evidence, mapping each cluster to an existing or proposed page, and identifying cannibalization or consolidation risk.

Do not use lexical similarity alone. Similar words may require different pages; different words may share one intent and ranking-page set.

## Purpose

Turn a usable keyword set into a bounded content and site-architecture decision: which intent belongs together, which page should serve it, and where the existing site competes with itself.

## Inputs

- SEO project context.
- Candidate keyword set and source evidence.
- Existing URLs, sitemap, page types, and content inventory when available.
- Search Console query-page or equivalent first-party evidence.
- Current SERP results for ambiguous or high-priority terms.
- Geography, language, device, and local-search context.
- Approved provider and mutation scope.

## Procedure

1. **Validate the keyword set.** Remove duplicates, off-strategy terms, unsupported markets, and candidates lacking enough evidence to map.
2. **Recover existing page relationships.** Use first-party query-page evidence and current ranking data to identify which URLs already receive impressions, clicks, or positions for each term.
3. **Propose initial clusters.** Group by user problem, intent, buyer stage, page type, and product or service fit.
4. **Test SERP overlap.** For important or borderline terms, compare ranking domains, URLs, content types, SERP features, and local-pack behavior. Shared wording is weaker evidence than shared result intent.
5. **Assign a page decision.** For each cluster choose exactly one primary state:
   - existing page to retain;
   - existing page to update or consolidate;
   - new page proposal;
   - local/location page proposal;
   - later or do-not-target.
6. **Detect cannibalization.** Flag cases where several URLs compete for the same query intent or where one URL serves incompatible intents. Use first-party query-page evidence when available rather than assuming from URL similarity.
7. **Respect site architecture.** Preserve existing route ownership, information architecture, localization rules, and design/content systems unless the user authorizes structural change.
8. **Create a minimal page brief.** State page type, searcher problem, primary intent, evidence, required sections, proof, internal links, conversion action, and content that must not be fabricated.
9. **Separate proposal from mutation.** URL creation, redirects, canonical changes, consolidation, deletion, tag replacement, saved-keyword updates, and publishing require explicit approval.
10. **Record uncertainty.** Label clusters directional when the query set, market sample, page inventory, or SERP evidence is incomplete. Unknown page relationships remain unknown rather than being forced into a cluster.

## Output Contract

Start with:

- number of supported clusters;
- existing pages to retain or update;
- proposed pages;
- cannibalization or consolidation issues;
- evidence gaps.

Then provide:

| Cluster | Primary intent | Primary keyword | Supporting terms | Current page evidence | Target page | Decision | Priority | Confidence | Caveat |
|---|---|---|---|---|---|---|---|---|---|

For each actionable cluster include a compact page brief and the evidence needed before implementation.

## Verification

- Every cluster has one primary intent and one explicit page decision.
- High-priority ambiguous terms were tested against current SERP evidence.
- Query-page first-party data was used when available.
- Existing and proposed URLs are clearly distinguished.
- Cannibalization findings identify the actual competing queries and pages.
- Local-pack and organic intent are not conflated.
- No page, redirect, canonical, deletion, saved-keyword, tracker, or publishing mutation occurred without approval.
- Page briefs contain truthful evidence requirements rather than invented claims.
- Unknown mappings are explicitly recorded rather than guessed.

## Failure Modes

- Clustering by embeddings or word similarity without search-intent evidence.
- Creating one page per keyword.
- Combining informational, commercial, navigational, and local intents indiscriminately.
- Declaring cannibalization because two pages mention the same topic.
- Proposing new pages without inspecting existing routes and content.
- Recommending consolidation or deletion without conversion and backlink evidence.
- Treating a directional sample as a complete site architecture.
- Mutating tags, URLs, redirects, or content as part of an analysis-only request.

## Provenance Boundary

This is an original first-party procedure distilled from reviewed OpenSEO clustering patterns. It copies no OpenSEO skill body, SERP response, keyword set, or page data.