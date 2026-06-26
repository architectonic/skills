---
name: Scientific Visualization
description: Meta-skill for publication-ready figures. Use when creating journal submission figures requiring multi-panel layouts, significance annotations, error bars, colorblind-safe palettes, and specific journal formatting (Nature, Science, Cell). Orchestrates matplotlib/seaborn/plotly with publication styles.
source: K-Dense-AI/scientific-agent-skills (MIT)
distilled: 2026-06-23
type: Playbook
---

# Scientific Visualization

## When to Use

- Creating plots for scientific manuscripts
- Preparing figures for journal submission (Nature, Science, Cell, PLOS, etc.)
- Ensuring figures are colorblind-friendly and accessible
- Making multi-panel figures with consistent styling
- Exporting figures at correct resolution and format
- Following specific publication guidelines

## Core Principles

### 1. Resolution and File Format

- **Raster images** (photos, microscopy): 300-600 DPI
- **Line art** (graphs, plots): 600-1200 DPI or vector format
- **Vector formats** (preferred): PDF, EPS, SVG
- **Raster formats**: TIFF, PNG (never JPEG for scientific data)

### 2. Color — Colorblind Accessibility

**Always use colorblind-friendly palettes.**

Recommended Okabe-Ito palette:
```python
okabe_ito = ['#E69F00', '#56B4E9', '#009E73', '#F0E442',
             '#0072B2', '#D55E00', '#CC79A7', '#000000']
```

For heatmaps/continuous data: use perceptually uniform colormaps (`viridis`, `plasma`, `cividis`). Avoid `jet` or `rainbow`. For diverging data: `PuOr`, `RdBu`, `BrBG`.

**Always test figures in grayscale.**

### 3. Typography

- Sans-serif fonts: Arial, Helvetica, Calibri
- Minimum sizes at final print size: axis labels 7-9pt, tick labels 6-8pt, panel labels 8-12pt bold
- Sentence case for labels: "Time (hours)" not "TIME (HOURS)"
- Always include units in parentheses

### 4. Figure Dimensions

| Journal | Single Column | Double Column |
|---|---|---|
| Nature | 89 mm | 183 mm |
| Science | 55 mm | 175 mm |
| Cell | 85 mm | 178 mm |

### 5. Multi-Panel Figures

- Label panels with bold letters: **A**, **B**, **C** (uppercase for most journals, lowercase for Nature)
- Maintain consistent styling across all panels
- Align panels along edges
- Use adequate white space between panels

## Statistical Rigor

**Always include:**
- Error bars (SD, SEM, or CI — specify which in caption)
- Sample size (n) in figure or caption
- Statistical significance markers (*, **, ***)
- Individual data points when possible (not just summary statistics)

## Quick Start

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Apply publication style
sns.set_theme(style='ticks', context='paper', font_scale=1.1)
sns.set_palette('colorblind')

# Single column Nature figure
fig, ax = plt.subplots(figsize=(3.5, 2.5))
# ... your plotting code ...
sns.despine()
fig.savefig('figure.pdf', dpi=300, bbox_inches='tight')
fig.savefig('figure.png', dpi=300, bbox_inches='tight')
```

## Common Tasks

1. **Line plot with error bars** → Use seaborn `lineplot` with `errorbar=('ci', 95)`
2. **Multi-panel figure** → Use `GridSpec`, add panel labels with `ax.text(-0.15, 1.05, 'A', transform=ax.transAxes, fontsize=10, fontweight='bold')`
3. **Heatmap** → Use `sns.heatmap` with `cmap='RdBu_r'` for diverging, `cmap='viridis'` for sequential
4. **Statistical comparison** → Box plot + strip plot for individual data points
5. **Distribution** → Violin plot with `inner='quartile'`

## Attribution

From K-Dense-AI/scientific-agent-skills (MIT), authored by K-Dense Inc.
