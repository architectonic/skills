---
name: image-generation
description: Generate or edit raster images, illustrations, mockups, product images, and similar bitmap assets. Use when the user asks for a new image, a transformation of an existing image, reference-guided variation, or a transparent-background cutout.
tags: [creative, agent-skill]
type: Playbook
---

# image-generation

Use this skill for bitmap image work.

## Decide the task
- Generate: create a new image from text and optional references.
- Edit: modify an existing image while preserving the parts the user wants unchanged.
- Pick the visual lane: realistic / photographic, illustrative / stylized, or product / UI / mockup.

## Provider and model selection
Do not suppress provider knowledge. Inspect what is actually available in the current environment before choosing a path.

1. Discover configured image providers, model routes, and keys available in the environment.
2. Prefer the best available provider/model for the requested look:
   - realistic / photo-like work -> the strongest photoreal model available
   - illustration / stylized work -> the strongest illustration-capable model available
   - compositing / cutouts / asset edits -> the most controllable edit-capable route available
3. If multiple providers are available, choose the one that best matches the request rather than hardcoding one backend.
4. If the needed provider or model is unavailable, tell the user exactly what is missing and how to add the required provider key or local setup.
5. If the environment has a preferred built-in tool path, use it when it matches the request; otherwise fall back to the best configured API/CLI route.

## Workflow
1. Identify the subject, style, composition, and required constraints.
2. Decide whether the image should feel realistic, illustrated, iconic, editorial, or product-focused.
3. Treat reference images as guidance unless the user says to preserve identity or composition.
4. Be specific about what must change and what must remain fixed.
5. For transparent or cutout requests, prefer a simple flat background first and verify the alpha result; if the available route cannot deliver true transparency, explain the limitation and the fallback setup needed.
6. Generate one candidate at a time unless the user explicitly wants variants.
7. Inspect outputs for fidelity, composition, text accuracy, and artifacts.
8. Iterate one change at a time.

## Prompt guidance
- State the use case first.
- Include exact text verbatim when text is part of the image.
- Specify mood, lighting, framing, palette, and material details when they matter.
- Avoid asking for unnecessary extra elements.
- For edits, say exactly which region changes and which must remain unchanged.
- For realistic images, bias toward camera, lens, lighting, and environment details.
- For illustration, bias toward medium, line quality, color treatment, and shape language.

## Good defaults
- Use references for style, composition, or mood.
- Use a strong negative list when the asset is sensitive to artifacts.
- Keep the prompt short when the user already gave good detail.
- Preserve the original asset unless replacement was explicitly requested.
- If the user did not specify realism vs illustration, infer the best match from context and choose accordingly.

## If setup is missing
When the required provider or model is not available:
- say what capability is missing,
- say which provider key or local dependency is needed,
- and offer the user the exact setup path instead of silently dropping detail.

## QA
- Check subject identity.
- Check text spelling and placement.
- Check edges, shadows, transparency, and compositing artifacts.
- Save the selected final artifact under a workspace path if the asset is project-bound.
