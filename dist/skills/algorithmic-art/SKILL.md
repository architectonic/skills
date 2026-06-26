---
name: algorithmic-art
description: Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use when users request creating art using code, generative art, algorithmic art, flow fields, or particle systems. Create original algorithmic art rather than copying existing artists' work to avoid copyright violations.
type: Playbook
---

# Algorithmic Art

Create generative art through p5.js algorithms expressed as computational aesthetic movements.

## Core Workflow

1. **Algorithmic Philosophy Creation** (.md file) — Define a generative aesthetic movement (4-6 paragraphs)
2. **Express in Code** (.html + .js files) — Build p5.js generative art expressing the philosophy

## Philosophy Creation

Name the movement (1-2 words), then articulate how it manifests through:
- Computational processes, noise functions, particle behaviors
- Temporal evolution, parametric variation, emergent complexity

Emphasize craftsmanship: the algorithm must feel meticulously crafted, refined through countless iterations.

## Implementation Requirements

**Seeded Randomness (Art Blocks Pattern):**
```javascript
let seed = 12345;
randomSeed(seed);
noiseSeed(seed);
```

**Parameter Structure:** Define tunable qualities — quantities, scales, probabilities, ratios, angles, thresholds.

**Canvas:** Standard p5.js, typically 1200x1200. Can be static (noLoop) or animated.

## Output Format

1. Algorithmic Philosophy as markdown
2. Single self-contained HTML artifact with p5.js (from CDN), algorithm, parameter controls, and UI

## Interactive Artifact

Build from the `templates/viewer.html` template. Fixed: layout, Anthropic branding, seed controls, action buttons. Variable: p5.js algorithm, parameter definitions, UI controls.

Include: seed navigation (prev/next/random/jump), parameter sliders, color pickers (optional), regenerate/reset/download buttons.

## Animation Concepts

Shake, pulse, bounce, spin, fade, slide, zoom, explode/particle burst. Combine concepts for richness.

## Optimization

For Slack GIFs: 128x128 emoji or 480x480 message, 10-30 FPS, 48-128 colors, under 3 seconds for emoji.

## Dependencies

```bash
pip install pillow imageio numpy
```
