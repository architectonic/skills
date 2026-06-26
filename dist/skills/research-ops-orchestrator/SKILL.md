---
name: research-ops-orchestrator
description: Domain orchestrator for enterprise Research Operations. Routes research planning inquiries to the right sub-skill: clinical-research (study design, endpoints, sample size), research-finance (R&D budget, burn rate, CapEx/OpEx), market-research (TAM/SAM/SOM, surveys, segmentation), or product-research (user interviews, usability tests, insight synthesis). Use when the inquiry spans research planning, funding, scoping, or synthesis across workstreams.
tags: [research, research-ops, orchestrator, clinical-research, research-finance, market-research, product-research, rd]
type: Playbook
---

# Research Operations — Domain Orchestrator

Routes enterprise research operations inquiries to the appropriate sub-skill. This is the **planning, funding, scoping, and synthesis** counterpart to the academic `research/` domain (which finds literature, grants, and patents).

## When to Invoke

| Symptom | Sub-skill |
|---|---|
| "Design a Phase 2 trial — endpoint and sample size?" | `clinical-research` |
| "What's our R&D burn, and is this cost CapEx or OpEx?" | `research-finance` |
| "What's the TAM and how do we survey the segment?" | `market-research` |
| "How many users to interview, and how to synthesize?" | `product-research` |

## Routing Logic

Single-signal → clarifying question. Mixed signals → highest-confidence first, chain second. Never silently chain.

### Signal Table

| Signal | Keywords | Sub-skill |
|---|---|---|
| **CLINICAL** | clinical trial, study design, protocol, endpoint, sample size, power, phase 1/2/3, biostatistics | `clinical-research` |
| **RD_FINANCE** | R&D budget, burn, runway, F&A, capitalize vs expense, R&D capex, portfolio ROI | `research-finance` |
| **MARKET** | TAM/SAM/SOM, market sizing, survey design, sampling, segmentation, competitive intelligence | `market-research` |
| **PRODUCT** | user interview, JTBD, usability test, concept test, insight synthesis, saturation | `product-research` |

## Workflow

1. **Explore before asking** — Check workspace for artifacts that resolve the lane (protocol draft → clinical, budget → finance, TAM model → market, interview guide → product)
2. **If ambiguous** — ONE forcing question with recommended answer
3. **Multi-lane inquiries** — Walk depth-first, confirm before chaining
4. **Invoke sub-skill** in forked context with structured inputs
5. **Return digest** — ≤200 words: top 3 findings, top 3 next actions, one grill challenge

## Forcing Questions (one at a time, with canon citation)

- **CLINICAL**: "Is your primary endpoint a clinical outcome or a surrogate?" → Recommended: clinical outcome unless surrogate is FDA-validated. Canon: FDA Surrogate Endpoint Table.
- **RD_FINANCE**: "Research phase or development phase — and can you evidence technical feasibility?" → Recommended: research = expense; development = capitalize-candidate with feasibility evidence. Canon: IAS 38; ASC 730.
- **MARKET**: "TAM top-down or bottoms-up — computed both ways?" → Recommended: both; reconcile the delta. Canon: Bessemer / a16z market-sizing.
- **PRODUCT**: "Generative (discover problems) or evaluative (test a solution)?" → Recommended: name it first; the method follows. Canon: Rohrer's UX research methods (NN/g).

## Anti-Patterns

- ❌ Present clinical power/endpoint output as fact — it is an **estimate** with named clinical owner
- ❌ Auto-decide capitalize-vs-expense — route to **named finance owner**
- ❌ Report market size as single unsourced number — show **method + triangulation + assumptions**
- ❌ Assert product insight from single participant — flag as **ANECDOTE**
- ❌ Run all 4 sub-skills "to be thorough" — pick one, digest, chain if needed

## Distinct From

- `research/` (academic) — finds literature, grants, patents; this plans/funds/scopes/synthesizes
- `ra-qm-team` — regulatory/QM submission; clinical-research designs the study
- `finance/financial-analysis` — corporate close + valuation; research-finance manages R&D spend
- `product-team` — persona/journey artifacts, live A/B; product-research is method + repository
- `marketing-skill` — campaign analytics; market-research is upstream methodology
