---
type: Skill
title: Interface Quality Audit
description: Use when an implemented or generated interface is functional but may be generic, visually incoherent, weakly hierarchical, inaccessible, or disconnected from its design system and brand context.
tags: [skill, design, interface, audit, hierarchy, brand, accessibility, anti-template, verification, okf]
timestamp: 2026-07-22T00:00:00-03:00
okf_version: "0.2"
source_status: distilled_candidate
source_name: Architectonic synthesis of Hallmark, Taste Skill, Kill AI Slop, and local design-system doctrine
source_url: https://github.com/Nutlope/hallmark
source_revision: unpinned-review-required
license: Apache-2.0
source_license_status: upstream-review-pending
domain: design
artifact_kind: skill
target_surfaces: [skills, design-system, click-blue, workframe]
risk_level: low
requires_review: false
review_status: utility_evaluation_pending
---

# Interface Quality Audit

## Trigger

Use when an implemented or generated interface is functional but may be generic, visually incoherent, weakly hierarchical, inaccessible, or disconnected from its design system and brand context.

## Purpose

Produce an evidence-backed interface critique that distinguishes structural defects from subjective preference and identifies the smallest coherent set of improvements.

This is an audit skill. It does not silently redesign or rewrite the interface.

## Inputs

- Rendered interface, screenshots, or a reproducible local page.
- Relevant source code when available.
- Product goal, primary user task, and intended audience.
- Brand, design-system, or `DESIGN.md` contract when one exists.
- Accessibility, platform, and responsive constraints.

## Procedure

1. **Establish intent.** State the page purpose, primary action, secondary actions, and information that must be understood first.
2. **Inspect hierarchy.** Check whether size, position, density, contrast, grouping, and sequence consistently express that intent.
3. **Inspect design-system fidelity.** Identify raw values, local exceptions, duplicated components, inconsistent states, or styling that bypasses shared tokens and primitives.
4. **Inspect specificity.** Identify generic template signals that are unsupported by the product: interchangeable hero copy, card walls, decorative pills, arbitrary gradients, uniform rounded containers, filler icons, dashboard chrome without a task need, and stock motion.
5. **Inspect composition.** Check alignment, spacing rhythm, line length, content density, responsive behavior, empty states, and whether related information is perceptually grouped.
6. **Inspect interaction states.** Check hover, focus, active, selected, loading, disabled, empty, success, warning, and failure states. Confirm that state is not communicated by colour alone.
7. **Inspect content quality.** Flag vague labels, duplicated explanation, placeholder language, unsupported claims, and copy that describes the UI instead of helping the user act.
8. **Inspect accessibility.** Check keyboard order, visible focus, semantic structure, contrast, target size, reduced motion, screen-reader labels, and error association.
9. **Separate findings.** Classify each issue as functional, accessibility, hierarchy, system consistency, content, brand specificity, or subjective preference.
10. **Prioritize.** Rank corrections by user impact, recurrence, implementation cost, and whether fixing one shared primitive resolves several symptoms.
11. **Recommend a bounded pass.** Specify the minimum set of changes that creates a coherent improvement. Do not recommend novelty for its own sake.

## Output Contract

Return:

1. interface intent;
2. evidence reviewed;
3. critical defects;
4. system-level defects;
5. generic or unsupported patterns;
6. accessibility findings;
7. prioritized corrections;
8. elements that should remain unchanged;
9. unresolved questions or missing evidence.

Each finding must identify the observed evidence and explain why it impairs the intended task or violates an explicit contract.

## Verification

- The audit can be traced to rendered evidence, code, or a stated design contract.
- Functional and accessibility issues are not presented as aesthetic preference.
- Subjective observations are labelled as such.
- The recommended pass is smaller and more coherent than a wholesale redesign.
- Shared-system corrections are preferred over one-off cosmetic patches.
- The audit preserves strong existing decisions instead of forcing a fashionable style.

## Failure Modes

- Treating personal taste as an objective defect.
- Replacing one generic style with another.
- Recommending gradients, motion, cards, or ornament without a task or brand reason.
- Ignoring content and interaction state while critiquing surface styling.
- Auditing screenshots without checking responsive and interactive behaviour when code is available.
- Declaring a design successful because it resembles a popular product.
- Expanding scope into implementation without explicit authorization.

## Provenance Boundary

This is an original local procedure distilled from public design-audit patterns and Architectonic design doctrine. It does not copy an upstream skill body. Before citing or adapting any upstream implementation details, record its exact revision and license separately.
