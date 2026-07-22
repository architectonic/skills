---
type: SourceReview
title: SEO Evidence Skill Cluster Review
date: 2026-07-22
status: reviewed_for_distillation
sources: [OpenSEO Agent Skills, ai-seo, competitive-intel]
tags: [skills, seo, search, keywords, competitors, links, source-review, provenance, deduplication]
okf_version: "0.2"
---

# SEO Evidence Skill Cluster Review

## Decision

Distill OpenSEO's strongest evidence and mutation boundaries into connector-neutral first-party procedures. Do not vendor the OpenSEO skill bodies wholesale and do not make OpenSEO MCP a required dependency of the local skills.

Supersede the packaged `ai-seo` reference because it combines unverified origin, volatile platform descriptions, static percentages, unsupported performance claims, and references to package skills that are not present. Retain `competitive-intel` conditionally as a broader business-intelligence playbook distinct from SEO competitive research.

## OpenSEO Agent Skills

- Repository: https://github.com/every-app/open-seo
- Reviewed revision: `95e95d48cb88e60e1277422254e59c59b3e7e2e2`
- Reviewed release line: `0.1.1`
- License: MIT
- License blob: `d7d884f16474e989ff443e080f6e0d1ddb42c444`
- Decision: distill procedures and evidence boundaries; do not vendor wholesale.

### Reviewed bodies

- MCP documentation: `abf38dce6c99c66f6fd8cdd1b617688150079724`
- `seo-project-setup`: `9101f1479e128fb08296348b8041df03a9a654d8`
- `seo-coach`: `8688416662a6b72a4ae3ee69d285842907e8ecf3`
- `keyword-research`: `4bdfc40dd4a27756f3abbc291b7b1bfe1176699c`
- `keyword-clustering`: `0fbadf7564b3127dd9f87f4fd14f7e17c9bc4b39`
- `competitive-landscape`: `0883708810e7fae718da8bb8b12200d759efacb5`
- `competitor-analysis`: `1ca9333ba7e8f8233d4df6e6e29db3736f9bf719`
- `link-prospecting`: `e9b9fb7114c092e41dd06c6b6d0e0e77f3afd4eb`

### Retain

- Start with the user's business goal, audience, positioning, site scope, geography, language, and first-party evidence.
- Prefer Google Search Console or equivalent first-party data over third-party estimates for the user's own site.
- Separate keyword discovery, metrics, SERP inspection, clustering, page mapping, competitive landscape, named-competitor analysis, and link prospecting.
- Treat SERP intent and ranking-page overlap as stronger clustering evidence than lexical similarity.
- Distinguish SEO competitors from business competitors and organic winners from local-pack/Maps winners.
- Label third-party traffic, volume, difficulty, CPC, backlink, and ranking data as estimates or provider-specific measurements.
- Keep unknown values unknown rather than inventing metrics.
- Require explicit confirmation before saving keywords, replacing tags, creating trackers, sending outreach, or publishing changes.
- Record contact details only when found in public evidence and retain the source URL.
- Prefer a small, representative query set before expanding research cost.
- Make the output actionable: priority, target page, evidence, caveat, and next verification step.

### Correct or localize

- OpenSEO MCP is one optional adapter, not the definition of the skill.
- `projectId`, hosted login, account scopes, credits, and provider-specific tool names belong in an adapter profile, not the first-party procedure.
- Connector availability does not authorize authentication, account changes, data writes, credit consumption, or access to Search Console.
- Local workspaces, exports, briefs, reports, and strategy files must follow the project's existing knowledge and filesystem contract instead of assuming `~/SEO/`.
- Google Search Console, analytics, customer, and rank-tracking data can be commercially sensitive. Treat access, retention, exports, and sharing as private-data decisions.
- Search, crawling, browser automation, local-business lookup, contact discovery, and social-profile research remain terms-of-service, privacy, and rate-limit-sensitive.
- Backlink and contact research must not become mass scraping, purchased-link automation, spam outreach, or fabricated contact enrichment.
- Keyword saving is a connector mutation. It is not part of read-only research approval.
- A search result, contact page, or public email does not imply consent to automated outreach.

## Existing `ai-seo`

- Packaged body blob: `62339de9a8c7ff51f3e8ff682e4c5e80a3dbc89d`
- Declared source: `antigravity-awesome-skills / coreyhaines31 marketingskills`
- Declared source status: `adapted-origin-unverified`
- Decision: supersede and do not install.

### Findings

The body includes date-sensitive claims about current search products, crawler behavior, citation sources, AI Overview prevalence, click reduction, citation multipliers, optimization gains, third-party citation shares, and schema effects without recoverable source/version/date context. It also refers to `content-strategy` and `copywriting` skills that are not present in the package catalog.

The durable procedure is not a static collection of percentages. It is a current, source-backed visibility audit that:

- identifies the exact search or answer surfaces in scope;
- tests representative user queries;
- records citations and source types;
- separates observed answers from inference;
- verifies crawler/indexing configuration from current official documentation;
- checks content extractability, entity clarity, authorship, dates, evidence, and structured data;
- avoids claiming ranking or citation causality without an experiment.

Superseded by: `skills/ai-search-visibility-audit.md`.

## Existing `competitive-intel`

- Packaged body blob: `98f6624a256b7a3407bf7009390f0485ec3b59f5`
- Decision: retain conditionally as business intelligence, not as the SEO competitive workflow.

### Retain

- Direct, indirect, and future competitor categories.
- Decision-oriented outputs for sales, marketing, product, leadership, and boards.
- Win/loss evidence and the warning against competitor-driven roadmaps.
- One recoverable source of truth and an explicit review cadence.

### Conditions

- Current company, funding, hiring, customer, pricing, partnership, and social signals require current source verification.
- Customer wins/losses, CRM data, interview notes, and churn evidence may be confidential or personal data.
- Do not infer revenue, hiring intent, customer loss, roadmap, or strategic threat from one weak signal.
- Do not automate monitoring, account access, CRM writes, social collection, or distribution without separate authorization.
- SEO market overlap should use `skills/seo-competitive-research.md`, not this broad business playbook.

## First-party procedures

Create:

1. `skills/seo-project-context.md`
2. `skills/seo-keyword-opportunity-research.md`
3. `skills/seo-keyword-page-mapping.md`
4. `skills/seo-competitive-research.md`
5. `skills/seo-link-prospecting.md`
6. `skills/ai-search-visibility-audit.md`

These procedures remain outside `core/manifest.json` until utility evaluation passes. They may use OpenSEO, Search Console, another SEO provider, browser/search tools, or user exports, but each must disclose the actual evidence source and preserve provider-specific caveats.

## Promotion gates

1. project setup without writing files or connecting accounts unless authorized;
2. keyword research from first-party data and from provider-only estimates;
3. keyword-to-page mapping with ambiguous intent and cannibalization evidence;
4. market-level and named-competitor research with clear scope separation;
5. link prospecting where no contact is found and no details are invented;
6. local SEO where organic and Maps evidence disagree;
7. AI-search visibility review requiring current official documentation;
8. mutation tests proving save/tag/tracker/outreach/publish actions remain separately gated;
9. cost/token review against wholesale OpenSEO skill installation;
10. one negative test where insufficient evidence produces a bounded unknown rather than a confident recommendation.

## Boundary

No OpenSEO skill body, API implementation, MCP configuration, customer data, keyword data, SERP data, contact detail, or provider response was copied into the first-party procedures. Existing imported package bodies remain unchanged. Catalog decisions alter routing and installation guidance only.