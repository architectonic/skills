---
name: syllabus
description: Generates a curated supplementary reading list from any course syllabus. Grill-me intake (syllabus input format + course audience + year range) plus a grouping forcing-options checkpoint before any search runs. Parses the syllabus to extract topics and learning outcomes, searches for recent peer-reviewed papers per topic, and produces a structured report with plain-language summaries calibrated to audience level and Bloom-higher-order discussion questions tied to course learning goals. Use when the user uploads a syllabus, course outline, or curriculum document and wants supplementary readings.
type: Playbook
---

# Syllabus — Course Supplementary Reading List

For an instructor or student with a course syllabus, produce a professional supplementary reading list containing recent peer-reviewed papers per course section.

## Agent Integrity Rules

- **Only use what search returns.** Every paper title, author, journal, year must come from this session's tool calls.
- **Confirm before moving on.** A search isn't complete until response received and inspected.
- **Track three counts.** Queries sent / papers received / papers cited.
- **Surface gaps, don't fill them.** Section with one paper + note > section padded with fabrications.

## Phase 0: Grill-Me Intake (3 forcing questions)

### Q1 (root) — Syllabus input

> **Provide the syllabus — pick one:**
> 1. File path (PDF, DOCX, text) — I'll read it
> 2. Pasted content — paste below
> 3. Image of a printed syllabus — attach the image

**Refuse to start without a syllabus.**

### Q2 (depends on Q1) — Course audience

> **Course audience — pick one:**
> 1. Undergraduate (intro level)
> 2. Undergraduate (advanced / upper division)
> 3. Graduate (Masters / early PhD)
> 4. Graduate (doctoral / advanced)
> 5. Professional / continuing education
> 6. Mixed

Audience dictates summary jargon level and discussion-question complexity.

### Q3 (depends on Q1) — Year range

> **Year range for papers — pick one:**
> 1. Last 1 year (most recent only)
> 2. Last 2 years (default)
> 3. Last 5 years (broader, includes foundational recent work)

## Phase 1: Parse the Syllabus

Per Q1 input format:
- **PDF**: use PDF reader; extract text
- **DOCX**: use pandoc or DOCX parser; extract text
- **Text/pasted**: read directly
- **Image**: use vision; extract text

Extract: course title + instructor + term, topic list, learning outcomes (mark inferred as `[inferred]`).

## Phase 2: Group Topics + Confirm with User

Cluster related topics into 6-12 sections. Present:

> **Proposed sections: [list with item counts]. Pick one:**
> 1. "Looks good — proceed"
> 2. "Merge sections [X] and [Y]"
> 3. "Split section [X] into two"
> 4. "Add a section for [topic]"
> 5. "Remove section [X]"

**Refuse to start Phase 3 without explicit user choice.**

## Phase 3: Search per Section

Sequential, 1 q/sec. 1-2 queries per section.

### Applied-Domain Weaving (Critical)

Don't just search the topic — **search the topic + applied domain**:

| ❌ Generic | ✅ Applied-domain |
|---|---|
| "enzyme kinetics" | "enzyme kinetics food processing applications" |
| "machine learning" | "machine learning clinical decision support" |

Boosts paper relevance dramatically.

**Selection priorities:** Relevance → Reviews/meta-analyses → Citation count → Applied-domain connection.

## Phase 4: Write Summaries + Discussion Questions

**Summary writing (per paper):**
- Plain language calibrated to audience (Q2)
- 2-3 sentences
- Define jargon if undergraduate; assume fluency if graduate

**Discussion questions (per paper):**
- Bloom **higher-order** (apply / analyze / evaluate)
- Tied to a specific course learning outcome
- Promotes discussion, not just recall

| ✅ Good question | ❌ Bad question |
|---|---|
| "If dietary fat quality can reshape your lipoprotein lipidome, what does this suggest about the biochemical basis for dietary guidelines?" | "What did the authors find?" (Just recall) |

## Phase 5: Report Generation

Structured report with:
1. Course title + date + year range
2. Learning outcomes
3. Per-section: heading + 1-3 papers with title/authors/journal/year + summary + discussion question
4. Audit log: queries sent / papers received / papers cited

## Anti-Patterns To Reject

- Searching topics without applied-domain angle
- Padding sections with fabricated entries
- Generic discussion questions ("What did the authors find?")
- Jargon-heavy summaries for undergrad audience
- Skipping the group-and-confirm step

---

**Version:** 1.0.0 (distilled 2026-07-23)
**Source:** claude-skills/research/syllabus — MIT License
