---
type: Skill
title: Recent Source Research
description: Use when a question depends on developments within a defined recent window, social bookmarks are hard to resolve, or stale knowledge would materially change the answer.
tags: [skill, research, recency, source-resolution, bookmarks, evidence, provenance, verification, okf]
timestamp: 2026-07-22T00:00:00-03:00
okf_version: "0.2"
source_status: distilled_candidate
source_name: Architectonic synthesis of Last30Days-style research and source-grounding doctrine
source_url: https://github.com/mvanhorn/last30days-skill
source_revision: unpinned-review-required
license: Apache-2.0
source_license_status: upstream-review-pending
domain: research
artifact_kind: workflow
target_surfaces: [skills, architectonic, click-blue, workframe]
risk_level: medium
requires_review: true
review_status: provider_and_terms_review_required
---

# Recent Source Research

## Trigger

Use when:

- the answer depends on developments within a defined recent window;
- a social bookmark has no readable body;
- a tool, repository, product, price, API, law, model, or standard may have changed;
- the user asks what appeared, changed, launched, or became relevant recently;
- stale internal knowledge could materially alter the conclusion.

## Purpose

Build a bounded, date-aware evidence set that resolves canonical sources, distinguishes event dates from publication dates, and labels unresolved items rather than filling gaps with inference.

## Inputs

- Research question.
- Absolute start and end dates.
- Candidate bookmarks, names, repositories, domains, or search terms.
- Required source hierarchy and excluded sources.
- Desired output: answer, candidate queue, comparison, or change report.

## Procedure

1. **Resolve the window.** Convert relative dates into exact dates and record the timezone when it matters.
2. **Define the claims.** Split the request into concrete facts or decisions that need current evidence.
3. **Establish source hierarchy.** Prefer canonical repositories, official documentation, release notes, papers, registries, and first-party product pages. Use social posts primarily to discover the linked source.
4. **Resolve identity.** Confirm that names, repositories, packages, domains, and accounts refer to the same entity before combining evidence.
5. **Search by source and concept.** Use exact URLs and identifiers first, then names, quoted phrases, linked domains, repository traces, and account-plus-topic searches.
6. **Separate dates.** Record publication date, update date, release date, and actual event date independently. Do not call an old event new because a recent page mentions it.
7. **Inspect primary artifacts.** Read the relevant README, changelog, release, source file, skill file, paper, or official documentation rather than relying on snippets.
8. **Resolve inaccessible social posts.** Try indexed references, linked domains, repository announcements, quoted identifiers, and account-topic searches. Do not infer the exact post from the account's general activity.
9. **Deduplicate.** Normalize canonical URL, repository, package, artifact name, capability, and source revision. Distinguish a new source from a genuinely new capability.
10. **Classify confidence.** Mark each item resolved, partially resolved, tentative, or unresolved and state why.
11. **Check freshness and maintenance.** Record last meaningful update, release cadence, active maintenance evidence, and whether the recent change affects the requested use case.
12. **Capture risk and rights.** Record license, executable dependencies, credentials, external calls, data movement, and redistribution uncertainty where applicable.
13. **Produce a decision-oriented result.** Explain what is new, what already existed, what changed materially, what remains uncertain, and what action is justified.

## Output Contract

Return:

1. exact research window;
2. claims investigated;
3. canonical sources and revisions;
4. resolved findings;
5. duplicates or previously known items;
6. tentative and unresolved items with attempted resolution paths;
7. maintenance, license, risk, and compatibility notes;
8. recommended next actions.

For candidate discovery, every record should include canonical identity, artifact kind, target surface, dedupe status, confidence, risk, and next review gate.

## Verification

- Every time-sensitive conclusion is tied to an exact date and recoverable source.
- Canonical sources support the claims attributed to them.
- Social posts are not treated as the sole evidence when a linked primary artifact exists.
- Event date and publication date are not conflated.
- Duplicate sources and duplicate capabilities are reported separately.
- Unresolved items remain unresolved; no plausible story is substituted for evidence.
- The result covers the full requested window rather than only the most visible recent item.

## Failure Modes

- Searching only the product or repository name without the date window.
- Treating search ranking, stars, or social engagement as evidence of utility.
- Declaring an inaccessible post deleted without confirmation.
- Inferring an exact bookmark from unrelated posts by the same account.
- Calling a repository new because it was recently copied, forked, or re-uploaded.
- Importing a skill before checking whether the capability already exists locally.
- Failing to record exact source revision and license.
- Producing a long link list without a decision or integration recommendation.

## Risk Boundary

Research providers, social APIs, browser sessions, private bookmarks, and authenticated sources may expose credentials or personal data. Use only approved access, preserve terms and privacy boundaries, and keep any external publication or account mutation outside this skill.

## Provenance Boundary

This is an original local procedure distilled from recent-source research patterns and Architectonic source-grounding doctrine. It does not copy an upstream skill body. Provider-specific behavior requires separate source, license, and security review.
