---
name: scenario-war-room
description: Cross-functional what-if modeling for cascading multi-variable scenarios. Unlike single-assumption stress testing, models compound adversity across all business functions simultaneously. Use when facing complex risk scenarios, strategic decisions with major downside, or when the user asks 'what if X AND Y both happen?
type: Playbook
---

# Scenario War Room

Model cascading what-if scenarios across all business functions. Not single-assumption stress tests — compound adversity showing how one problem creates the next.

**NOT** a single-assumption stress test. **NOT** financial modeling only. **NOT** worst-case-only. **NOT** paralysis by analysis — outputs concrete hedges and triggers.

## 6-Step Cascade Model

### Step 1: Define Scenario Variables (max 3)
Each variable: what changes (quantified), probability, timeline.

```
Variable A: Top customer (28% ARR) gives 60-day termination notice
  Probability: 15% | Timeline: Within 90 days

Variable B: Series A fundraise delayed 6 months beyond target close
  Probability: 25% | Timeline: Q3

Variable C: Lead engineer resigns
  Probability: 20% | Timeline: Unknown
```

### Step 2: Domain Impact Mapping

| Domain | Owner | Models |
|--------|-------|--------|
| Cash & runway | CFO | Burn impact, runway change, bridge options |
| Revenue | CRO | ARR gap, churn cascade risk, pipeline |
| Product | CPO | Roadmap impact, PMF risk |
| Engineering | CTO | Velocity impact, key person risk |
| People | CHRO | Attrition cascade, hiring freeze |
| Operations | COO | Capacity, OKR impact, process risk |
| Market | CMO | CAC impact, competitive exposure |

### Step 3: Cascade Effect Mapping (the core)
Show how Variable A triggers consequences that trigger Variable B's effects:

```
TRIGGER: Customer churn ($560K ARR)
  ↓
CFO: Runway drops 14 → 8 months
  ↓
CHRO: Hiring freeze; retention risk increases
  ↓
CTO: 3 open reqs frozen; roadmap slips
  ↓
CPO: Q4 feature launch delayed → customer retention risk
  ↓
CRO: NRR drops; existing accounts see reduced velocity → more churn risk
  ↓
CFO: [Secondary cascade — potential death spiral if not interrupted]
```

Name the cascade explicitly. Show where it can be interrupted.

### Step 4: Severity Matrix

| Scenario | Definition | Recovery |
|----------|------------|----------|
| **Base** | One variable hits; others don't | Manageable with plan |
| **Stress** | Two variables hit simultaneously | Requires significant response |
| **Severe** | All variables hit; full cascade | Existential; requires board intervention |

For each: runway impact, ARR impact, headcount impact, timeline to trigger point.

### Step 5: Trigger Points (Early Warning Signals)
Measurable signals that tell you a scenario is unfolding **before** it's confirmed:

```
Trigger for Customer Churn Risk:
  - Sponsor goes dark for >3 weeks
  - Usage drops >25% MoM
  - No Q1 QBR confirmed by Dec 1

Trigger for Fundraise Delay:
  - <3 term sheets after 60 days of process
  - Lead investor requests >30-day extension on DD
  - Competitor raises at lower valuation
```

### Step 6: Hedging Strategies
Actions to take **now** that reduce impact if the scenario materializes:

| Hedge | Cost | Impact | Owner | Deadline |
|-------|------|--------|-------|----------|
| Establish $500K credit line | $5K/year | Buys 3 months if churn hits | CFO | 60 days |
| 12-month retention bonus for 3 key engineers | $90K | Locks team through fundraise | CHRO | 30 days |
| Diversify to <20% revenue concentration | Sales effort | Reduces single-customer risk | CRO | 2 quarters |

## Rules for Good War Room Sessions

- **Max 3 variables per scenario.** More than 3 is noise.
- **Quantify or estimate.** "$420K ARR at risk over 60 days" not "revenue drops."
- **Don't stop at first-order effects.** The damage is always in the cascade.
- **Model recovery, not just impact.** Every scenario needs a "what we do" path.
- **3–4 scenarios per planning cycle.** More creates analysis paralysis.

## Common Scenarios by Stage

**Seed:** Co-founder leaves + product misses launch. Funding runs out + bridge terms unfavorable.

**Series A:** Miss ARR target + fundraise delayed. Key customer churns + competitor raises.

**Series B:** Market contraction + burn multiple spikes. Lead investor wants pivot + team resists.
