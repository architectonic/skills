---
name: regulated-domain-skill-governance
description: Govern skills that operate in regulated domains such as finance, healthcare, legal, or any domain with compliance, disclosure, or liability requirements. Use when reviewing or creating skills that touch regulated APIs, produce reports that could be construed as advice, or handle sensitive domain data.
tags: [skill-management, skill-management, governance, regulated-domain, compliance, disclosure]
type: Playbook
---

# regulated-domain-skill-governance

Govern skills that operate in regulated domains such as finance, healthcare, legal, or any domain with compliance, disclosure, or liability requirements.

## When to use

- A skill interfaces with regulated APIs (trading, banking, health records, legal filings)
- A skill produces reports that could be construed as professional advice
- A skill handles sensitive domain data (PHI, PII, financial records)
- A skill operates in a domain with specific disclosure or licensing requirements

## Why it matters

Regulated-domain skills carry legal, financial, and ethical risk beyond ordinary agent skills. A backtest skill that looks like investment advice, or a health skill that looks like medical guidance, can create liability even when the agent is just following instructions.

## Governance envelope

```
User request
→ Formalized assumptions
→ Source-of-truth CLI/help/schema checks
→ Isolated run folder
→ Raw and normalized data artifacts
→ Data fingerprints
→ Deterministic simulation script
→ Metrics / report / disclosures
→ Caveats and provenance
```

## Required patterns

### Mandatory disclosure blocks
- Every regulated-domain skill must include a disclosure section
- Disclosures must state what the skill does NOT do (e.g., "not investment advice")
- Disclosures must clarify paper vs. live vs. hypothetical contexts
- Disclosures must note data limitations and assumptions

### Credential handling
- Regulated APIs require explicit secret-handling rules
- Skills must never hardcode credentials
- Skills must document which credentials are needed and why
- Paper/live/hypothetical modes must be clearly separated in credential usage

### Reproducible run contract
- Each run must produce a run folder with inputs, parameters, and outputs
- Data fingerprints (hashes) must be captured for reproducibility
- Assumptions must be explicit and recorded
- Fill models, fee models, and lineage must be documented

### Output separation
- Educational backtests must be clearly separated from investment advice
- Hypothetical results must be labeled as such
- Live trading actions require explicit human approval and separate skill classification
- Report language must be reviewed for regulatory compliance

## Risk classification

| Domain | Default risk class | Notes |
|---|---|---|
| Finance / trading | High | Regulatory, liability, live-mutation |
| Healthcare / PHI | Critical | HIPAA, liability, safety |
| Legal | High | Licensing, liability, jurisdiction |
| Government / compliance | High | Regulatory, audit trail |
| Education / research | Medium | Lower direct liability |

## Promotion gate

Regulated-domain skills are promoted only if:
- Disclosure blocks are present and adequate
- Credential handling follows secret-management policy
- Run contract is reproducible and auditable
- Output language is reviewed for domain-appropriate disclaimers
- Risk class is classified and acceptable
- Human review is required before any live/external-mutation use

## Anti-patterns

- Treating a backtest skill as a general-purpose data analysis skill
- Allowing paper-trading skills to execute live trades without re-review
- Copying regulated-domain skills without preserving disclosure blocks
- Assuming MIT/Apache license eliminates regulatory risk

## Sources

- alpacahq/alpaca-skills — official vendor trading API skill with disclosure patterns
- alpacahq-alpaca-skills (graphify-corpus source profile)
