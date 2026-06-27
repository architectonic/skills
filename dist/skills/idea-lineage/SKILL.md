---
name: idea-lineage
title: Idea Lineage — Single-Idea Evolution
description: 'Trace how one idea changed across time: when it first appeared, when
  it became sharp, what it displaced, what it contradicted, and what version is alive
  now.'
type: Playbook
domain: writing
tags:
- writing
- okf
risk_level: medium
requires_review: true
---

# Idea Lineage — Single-Idea Evolution

## Purpose

Trace how one idea changed across time: when it first appeared, when it became sharp, what it displaced, what it contradicted, and what version is alive now.

Canonical examples:
- "Run idea lineage on founder-led sales."
- "How has my thinking about compounding trust changed?"
- "What is my current version of this idea?"
- "Where did this idea come from?"

## What This Is Not

- Not `concept-synthesis`: that skill deduplicates many concept stubs and builds a broad intellectual map
- Not `find_trajectory`: that operation charts typed facts or event rows for an entity
- Not a writing mode by default: do not write a lineage page unless the user explicitly asks

## Contract

- A single-idea scope is preserved
- Every lineage claim cites existing evidence: page slug, date, and short quote
- Missing evidence is labeled as a gap, not patched with plausible narrative
- Contradictions, reversals, and abandoned branches are separated from normal temporal evolution
- The default mode is read-only and does not mutate knowledge pages

## Phases

### Phase 1: Resolve the Idea Target

1. Restate the idea in one sentence
2. Search for exact phrase variants
3. Run one semantic query for the natural-language version
4. Check for concept pages with obvious slug or title

If multiple distinct ideas share the same phrase, ask the user to choose.

### Phase 2: Gather Evidence

- Search chunks with dates and source slugs
- Full pages for the top relevant concept, note, transcript, meeting, article pages
- Related concept pages through backlinks or co-occurrence
- Cached contradiction findings when available

Prefer fewer high-quality sources over a long unsorted pile.

### Phase 3: Classify Lineage Moments

Classify evidence into buckets:

1. **First mention** — earliest dated evidence
2. **Best articulation** — clearest/most complete expression (not necessarily newest)
3. **Current live version** — most recent high-authority version that still appears active
4. **Reversals** — places where stance changed direction
5. **Contradictions** — claims that cannot both be true (distinct from temporal supersession)
6. **Abandoned branches** — promising variants that appear then disappear
7. **Related concepts** — nearby ideas that shaped or inherited part of the original

When a bucket has no evidence, write "No clear evidence found."

### Phase 4: Synthesize the Lineage

```markdown
## Current Live Version
[1-3 sentences. Include confidence: high / medium / low.]

## Lineage
- First mention: [date] - [claim] ([source], "short quote")
- Best articulation: [date] - [claim] ([source], "short quote")
- Turning point: [date] - [what changed] ([source])

## Reversals and Contradictions
- Reversal: [what changed, with before/after evidence]
- Contradiction: [what conflicts, or "No clear evidence found"]

## Abandoned Branches
- [branch] - [why it appears abandoned, with evidence]

## Related Concepts
- [concept] - [relationship]

## Evidence Gaps
- [bucket or claim] - [what was checked and what is missing]
```

### Phase 5: Suggest Optional Next Action

If useful, offer one concrete follow-up:
- Save the lineage as a knowledge page
- Run broad concept-synthesis if the user wants the whole concept map refreshed

## Quality Rules

- Quote exact text when naming first mention or best articulation
- Include dates when available; say "undated" rather than guessing
- Treat the user's direct statements as highest authority for their own current view
- Mark confidence low when evidence comes from a single weak snippet
