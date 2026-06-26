---
name: patent
description: Patent prior-art and landscape intelligence — not generic patent help. Commits to one of five sub-use-cases via forcing intake (novelty search / freedom-to-operate / competitive landscape / acquisition diligence / litigation prior-art) before any search runs. Searches Google Patents, Espacenet, USPTO. Output is a structured report with verdict, ranked closest art with claim-text, CPC-class-aware landscape, family-resolved hits, FTO flags, strategy recommendations, and audit log. Use when the user asks for patent searching or analysis. Produces search signal, not legal advice — always recommends consulting a patent attorney.
type: Playbook
---

# Patent — Prior-Art + Landscape Intelligence

> **Legal disclaimer:** This skill produces search signal, not legal advice. Verdicts are technical assessments. **Always consult a patent attorney before filing or licensing decisions.**

> **Out of scope:** trademark, copyright, trade-secret.

## Non-Generic Framing

This skill is **prior-art + landscape intelligence**. It **refuses to be a bucket**. Every invocation commits to one of five sub-use-cases via grill-me intake before any search runs.

| Sub-use-case | Search strategy | Report emphasis |
|---|---|---|
| **Novelty search** | Narrow + claims-text focused | Closest art + claim-differentiation |
| **Freedom-to-operate** | Broad + active patents only; jurisdiction-filtered | FTO flags + claim-by-claim risk |
| **Competitive landscape** | Breadth + filer tally + CPC trends | Filer map + investment hotspots |
| **Acquisition diligence** | Specific assignee + portfolio scope | Portfolio table + ownership verification |
| **Litigation prior-art** | Specific target patent + adjacent art before priority date | Knock-out candidates ranked |

## Agent Integrity Rules

- **Execution discipline.** Sequential search calls only. 1 query/sec rate limit.
- **Source discipline.** Cite only patents returned by this session's tool calls.
- **Three-count tracking.** Queries sent / patents received / patents cited.
- **Retry policy.** On failure → wait 3s → retry once → log.

## Phase 1: Grill-Me Intake (6 forcing questions)

### Q1 — Invention description
> **Describe the invention in 2–3 sentences. What does it do, and what's new about it?**

**Refuse mush.** If answer is generic, ask once more: "What does it do that existing systems don't?"

### Q2 — Sub-use-case commitment
> **What's the purpose of this search? Pick one:**
> 1. Novelty search (am I novel enough to file)
> 2. Freedom-to-operate (will I get sued if I ship)
> 3. Competitive landscape (who else plays here)
> 4. Acquisition diligence (does target really own X)
> 5. Litigation prior-art hunting (kill a specific patent)

**Refuse to start without a pick.**

### Q3 (FTO/landscape/diligence only) — Jurisdictions
> **Which jurisdictions matter? US / EP / CN / JP / KR / PCT / worldwide.**

### Q4 — Known prior art
> **Have you already seen prior art close to this? Cite a patent number or paper.**

### Q5 (novelty/FTO only) — Risk tolerance
> **Risk tolerance: strict (one close hit means abandon) or signal-gathering (want the lay of the land)?**

### Q6 (novelty/FTO only) — Attorney status
> **Have you spoken to a patent attorney? This skill produces search signal, not legal advice.**

## Phase 2: Search Strategy Selection

Deterministic from intake answers. Returns: query plan (5-8 queries) + ranking heuristic + report emphasis flags.

## Phase 3: Multi-Source Search (Sequential)

**Source priority:**
1. **Google Patents** (https://patents.google.com) — workhorse, no auth required
2. **Espacenet** (https://worldwide.espacenet.com) — global coverage
3. **USPTO PPS** (https://ppubs.uspto.gov) — US deep dive

**Per-sub-use-case query patterns:**

- **Novelty:** 3 narrow + 2 broad concept + 1 CPC-class-restricted
- **FTO:** Jurisdiction-filtered, active patents only, claim text extraction
- **Landscape:** Broader queries, CPC class tally, 10-year filing trend
- **Acquisition diligence:** Specific assignee + assignment chain check
- **Litigation:** Target patent + art before priority date in same CPC classes

## Phase 4: Claim Extraction + Relevance Scoring

For each closest-art hit: pull **independent claim 1** (broadest claim), pull key dependent claims, score relevance against invention description.

## Phase 5: Family Resolution

Group same-invention filings across jurisdictions by family ID or priority number to avoid double-counting.

## CPC/IPC Classification Awareness

After initial search, extract CPC/IPC classes from top 5 hits and run **one class-restricted query**. This consistently surfaces art that keyword search misses.

## Phase 6: Report Generation (8 Sections)

1. **Executive Summary + Verdict** — Sub-use-case banner + one-line verdict + legal disclaimer
2. **Closest Prior Art** — 5-10 patents ranked. Per hit: title + assignee + dates + independent claim 1 text + relevance score
3. **Patent Landscape** — Top filers table + 10-year trend + CPC distribution
4. **Citation Graph Signals** — Foundational patents + recent high-cite activity
5. **Geographic Coverage** — Filings by jurisdiction (FTO/landscape/diligence only)
6. **FTO Flags** (FTO only) — Active patents posing risk. Per flag: patent + jurisdiction + claims + risk level
7. **Strategy + Recommendations** — Sub-use-case-specific + mandatory attorney disclaimer
8. **Audit Log** — Searches table + counts + tool constraints

## Date Discipline

Distinguish at every hit: filing date / priority date / publication date / grant date. Surface the **legally-relevant date** per sub-use-case.

## Phase 7: Deliver

- Save report as markdown
- Chat summary: sub-use-case + verdict + audit counts
- Reminder: "Consult patent attorney before filing/licensing"

## Anti-Patterns To Reject

- Starting search before user commits to sub-use-case
- Batching intake questions
- Keyword-only search without CPC/IPC class follow-up
- Treating family members as separate hits
- Confusing filing/priority/publication dates
- Skipping legal disclaimer for novelty/FTO
- Reporting verdict without claim-text evidence

---

**Version:** 1.0.0 (distilled 2026-07-23)
**Source:** claude-skills/research/patent — MIT License
