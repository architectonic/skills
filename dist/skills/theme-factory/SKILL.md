---
name: theme-factory
description: Toolkit for styling artifacts with a professional theme. These artifacts can be slides, docs, reports, HTML landing pages, etc. Provides 10 pre-set themes with curated color palettes and font pairings, or generate a new theme on-the-fly. Use when styling presentations, reports, documents, or any artifact that needs consistent professional visual identity.
type: Playbook
---

# Theme Factory

Source: anthropics/skills (Apache-2.0). Adapted for Hermes Agent.

Apply consistent, professional styling to any artifact — slides, docs, reports, HTML landing pages — using curated font and color themes.

## Usage

1. **Show the theme showcase** to the user so they can see available themes
2. **Ask for their choice** — get explicit confirmation
3. **Apply the theme** — use the selected theme's colors and fonts consistently

## Available Themes

1. **Ocean Depths** — Professional and calming maritime theme
2. **Sunset Boulevard** — Warm and vibrant sunset colors
3. **Forest Canopy** — Natural and grounded earth tones
4. **Modern Minimalist** — Clean and contemporary grayscale
5. **Golden Hour** — Rich and warm autumnal palette
6. **Arctic Frost** — Cool and crisp winter-inspired theme
7. **Desert Rose** — Soft and sophisticated dusty tones
8. **Tech Innovation** — Bold and modern tech aesthetic
9. **Botanical Garden** — Fresh and organic garden colors
10. **Midnight Galaxy** — Dramatic and cosmic deep tones

Each theme provides:
- A cohesive color palette with hex codes
- Complementary font pairings for headers and body text
- A distinct visual identity suitable for different contexts

## Application Process

After theme selection:
1. Read the corresponding theme file from the `themes/` directory
2. Apply the specified colors and fonts consistently throughout the artifact
3. Ensure proper contrast and readability
4. Maintain the theme's visual identity across all pages/slides

## Creating Custom Themes

When none of the existing themes work, create a custom theme:
1. Choose a name describing what the font/color combinations represent
2. Define a cohesive color palette (primary, secondary, accent, background, text)
3. Select complementary font pairings (heading + body)
4. Show the generated theme for review before applying
