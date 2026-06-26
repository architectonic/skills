---
name: docx
description: Create, edit, redline, and comment on `.docx` files. Use when the user needs to create or modify Word documents, including reading, creating, editing, redlining, commenting, accessibility audits, redaction, merging, and template work. Render to images for visual QA before delivering.
tags: [productivity, agent-skill]
type: Playbook
---

# docx

Create, edit, redline, and comment on `.docx` files with a strict render-and-verify workflow.

## Non-negotiable: render → inspect PNGs → iterate

You do not "know" a DOCX is satisfactory until you've rendered it and visually inspected page images. DOCX text extraction (or reading XML) will miss layout defects: clipping, overlap, missing glyphs, broken tables, spacing drift, and header/footer issues.

**Shipping gate:** before delivering any DOCX, you must:
- Run the renderer to produce page images
- Open the images (100% zoom) and confirm every page is clean
- If anything looks off, fix the DOCX and re-render (repeat until flawless)

If rendering fails, fix rendering first rather than guessing.

**Deliverable discipline:** Rendered artifacts are for internal QA only. Unless the user explicitly asks for intermediates, return only the requested final deliverable.

## Quick start

```bash
# Render any DOCX to PNGs (visual QA)
python render_docx.py input.docx --output_dir out

# Remove reviewer comments (finalization)
python scripts/comments_strip.py input.docx --out no_comments.docx

# Accept tracked changes (finalization)
python scripts/accept_tracked_changes.py input.docx --mode accept --out accepted.docx

# Accessibility audit (+ optional safe fixes)
python scripts/a11y_audit.py input.docx
python scripts/a11y_audit.py input.docx --out_json a11y_report.json
python scripts/a11y_audit.py input.docx --fix_image_alt from_filename --out a11y_fixed.docx

# Redact sensitive text (layout-preserving by default)
python scripts/redact_docx.py input.docx redacted.docx --emails --phones
```

## Default workflow (80/20)

1. **Author/edit with `python-docx`** (paragraphs, runs, styles, tables, headers/footers).
2. **Render → inspect PNGs immediately** (DOCX → PNGs). Treat this as your feedback loop.
3. **Fix and repeat** until the PNGs are visually perfect.
4. **Only if needed**: use OOXML patching for tracked changes, comments, hyperlinks, or fields.
5. **Re-render and inspect again** after any OOXML patch or layout-sensitive change.
6. **Deliver only after the latest PNG review passes** (all pages, 100% zoom).

## Visual review

```bash
python render_docx.py input.docx --output_dir out
# Optional: also write PDF for debugging/archival
python render_docx.py input.docx --output_dir out --emit_pdf
```

**Success criteria:**
- PNGs exist for each page
- Page count matches expectations
- Inspect every page at 100% zoom (no "spot check" for final delivery)
- No clipping/overlap, no broken tables, no missing glyphs, no header/footer misplacement

**Note:** LibreOffice sometimes prints scary-looking stderr even when output is correct. Treat the render as successful if the PNGs exist and look right.

## Coverage

### Layout & style
- `style_lint.py`, `style_normalize.py` — format consistency, cleanup
- `apply_template_styles.py` — apply DOTX template styles
- `section_audit.py`, `heading_audit.py` — structure audits

### Figures / images
- `images_audit.py`, `a11y_audit.py` — image and accessibility checks
- `captions_and_crossrefs.py` — captions and cross-references

### Tables
- `xlsx_to_docx_table.py` — spreadsheet → DOCX table
- `docx_table_to_csv.py` — DOCX table → CSV

### Fields & references
- `fields_report.py`, `fields_materialize.py` — field inspection and materialization
- `insert_ref_fields.py`, `flatten_ref_fields.py` — cross-references
- `insert_toc.py` — table of contents

### Review lifecycle (comments / tracked changes)
- `add_tracked_replacements.py`, `accept_tracked_changes.py` — tracked changes
- `comments_add.py`, `comments_extract.py`, `comments_apply_patch.py`, `comments_strip.py` — comments

### Privacy / publishing
- `privacy_scrub.py` — remove personal metadata
- `redact_docx.py` — layout-preserving redaction
- `watermark_add.py`, `watermark_audit_remove.py` — watermarks

### Navigation & multi-doc assembly
- `internal_nav.py` — internal navigation links
- `merge_docx_append.py` — merge/append DOCXs

### Forms & protection
- `content_controls.py` — content controls (SDTs)
- `set_protection.py` — restrict editing

### QA / regression
- `render_and_diff.py` — render + per-page image diff between two DOCXs
- `make_fixtures.py` — reproducible edge-case fixtures

## Quality reminders
- Don't ship visible defects (clipped/overlapping text, broken tables, unreadable glyphs).
- Don't leak tool citation tokens into the DOCX (convert them to normal human citations).
- Prefer ASCII punctuation (avoid exotic Unicode hyphens/dashes that render inconsistently).
