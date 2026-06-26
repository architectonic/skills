---
name: Liteparse
description: Local document and PDF parsing with spatial text and bounding boxes. Use for extracting text from PDFs, DOCX, Office files, and images; OCR on scans; layout-preserved JSON for RAG; batch-ingesting paper folders; or page screenshots for multimodal agents. Prefer over MarkItDown when you need bboxes, fast local parsing, or PNG page renders. All processing is local — no cloud API required.
source: K-Dense-AI/scientific-agent-skills (MIT), based on run-llama/liteparse
distilled: 2026-06-23
type: Playbook
---

# LiteParse — Local Document Parsing

## When to Use

- **Fast local parsing** of PDFs or Office/image files without cloud dependencies
- **Spatial text** with bounding boxes for layout-aware RAG, citation grounding
- **OCR** on scanned PDFs or images (bundled Tesseract)
- **Page screenshots** (PNG) for multimodal agents that must see charts/figures
- **Batch ingestion** of literature folders, supplementary PDFs
- **Page subsets** or **password-protected** PDFs

## When NOT to Use

| Task | Use instead |
|---|---|
| Markdown for LLM ingestion (EPUB, audio, YouTube) | markitdown skill |
| Merge/split PDFs, forms, watermarks | pdf skill |
| Dense tables, handwriting, production cloud | LlamaParse (cloud) |

## Installation

```bash
uv pip install "liteparse==2.0.0"
# Optional: LibreOffice (Office formats), ImageMagick (images)
```

## Quick Start

```python
from liteparse import LiteParse

parser = LiteParse(quiet=True)
result = parser.parse("paper.pdf")
print(result.text)

for page in result.pages:
    print(f"Page {page.page_num}: {len(page.text_items)} items")
```

```bash
# Layout-preserved text
lit parse paper.pdf

# Structured JSON with bounding boxes
lit parse paper.pdf --format json -o paper.json

# Disable OCR on text-native PDFs (faster)
lit parse paper.pdf --no-ocr
```

## Core Workflows

### Parse to structured JSON (bounding boxes)

```python
parser = LiteParse(output_format="json", quiet=True)
result = parser.parse("document.pdf")
for page in result.pages:
    for item in page.text_items:
        bbox = (item.x, item.y, item.width, item.height)
        # item.text, item.confidence, item.font_name, item.font_size
```

### Page screenshots for multimodal agents

```python
parser = LiteParse(dpi=150, quiet=True)
shots = parser.screenshot("document.pdf", page_numbers=[1, 2, 3])
```

### Batch-parse a directory

```bash
lit batch-parse ./papers ./parsed --format json --recursive
```

### OCR configuration

```python
parser = LiteParse(
    ocr_enabled=True,
    ocr_language="eng",
    num_workers=4,
    dpi=150,
)
```

Air-gapped: set `TESSDATA_PREFIX` to directory of `.traineddata` files.

## Multi-Format Inputs

| Category | Extensions | Requirement |
|---|---|---|
| PDF | `.pdf` | Native |
| Office | `.docx`, `.xlsx`, `.pptx`, `.doc` | LibreOffice |
| Images | `.png`, `.jpg`, `.tiff`, `.webp` | ImageMagick |

Files are converted to PDF internally, then parsed.

## Performance Tips

- `--no-ocr` on born-digital PDFs (largest speedup)
- `target_pages` for specific sections
- `num_workers` to scale OCR across CPU cores
- Lower `dpi` (e.g. 100) when OCR quality is sufficient

## Resources

- GitHub: https://github.com/run-llama/liteparse
- PyPI: https://pypi.org/project/liteparse/2.0.0/

## Attribution

From K-Dense-AI/scientific-agent-skills (MIT), based on run-llama/liteparse (Apache-2.0).
