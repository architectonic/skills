---
name: Compliance OS — Multi-Framework Compliance Orchestration
description: Meta-orchestrator for compliance teams. CONFIGURE which frameworks apply,
  COMPUTE cross-framework control overlap, SIMULATE internal audits, and CONSOLIDATE
  evidence across multiple frameworks. Supports ISO 27001/13485/42001/14971, EU AI
  Act, MDR 745, GDPR, SOC 2, FDA QSR, NIST CSF 2.0, NIS2, HIPAA. Does NOT replace
  per-framework skills — it orchestrates them.
version: 1.0.0
source: claude-skills/compliance-os/compliance-os (MIT)
author: Alireza Rezvani (distilled by Agent-Memory-Ops-Kit)
tags:
- business
- productivity
- compliance
- grc
- iso27001
- soc2
- gdpr
- hipaa
- nist
- ai-act
- audit
- multi-framework
- okf
type: Playbook
title: Compliance OS — Multi-Framework Compliance Orchestration
domain: business
risk_level: medium
requires_review: true
source_family: amok-native
source_status: adapted
---

# Compliance OS — Multi-Framework Compliance Orchestration

Multi-framework compliance program orchestration. **Four decisions, no per-framework deep-dive:**

1. **Which frameworks apply to this company?** — Rank 12 supported frameworks against company profile (industry, geography, AI use, medical, financial, headcount, customers, healthcare-PHI, NIS2 essential/important entity, US gov contractor).
2. **How much do selected frameworks overlap?** — Compute control-level overlap with confidence rating; output unified control matrix + evidence-reuse opportunities.
3. **What does a mock audit produce?** — Generate 8–15 finding scenarios with severity distribution matching IIA expectations + interview questions per control.
4. **What's the unified evidence checklist?** — Consolidate evidence across enabled frameworks; output which artefact satisfies which controls across which frameworks.

This skill is **NOT** a per-framework deep-dive. The per-framework skills do the operational work. Compliance OS orchestrates them.

## Supported Frameworks

- ISO 27001 (Information Security)
- ISO 13485 (Medical Devices Quality)
- ISO 42001 (AI Management)
- ISO 14971 (Medical Device Risk)
- EU AI Act
- EU MDR 745 (Medical Devices Regulation)
- GDPR
- SOC 2
- FDA QSR (Quality System Regulation)
- NIST CSF 2.0
- NIS2
- HIPAA

## When to use

- Standing up a multi-framework compliance program.
- Planning the annual audit calendar.
- Preparing for certification stage 1.
- Post-acquisition compliance integration.
- Annual program review and framework overlap analysis.

## Key Questions (ask these first)

1. **Have you named every applicable framework?** Forgetting one means rebuilding the audit program later.
2. **What's the most certificate/regulation your company already operates?** That's your reuse anchor. Map every new framework against it.
3. **What's the audit calendar?** A multi-framework program means surveillance audits stacked through the year — plan auditor independence + capacity.
4. **Where is evidence stored?** Multi-framework programs collapse when evidence lives in one team's drive without an index.
5. **What's the management-review cadence across frameworks?** Each framework wants its own management review, but a single integrated review (per ISO Annex SL) typically satisfies all of them with one calendar slot.
6. **Who owns the meta-program?** If no single accountable role, the program fragments.

## Framework Selection Criteria

| Criterion | Frameworks triggered |
|-----------|---------------------|
| Handles personal data (EU) | GDPR |
| Handles PHI (US) | HIPAA |
| SaaS with customer data | SOC 2, ISO 27001 |
| Uses AI/ML systems | EU AI Act, ISO 42001 |
| Medical devices | ISO 13485, MDR 745, ISO 14971, FDA QSR |
| Critical infrastructure (EU) | NIS2 |
| US government contractor | NIST CSF 2.0, FedRAMP |
| Financial data processing | PCI-DSS, SOC 2 |

## Cross-Framework Evidence Reuse

The highest-value insight from multi-framework orchestration: **one piece of evidence can satisfy controls across multiple frameworks.**

Examples:
- ISO 27001 A.9 (Access Control) ↔ SOC 2 CC6.1 ↔ GDPR Article 32
- ISO 27001 A.12 (Operations Security) ↔ NIST CSF PR.DS ↔ SOC 2 CC6.6
- ISO 13485 §4.2 (Document Control) ↔ FDA QSR 820.40 ↔ ISO 27001 A.5

Map these overlaps explicitly to reduce audit preparation burden by 30-50%.

## Source

Distilled from `claude-skills/compliance-os/skills/compliance-os/SKILL.md` (Alireza Rezvani, MIT).
Adapted for Hermes Agent — removed Claude Code-specific tool references.
