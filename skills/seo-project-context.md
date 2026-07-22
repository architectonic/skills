---
type: Skill
title: SEO Project Context
description: Use when beginning or resuming SEO work for a site and the agent needs a durable, evidence-aware project context before researching keywords, competitors, pages, links, or search visibility.
tags: [skill, seo, project-context, search-console, positioning, goals, evidence, privacy, verification, okf]
timestamp: 2026-07-22T00:00:00-03:00
okf_version: "0.2"
source_status: distilled-reviewed
source_name: Architectonic synthesis of reviewed OpenSEO project setup and coaching workflows
source_url: https://github.com/architectonic/skills/blob/main/sources/reviewed/2026-07-22-seo-evidence-cluster.md
source_revision: open-seo@95e95d48cb88e60e1277422254e59c59b3e7e2e2; seo-project-setup@9101f1479e128fb08296348b8041df03a9a654d8; seo-coach@8688416662a6b72a4ae3ee69d285842907e8ecf3
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

# SEO Project Context

## Trigger

Use when beginning or resuming SEO work for a site and the agent needs a durable, evidence-aware project context before researching keywords, competitors, pages, links, or search visibility.

Do not run a full audit merely because context is incomplete. Collect only the information required for the next SEO decision.

## Purpose

Create or recover the smallest sufficient SEO context so later workflows can distinguish business goals, site scope, first-party evidence, provider estimates, assumptions, preferences, and unresolved questions.

## Inputs

- Site or domain in scope.
- Business, product, service, audience, and positioning material.
- Target countries, languages, cities, or service areas.
- Current site state: new, established, migrating, redesigned, or recovering.
- User goal and measurable outcome.
- Existing SEO notes, reports, exports, content inventories, keyword sets, and competitor lists.
- Available first-party sources such as Search Console, analytics, CRM, conversions, or rank tracking.
- Available provider or connector tools and their account/project scope.
- Existing project knowledge and filesystem conventions.

## Procedure

1. **Inspect existing context first.** Read project instructions, knowledge files, prior reports, saved searches, site configuration, sitemap, and relevant business documents before asking questions.
2. **Define site scope.** Record the primary domain, relevant subdomains, products, services, categories, locations, languages, and excluded areas.
3. **Define the business outcome.** Translate vague goals into one or more measurable outcomes such as qualified organic leads, non-branded signups, revenue, local enquiries, recovery, or visibility for named page groups.
4. **Capture positioning.** Record audience, problem, differentiated value, alternatives, strongest customers, bad-fit users, proof, and claims that require evidence.
5. **Inventory first-party evidence.** Identify Search Console, analytics, conversions, existing rankings, customer questions, internal search, and content performance. Mark each source as connected, exported, unavailable, stale, or unverified.
6. **Inventory external evidence.** Record SEO providers, SERP tools, local-search data, backlink tools, browser/search access, and their geographic, language, freshness, and estimation boundaries.
7. **Resolve connector scope.** When an authenticated connector is available, confirm the current account, project, property, and approved scopes using read-only identity/list operations. Do not run research merely to test connectivity.
8. **Protect private data.** Treat Search Console, analytics, conversions, CRM, customer, contact, and ranking exports as private project data. Record retention and sharing constraints before writing or exporting them.
9. **Choose the next workflow.** Recommend exactly one primary next action based on the evidence gap: keyword opportunity research, keyword-to-page mapping, competitive research, link prospecting, AI-search visibility, technical/index inspection, or no SEO action yet.
10. **Write only with authorization.** If durable files are requested, follow the project's existing knowledge structure. Do not create a parallel `SEO/` hierarchy when the repository already defines where context belongs.

## Output Contract

Record:

1. site and market scope;
2. business goal and success measure;
3. positioning and audience;
4. first-party evidence inventory;
5. provider and connector inventory;
6. privacy, retention, and sharing constraints;
7. known competitors and alternatives;
8. existing content and page inventory;
9. assumptions and unresolved questions;
10. one recommended next workflow.

## Verification

- The domain, geography, language, audience, and business outcome are explicit.
- First-party measurements are separated from third-party estimates.
- Connector account/project scope is confirmed rather than assumed.
- Missing exports or integrations are not represented as available.
- Private data boundaries are recorded.
- No files, accounts, integrations, tags, trackers, or research jobs were created without authorization.
- The next workflow is tied to a specific decision, not a generic request to "do SEO."

## Failure Modes

- Asking the user to repeat information already present in project documents.
- Creating a new workspace that competes with the project's canonical knowledge structure.
- Treating a connected account as authorization to read every property or dataset.
- Claiming Search Console or analytics is connected without evidence.
- Starting broad keyword research before defining the business outcome.
- Treating traffic as the goal when conversions or qualified demand matter.
- Mixing private first-party data into public reports or prompts.
- Producing a large SEO plan when one next evidence-gathering step is sufficient.

## Provenance Boundary

This is an original first-party procedure distilled from reviewed OpenSEO setup and coaching patterns and Architectonic source-first knowledge doctrine. No OpenSEO skill body, MCP configuration, customer data, or provider response was copied.