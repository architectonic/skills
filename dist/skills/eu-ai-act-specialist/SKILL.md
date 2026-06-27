---
name: eu-ai-act-specialist
title: EU AI Act Compliance Specialist
description: Operational skill for Regulation (EU) 2024/1689. **Three decisions, no
  executive AI strategy:**
type: Playbook
domain: writing
tags:
- writing
- okf
risk_level: medium
requires_review: true
---

# EU AI Act Compliance Specialist

Operational skill for Regulation (EU) 2024/1689. **Three decisions, no executive AI strategy:**

1. **What tier is this AI system?** — prohibited / high-risk / limited-risk / minimal-risk
2. **For high-risk: conformity assessment route + documentation?** — Module A vs Module H + Annex IV
3. **Per organizational role: what are the obligations?** — provider / deployer / importer / distributor matrix

**NOT** executive AI strategy (see chief-ai-officer-advisor). **NOT** a legal substitute. **NOT** GDPR (see gdpr-dsgvo-expert).

## Risk Classification (4 Tiers)

| Tier | Source | Examples | Obligations |
|------|--------|---------|-------------|
| **Prohibited** | Article 5 | Social scoring, emotion recognition in workplace/education, subliminal manipulation, real-time public biometrics | Cannot be placed on market (penalties up to EUR 35M / 7% turnover) |
| **High-risk** | Article 6 + Annex III | CV-screening, credit scoring, biometric categorisation, safety components | Articles 8–17 (provider) + Article 26 (deployer); conformity assessment; CE marking |
| **Limited-risk** | Article 50 | Chatbots, deepfakes, emotion recognition outside Article 5 | Transparency disclosures to natural persons |
| **Minimal-risk** | Default | Spam filters, video-game AI, inventory forecasters | None under the Act |

**Critical carve-outs (Article 6(3)):** An Annex III system is NOT high-risk if it performs a narrow procedural task, improves a previously completed human activity, detects decision-making patterns without replacing human assessment, or performs a preparatory task. **Exception:** Profiling of natural persons is always high-risk.

## Conformity Assessment (Article 43)

Two routes for high-risk systems:

- **Module A — Internal control** (Annex VI): Provider self-assesses. Applies to most Annex III systems with harmonised standards.
- **Module H — Full QMS + notified body** (Annex VII): Required for biometrics systems.

**Annex IV Technical Documentation requires:**
1. General description (intended purpose, identification, version)
2. Detailed system elements (architecture, training data, validation)
3. Monitoring, functioning, and control info
4. Risk management system (Article 9)
5. Post-placing changes
6. Harmonised standards applied
7. EU declaration of conformity (Article 47)
8. Post-market monitoring system (Article 72)

## Per-Role Obligation Matrix

| Role | Primary Articles | Key obligations |
|------|-----------------|-----------------|
| **Provider** | 8–17, 47, 49, 72 | Conformity assessment; CE marking; risk management; data governance; technical docs; post-market monitoring; serious incident reporting |
| **Deployer** | 26 | Use per instructions; human oversight; input data quality; record-keeping; inform workers; FRIA if public-sector/essential-services |
| **Importer** | 23 | Verify conformity; CE marking; technical docs availability |
| **Distributor** | 24 | Verify CE marking + docs before making available |
| **Authorized rep** | 22 | Non-EU providers must appoint one; representative liable for provider obligations |

**Important:** A deployer who substantially modifies a high-risk AI system, or places it on the market under their own name, becomes a **provider** (Article 25).

## GPAI Track (Articles 51–55)
General-purpose AI models have their own track. Stricter rules above 10²⁵ FLOPs training compute (systemic risk threshold).

## Key Workflows

### AI System Intake Review (~2 hours)
1. Document system characteristics
2. Run risk classifier (check Article 5 → Annex III → Article 6(3) carve-outs → Article 50 → minimal)
3. If high-risk: run conformity assessment planner
4. Identify org roles (provider/deployer/both)
5. Cross-check with GDPR DPIA if personal data
6. Cross-check with ISO 42001 AIMS evidence

### Annual Compliance Refresh
1. List all AI systems on/planned for EU market
2. Re-run classifier (Article 5 prohibited list may expand)
3. Re-run obligation tracker (deadlines shift as Title III phases in: 2025 → 2026 → 2027)
4. Verify post-market monitoring + serious incident reporting capacity
5. Update Annex IV technical documentation

## Adjacent Skills
- **gdpr-dsgvo-expert** — GDPR DPIA + lawful basis (most AI systems also trigger GDPR)
- **iso42001-specialist** — ISO 42001 AIMS (satisfies parts of Article 17 QMS)
- **iso27001-audit-prep** — ISO 27001 for cybersecurity requirements (Article 15)
- **compliance-os** — Multi-framework orchestration
