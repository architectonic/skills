---
type: Skill
title: Interface Design
description: Use when building or redesigning a user-facing component, section, page, flow, or application where design intent, project boundaries, truthful content, system fidelity, accessibility, and implementation verification must remain coherent.
tags: [skill, design, frontend, interface, design-system, accessibility, responsive, implementation, verification, okf]
timestamp: 2026-07-22T00:00:00-03:00
okf_version: "0.2"
source_status: distilled-reviewed
source_name: Architectonic synthesis of reviewed Hallmark, Taste Skill, Transitions.dev patterns and local design-system doctrine
source_url: https://github.com/architectonic/skills/blob/main/sources/reviewed/2026-07-22-design-quality-cluster.md
source_revision: hallmark@aeb42fb354ff4efa36ab475773a082315a3af2ce; taste-skill@98565e65bc3274ddf6eb0838734341714057178b; transitions.dev@047d036a79cc2ddecd868e7f1e3aa04b495644b2
license: Apache-2.0
source_license_status: hallmark-mit; taste-skill-mit; transitions-reference-only-license-unclear
domain: design
artifact_kind: skill
target_surfaces: [skills, design-system, click-blue, workframe]
risk_level: medium
requires_review: false
review_status: source_reviewed_utility_evaluation_pending
---

# Interface Design

## Trigger

Use when building or redesigning a user-facing component, section, page, flow, or application where design intent, project boundaries, truthful content, system fidelity, accessibility, and implementation verification must remain coherent.

Use `interface-quality-audit` instead when the requested deliverable is critique only. Use `interface-transition-review` when motion is the primary question. Use a static visual-art skill rather than this skill for posters, illustrations, or standalone image/PDF compositions.

## Purpose

Translate a product brief and an existing project context into a specific, production-quality interface without falling back to a generic template, forcing a fashionable aesthetic, inventing content, or bulldozing the codebase.

Distinctive design means the structure and interaction fit the product. It does not mean maximum novelty, animation, asymmetry, ornament, or implementation complexity.

## Inputs

- User goal and primary task.
- Intended audience and context of use.
- Requested scope: component, section, page, flow, or application.
- Existing repository, routes, components, dependencies, styles, and tests when present.
- Brand assets, content, design tokens, design-system package, `DESIGN.md`, or equivalent contract.
- Platform, accessibility, responsive, performance, and regulatory constraints.
- Reference images or URLs only when the user supplied or explicitly authorized their use.

## Procedure

### 1. Resolve scope

Classify the work as one of:

- **component** — one reusable control or display unit;
- **section** — one bounded region inside an existing page;
- **page** — one route or complete document;
- **flow** — several states or routes forming one user task;
- **application** — a broader product surface requiring architecture and design-system decisions.

Do not apply page-level hero, navigation, footer, or visual-story machinery to a component request. When ambiguity materially changes the work, ask one consequential question; otherwise choose the smallest plausible scope.

### 2. Inspect before designing

When a project exists, inspect before proposing a direction:

1. route and component ownership;
2. design tokens and shared primitives;
3. typography and icon families;
4. existing spacing, radius, colour, elevation, and motion scales;
5. framework and dependency versions;
6. responsive conventions;
7. accessibility and test infrastructure;
8. content and brand assets;
9. strong existing decisions that should remain unchanged.

An established design system outranks an external style preference unless the user explicitly asks to replace it.

### 3. State the design read

Write one concise design read containing:

- interface kind;
- audience;
- primary task;
- trust or regulatory posture;
- intended design language;
- existing system or implementation foundation;
- degree of preservation versus change.

Base it on evidence from the brief and project. Do not select an extreme aesthetic merely to make the result appear distinctive.

### 4. Set the preservation boundary

Before editing an existing project, state the files expected to change and what must remain stable:

- routes and URLs;
- component ownership and public APIs;
- data and state behavior;
- content intent;
- brand assets;
- accessibility behavior;
- test contracts.

Deleting production files, removing routes, replacing a component hierarchy, migrating frameworks, or introducing a new design system requires explicit authorization.

### 5. Design structure before surface

Define:

1. information priority;
2. primary and secondary actions;
3. grouping and sequence;
4. component or section hierarchy;
5. responsive collapse behavior;
6. empty, loading, success, warning, and failure states that are semantically applicable.

Avoid automatic template rhythms such as centered hero → equal feature cards → CTA → footer when the content does not require them. Structural variety must come from the task and information architecture, not from random composition.

### 6. Lock the system

Use existing semantic tokens and components. When a new value or primitive is justified, add it to the shared system rather than improvising raw values throughout the implementation.

Keep one coherent:

