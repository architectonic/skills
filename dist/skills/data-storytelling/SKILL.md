---
name: Data Storytelling
description: Transform data into compelling narratives using visualization, context, and persuasive structure. Use when presenting analytics to stakeholders, creating data reports, or building executive presentations.
source: AgentSkillOS (AgentSkillOS/data/skill_seeds/data-storytelling/SKILL.md)
license: MIT
tags: [productivity, data, storytelling, visualization, presentation, analytics, communication]
type: Playbook
---

# Data Storytelling

Transform raw data into compelling narratives that drive decisions and inspire action.

## When to Use This Skill

- Presenting analytics to executives
- Creating quarterly business reviews
- Building investor presentations
- Writing data-driven reports
- Communicating insights to non-technical audiences

## Core Concepts

### Story Structure

```
Setup → Conflict → Resolution

Setup: Context and baseline
Conflict: The problem or opportunity
Resolution: Insights and recommendations
```

### Narrative Arc

```
1. Hook: Grab attention with surprising insight
2. Context: Establish the baseline
3. Rising Action: Build through data points
4. Climax: The key insight
5. Resolution: Recommendations
6. Call to Action: Next steps
```

### Three Pillars

| Pillar | Purpose | Components |
|--------|---------|------------|
| **Data** | Evidence | Numbers, trends, comparisons |
| **Narrative** | Meaning | Context, causation, implications |
| **Visuals** | Clarity | Charts, diagrams, highlights |

## Story Frameworks

### The Problem-Solution Story

```markdown
# Customer Churn Analysis

## The Hook
"We're losing $2.4M annually to preventable churn."

## The Context
- Current churn rate: 8.5% (industry average: 5%)
- Average customer lifetime value: $4,800

## The Problem
73% churned within first 90 days. Common factor: < 3 support interactions.

## The Insight
Customers who don't engage in the first 14 days are 4x more likely to churn.

## The Solution
1. Implement 14-day onboarding sequence
2. Proactive outreach at day 7
3. Feature adoption tracking

## Expected Impact
- Reduce early churn by 40%
- Save $960K annually

## Call to Action
Approve $50K budget for onboarding automation.
```

### The Trend Story

```markdown
# Q4 Performance Analysis

## Where We Started
Q3 ended with $1.2M MRR, 15% below target.

## What Changed
- Oct: Launched self-serve pricing
- Nov: Reduced friction in signup
- Dec: Added customer success calls

## The Transformation
| Metric         | Q3  | Q4  | Change |
|----------------|-----|-----|--------|
| Trial → Paid   | 8%  | 15% | +87%   |
| Time to Value  | 14d | 5d  | -64%   |

## Key Insight
Self-serve + high-touch creates compound growth.
```

### The Comparison Story

```markdown
# Market Opportunity: EMEA vs APAC

| Factor      | Weight | EMEA | APAC |
|-------------|--------|------|------|
| Market Size | 25%    | 5    | 4    |
| Growth      | 30%    | 3    | 5    |
| Competition | 20%    | 2    | 4    |
| Ease        | 25%    | 2    | 3    |
| **Total**   |        | 2.9  | 4.1  |

## Recommendation
APAC first. Higher growth, less competition.
Start with Singapore hub.
```

## Visualization Techniques

### Progressive Reveal

```
Slide 1: "Revenue is growing" [single line chart]
Slide 2: "But growth is slowing" [add growth rate overlay]
Slide 3: "Driven by one segment" [add segment breakdown]
Slide 4: "Which is saturating" [add market share]
Slide 5: "We need new segments" [add opportunity zones]
```

### Contrast and Compare

```
Before/After:
┌─────────────────┬─────────────────┐
│    BEFORE       │     AFTER       │
│  Process: 5 days│  Process: 1 day │
│  Errors: 15%    │  Errors: 2%     │
└─────────────────┴─────────────────┘
```

### Annotation and Highlight

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(dates, revenue, linewidth=2, color='#2E86AB')

ax.annotate('Product Launch\n+32% spike',
    xy=(launch_date, launch_revenue),
    xytext=(launch_date, launch_revenue * 1.2),
    arrowprops=dict(arrowstyle='->', color='#E63946'),
    color='#E63946')

ax.axvspan(growth_start, growth_end, alpha=0.2, color='green', label='Growth Period')
ax.axhline(y=target, color='gray', linestyle='--', label=f'Target: ${target:,.0f}')
```

## Presentation Templates

### Data Story Flow

```
Slide 1: THE HEADLINE — "We can grow 40% faster by fixing onboarding"
Slide 2: THE CONTEXT — Current state metrics, industry benchmarks
Slide 3: THE DISCOVERY — What the data revealed
Slide 4: THE DEEP DIVE — Root cause analysis, segment breakdowns
Slide 5: THE RECOMMENDATION — Proposed actions, resources, timeline
Slide 6: THE IMPACT — Expected outcomes, ROI, risk assessment
Slide 7: THE ASK — Specific request, decision needed, next steps
```

### One-Page Dashboard Story

```markdown
# Monthly Business Review: January 2024

## THE HEADLINE
Revenue up 15% but CAC increasing faster than LTV

## KEY METRICS
┌────────┬────────┬────────┬────────┐
│  MRR   │  NRR   │  CAC   │  LTV   │
│ $125K  │ 108%   │ $450   │ $2,200 │
│  ▲15%  │  ▲3%   │  ▲22%  │  ▲8%   │
└────────┴────────┴────────┴────────┘

## WHAT'S WORKING
✓ Enterprise segment growing 25% MoM
✓ Referral program driving 30% of new logos

## WHAT NEEDS ATTENTION
✗ SMB acquisition cost up 40%
✗ Trial conversion down 5 points

## RECOMMENDATION
1. Shift $20K/mo from paid to content
2. Launch SMB self-serve trial
```

## Writing Techniques

### Headlines That Work

```
BAD: "Q4 Sales Analysis"
GOOD: "Q4 Sales Beat Target by 23% - Here's Why"

BAD: "Customer Churn Report"
GOOD: "We're Losing $2.4M to Preventable Churn"

Formula: [Specific Number] + [Business Impact] + [Actionable Context]
```

### Transition Phrases

```
Building the narrative:
• "This leads us to ask..."
• "When we dig deeper..."
• "The pattern becomes clear when..."

Introducing insights:
• "The data reveals..."
• "What surprised us was..."
• "The key finding is..."

Moving to action:
• "This insight suggests..."
• "Based on this analysis..."
• "Our recommendation is..."
```

### Handling Uncertainty

```
• "With 95% confidence, we can say..."
• "Impact estimate: $400K-$600K"
• "Best case: X, Conservative: Y"
```

## Best Practices

### Do's
- **Start with the "so what"** — Lead with insight
- **Use the rule of three** — Three points, three comparisons
- **Show, don't tell** — Let data speak
- **Make it personal** — Connect to audience goals
- **End with action** — Clear next steps

### Don'ts
- **Don't data dump** — Curate ruthlessly
- **Don't bury the insight** — Front-load key findings
- **Don't use jargon** — Match audience vocabulary
- **Don't show methodology first** — Context, then method
- **Don't forget the narrative** — Numbers need meaning

## Resources

- [Storytelling with Data (Cole Nussbaumer)](https://www.storytellingwithdata.com/)
- [The Pyramid Principle (Barbara Minto)](https://www.amazon.com/Pyramid-Principle-Logic-Writing-Thinking/dp/0273710516)
- [Resonate (Nancy Duarte)](https://www.duarte.com/resonate/)
