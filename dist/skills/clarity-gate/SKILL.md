---
name: clarity-gate
description: Pre-ingestion verification for epistemic quality in RAG systems. Ensures documents are properly qualified before entering knowledge bases. 9 verification points covering hypothesis vs fact labeling, uncertainty markers, assumption visibility, and data consistency.
tags: [agent-operations, rag, quality-gate, epistemic, document-verification, pre-ingestion]
type: Playbook
---

# Clarity Gate

Pre-ingestion verification system that enforces epistemic quality before documents enter RAG knowledge bases.

**Core Question:** "If another LLM reads this document, will it mistake assumptions for facts?"

**Core Principle:** "Detection finds what is; enforcement ensures what should be. In practice: find the missing uncertainty markers before they become confident hallucinations."

## Critical Limitation

> **Clarity Gate verifies FORM, not TRUTH.**
>
> This skill checks whether claims are properly marked as uncertain — it cannot verify if claims are actually true.
>
> **Risk:** An LLM can hallucinate facts INTO a document, then "pass" Clarity Gate by adding source markers to false claims.
>
> **Solution:** HITL (Human-In-The-Loop) verification is **MANDATORY** before declaring PASS.

## When to Use

- Before ingesting documents into RAG systems
- Before sharing documents with other AI systems
- After writing specifications, state docs, or methodology descriptions
- When a document contains projections, estimates, or hypotheses
- Before publishing claims that haven't been validated
- When handing off documentation between LLM sessions

## The 9 Verification Points

### Epistemic Checks (Points 1-4)

**1. HYPOTHESIS vs FACT LABELING**
Every claim must be clearly marked as validated or hypothetical.

| Fails | Passes |
|-------|--------|
| "Our architecture outperforms competitors" | "Our architecture outperforms competitors [benchmark data in Table 3]" |
| "The model achieves 40% improvement" | "The model achieves 40% improvement [measured on dataset X]" |

**Fix:** Add markers: "PROJECTED:", "HYPOTHESIS:", "UNTESTED:", "(estimated)", "~", "?"

**2. UNCERTAINTY MARKER ENFORCEMENT**
Forward-looking statements require qualifiers.

| Fails | Passes |
|-------|--------|
| "Revenue will be $50M by Q4" | "Revenue is **projected** to be $50M by Q4" |
| "The feature will reduce churn" | "The feature is **expected** to reduce churn" |

**Fix:** Add "projected", "estimated", "expected", "designed to", "intended to"

**3. ASSUMPTION VISIBILITY**
Implicit assumptions that affect interpretation must be explicit.

| Fails | Passes |
|-------|--------|
| "The system scales linearly" | "The system scales linearly [assuming <1000 concurrent users]" |
| "Response time is 50ms" | "Response time is 50ms [under standard load conditions]" |

**Fix:** Add bracketed conditions: "[assuming X]", "[under conditions Y]", "[when Z]"

**4. AUTHORITATIVE-LOOKING UNVALIDATED DATA**
Tables with specific percentages and checkmarks look like measured data.

**Red flag:** Tables with specific numbers (89%, 95%, 100%) without sources

**Fix:** Add "(guess)", "(est.)", "?" to numbers. Add explicit warning: "PROJECTED VALUES - NOT MEASURED"

### Data Quality Checks (Points 5-7)

**5. DATA CONSISTENCY**
Scan for conflicting numbers, dates, or facts within the document.

**Red flag:** "500 users" in one section, "750 users" in another

**Fix:** Reconcile conflicts or explicitly note the discrepancy with explanation.

**6. IMPLICIT CAUSATION**
Claims that imply causation without evidence.

**Red flag:** "Shorter prompts improve response quality" (plausible but unproven)

**Fix:** Reframe as hypothesis: "Shorter prompts MAY improve response quality (hypothesis, not validated)"

**7. FUTURE STATE AS PRESENT**
Describing planned/hoped outcomes as if already achieved.

**Red flag:** "The system processes 10,000 requests per second" (when it hasn't been built)

**Fix:** Use future/conditional: "The system is DESIGNED TO process..." or "TARGET: 10,000 rps"

### Verification Routing (Points 8-9)

**8. TEMPORAL COHERENCE**
Document dates and timestamps must be internally consistent and plausible.

| Fails | Passes |
|-------|--------|
| "Last Updated: December 2024" (when current is 2026) | "Last Updated: January 2026" |
| v1.0.0 dated 2024-12-23, v1.1.0 dated 2024-12-20 | Versions in chronological order |

**Sub-checks:**
1. Document date vs current date
2. Internal chronology (versions, events in order)
3. Reference freshness ("current", "now", "today" claims)

**9. EXTERNALLY VERIFIABLE CLAIMS**
Specific numbers that could be fact-checked should be flagged for verification.

| Type | Example | Risk |
|------|---------|------|
| Pricing | "Costs ~$0.005 per call" | API pricing changes |
| Statistics | "Papers average 15-30 equations" | May be wildly off |
| Rates/ratios | "40% of researchers use X" | Needs citation |
| Competitor claims | "No competitor offers Y" | May be outdated |

**Fix options:**
1. Add source with date
2. Add uncertainty marker
3. Route to HITL or external search
4. Generalize ("low cost" instead of "$0.005")

## The Verification Hierarchy

```
Claim Extracted → Does Source of Truth Exist?
                    |
     +--------------+--------------+
     YES                           NO
     |                             |
Tier 1: Automated              Tier 2: HITL
Consistency & Verification     Two-Round Verification
     |                             |
PASS / BLOCK                Round A → Round B → APPROVE / REJECT
```

### Tier 1: Automated Verification
- **Internal Consistency:** Figure vs. Text, Abstract vs. Body, Table vs. Prose, Numerical consistency
- **External Verification:** User-provided connectors to structured sources

### Tier 2: Two-Round HITL Verification — MANDATORY
- **Round A:** Derived Data Confirmation — Claims from sources found in session
- **Round B:** True HITL Verification — Claims needing actual verification

## Exclusion Blocks

When content cannot be resolved (no SME available, legacy prose, etc.), mark it as excluded:

```markdown
<!-- CG-EXCLUSION:BEGIN id=auth-legacy-1 -->
Legacy authentication details that require SME review...
<!-- CG-EXCLUSION:END id=auth-legacy-1 -->
```

**Rules:**
- IDs must match: `[A-Za-z0-9][A-Za-z0-9._-]{0,63}`
- No nesting or overlapping blocks
- Each ID used only once
- Documents with exclusion blocks are **not RAG-ingestable**

## Related Skills

- `rag-implementation` — RAG pipeline design
- `context-engineering` — Context management for agent systems
- `data-structure-protocol` — Structural memory for codebases

## Source

- [Clarity Gate Repository](https://github.com/frmoretto/clarity-gate)
- Distilled from antigravity-awesome-skills collection
