---
name: iso27001-audit-prep
description: ISO 27001 ISMS audit readiness 6-question forcing interrogation. Use before annual Clause 9.2 internal audit, surveillance audit prep, or stage 1 certification readiness.
type: Playbook
---

# ISO 27001 ISMS Audit Prep

Six forcing questions before any internal audit, stage 1 readiness, or surveillance audit.

## When to Run
- Before annual Clause 9.2 internal audit
- Before stage 1 / stage 2 certification audit
- Before surveillance audit (year 2 / year 3)
- After material change to ISMS scope
- Post-incident (breach triggers ad-hoc ISMS audit)
- Quarterly during high-growth phase

## The Six ISMS Questions

### 1. What's the audit scope, and is rolling 3-year coverage on track?
**No 3-year coverage discipline = no defensible programme.**
- Every Clause 4–10 + every applicable Annex A control must be audited at least once per 3-year cycle
- Confirm auditor independence — no self-audit on any sample

### 2. When was the risk register last refreshed, and are treatments linked to Annex A controls?
**Stale risk register = certification finding.**
- Quarterly refresh expected; annual minimum
- Every high/critical risk must link to ≥ 1 Annex A control treating it
- Residual risk acceptance documented + signed

### 3. Show me the access review records — quarterly cadence, the last 4 quarters.
**Most-cited finding area.**
- Annex A.5.15 + A.8.2 + A.8.3 access controls
- Sample real records from Okta / IAM, not curated audit-prep packs
- For each terminated employee in last 90 days: deprovisioning evidence within 24-hour SLA
- Privileged access reviewed at finer granularity

### 4. What's the supplier inventory + last review evidence?
**Second-most-cited finding area.**
- Annex A.5.19–A.5.21 supplier management
- Critical SaaS suppliers reviewed at least annually
- DPAs signed for personal-data sub-processors
- AI-specific contract clauses where third-party AI services in use

### 5. Where's the incident response evidence + post-incident review?
**A.5.24-27 + A.6.8 — high-stakes audit area.**
- Severity definitions documented + consistently applied
- Last 5 incidents have post-incident review (PIR) within 30-day SLA
- GDPR Article 33 / 34 notification timing aligned with A.5.24
- Blameless retro culture; not punitive

### 6. What's the management review cadence + inputs?
**Clause 9.3 required inputs are prescriptive — easy to miss.**
- Required inputs: audit results, risks, performance, nonconformities, opportunities
- Schedule: annual minimum; quarterly preferred for mature programs
- Outputs documented + tracked to closure

## Cross-Framework Reuse
- **SOC 2:** 75% control overlap — coordinate audit calendar, share evidence
- **ISO 42001:** 60% reuse for AI management systems
- **GDPR:** Article 32 organizational measures overlap

## Output Verdict
🟢 **READY** | 🟡 **CLOSE-CRITICALS-FIRST** | 🔴 **NOT-READY**

Plus top 3 actions with owner + corrective-action timeline.
