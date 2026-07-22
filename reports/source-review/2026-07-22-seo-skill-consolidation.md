---
type: SourceReviewReport
title: SEO Skill Consolidation
date: 2026-07-22
status: merged_to_main
branch: agent/seo-skill-consolidation
sources: [OpenSEO Agent Skills, ai-seo, competitive-intel]
tags: [skills, seo, search, source-review, lifecycle, privacy, validation]
okf_version: "0.2"
---

# SEO Skill Consolidation

## Decision

Distill the reviewed OpenSEO workflows into six provider-neutral first-party skills. Keep OpenSEO MCP as an optional authenticated data adapter rather than a mandatory runtime dependency. Supersede the existing `ai-seo` reference and retain `competitive-intel` conditionally for broad business intelligence.

## Source evidence

### OpenSEO

- reviewed revision: `95e95d48cb88e60e1277422254e59c59b3e7e2e2`;
- observed release line: `0.1.1`;
- license: MIT;
- license blob: `d7d884f16474e989ff443e080f6e0d1ddb42c444`;
- reviewed MCP documentation and seven skill bodies;
- decision: distill; do not vendor wholesale.

OpenSEO's reviewed workflows correctly:

- start from first-party Search Console evidence when available;
- preserve unknown metrics;
- distinguish provider estimates from observed data;
- use SERP intent and overlap rather than lexical similarity alone;
- distinguish business competitors, SEO competitors, publishers, directories, communities, organic results, and local packs;
- require confirmation before saving keywords;
- require public evidence for contact details.

The local skills remove assumptions about `projectId`, hosted login, OpenSEO account scope, credit model, fixed tool names, and a separate `~/SEO/` workspace.

### Existing `ai-seo`

- body blob: `62339de9a8c7ff51f3e8ff682e4c5e80a3dbc89d`;
- source status: `adapted-origin-unverified`;
- decision: superseded, do-not-install;
- replacement: `skills/ai-search-visibility-audit.md`.

The body embeds volatile, unsupported platform descriptions, crawler lists, prevalence percentages, traffic-loss claims, citation multipliers, optimization gains, and citation-source shares. It also references `content-strategy` and `copywriting` skills that are not present in the package.

### Existing `competitive-intel`

- body blob: `98f6624a256b7a3407bf7009390f0485ec3b59f5`;
- decision: reviewed, conditional, medium risk;
- retained scope: broad company, positioning, sales, product, and leadership intelligence;
- excluded scope: SEO market and ranking analysis, which routes to `skills/seo-competitive-research.md`.

Current funding, hiring, pricing, partnership, customer, win/loss, churn, CRM, and social evidence requires freshness, privacy, confidentiality, and authorization review.

## First-party working source

Added:

1. `skills/seo-project-context.md`
2. `skills/seo-keyword-opportunity-research.md`
3. `skills/seo-keyword-page-mapping.md`
4. `skills/seo-competitive-research.md`
5. `skills/seo-link-prospecting.md`
6. `skills/ai-search-visibility-audit.md`

All six:

- use pinned reviewed-source revisions;
- declare `source_content_copied: false`;
- remain outside `core/manifest.json`;
- preserve provider and evidence provenance;
- separate first-party measurements from provider estimates;
- gate connector and external-system mutations.

## Mutation boundaries

Separate authorization is required before:

- connecting an authenticated SEO or Search Console account;
- changing account/project scopes;
- consuming paid credits beyond an approved budget;
- saving or retagging keywords;
- creating rank trackers;
- writing project files when not requested;
- crawling or scraping external sites;
- collecting or enriching contacts;
- writing to CRM or outreach systems;
- sending outreach or follow-ups;
- changing URLs, redirects, canonicals, robots, schema, or page content;
- publishing or distributing reports.

A read-only research request does not authorize any of those actions.

## Catalog decisions

| Entry | Lifecycle | Install | Replacement/scope |
|---|---|---|---|
| `ai-seo` | superseded | do-not-install | `skills/ai-search-visibility-audit.md` |
| `competitive-intel` | reviewed | conditional | broad business intelligence only |

Total deep package decisions after this batch: 13.

## Boundaries

- No OpenSEO skill body or MCP implementation was copied.
- No provider, connector, authenticated account, Search Console property, keyword dataset, SERP result, backlink dataset, local-business dataset, or contact detail was accessed.
- No keyword, tag, tracker, contact, CRM item, message, page, redirect, schema, crawler rule, or report destination was mutated.
- No imported package body was edited.
- No new skill was promoted into the reviewed core.
- No npm publication was attempted.

## Acceptance tests

| Test | Expected |
|---|---|
| Thirteen deep catalog decisions are applied | Pass in PR validation |
| `ai-seo` is superseded and do-not-install | Pass in PR validation |
| `competitive-intel` is conditional and business-scoped | Pass in PR validation |
| Six first-party SEO skills have pinned reviewed provenance | Pass in PR validation |
| Link prospecting preserves public-source and no-send boundaries | Pass in PR validation |
| Keyword skills preserve unknowns and gate saved-data mutations | Pass in PR validation |
| AI visibility audit avoids static unsupported platform statistics | Pass in PR validation |
| OpenSEO exact revision and MIT license evidence are present | Pass in PR validation |
| Prior classification, design, and video decisions remain intact | Pass in PR validation |

## Next justified action

After validation and merge:

1. evaluate the local SEO skills against provider-neutral fixtures and optional OpenSEO fixtures;
2. inspect other packaged marketing skills before adding OpenClaw marketing sources;
3. continue metadata repair separately in bounded clusters;
4. defer OpenSEO application/MCP deployment to the later Workframe integration pass.
