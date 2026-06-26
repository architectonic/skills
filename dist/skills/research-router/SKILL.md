---
name: research-router
description: Default entry point for any research request — a hybrid router that classifies the question deterministically and either delegates to a specialist research skill (pulse for trends/sentiment, litreview for academic literature, syllabus for course reading, patent for prior-art, dossier for entity research) or runs its own plan-decompose-multi-source-search-synthesize-cite fallback workflow. Always surfaces the routing decision so users can override. Use when the user makes any research request that doesn't obviously match a more-specific specialist skill (e.g., 'research [topic]', 'look into [topic]', 'what do we know about [topic]').
type: Playbook
---

# Research — Hybrid Router + Fallback

**The runtime orchestrator for the research domain.** Deterministic classification → specialist delegation OR own plan-decompose-search-synthesize-cite workflow.

## Specialist Registry

| Specialist | Routing signals | Domain |
|---|---|---|
| `pulse` | reddit / hn / sentiment / trending / "what's people saying" / "pulse on" | Multi-source recency research |
| `litreview` | literature review / PICO / SPIDER / systematic review / meta-analysis | Academic literature orientation |
| `syllabus` | syllabus / course outline / curriculum / "reading list" / "for my class" | Course supplementary reading |
| `patent` | prior art / FTO / freedom to operate / patent / "patent landscape" / novelty search | Patent prior-art + landscape |
| `dossier` | "dossier on" / "due diligence" / "background check" / "prep me for" / "competitor research" | Decision-grade entity research |

## Agent Integrity Rules

- **Source discipline**: Cite only sources returned by this session's tool calls. Training knowledge labeled `[Background — not from search]`.
- **Three-count tracking**: Queries sent / sources received / sources cited.
- **Retry policy**: On failure → wait 3s → retry once → log. After 3 consecutive failures: stop, alert user.
- **Routing discipline**: Never delegate silently. Always state the decision + accept override.

## Phase 1: Grill-Me Intake (2–4 Questions)

### Q1 (always) — Research question

> **What's the research question? State it in 1–2 sentences. Specific is better than broad.**

**Refuse mush.** Push back once if too vague.

### Q2 (always) — Output preference

> **What output do you want?**
> 1. Quick chat briefing (markdown in chat)
> 2. Standalone document (structured report with citations)

### Q3 (only if classification ambiguous) — Domain disambiguation

> **Quick clarification — pick the closest match:**
> 1. Academic literature
> 2. Industry / trends / sentiment
> 3. Specific entity (company, person, org)
> 4. Technology / patents
> 5. Course material
> 6. None of the above — run general research

### Q4 (only if Q3 = "none of the above") — General-research scope

> **Quick scan (5 searches) or thorough (15 searches)?**

## Phase 2: Deterministic Classification

Signals are case-insensitive literal phrases (multi-word substring match):

```
pulse:    ["reddit", "hn", "hacker news", "sentiment", "trending",
           "what are people saying", "pulse on", "take the pulse"]
litreview:["literature review", "lit review", "pico", "spider",
           "systematic review", "review papers on", "meta-analysis"]
syllabus: ["syllabus", "course outline", "curriculum", "reading list",
           "for my class", "for my students"]
patent:   ["prior art", "fto", "freedom to operate", "patent",
           "patent landscape", "novelty search", "ip landscape"]
dossier:  ["dossier on", "due diligence", "background check",
           "prep me for", "competitor research", "interview prep"]
```

Scoring: count of signal phrases matched in question (case-insensitive).
- **≥2 signals** → route to that specialist (high confidence)
- **1 signal, single specialist** → route (weak match)
- **Otherwise** → ask Q3, then route or fallback

## Phase 3a: Specialist Delegation

When delegating:
1. Pass the user's question verbatim plus output preference
2. **Let the specialist run its own grill-me intake** — do NOT pre-answer
3. Tag output with `[Delegated to: research → {specialist}]`

## Phase 3b: Own Fallback Workflow

If no specialist matched, run the 8-step fallback:

1. **Decompose** — Break into 3–5 sub-questions (what / why / how / who / what's next)
2. **Source Selection** — Per sub-question: recency-sensitive → WebSearch+WebFetch; academic → Google Scholar; entity → offer dossier override
3. **Search** — Sequential per sub-question, 1 q/sec, broad-to-narrow
4. **Read + Extract** — WebFetch high-signal results
5. **Synthesize** — Per sub-question: 2–4 paragraphs with inline citations
6. **Cross-Cutting Patterns** — Consensus, controversy, gaps across sub-questions
7. **Output** — Markdown brief or structured report
8. **Audit Log** — Three counts + per-source tier

## Routing Transparency Protocol (Mandatory)

After classification, **always**:
1. **State the decision**: "Routing to `litreview` because you mentioned PICO and meta-analysis (2 signals)."
2. **Offer override**: "If you want general research instead, say so now."
3. **Wait** for confirmation (or auto-proceed after 5s).
4. **If user overrides** → accept, re-route, log the override.

**Never delegates silently.**

## Output Format (Fallback)

```markdown
# [Research Question] — Briefing
*Generated: [DATE] | Routed: [specialist | fallback]*

## TL;DR
[2-3 sentences]

## Findings
### [Sub-question 1]
[2-4 paragraphs with inline citations]

## Cross-Cutting Patterns
[1-2 paragraphs]

## Sources
[Numbered list with URLs, reliability tier]

## Audit
[Three counts + per-source tier + failures]
```

## Anti-Patterns Rejected

- LLM-reasoned classification (must be deterministic keyword matching)
- Silent delegation
- Routing to specialist when classification is genuinely ambiguous
- Pre-answering the specialist's grill-me intake
- Running fallback when a specialist would clearly do better
- Fabricating sources when search is thin

---

**Version:** 1.0.0 (distilled 2026-07-23)
**Source:** claude-skills/research/research — MIT License
