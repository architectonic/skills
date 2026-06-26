---
name: litreview
description: Academic literature orientation — searches papers via web academic search, builds a strategic search plan using PICO (default) or SPIDER / Decomposition, and synthesizes findings into a structured research guide. Grill-me intake (research question + framework hint + depth) before recon search; second forcing checkpoint after framework selection confirms sub-areas + depth. Configurable depth (5/10/20 queries). Output is a 'launching pad' — an orientation guide for a researcher entering an unfamiliar field, not a finished review. Use when starting literature-oriented research (e.g., 'litreview on [topic]', 'literature review on [topic]', 'I'm writing a paper on X').
type: Playbook
---

# Litreview — Academic Literature Orientation

Produce a **launching pad** — not a finished literature review, but an orientation document that gives a researcher entering an unfamiliar field everything they need to start reading and searching with confidence.

## Agent Integrity Rules

- **Source discipline.** Only cite papers returned by this session's tool calls. Training knowledge labeled `[Not from search — model knowledge]` and excluded.
- **Counting discipline.** Three numbers: searches executed / unique papers received (deduplicated) / papers cited.
- **Tool constraints.** Rate limit is 1 query/sec — sequential execution mandatory.
- **Retry policy.** On failure → wait 3s → retry once → log. After 3 consecutive failures: stop, alert user.

## Phase 0: Grill-Me Intake (3 forcing questions)

### Q1 (root) — Research question specificity

> **State the research question in 1–2 sentences. Specific is better — "How do LLMs perform on clinical reasoning tasks compared to physicians?" beats "AI in medicine".**

**Refuse mush.** Re-ask once with examples if too broad.

### Q2 (depends on Q1) — Framework hint

> **Framework — pick one or say "you pick":**
> 1. **PICO** (Population / Intervention / Comparison / Outcome — clinical)
> 2. **SPIDER** (Sample / Phenomenon / Design / Evaluation / Research-type — qualitative)
> 3. **Decomposition** (Problem / Solution / Evaluation / Limitations — technology)
> 4. **Hybrid**
> 5. **You pick** — analyze Q1 and recommend

### Q3 (depends on Q1) — Tentative depth

> **Tentative depth — pick one. Final confirmation comes after the framework breakdown:**
> 1. **Quick scan** (5 searches)
> 2. **Standard review** (10 searches)
> 3. **Deep dive** (20 searches)

**Stop condition:** 3 questions max before Phase 1.

## Phase 1: Initial Reconnaissance

**One broad academic search** to map themes, terminology, methodological distinctions.

Synthesize for the checkpoint: themes, terminology variations, methodological distinctions, coverage gaps.

## Phase 2: Framework Selection + Sub-area Generation

Choose framework (from Q2 OR override based on recon):
- **PICO** — most clinical questions (~70% default)
- **SPIDER** — social / qualitative
- **Decomposition** — technology focus
- **Hybrid** — explicit cross-framework mapping

Generate **4-5 sub-area questions** mapped to framework components.

## Checkpoint (grill-me forcing-options moment)

After Phase 2, halt and present:
1. 3-4 sentence recon summary
2. Framework breakdown table (Component | How It Maps | Proposed Sub-area)
3. Depth re-confirmation
4. Sub-area forcing options: "Looks good" / "Adjust: add/remove/merge" / "Restart with different framework"

**Wait for user response before Phase 3.**

## Phase 3: Targeted Searches

Sequential (1 query/sec), budget per depth tier:

**Quick scan (5 searches):** 5 sub-area searches (one per sub-area)

**Standard review (10 searches):**
- 5 sub-area searches
- 2 review article searches (top 2 sub-areas)
- 2 era-gated searches (old + new for most important sub-area)
- 1 follow-up on highest-cited paper

**Deep dive (20 searches):**
- 5 sub-area + 5 review article + 4 era-gated + 3 follow-ups + 3 spare for emerging threads

## Cross-Search Intelligence

After Phase 3:
1. **Repeat-hit papers** — same paper in 3+ sub-area searches = likely foundational
2. **Recurring authors** — same author in multiple searches = dominant research group
3. **Citation-per-year heuristic** — a 2023 paper with 150 citations >> 2008 paper with 150 citations

## Phase 4: Research Guide Report

8 sections:
1. **Topic Overview** — single tight paragraph (4-6 sentences)
2. **Start Here — Priority Reading Order** — 5-7 papers: best recent review → foundational → frontier → gap. Each: title + authors/year + 1-sentence contribution + "what to look for"
3. **How the Field Got Here** — chronological narrative + timeline table (5-8 milestones) + terminology evolution
4. **Sub-area Guides** (one per sub-area): What the Research Shows + Key Papers + Key Search Terms + Boolean Search Strings
5. **Key Research Groups** — top 3-5 authors/groups with affiliations + representative paper
6. **Open Questions & Gaps** — methodological / population-context / conceptual-theoretical
7. **Bibliography** — alphabetical, every entry with source URL
8. **Audit Log** — search summary + counts + coverage notes

## Anti-Patterns To Reject

- Parallelizing search calls
- Skipping the interactive checkpoint
- Padding thin results with training knowledge
- Defaulting to non-PICO framework without justification
- Citing papers that didn't come from this session's searches
- Skipping era-gated searches in standard/deep budgets
- Skipping cross-search intelligence

---

**Version:** 1.0.0 (distilled 2026-07-23)
**Source:** claude-skills/research/litreview — MIT License
