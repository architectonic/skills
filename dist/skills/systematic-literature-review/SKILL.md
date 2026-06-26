---
name: Systematic Literature Review
description: Produce a structured systematic literature review (SLR) across multiple academic papers on a research topic. Searches arXiv, extracts structured metadata (research question, methodology, key findings, limitations) in parallel, synthesizes themes across the full set, and emits a final report with APA, IEEE, or BibTeX citations. Distinct from academic-paper-review (single paper) and deep-research (general web research).
source: deer-flow/skills/public/systematic-literature-review/SKILL.md (MIT license, https://github.com/deer-flow/deer-flow)
category: research
tags: [research, literature-review, arxiv, academic, synthesis, citations, SLR]
type: Playbook
---

# Systematic Literature Review

## Overview

Produce a structured **systematic literature review (SLR)** across multiple academic papers on a research topic. Given a topic query, search arXiv, extract structured metadata from each paper, synthesize themes, and emit a final report with consistent citations.

**Distinct from `academic-paper-review`:** that skill does deep peer review of a single paper. This skill does breadth-first synthesis across many papers.

**Distinct from `deep-research`:** that skill does general web research. This skill is specifically for academic paper synthesis with structured metadata extraction.

## When to Use

- Literature survey on a topic ("survey transformer attention variants")
- Synthesis across multiple papers ("what do recent papers say about X")
- Systematic review with citation format ("do an SLR on Z in APA format")
- Annotated bibliography on a topic
- Research trends overview in a field over a time window

Do **not** use when:
- User provides exactly one paper to review → use `academic-paper-review`
- User asks a factual question not requiring synthesis → answer directly
- User wants general web research without academic rigor → use `deep-research`

## Workflow

### Phase 1: Plan

Before any retrieval, confirm:
- **Topic**: research area in plain English
- **Scope**: how many papers (default 20, hard upper bound 50), optional time window, optional arXiv category
- **Citation format**: APA, IEEE, or BibTeX (default APA)
- **Output location**: where to save the final report

If the user says "50+ papers", cap at 50 — for larger surveys they should split by sub-topic.

### Phase 2: Search arXiv

Use the arXiv search skill or API. Extract 2-3 core keywords before searching — do not pass the full topic description as the query.

**Query phrasing — keep it short:**
- `"diffusion models"` → good (2-word phrase)
- `"diffusion models in computer vision"` → too specific, likely returns 0 results

Use category filters to narrow the field instead of stuffing field names into the query.

**Sort strategy:**
- Always use `relevance` sorting (arXiv's BM25-style scoring)
- For "recent" papers, combine `--sort-by relevance` with `--start-date`
- `submittedDate` sorting only when user explicitly asks for chronological order

### Phase 3: Extract Metadata in Parallel

Split papers into batches of ~5. For each batch, delegate extraction (via subagent if available, or process inline for small sets).

For each paper, extract:
- arxiv_id, title, authors, published_date
- research_question (1 sentence)
- methodology (1-2 sentences)
- key_findings (3-5 bullet points)
- limitations (1-2 sentences)

### Phase 4: Synthesize and Format

**Cross-paper synthesis** — identify:
- **Themes**: 3-6 recurring research directions or approaches
- **Convergences**: findings multiple papers agree on
- **Disagreements**: where papers reach different conclusions
- **Gaps**: what the collective literature does not yet address

If the paper set is too small or heterogeneous for thematic synthesis, say so explicitly.

**Citation formatting** per user preference:
- APA 7th edition (default for social sciences and most CS journals)
- IEEE numeric citations (for IEEE venues)
- BibTeX `@misc` entries (for LaTeX; arXiv papers are `@misc`, not `@article`)

### Phase 5: Save and Present

Save the full report. In the chat, show:
1. Executive summary (3-5 sentences)
2. Themes list (bullet list of theme names + one-line gloss)
3. Paper count + file pointer

Do not dump the full report inline — per-paper annotations and references belong in the file.

## Quality Bar

The report must do more than list papers. It must identify themes, compare findings, and highlight gaps. A report that only lists papers one after another is a failure mode.

## Notes

- **arXiv only, by design.** This skill does not query Semantic Scholar, PubMed, or Google Scholar.
- **Hard upper bound of 50 papers** for synthesis quality.
- **Synthesis, not listing.** The final report must identify themes and compare findings across papers.
