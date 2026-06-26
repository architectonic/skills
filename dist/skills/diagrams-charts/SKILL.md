---
name: diagrams-charts
description: Create diagrams, charts, and data visualizations. Use for architecture diagrams (SVG/HTML), hand-drawn diagrams (Excalidraw), infographics (image generation), and data charts (JavaScript/PNG). Covers multiple output formats and tools.
tags: [creative, agent-skill]
type: Playbook
---

# diagrams-charts

Create diagrams, charts, and data visualizations across multiple formats.

## Tool selection

| Need | Tool | Output |
|------|------|--------|
| Architecture / cloud / infra diagrams | SVG/HTML (dark theme) | `.html` file |
| Hand-drawn whiteboard sketches | Excalidraw JSON | `.excalidraw` file |
| Infographics (21 layouts × 21 styles) | image_generation | `.png` file |
| Data charts (26 chart types) | JavaScript/Node.js | `.png` URL |

---

## Architecture diagrams (SVG/HTML)

Generate professional, dark-themed technical architecture diagrams as standalone HTML files with inline SVG.

**Best for:** Software system architecture, cloud infrastructure, microservice topology, database + API maps, deployment diagrams.

**Not for:** Scientific subjects, physical objects, floor plans, animated explainers.

### Workflow
1. User describes system architecture (components, connections, technologies)
2. Generate HTML file following the design system below
3. Save to `.html` file — works offline, no dependencies

### Color palette (semantic mapping)

| Component Type | Fill (rgba) | Stroke (Hex) |
|---|---|---|
| Frontend | `rgba(8, 51, 68, 0.4)` | `#22d3ee` (cyan) |
| Backend | `rgba(6, 78, 59, 0.4)` | `#34d399` (emerald) |
| Database | `rgba(76, 29, 149, 0.4)` | `#a78bfa` (violet) |
| AWS/Cloud | `rgba(120, 53, 15, 0.3)` | `#fbbf24` (amber) |
| Security | `rgba(136, 19, 55, 0.4)` | `#fb7185` (rose) |
| Message Bus | `rgba(251, 146, 60, 0.3)` | `#fb923c` (orange) |
| External | `rgba(30, 41, 59, 0.5)` | `#94a3b8` (slate) |

### Design specs
- **Font:** JetBrains Mono (monospace), loaded from Google Fonts
- **Sizes:** 12px names, 9px sublabels, 8px annotations
- **Background:** Slate-950 (`#020617`) with 40px grid pattern
- **Components:** Rounded rectangles (`rx="6"`), 1.5px strokes
- **Double-rect masking:** Opaque background rect + semi-transparent styled rect on top (prevents arrows showing through)
- **Arrows:** Draw early (behind components), use SVG markers
- **Security flows:** Dashed lines in rose color
- **Legend:** Place outside all boundary boxes, at least 20px below lowest boundary

### Output requirements
- Single self-contained `.html` file
- All CSS and SVG inline (except Google Fonts)
- No JavaScript — pure CSS for animations
- Renders correctly in any modern browser

---

## Excalidraw diagrams (hand-drawn)

Create diagrams by writing standard Excalidraw element JSON. Files can be drag-and-dropped onto excalidraw.com.

**Best for:** Architecture diagrams, flowcharts, sequence diagrams, concept maps, whiteboard sketches.

### Workflow
1. Write elements JSON array
2. Save as `.excalidraw` file
3. Optionally upload for shareable link

### File format
```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "agent",
  "elements": [ ... ],
  "appState": { "viewBackgroundColor": "#ffffff" }
}
```

### Element types

**Rectangle:**
```json
{ "type": "rectangle", "id": "r1", "x": 100, "y": 100, "width": 200, "height": 100 }
```

**Labeled shape (container binding):**
```json
{ "type": "rectangle", "id": "r1", "x": 100, "y": 100, "width": 200, "height": 80,
  "roundness": { "type": 3 }, "backgroundColor": "#a5d8ff", "fillStyle": "solid",
  "boundElements": [{ "id": "t_r1", "type": "text" }] }
{ "type": "text", "id": "t_r1", "x": 105, "y": 110, "width": 190, "height": 25,
  "text": "Hello", "fontSize": 20, "fontFamily": 1,
  "textAlign": "center", "verticalAlign": "middle",
  "containerId": "r1", "originalText": "Hello", "autoResize": true }
```

**Arrow:**
```json
{ "type": "arrow", "id": "a1", "x": 300, "y": 150, "width": 200, "height": 0,
  "points": [[0,0],[200,0]], "endArrowhead": "arrow" }
```

