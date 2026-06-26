---
name: dossier
description: Decision-grade entity research — produces a hypothesis-tested dossier on a specific company, person, nonprofit, or government org. Forces intake to state a hypothesis upfront so the dossier tests it rather than confirms it. Output is a structured report with verdict on hypothesis, identity facts, 12-month activity timeline, network and reputation signals, red flags, conversation hooks tied to specific findings, and source-provenance audit log. Use when the user asks for background research, diligence, or meeting prep on a specific entity (e.g., 'prep me for a meeting with [person/company]', 'due diligence on [company]').
type: Playbook
---

# Dossier — Decision-Grade Entity Research

## Non-Generic Framing — The Differentiator

This skill is **decision-grade entity research with hypothesis-testing**. It **refuses** to be "tell me about Microsoft". Every invocation forces the user to expose their hypothesis upfront (Q4) so the dossier *tests* it rather than confirms it.

The use case shape:

> "I'm pitching Microsoft Tuesday. My hypothesis is they're consolidating AI spend on their first-party Foundry platform. Validate or disprove, and give me three conversation hooks tied to what you find."

**NOT:**

> "Tell me about Microsoft."

The forcing Q4 — the hypothesis question — is the non-generic anchor. Skip it and the skill produces a Wikipedia summary.

## Agent Integrity Rules

- **Execution discipline.** Sequential search calls. WebSearch + WebFetch with 1 q/sec etiquette. Confirm response received before next call.
- **Source discipline.** Cite only sources returned by this session's tool calls. Wikipedia / training knowledge labeled `[Background — verify before quoting]` and excluded from primary findings count.
- **Three-count tracking.** Queries sent / sources received / sources cited. Plus per-tier breakdown (primary / secondary / tertiary).
- **Retry policy.** On failure → wait 3s → retry once → log. After 3 consecutive failures: stop, alert user.
- **Source reliability tier.** Each citation tagged primary (official, SEC, court records) / secondary (mainstream news, trade press) / tertiary (blogs, forums).

## Phase 1: Grill-Me Intake (6 forcing questions, one at a time)

### Q1 (root) — Subject identity

> **Who is the subject? Give me the exact name and, if a company, the website or LinkedIn URL. If a person, their LinkedIn URL or a unique identifier (company affiliation + role).**

If user gives only a name, push for a second identifier. **Refuse to proceed on ambiguous names.**

### Q2 (depends on Q1) — Subject type

> **What kind of subject is this? Pick one: person / company / nonprofit / government org / other.**

Forcing choice. "Other" requires a one-line description.

### Q3 (depends on Q2) — Purpose

> **What are you preparing for? Pick one:**
> 1. Sales meeting / partnership pitch
> 2. Investment diligence
> 3. Acquisition diligence
> 4. Journalism / due diligence
> 5. Job interview prep
> 6. Competitive intelligence
> 7. Personal vetting
> 8. Other (specify)

### Q4 (depends on Q3) — **Hypothesis — MANDATORY**

> **What's your hypothesis going in? What do you already believe about this subject, and what do you want to verify or disprove?**

**MANDATORY.** If user says "I don't have one", push back **once**: "Then guess. Commit to a position you can update later."

If still refused: fall back to implicit hypothesis "what's the most surprising thing I could find?" and **flag the fallback in audit log**.

### Q5 (depends on Q3) — Depth

> **Time horizon: 5-minute brief or 15-minute decision-grade dossier?**

### Q6 (asked only if Q3 ∈ {journalism, personal vetting}) — Sensitivities

> **Anything sensitive to exclude? E.g., personal medical, family details, political history, or specific topics off-limits?**

**Stop condition:** After Q6 (or earlier with dependency skips), commit and start Phase 2.

## Phase 2: Subject Disambiguation

Before Phase 3, resolve the subject to a specific entity:
- For people: confirm LinkedIn URL OR (employer + role + city)
- For companies: confirm domain OR (legal name + incorporation jurisdiction)
- For nonprofits: confirm EIN OR (legal name + state)
- For government orgs: confirm official .gov URL

If still ambiguous: **halt and re-ask Q1**. Refuse to proceed.

## Phase 3: Source Matrix Selection

Routed by Q2 subject type:

- **Person:** LinkedIn, personal website, Twitter/X, GitHub, Google Scholar, news
- **Company:** Official website, SEC EDGAR (public), Crunchbase, news, GitHub (tech orgs), Glassdoor
- **Nonprofit:** ProPublica Nonprofit Explorer (Form 990s), official website, news
- **Government org:** Official .gov sites, news, ProPublica

## Phase 4: Hypothesis-Driven Search

Every search MUST be classified as either:
- **Supporting evidence** (confirms hypothesis), OR
- **Disconfirming evidence** (would refute hypothesis)

**≥30% of search budget allocated to disconfirming queries.**

## Phase 5: 12-Month Activity Timeline

Categories: news (acquisitions, hires, departures, product launches), funding rounds, controversies/legal events, public statements/strategy shifts. Reverse chronological.

## Phase 6: Network + Reputation Signals

**Network:** investors, customers, partners (companies); co-founders, advisors, board roles (people). 5-10 entries ranked by relevance to hypothesis.

**Reputation:** sentiment from news, Glassdoor for companies, peer mentions for people.

## Phase 7: Red-Flag Pass

Surface but don't sensationalize: litigation, regulatory actions, unusual departures, financial signals, reputation hits. **Each flag tiered.**

## Phase 8: Conversation Hook Generation

3-5 specific hooks tied to **actual findings**, not generic talking points. Each hook: the hook (one sentence) + the finding it's tied to (with source + tier) + suggested framing (verbatim phrasing).

## Phase 9: Report Generation

9 sections:
1. Executive Summary — who they are + verdict on hypothesis (SUPPORTED / PARTIALLY SUPPORTED / DISPROVEN / INCONCLUSIVE)
2. Identity Facts Table
3. Hypothesis Test — supporting + disconfirming evidence + verdict paragraph
4. 12-Month Activity Timeline
5. Network Signals
6. Reputation Signals
7. Red Flags + Hidden Patterns
8. Conversation Hooks
9. Source Provenance + Audit Log

## Phase 10: Deliver

- Save report as markdown
- Chat summary: file path + verdict on hypothesis + audit counts + tier breakdown

## Anti-Patterns To Reject

- Producing a dossier without forcing Q4 hypothesis
- Allocating <30% of search budget to disconfirming evidence
- Batching intake questions
- Accepting ambiguous subject names
- Generic conversation hooks ("ask about their roadmap")
- Sensationalizing red flags
- Fabricating coverage when sources are blocked

---

**Version:** 1.0.0 (distilled 2026-07-23)
**Source:** claude-skills/research/dossier — MIT License
