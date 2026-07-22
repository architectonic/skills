---
type: SourceReview
title: Design Quality Skill Cluster Review
date: 2026-07-22
status: reviewed_for_distillation
sources: [Hallmark, Taste Skill, Transitions.dev]
tags: [skills, design, frontend, source-review, provenance, deduplication]
okf_version: "0.2"
---

# Design Quality Skill Cluster Review

## Decision

Distill the strongest procedures into first-party Architectonic skills. Do not vendor any of the three upstream skills wholesale and do not promote them directly into the reviewed core.

The three sources overlap heavily around anti-template interface work, but they serve different useful roles:

- Hallmark contributes structural variety, explicit audit/redesign/study separation, preservation rails, truthful content, token discipline, and pre-emit critique.
- Taste Skill contributes brief inference, audience and regulatory constraint recognition, audit-first redesign, design-system selection, dependency verification, and framework-aware implementation checks.
- Transitions.dev contributes concrete state-change matching, namespaced review/apply/refine verbs, shared motion tokens, reduced-motion guards, and implementation references.

The retained local shape is deliberately smaller:

- `skills/interface-design.md` — build or redesign within an existing project contract;
- `skills/interface-quality-audit.md` — audit only, with evidence and no silent edits;
- `skills/interface-transition-review.md` — motion review and state-transition contract;
- `dist/skills/frontend-ui-engineering/SKILL.md` — implementation-oriented engineering reference;
- `dist/skills/canvas-design/SKILL.md` — static visual-art procedure.

## Hallmark

- Repository: https://github.com/Nutlope/hallmark
- Reviewed revision: `aeb42fb354ff4efa36ab475773a082315a3af2ce`
- Reviewed skill blob: `e0715e9d8bf5fd12c6a31f677b181a212b4f2cf1`
- Upstream version: `1.1.0`
- License: MIT
- Decision: distill selected procedures; do not vendor wholesale.

### Retain

- Separate build, audit, redesign, and study intentions.
- Preserve routes, component ownership, copy intent, brand, information architecture, and implementation boundaries during redesign.
- Read existing tokens and project conventions before proposing a visual direction.
- Prevent fabricated metrics, testimonials, logos, or proof.
- Prefer structural specificity over theme-only variation.
- Verify responsive behavior, interactive states, accessibility, and token use.
- Require a pre-emit critique and a correction pass when evidence shows weak hierarchy, execution, specificity, restraint, or system fidelity.

### Reject or localize

- Do not require a named theme catalog or project rotation log.
- Do not stamp Hallmark branding or scores into production artifacts.
- Do not treat universal typography preferences as objective design law.
- Do not require all eight states for components that cannot semantically enter every state.
- Do not make URL study or external page fetching implicit; it remains an explicitly authorized research action.
- Do not let an anti-slop objective justify a broad rebuild.

## Taste Skill

- Repository: https://github.com/Leonxlnx/taste-skill
- Reviewed revision: `98565e65bc3274ddf6eb0838734341714057178b`
- Reviewed skill blob: `b72132fcd466da605623ffe96e370b3991fc5285`
- Upstream status: default v2 is explicitly experimental
- License: MIT
- Decision: distill selected procedures; do not vendor wholesale.

### Retain

- Infer page kind, audience, brand assets, reference signals, trust constraints, accessibility requirements, and regulatory context before choosing a visual direction.
- State a concise design read before implementation.
- Prefer an existing project design system and official packages when the project already depends on them.
- Distinguish official design systems from aesthetic inspiration.
- Inspect package versions and dependencies before adding libraries.
- Keep redesign work audit-first and bounded to the existing stack.
- Verify responsive layout mechanics and avoid fragile viewport or flex-math patterns.

### Reject or localize

- Do not use fixed default variance, motion, or density numbers as universal settings.
- Do not default every new project to React, Next.js, Tailwind, Motion, or a prescribed icon family.
- Do not ban a font, library, serif style, or visual device without project evidence.
- Do not make novelty or asymmetry an automatic quality criterion.
- Do not mix marketing-page guidance into dashboards, data tables, or product flows without an explicit fit check.
- Do not import the source's full token cost and opinionated implementation catalog into every interface task.

## Transitions.dev

- Repository: https://github.com/Jakubantalik/transitions.dev
- Reviewed revision: `047d036a79cc2ddecd868e7f1e3aa04b495644b2`
- Reviewed skill blob: `f39bc0538a612700638da314bd26fdd240c64d49`
- License: unclear. No root `LICENSE` file was found and the root `package.json` declares no license.
- Decision: reference and watch only; do not copy or redistribute snippets until licensing is explicit.

### Retain as original local procedure

- Start from the state change and communication purpose rather than an animation effect.
- Match the smallest coherent transition to the actual component and interaction.
- Separate review from mutation.
- Use shared duration and easing tokens based on usage, not numeric proximity.
- Require interruption, reversal, focus, responsive, performance, and reduced-motion behavior.
- Leave unmatched custom motion untouched rather than forcing it into a token.

### Do not copy

- CSS snippets, transition reference files, `_root.css`, or generated implementation payloads.
- Upstream command wording or catalog prose beyond factual source review.
- Premium or authenticated transition material.

## Existing registry decisions

### `frontend-design`

Lifecycle: blocked and superseded.

The packaged body forces an external `Created By Deerflow` link into every generated interface, requires `index.html` regardless of the host project, and encourages arbitrary aesthetic escalation. These are not acceptable default behaviors for a shared skill registry. The body remains preserved as imported evidence, but installers should not recommend it.

Superseded by: `skills/interface-design.md`.

### `frontend-ui-engineering`

Lifecycle: retained conditionally.

It contains useful component architecture, accessibility, state-management, responsive, and implementation guidance. It should run after design intent and project boundaries are known. It is not the canonical source of visual direction.

### `canvas-design`

Lifecycle: retained conditionally.

It is scoped to static visual artifacts and does not replace interface design or UI engineering. Its two-phase philosophy-to-canvas procedure remains distinct.

## Promotion gates

The three first-party interface skills remain outside `core/manifest.json` until they pass:

1. a greenfield component task;
2. an existing-project bounded redesign;
3. an audit-only task where no edits are made;
4. a responsive and accessible interface task;
5. a motion review with interruption and reduced-motion behavior;
6. comparison against the current packaged `frontend-design` and `frontend-ui-engineering` entries;
7. token-cost review showing the composed skills are smaller and more precise than wholesale upstream imports.

## Boundary

No upstream skill body or implementation snippet was copied into Architectonic. The resulting local procedures are original, source-attributed distillations governed by the repository's Apache-2.0 license. Hallmark and Taste license review permits adaptation with attribution; Transitions.dev remains reference-only pending an explicit upstream license.