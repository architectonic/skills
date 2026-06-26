---
name: data-quality-auditor
description: Audit datasets for completeness, consistency, accuracy, and validity. Profile data distributions, detect anomalies and outliers, surface structural issues, and produce an actionable remediation plan. Use when the user asks to check data quality, profile a dataset, hunt outliers or missing values, or validate data before analysis or model training.
tags: [data-science, data-quality, data-profiling, data-validation, missing-values, outliers, etl]
type: Playbook
---

# Data Quality Auditor

Systematically assess dataset health, surface hidden issues that corrupt downstream analysis, and prescribe prioritized fixes. Move fast, think in impact, and never let "good enough" data quietly poison a model or dashboard.

## Modes

### Mode 1 — Full Audit (New Dataset)

1. **Profile** — Get shape, types, completeness, and distributions
2. **Missing Values** — Classify missingness patterns (MCAR/MAR/MNAR)
3. **Outliers** — Flag anomalies using IQR and Z-score methods
4. **Cross-column checks** — Referential integrity, duplicate rows, logical constraints
5. **Score & Report** — Assign a Data Quality Score (DQS) and produce the remediation plan

### Mode 2 — Targeted Scan (Specific Concern)

1. Ask: *What broke, when did it start, and what changed upstream?*
2. Run checks against the suspect columns only
3. Compare distributions against a known-good baseline if available
4. Trace issues to root cause (source system, ETL transform, ingestion lag)

### Mode 3 — Ongoing Monitoring Setup

1. Identify the 5–8 critical columns driving key metrics
2. Define thresholds: acceptable null %, outlier rate, value domain
3. Generate monitoring checklist and alerting logic
4. Schedule checks at ingestion cadence

## Data Quality Score (DQS)

The DQS is a 0–100 composite score across five dimensions. Report it at the top of every audit.

| Dimension | Weight | What It Measures |
|---|---|---|
| Completeness | 30% | Null / missing rate across critical columns |
| Consistency | 25% | Type conformance, format uniformity, no mixed types |
| Validity | 20% | Values within expected domain (ranges, categories, regexes) |
| Uniqueness | 15% | Duplicate rows, duplicate keys, redundant columns |
| Timeliness | 10% | Freshness of timestamps, lag from source system |

**Scoring thresholds:**
- 🟢 85–100 — Production-ready
- 🟡 65–84 — Usable with documented caveats
- 🔴 0–64 — Remediation required before use

## Proactive Risk Triggers

Surface these unprompted whenever you spot the signals:

- **Silent nulls** — Nulls encoded as `0`, `""`, `"N/A"`, `"null"` strings. Completeness metrics lie until these are caught.
- **Leaky timestamps** — Future dates, dates before system launch, or timezone mismatches.
- **Cardinality explosions** — Free-text fields with thousands of unique values masquerading as categorical.
- **Duplicate keys** — PKs that aren't unique invalidate joins and aggregations downstream.
- **Distribution shift** — Columns where current distribution diverges from baseline (>2σ on mean/std).
- **Correlated missingness** — Nulls concentrated in a specific time range, user segment, or region (MNAR, not random).

## Remediation Playbook

### Missing Values

| Null % | Recommended Action |
|---|---|
| < 1% | Drop rows (if dataset is large) or impute with median/mode |
| 1–10% | Impute; add a binary indicator column `col_was_null` |
| 10–30% | Impute cautiously; investigate root cause; document assumption |
| > 30% | Flag for domain review; do not impute blindly; consider dropping column |

### Outliers

- **Likely data error** (value physically impossible): cap, correct, or drop
- **Legitimate extreme** (valid but rare): keep, document, consider log transform for modeling
- **Unknown** (can't determine without domain input): flag, do not silently remove

### Duplicates

1. Confirm uniqueness key with data owner before deduplication
2. Prefer `keep='last'` for event data (most recent state wins)
3. Prefer `keep='first'` for slowly-changing-dimension tables

## Quality Loop

Tag every finding with a confidence level:
- 🟢 **Verified** — confirmed by data inspection or domain owner
- 🟡 **Likely** — strong signal but not fully confirmed
- 🔴 **Assumed** — inferred from patterns; needs domain validation

Never auto-remediate 🔴 findings without human confirmation.

## Output Structure

All audit reports follow:

**Bottom Line** — DQS score and one-sentence verdict (e.g., "DQS: 61/100 — remediation required before production use")

**What** — The specific issues found (ranked by severity × breadth)

**Why It Matters** — Business or analytical impact of each issue

**How to Act** — Specific, ordered remediation steps
