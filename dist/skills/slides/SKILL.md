---
name: slides
description: Create, edit, review, and export slide decks and .pptx presentations. Use when the user asks for slides, presentations, pitch decks, speaker notes, templates, or any .pptx workflow.
tags: [productivity, agent-skill]
type: Playbook
---

# slides

Use this skill for any presentation work.

## Scope
- Create slide decks from scratch or from a plan
- Edit existing presentations without breaking formatting
- Read and extract text from .pptx files
- Work with templates, notes, comments, split/merge, and layout changes
- Generate presentation visuals and compose them into slides when needed

## When to use
- The user asks for a deck, pitch, talk, lesson, report, or presentation
- The user mentions `.pptx`, slides, speaker notes, templates, or slide layouts
- The user wants a presentation edited, cleaned up, extracted, split, or merged

## Workflow
1. Clarify the topic, audience, slide count, format, and deadline.
2. Decide whether the task is create, edit, or inspect.
3. Draft a slide outline before building.
4. Keep one visual system across the deck.
5. Build or place visuals one slide at a time when consistency matters.
6. If slide imagery is needed, generate it sequentially so each slide can inherit the style of the previous one.
7. Validate by rendering and checking for overflow, placeholder text, and alignment issues.
8. Fix the smallest thing that solves the problem, then re-check.

## Presentation planning
- Decide the visual style before producing slides.
- Keep the color palette, typography, and spacing system consistent.
- Match the slide structure to the user’s goal: title, agenda, content, comparison, timeline, conclusion.
- Keep text density low unless the user explicitly wants a dense report deck.

## Style directions
Choose a style that matches the content:

- glassmorphism: frosted panels, blur, gradients, futuristic product launches
- dark-premium: deep black backgrounds, luminous accents, luxury brand feel
- gradient-modern: bold gradients, contemporary typography, startup or creative work
- neo-brutalist: raw bold type, thick borders, anti-design energy
- 3d-isometric: clean isometric visuals, friendly tech explainer feel
- editorial: magazine-style layouts, sophisticated typography, thought leadership
- minimal-swiss: strict grid, white space, timeless modernism
- keynote: cinematic Apple-style presentations with bold imagery and strong hierarchy

## Slide imagery workflow
When the deck needs generated visuals:
1. Make a simple presentation plan with slide-by-slide intent.
2. Generate the first slide to establish the visual language.
3. Generate later slides one by one, referencing the previous slide when continuity matters.
4. Keep the visual system stable unless a deliberate transition is requested.

## Design rules
- Every slide needs a purpose and at least one visual element.
- Prefer one strong visual idea over clutter.
- Use consistent spacing, hierarchy, and typography.
- Avoid generic title-plus-bullets slides when a stronger layout is possible.
- Keep text readable and high-contrast.
- Do not mix multiple visual systems inside the same deck unless the structure requires it.

## QA
- Extract text from the final deck and check for missing or wrong content.
- Render slides to images when visual fidelity matters.
- Check for overflow, overlap, low contrast, and leftover placeholders.
- Re-verify after each fix.
- If a slide looks inconsistent, regenerate or revise only the affected slide first.

## Notes
- If a template exists, inspect it before editing.
- If the user wants a specific style, keep it consistent across all slides.
- If generated slide art is used, keep the slide sequence ordered and style-consistent.