- type system;
- icon family;
- spacing scale;
- radius logic;
- surface hierarchy;
- status language;
- motion language.

Do not ban or replace a font, library, colour, or component merely because it is common. Replace it only when it conflicts with the product, brand, accessibility, or system contract.

### 7. Keep content truthful

Do not invent metrics, customer counts, testimonials, logos, awards, case studies, quotes, or claims.

When evidence is missing, use one of:

- an explicitly labelled placeholder;
- neutral structural copy;
- a layout that does not depend on the missing proof;
- a request for the missing material when it blocks completion.

Do not copy prose from reference documents or external pages unless the user explicitly authorizes verbatim use.

### 8. Implement within the existing stack

- Preserve the current framework and styling approach unless change is authorized.
- Inspect dependency files before importing a package.
- Prefer existing primitives over new dependencies.
- Keep component boundaries focused and composable.
- Separate data behavior from presentation when the repository already follows that pattern.
- Do not force an `index.html`, framework, CSS system, icon library, attribution link, watermark, or generated signature onto an incompatible project.

### 9. Define interaction states

Every interactive element must implement the states it can actually enter. Typical states include:

- default;
- hover where pointer input exists;
- focus-visible;
- active or pressed;
- selected or expanded;
- disabled;
- loading;
- error;
- success.

Do not manufacture semantically impossible states merely to satisfy a checklist. State must remain understandable without colour alone.

### 10. Treat motion as state communication

Use motion only when it improves continuity, spatial understanding, feedback, progress, or attention.

For consequential motion, apply `interface-transition-review` and document:

- trigger;
- start and end state;
- duration and easing token;
- animated properties;
- interruption and reversal behavior;
- focus behavior;
- reduced-motion alternative;
- performance verification.

Do not add animation because a static hierarchy is weak.

### 11. Verify responsive and accessible behavior

At minimum, verify:

- no unintended horizontal overflow;
- readable line lengths and wrapping;
- stable grid and flex behavior with long content;
- keyboard order and visible focus;
- semantic controls and labels;
- contrast and non-colour state cues;
- target size;
- dialog and overlay focus behavior;
- reduced-motion behavior;
- loading, empty, error, and recovery paths;
- content at the project's supported breakpoints.

Use actual repository breakpoints when defined. Do not impose arbitrary viewport lists as a substitute for testing the supported system.

### 12. Run a pre-emit critique

Before declaring completion, evaluate the implementation on:

1. task fit;
2. hierarchy;
3. system fidelity;
4. specificity to the product;
5. restraint;
6. accessibility;
7. functional completeness;
8. responsive robustness.

Revise failed areas before delivery. Keep the critique in the work report or verification evidence; do not stamp internal scores or external branding into production artifacts.

### 13. Verify the implementation

Use the strongest available evidence:

- build, typecheck, lint, and relevant tests;
- rendered inspection;
- keyboard interaction;
- responsive inspection;
- state coverage;
- accessibility checks;
- console and network errors;
- before/after evidence for redesign work.

Do not claim visual or interaction quality from source inspection alone when the interface can be rendered.

## Output Contract

Return or record:

1. scope classification;
2. design read;
3. evidence inspected;
4. preservation boundary;
5. structural and system decisions;
6. files changed;
7. state and motion contracts;
8. responsive and accessibility evidence;
9. tests and rendered verification;
10. unresolved limitations.

## Verification

- The interface solves the stated user task.
- Existing project and design-system boundaries were respected.
- The structure follows content priority rather than a default template.
- Content and proof are truthful or explicitly marked unresolved.
- Shared tokens and primitives are used consistently.
- Applicable interaction states are complete.
- Responsive, keyboard, focus, and reduced-motion behavior were inspected.
- No external attribution, watermark, or technology preference was inserted without user authorization.
- The implementation was rendered and tested when tooling allowed it.

## Failure Modes

- Replacing context with an aesthetic preset.
- Treating novelty as quality.
- Rebuilding an existing interface without a preservation boundary.
- Applying landing-page advice to product UI or data-heavy surfaces.
- Inventing proof to make a composition work.
- Forcing a preferred framework, font, icon family, motion library, or file layout.
- Using anti-template rhetoric to justify visual noise.
- Copying an admired interface rather than extracting general principles.
- Shipping only the default state of an interactive element.
- Adding motion instead of repairing hierarchy.
- Declaring success without rendered evidence.

## Provenance Boundary

This is an original first-party procedure distilled after reviewing Hallmark, Taste Skill, Transitions.dev, the existing Architectonic registry, and local design-system doctrine. It does not copy an upstream skill body or implementation snippet. The exact source review and license decisions are recorded in `sources/reviewed/2026-07-22-design-quality-cluster.md`.