**Arrow bindings:**
```json
{ "type": "arrow", "id": "a1",
  "startBinding": { "elementId": "r1", "fixedPoint": [1, 0.5] },
  "endBinding": { "elementId": "r2", "fixedPoint": [0, 0.5] } }
```

### Drawing order
Array order = z-order (first = back, last = front). Emit: background zones → shape → bound text → arrows → next shape.

### Sizing
- Minimum fontSize: 16 for body text, 20 for titles, 14 for secondary annotations
- Minimum shape size: 120x60 for labeled rectangles
- Leave 20-30px gaps between elements

### Color palette

| Use | Fill Color | Hex |
|-----|-----------|-----|
| Primary / Input | Light Blue | `#a5d8ff` |
| Success / Output | Light Green | `#b2f2bb` |
| Warning / External | Light Orange | `#ffd8a8` |
| Processing / Special | Light Purple | `#d0bfff` |
| Error / Critical | Light Red | `#ffc9c9` |
| Notes / Decisions | Light Yellow | `#fff3bf` |
| Storage / Data | Light Teal | `#c3fae8` |

### Tips
- Never use `label` property on shapes — use container binding instead
- Never use emoji in text — they don't render in Excalidraw's font
- Text contrast is critical — minimum text color on white: `#757575`

---

## Infographics (image generation)

Create infographics using 21 layouts × 21 styles. Freely combine any layout with any style.

**Best for:** Visual summaries, information graphics, high-density information images.

### Layouts (21 options)

| Layout | Best For |
|--------|----------|
| `linear-progression` | Timelines, processes, tutorials |
| `binary-comparison` | A vs B, before-after, pros-cons |
| `comparison-matrix` | Multi-factor comparisons |
| `hierarchical-layers` | Pyramids, priority levels |
| `tree-branching` | Categories, taxonomies |
| `hub-spoke` | Central concept with related items |
| `structural-breakdown` | Exploded views, cross-sections |
| `bento-grid` | Multiple topics, overview (default) |
| `iceberg` | Surface vs hidden aspects |
| `bridge` | Problem-solution |
| `funnel` | Conversion, filtering |
| `isometric-map` | Spatial relationships |
| `dashboard` | Metrics, KPIs |
| `periodic-table` | Categorized collections |
| `comic-strip` | Narratives, sequences |
| `story-mountain` | Plot structure, tension arcs |
| `jigsaw` | Interconnected parts |
| `venn-diagram` | Overlapping concepts |
| `winding-roadmap` | Journey, milestones |
| `circular-flow` | Cycles, recurring processes |
| `dense-modules` | High-density, data-rich guides |

### Styles (21 options)

`craft-handmade` (default), `claymation`, `kawaii`, `storybook-watercolor`, `chalkboard`, `cyberpunk-neon`, `bold-graphic`, `aged-academia`, `corporate-memphis`, `technical-schematic`, `origami`, `pixel-art`, `ui-wireframe`, `subway-map`, `ikea-manual`, `knolling`, `lego-brick`, `pop-laboratory`, `morandi-journal`, `retro-pop-grid`, `hand-drawn-edu`

### Workflow
1. Analyze content (topic, data type, complexity, tone, audience)
2. Generate structured content (title, sections, key concepts, data points)
3. Recommend 3-5 layout×style combinations
4. Confirm options with user (layout, aspect ratio, language)
5. Generate prompt combining layout + style + structured content
6. Generate image via `image_generate` tool
7. Report: topic, layout, style, aspect, output path

### Core principles
- Preserve source data faithfully — no summarization or rephrasing
- Strip credentials/secrets from output
- One message per section
- Style consistency across entire infographic
- `image_generate` only supports `landscape`, `portrait`, `square` — map custom ratios to nearest

---

## Data charts (JavaScript)

Generate chart images from data using 26 chart types.

### Chart selection

| Data type | Chart types |
|-----------|-------------|
| Time series | Line chart, area chart, dual axes chart |
| Comparisons | Bar chart, column chart, histogram |
| Part-to-whole | Pie chart, treemap |
| Relationships | Scatter, Sankey, Venn |
| Maps | District map, pin map, path map |
| Hierarchies | Organization chart, mind map |
| Specialized | Radar, funnel, liquid, word cloud, boxplot, violin, network graph, fishbone, flow diagram |

### Workflow
1. Analyze data features → select chart type
2. Read chart spec from `references/` directory
3. Extract parameters and data
4. Generate chart

```bash
node ./scripts/generate.js '<payload_json>'
```

**Payload format:**
```json
{
  "tool": "generate_chart_type_name",
  "args": {
    "data": [...],
    "title": "...",
    "theme": "...",
    "style": { ... }
  }
}
```

The script outputs the URL of the generated chart image.
