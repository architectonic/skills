---
name: progressive-estimation
description: Estimate AI-assisted and hybrid human+agent development work with research-backed PERT statistics and calibration feedback loops. Use when estimating development tasks where AI agents handle part of the work, sprint planning with hybrid teams, batch sizing a backlog, or release date forecasting with confidence intervals.
tags: [productivity, estimation, project-management, pert, sprint-planning, ai-agents, capacity-planning, forecasting]
type: Playbook
---

# Progressive Estimation

Estimate AI-assisted and hybrid human+agent development work using research-backed formulas with PERT statistics, confidence bands, and calibration feedback loops.

**Source:** Distilled from `antigravity-awesome-skills/skills/progressive-estimation/SKILL.md` by Enreign (MIT).

## When to Use This Skill

- Estimating development tasks where AI agents handle part of the work
- Sprint planning with hybrid human+agent teams
- Batch sizing a backlog (handles 5 or 500 issues)
- Staffing and capacity planning with agent multipliers
- Release date forecasting with confidence intervals

## How It Works

1. **Mode Detection** — Determines if the team works human-only, hybrid, or agent-first
2. **Task Classification** — Categorizes by size (XS–XL), complexity, and risk
3. **Formula Application** — Applies research-backed multipliers grounded in empirical studies
4. **PERT Calculation** — Produces expected values using three-point estimation
5. **Confidence Bands** — Generates P50, P75, P90 intervals
6. **Output Formatting** — Formats for Linear, JIRA, ClickUp, GitHub Issues, Monday, or GitLab
7. **Calibration** — Feeds back actuals to improve future estimates

## Examples

**Single task:**
> "Estimate building a REST API with authentication using Claude Code"

**Batch mode:**
> "Estimate these 12 JIRA tickets for our next sprint"

**With context:**
> "We have 3 developers using AI agents for ~60% of implementation. Estimate this feature."

## Best Practices

- Start with a single task to calibrate before moving to batch mode
- Feed back actual completion times to improve the calibration system
- Use "instant mode" for quick T-shirt sizing without full PERT analysis
- Be explicit about team composition and agent usage percentage

## Common Pitfalls

- **Problem:** Overconfident estimates
  **Solution:** Use P75 or P90 for commitments, not P50

- **Problem:** Missing context
  **Solution:** The skill asks clarifying questions — provide team size and agent usage

- **Problem:** Stale calibration
  **Solution:** Re-calibrate when team composition or tooling changes significantly

## PERT Formula

The three-point estimation formula:

```
Expected = (Optimistic + 4 × Most Likely + Pessimistic) / 6
Standard Deviation = (Pessimistic - Optimistic) / 6
```

Confidence intervals:
- **P50**: Expected value (50% confidence)
- **P75**: Expected + 0.67 × SD (75% confidence)
- **P90**: Expected + 1.28 × SD (90% confidence)

## Task Size Classification

| Size | Description | Typical Range |
|------|-------------|---------------|
| XS | Trivial change, well-understood | < 2 hours |
| S | Small feature or bug fix | 2-8 hours |
| M | Medium feature, some unknowns | 1-3 days |
| L | Large feature, significant complexity | 3-5 days |
| XL | Epic-level, needs decomposition | 5+ days |

## Agent Multipliers

| Mode | Multiplier | Notes |
|------|------------|-------|
| Human-only | 1.0× | Baseline |
| Hybrid (30-60% agent) | 0.6-0.8× | Agent handles implementation, human reviews |
| Agent-first (60-90% agent) | 0.3-0.5× | Agent does most work, human directs and validates |

**Important:** These are starting estimates. Calibrate with your team's actual data.

## Calibration Loop

After each sprint or batch of work:

1. Compare estimated vs. actual completion times
2. Calculate the estimation error ratio: `actual / estimated`
3. Adjust multipliers by the average error ratio
4. Track calibration history to detect trends

```
Calibration factor = average(actual / estimated) for last N tasks
Adjusted estimate = raw estimate × calibration factor
```

## Limitations

- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
- Estimates are only as good as the calibration data — new teams should use conservative (P90) estimates until calibrated.
