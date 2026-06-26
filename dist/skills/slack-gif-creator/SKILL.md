---
name: slack-gif-creator
description: Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use when users request animated GIFs for Slack.
type: Playbook
---

# Slack GIF Creator

Create animated GIFs optimized for Slack using PIL/Pillow.

## Slack Requirements

- **Emoji GIFs:** 128x128, 10-30 FPS, 48-128 colors, under 3 seconds
- **Message GIFs:** 480x480

## Core Workflow

```python
from core.gif_builder import GIFBuilder

builder = GIFBuilder(width=128, height=128, fps=10)
# Generate frames using PIL primitives
for i in range(12):
    frame = generate_frame(i)
    builder.add_frame(frame)
builder.save('output.gif', num_colors=48, optimize_for_emoji=True)
```

## Drawing

Use PIL ImageDraw primitives (ellipse, polygon, line, rectangle). Don't use emoji fonts (unreliable across platforms).

**For complex shapes:** Combine multiple shapes, add highlights/glows, use thicker lines (width=2+).

## Animation Concepts

- **Shake/Vibrate:** Offset position with `math.sin()`
- **Pulse/Heartbeat:** Scale size rhythmically
- **Bounce:** Use `interpolate()` with `easing='bounce_out'`
- **Spin/Rotate:** `image.rotate(angle)`
- **Fade:** Adjust alpha channel or `Image.blend()`
- **Slide:** Move from off-screen to position
- **Zoom:** Scale and crop center
- **Explode:** Particles radiating outward with gravity

## Easing Functions

```python
from core.easing import interpolate
y = interpolate(start=0, end=400, t=t, easing='ease_out')
# Available: linear, ease_in, ease_out, ease_in_out, bounce_out, elastic_out, back_out
```

## Optimization

Fewer frames, fewer colors, smaller dimensions, remove duplicates, emoji mode.

## Dependencies

```bash
pip install pillow imageio numpy
```
