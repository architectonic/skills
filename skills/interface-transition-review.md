---
type: Skill
title: Interface Transition Review
description: Use when adding or reviewing interface motion so transitions communicate state, preserve continuity, remain interruptible, and degrade safely for reduced-motion users.
tags: [skill, design, motion, transitions, accessibility, reduced-motion, performance, verification, okf]
timestamp: 2026-07-22T00:00:00-03:00
okf_version: "0.2"
source_status: distilled-reviewed
source_name: Architectonic synthesis of reviewed Transitions.dev patterns and local design-system doctrine
source_url: https://github.com/architectonic/skills/blob/main/sources/reviewed/2026-07-22-design-quality-cluster.md
source_revision: transitions.dev@047d036a79cc2ddecd868e7f1e3aa04b495644b2; skill-blob@f39bc0538a612700638da314bd26fdd240c64d49
license: Apache-2.0
source_license_status: upstream-license-unclear-reference-only-no-content-copied
domain: design
artifact_kind: skill
target_surfaces: [skills, design-system, workframe]
risk_level: low
requires_review: false
review_status: source_reviewed_utility_evaluation_pending
---

# Interface Transition Review

## Trigger

Use when adding or reviewing interface motion so transitions communicate state, preserve continuity, remain interruptible, and degrade safely for reduced-motion users.

## Purpose

Treat motion as state communication rather than decoration. Define transitions from explicit before-and-after states, then verify accessibility, continuity, responsiveness, and performance.

## Inputs

- Interaction or state change being reviewed.
- Start state and end state.
- Trigger, cancellation, and interruption behaviour.
- Relevant component and design-system motion tokens.
- Platform and browser constraints.
- Reduced-motion requirements.
- Recording, rendered page, or reproducible implementation when available.

## Procedure

1. **Name the state change.** Identify the exact trigger and the user-visible state transition. Do not begin with an animation technique.
2. **State the communication purpose.** Classify the transition as continuity, hierarchy, spatial relationship, feedback, progress, attention, or error recovery.
3. **Test necessity.** Remove the transition mentally or in a still-state comparison. Keep it only when it improves comprehension, continuity, or feedback.
4. **Define start and end states.** Both states must be stable, legible, and usable without relying on motion.
5. **Choose the smallest property set.** Prefer opacity and transform when they preserve layout. Avoid animating layout dimensions unless the layout change itself must be communicated and performance is verified.
6. **Set duration and easing from the interaction.** Use shared motion tokens. Faster transitions suit frequent local feedback; slower transitions require a stronger continuity or attention reason.
7. **Define interruption.** Specify what happens when the user reverses, repeats, navigates away, changes input, or triggers a competing state before completion.
8. **Preserve input and focus.** Motion must not steal focus, reorder keyboard navigation unexpectedly, hide active controls, or delay required interaction.
9. **Provide reduced-motion behaviour.** Replace spatial or continuous movement with immediate state change, opacity, or another low-motion alternative where appropriate.
10. **Check responsive behaviour.** Verify that changed geometry, viewport size, text wrapping, and content growth do not break the transition.
11. **Check performance.** Inspect dropped frames, layout thrashing, long tasks, oversized assets, and animation work that continues offscreen or after cancellation.
12. **Check consistency.** Confirm the transition uses design-system tokens and does not introduce an isolated motion language.
13. **Record the contract.** Document trigger, duration token, easing token, properties, interruption rule, reduced-motion rule, and verification evidence.

## Output Contract

Return:

1. state change and purpose;
2. keep, revise, or remove decision;
3. start and end states;
4. property, duration, and easing recommendation;
5. interruption and cancellation behaviour;
6. focus and accessibility behaviour;
7. reduced-motion alternative;
8. responsive and performance checks;
9. design-system token or primitive changes required.

## Verification

- The transition communicates an explicit state relationship.
- The interface remains understandable with animation disabled.
- Repeated or reversed input does not leave an impossible intermediate state.
- Keyboard focus and semantic state remain correct throughout.
- Reduced-motion behaviour is implemented and tested.
- Motion tokens are shared or the exception is documented.
- The transition does not cause avoidable layout instability or persistent main-thread work.

## Failure Modes

- Adding motion because an interface feels visually plain.
- Choosing a library effect before defining the state change.
- Using movement to compensate for weak hierarchy or unclear content.
- Allowing animations to queue after repeated input.
- Treating `prefers-reduced-motion` as merely shorter duration.
- Animating every component independently until the interface loses a coherent rhythm.
- Optimizing a recorded demo while breaking live interaction or responsive layouts.

## Provenance Boundary

This is an original local procedure distilled from reviewed transition-design patterns and Architectonic design doctrine. It does not copy an upstream skill body or CSS implementation. Exact revision, unresolved upstream licensing, retained ideas, and prohibited copying are recorded in `sources/reviewed/2026-07-22-design-quality-cluster.md`.