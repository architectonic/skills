---
type: Skill
title: SEO Competitive Research
description: Use when identifying who wins a search market or analyzing one named domain's organic, local, content, keyword, SERP, and authority evidence without confusing search competitors with business competitors.
tags: [skill, seo, competitors, serp, keywords, backlinks, local-seo, market-research, evidence, verification, okf]
timestamp: 2026-07-22T00:00:00-03:00
okf_version: "0.2"
source_status: distilled-reviewed
source_name: Architectonic synthesis of reviewed OpenSEO competitive landscape and competitor analysis workflows
source_url: https://github.com/architectonic/skills/blob/main/sources/reviewed/2026-07-22-seo-evidence-cluster.md
source_revision: open-seo@95e95d48cb88e60e1277422254e59c59b3e7e2e2; competitive-landscape@0883708810e7fae718da8bb8b12200d759efacb5; competitor-analysis@1ca9333ba7e8f8233d4df6e6e29db3736f9bf719
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

# SEO Competitive Research

## Trigger

Use when identifying who wins a search market or analyzing one named domain's organic, local, content, keyword, SERP, and authority evidence without confusing search competitors with business competitors.

Choose one mode:

- **landscape** — several domains across a representative query set;
- **named competitor** — one domain examined deeply;
- **head-to-head** — the user's site compared with one or more domains.

Use the broader `competitive-intel` playbook for pricing, funding, hiring, sales, roadmap, and company-strategy intelligence.

## Purpose

Turn current search evidence into a bounded market or competitor decision while preserving domain-type distinctions, provider uncertainty, first-party baselines, local-search differences, and content-truth constraints.

## Inputs

- SEO project context.
- Mode and decision question.
- User domain when relevant.
- Market, product, category, topic, seed queries, or named competitor.
- Geography, language, device, and local-search scope.
- First-party user-site data when available.
- Approved SERP, keyword, domain, local, and backlink providers.
- Current web evidence when page/content claims are required.

## Procedure

1. **Define the comparison.** State whether the task is landscape, named competitor, or head-to-head and what decision it must support.
2. **Build a representative query set.** Include relevant informational, commercial, comparison, transactional, tool, and local intents. Keep the first sample small enough to inspect.
3. **Anchor the user's position.** For the user's own site, prefer first-party clicks, impressions, CTR, position, conversions, and actual ranking URLs over third-party traffic estimates.
4. **Identify recurring search competitors.** Use query overlap and current SERPs. Classify each domain as direct product competitor, publisher, marketplace, directory, community, documentation source, local business, or another type.
5. **Inspect footprint.** Record provider-estimated ranking keywords, pages, traffic, authority, backlinks, local visibility, and trends with provider/date/market caveats.
6. **Inspect pages before content claims.** Use current SERP or web evidence to determine page type, content structure, positioning, proof, freshness, and search intent. Keyword rows alone do not prove a content pattern.
7. **Separate organic and local evidence.** For location-sensitive work, inspect Maps/local-pack and organic results independently.
8. **Assess authority carefully.** Use backlink/referring-domain evidence when available, but do not assume authority explains every ranking difference or that provider data is complete.
9. **Find actionable gaps.** Identify underserved intent, weak answers, missing formats, stale pages, poor local coverage, evidence gaps, and opportunities aligned with the user's actual product.
10. **Reject imitation.** Recommend a stronger answer, asset, proof, structure, or positioning—not copied content or a competitor-driven roadmap.
11. **State confidence.** Label findings directional when the query sample, provider coverage, market scope, or page inspection is limited.

## Output Contract

Start with:

- market or competitor read;
- strongest search competitors and their types;
- most defensible opportunity;
- largest barrier;
- confidence and data limitations.

Then provide:

| Domain | Domain type | Query overlap | Evidence source | Winning pages/themes | Authority/local signal | Gap | Recommended response | Confidence |
|---|---|---|---|---|---|---|---|---|

For a named competitor include a separate section for lessons, vulnerabilities, pages/queries to pursue, and patterns not to copy.

## Verification

- The research mode and decision question are explicit.
- The query set and market scope are recorded.
- SEO competitors are distinguished from business competitors.
- User-site first-party evidence is distinguished from provider estimates.
- Page/content claims are backed by page or SERP evidence.
- Organic and local-pack conclusions are separated.
- Traffic, backlinks, authority, and rankings retain provider/date caveats.
- No competitor content, customer data, credentials, monitoring, tracker, report distribution, or publishing action was copied or mutated without authorization.

## Failure Modes

- Treating a named business competitor as a search competitor without overlap evidence.
- Treating publishers, directories, or communities as direct product competitors.
- Inferring content strategy from keyword rows alone.
- Presenting provider traffic or authority values as exact.
- Using national organic metrics to explain local-pack performance.
- Expanding a small query sample into a complete market claim.
- Recommending copied content, features, or positioning.
- Mixing confidential win/loss or CRM evidence into public SEO research.
- Automating competitor monitoring or account access without explicit scope.

## Provenance Boundary

This is an original first-party procedure distilled from reviewed OpenSEO competitive-search workflows. It copies no OpenSEO skill body, competitor data, SERP response, or provider metric.