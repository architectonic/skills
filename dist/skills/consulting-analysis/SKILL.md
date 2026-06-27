---
name: consulting-analysis
title: Consulting Analysis & Report Generation
description: Produce professional, consulting-grade research reports in Markdown format,
  covering domains such as **market analysis, consumer insights, brand strategy, financial
  analysis, industry research, competitive intelligence, investment research, and
  macroeconomic analysis**.
type: Playbook
domain: research
tags:
- research
- okf
risk_level: medium
requires_review: true
source_family: agent-skills-standard
source_status: adapted
---

# Consulting Analysis & Report Generation

## Overview

Produce professional, consulting-grade research reports in Markdown format, covering domains such as **market analysis, consumer insights, brand strategy, financial analysis, industry research, competitive intelligence, investment research, and macroeconomic analysis**.

Operates across two distinct phases:
1. **Phase 1 — Analysis Framework Generation**: Given a research subject, produce a rigorous analysis framework including chapter skeleton, per-chapter data requirements, analysis logic, and visualization plan.
2. **Phase 2 — Report Generation**: After data has been collected, synthesize all inputs into a final polished report.

Output adheres to McKinsey/BCG consulting voice standards.

## Data Authenticity Protocol

**Strict Adherence Rule**: All data presented in the report and visualized in charts MUST be derived directly from the provided **Data Summary** or **External Search Findings**.
- **NO Hallucinations**: Do not invent, estimate, or simulate data. If data is missing, state "Data not available" rather than fabricating numbers.
- **Traceable Sources**: Every major claim and chart must be traceable back to the input data package.

## When to Use This Skill

- User asks for a market analysis, consumer insight report, financial analysis, industry research, or any consulting-grade analytical report
- User provides a research subject and needs a structured analysis framework before data collection
- User provides data summaries, analysis frameworks, or chart files to be synthesized into a report
- The task involves transforming research findings into structured strategic narratives

---

# Phase 1: Analysis Framework Generation

## Purpose

Given a **research subject** (e.g., "Gen-Z Skincare Market Analysis", "NEV Industry Competitive Landscape"), produce a complete **analysis framework** that serves as the blueprint for downstream data collection and final report generation.

## Phase 1 Workflow

### Step 1: Understand the Research Subject

Parse the research subject to identify the **core entity** (market, brand, product, industry, consumer segment, financial instrument, etc.) and the **analytical domain** (marketing, finance, industry, brand, consumer, investment, macro, etc.).

Determine the **natural analytical dimensions** based on domain:

| Domain | Typical Dimensions |
|--------|--------------------|
| Market Analysis | Market size, growth trends, market segmentation, growth drivers, competitive landscape, consumer profiling |
| Brand Analysis | Brand positioning, market share, consumer perception, marketing strategy, competitor comparison |
| Consumer Insights | Demographic profiling, purchase behavior, decision journey, pain points, scenario analysis |
| Financial Analysis | Macro environment, industry trends, company fundamentals, financial metrics, valuation, risk assessment |
| Industry Research | Value chain analysis, market size, competitive landscape, policy environment, technology trends, entry barriers |
| Investment Due Diligence | Business model, financial health, management assessment, market opportunity, risk factors, exit pathways |
| Competitive Intelligence | Competitor identification, strategic comparison, SWOT analysis, differentiated positioning, market dynamics |

### Step 2: Select Analysis Frameworks

Based on the identified domain and research subject, select **2-4** professional analysis frameworks:

#### Strategic & Environmental Analysis

| Framework | Description | Best For |
|-----------|-------------|----------|
| **SWOT Analysis** | Strengths, Weaknesses, Opportunities, Threats | Brand assessment, competitive positioning, strategic planning |
| **PEST / PESTEL Analysis** | Political, Economic, Social, Technological (+ Environmental, Legal) | Macro-environment scanning, market entry assessment |
| **Porter's Five Forces** | Supplier/buyer bargaining power, threat of new entrants/substitutes, industry rivalry | Industry competitive landscape, entry barrier assessment |
| **VRIO Analysis** | Value, Rarity, Imitability, Organization | Core competency assessment, resource advantage analysis |

#### Market & Growth Analysis

| Framework | Description | Best For |
|-----------|-------------|----------|
| **STP Analysis** | Segmentation, Targeting, Positioning | Market segmentation, target market selection |
| **BCG Matrix** | Stars, Cash Cows, Question Marks, Dogs | Product portfolio management, resource allocation |
| **Ansoff Matrix** | Market penetration, market development, product development, diversification | Growth strategy selection |
| **TAM-SAM-SOM** | Total / Serviceable / Obtainable Market | Market sizing, opportunity quantification |

#### Consumer & Behavioral Analysis

| Framework | Description | Best For |
|-----------|-------------|----------|
| **Consumer Decision Journey** | Awareness → Consideration → Evaluation → Purchase → Loyalty | Consumer behavior path mapping |
| **AARRR Funnel** | Acquisition, Activation, Retention, Revenue, Referral | User growth analysis, conversion optimization |
| **RFM Model** | Recency, Frequency, Monetary | Customer value segmentation |
| **Jobs-to-be-Done (JTBD)** | The "job" a user needs to accomplish in a specific context | Demand insight, product innovation direction |

#### Financial & Valuation Analysis

| Framework | Description | Best For |
|-----------|-------------|----------|
| **DuPont Analysis** | ROE = Net Profit Margin × Asset Turnover × Equity Multiplier | Profitability decomposition |
| **DCF** | Free cash flow discounting | Enterprise/project valuation |
| **Comparable Company Analysis** | PE, PB, PS, EV/EBITDA multiples comparison | Relative valuation, peer benchmarking |

#### Competitive & Strategic Positioning

| Framework | Description | Best For |
|-----------|-------------|----------|
| **Benchmarking** | Key performance indicator item-by-item comparison | Competitor gap analysis |
| **Strategic Group Mapping** | Cluster competitors along two key dimensions | Competitive landscape visualization |
| **Value Chain Analysis** | Primary activities + support activities value decomposition | Cost advantage sources |
| **Blue Ocean Strategy** | Value curve, four-action framework (Eliminate-Reduce-Raise-Create) | Differentiated innovation |

#### Selection Principles

1. **Domain-First**: Select 2-4 most relevant frameworks from the toolkit above
2. **Complementary**: Choose complementary rather than overlapping frameworks
3. **Depth over Breadth**: Better to deeply apply 2 frameworks than superficially stack 6
4. **Data-Feasible**: Selected frameworks must be supportable by downstream data collection
5. **Explicit Mapping**: In the chapter skeleton, explicitly annotate which framework each chapter uses

### Step 3: Design Chapter Skeleton

Produce a hierarchical chapter structure. Each chapter must include:
1. **Chapter Title** — Professional, concise, subject-based
2. **Analysis Objective** — What this chapter aims to reveal
3. **Analysis Logic** — The reasoning chain or framework (must reference chosen frameworks)
4. **Core Hypothesis** — Preliminary hypotheses to be validated or refuted by data

### Step 4: Define Data Query Requirements Per Chapter

For each chapter, specify exactly what data needs to be collected:

| Field | Description |
|-------|-------------|
| **Data Metric** | The specific metric or data point needed |
| **Data Type** | Quantitative, Qualitative, or Mixed |
| **Suggested Sources** | Industry reports, financial statements, government statistics, etc. |
| **Search Keywords** | Suggested search queries for data collection |
| **Priority** | P0 (Required) / P1 (Important) / P2 (Supplementary) |
| **Time Range** | The time period the data should cover |

### Step 5: Define Visualization & Content Structure Per Chapter

For each chapter, specify the planned visualization and content structure:
- **Visualization Type**: Line chart, bar chart, pie chart, scatter plot, radar chart, heatmap, Sankey diagram, comparison table, etc.
- **Visualization Title**: Descriptive title for the chart
- **Visualization Data Mapping**: Which data indicators map to X/Y axes or segments
- **Argument Structure**: The planned "What → Why → So What" narrative outline

### Step 6: Output Complete Analysis Framework

Assemble all outputs into a single, structured **Analysis Framework Document** including:
- Research Overview (subject, scope, domain, core research questions)
- Framework Selection table
- Chapter Skeleton with Data Requirements and Visualization Plans
- Data Collection Task List (consolidated P0/P1 requirements across chapters)

---

# Phase 2: Report Generation

## Purpose

Receive the completed **Analysis Framework** and **Data Package** from upstream, and synthesize them into a final consulting-grade report.

## Phase 2 Workflow

### Step 1: Receive and Validate Inputs

Verify that all required inputs are present: Analysis Framework, Data Summary, Chart Files (optional). If any P0 data is missing, note it in the report and flag for the user.

### Step 2: Map Report Structure

Map the final report structure from the Analysis Framework:
1. **Abstract** — Executive summary with key takeaways
2. **Introduction** — Background, objectives, methodology
3. **Main Body Chapters (2...N)** — Mapped from the Framework's chapter skeleton
4. **Conclusion** — Pure, objective synthesis
5. **References** — GB/T 7714-2015 formatted references

### Step 3: Generate Chapter Charts

Before writing the report, generate all planned charts from the Analysis Framework's Visualization & Content Plan. Use ONLY the numbers provided in the Data Summary. Do NOT invent or "smooth" data.

### Step 4: Write the Report

For each sub-chapter, follow the **"Visual Anchor → Data Contrast → Integrated Analysis"** flow:
1. **Visual Evidence Block**: Embed charts
2. **Data Contrast Table**: Create comparison tables for key metrics
3. **Integrated Narrative Analysis**: Write analytical text following "What → Why → So What"

Each sub-chapter must end with a robust analytical paragraph (min. 200 words) that synthesizes conflicting or reinforcing data points and reveals the underlying user tension or opportunity.

### Step 5: Final Structure Self-Check

Before outputting, confirm the report contains all sections in order: Abstract → Introduction → Body Chapters → Conclusion → References.

## Formatting & Tone Standards

### Consulting Voice
- **Tone**: McKinsey/BCG — Authoritative, Objective, Professional
- **Number Formatting**: Use English commas for thousands separators
- **Data emphasis**: **Bold** important viewpoints and key numbers

### Titling Constraints
- **Numbering**: Use standard numbering (`1.`, `1.1`) directly followed by the title
- **Forbidden Prefixes**: Do NOT use "Chapter", "Part", "Section" as prefixes
- **Allowed Tone Words**: Analysis, Profiling, Overview, Insights, Assessment
- **Forbidden Words**: "Decoding", "DNA", "Secrets", "Mindscape", "Solar System", "Unlocking"

### Insight Depth (The "So What" Chain)

Every insight must connect **Data → User Psychology → Strategy Implication**:

```
❌ Bad: "Females are 60%. Strategy: Target females."

✅ Good: "Females constitute 60% with a high TGI of 180. This suggests
   the purchase decision is driven by aesthetic and social validation
   rather than pure utility. Consequently, media spend should pivot
   towards visual-heavy platforms to maximize CTR."
```

## Report Structure Template

```markdown
# [Report Title]

## Abstract
[Executive summary with key takeaways]

## 1. Introduction
[Background, objectives, methodology]

## 2. [Body Chapter Title]
### 2.1 [Sub-chapter Title]
![Chart Description](chart_file_path)

| Metric | Brand A | Brand B |
|--------|---------|---------|
| ... | ... | ... |

[Integrated narrative analysis: What → Why → So What, min. 200 words]

> [Optional: One-liner strategic truth]

## N+1. Conclusion
[Objective synthesis]

## N+2. References
[GB/T 7714-2015 formatted references]
```

## Notes

- This skill does NOT perform data collection — it only produces the framework (Phase 1) and the final report (Phase 2).
- For chart generation, delegate to available visualization/charting skills.
- The report MUST NOT stop after the Conclusion — it MUST include References as the final section.
