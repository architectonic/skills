---
name: postmortem-writing
description: Comprehensive guide to writing effective, blameless postmortems that drive organizational learning and prevent incident recurrence. Use when conducting post-incident reviews, writing postmortem documents, facilitating blameless postmortem meetings, or identifying root causes and contributing factors.
tags: [postmortem, blameless, incident-review, root-cause, organizational-learning, devops, reliability]
type: Playbook
---

# Postmortem Writing

Comprehensive guide to writing effective, blameless postmortems that drive organizational learning and prevent incident recurrence.

**Source:** Distilled from `antigravity-awesome-skills/skills/postmortem-writing/SKILL.md` (MIT).

## When to Use This Skill

- Conducting post-incident reviews
- Writing postmortem documents
- Facilitating blameless postmortem meetings
- Identifying root causes and contributing factors
- Creating actionable follow-up items
- Building organizational learning culture

## When NOT to Use This Skill

- The task is unrelated to postmortem writing
- You need a different domain or tool outside this scope

## Core Concepts

### 1. Blameless Culture

| Blame-Focused | Blameless |
|---------------|-----------|
| "Who caused this?" | "What conditions allowed this?" |
| "Someone made a mistake" | "The system allowed this mistake" |
| Punish individuals | Improve systems |
| Hide information | Share learnings |
| Fear of speaking up | Psychological safety |

### 2. Postmortem Triggers

- SEV1 or SEV2 incidents
- Customer-facing outages > 15 minutes
- Data loss or security incidents
- Near-misses that could have been severe
- Novel failure modes
- Incidents requiring unusual intervention

## Postmortem Timeline

```
Day 0: Incident occurs
Day 1-2: Draft postmortem document
Day 3-5: Postmortem meeting
Day 5-7: Finalize document, create tickets
Week 2+: Action item completion
Quarterly: Review patterns across incidents
```

## Templates

### Template 1: Standard Postmortem

```markdown
# Postmortem: [Incident Title]

**Date**: YYYY-MM-DD
**Authors**: @alice, @bob
**Status**: Draft | In Review | Final
**Incident Severity**: SEV2
**Incident Duration**: 47 minutes

## Executive Summary

[One-paragraph summary: what happened, impact, root cause, resolution.]

**Impact**:
- [Quantified customer impact]
- [Quantified business impact]
- [Support/engineering cost]

## Timeline (All times UTC)

| Time | Event |
|------|-------|
| HH:MM | [Event] |

## Root Cause Analysis

### What Happened
[Description of the technical failure.]

### Why It Happened
1. **Proximate Cause**: [Immediate technical cause]
2. **Contributing Factors**:
   - [Factor 1]
   - [Factor 2]
3. **5 Whys Analysis**:
   - Why did the service fail? → [Answer]
   - Why were [conditions] present? → [Answer]
   - ...

## Detection
### What Worked
### What Didn't Work
### Detection Gap

## Response
### What Worked
### What Could Be Improved

## Impact
### Customer Impact
### Business Impact
### Technical Impact

## Lessons Learned
### What Went Well
### What Went Wrong
### Where We Got Lucky

## Action Items

| Priority | Action | Owner | Due Date | Ticket |
|----------|--------|-------|----------|--------|
| P0 | [Action] | @owner | YYYY-MM-DD | TICKET-123 |

## Appendix
### Supporting Data
### Related Incidents
### References
```

### Template 2: 5 Whys Analysis

```markdown
# 5 Whys Analysis: [Incident]

## Problem Statement
[One-sentence problem description.]

## Analysis

### Why #1: Why did the service fail?
**Answer**: [Answer]
**Evidence**: [Evidence]

### Why #2: [Follow-up question]
**Answer**: [Answer]
**Evidence**: [Evidence]

[Continue for 5 levels...]

## Root Causes Identified
1. **Primary**: [Root cause]
2. **Secondary**: [Contributing factor]
3. **Tertiary**: [Systemic issue]

## Systemic Improvements

| Root Cause | Improvement | Type |
|------------|-------------|------|
| [Cause] | [Improvement] | Prevention/Detection/Mitigation |
```

### Template 3: Quick Postmortem (Minor Incidents)

```markdown
# Quick Postmortem: [Brief Title]

**Date**: YYYY-MM-DD | **Duration**: 12 min | **Severity**: SEV3

## What Happened
[One-paragraph description.]

## Timeline
- HH:MM - [Event]

## Root Cause
[One-sentence root cause.]

## Fix
- Immediate: [What was done]
- Long-term: [Follow-up ticket]

## Lessons
[Key takeaway.]
```

## Facilitation Guide

### Running a Postmortem Meeting (60 minutes)

1. **Opening (5 min)** — Remind everyone of blameless culture. "We're here to learn, not to blame."
2. **Timeline Review (15 min)** — Walk through events chronologically. Identify gaps.
3. **Analysis Discussion (20 min)** — What failed? Why? What conditions allowed this?
4. **Action Items (15 min)** — Brainstorm improvements. Prioritize by impact. Assign owners.
5. **Closing (5 min)** — Summarize key learnings. Confirm action item owners.

### Facilitation Tips
- Keep discussion on track
- Redirect blame to systems
- Encourage quiet participants
- Document dissenting views
- Time-box tangents

## Anti-Patterns to Avoid

| Anti-Pattern | Problem | Better Approach |
|--------------|---------|-----------------|
| **Blame game** | Shuts down learning | Focus on systems |
| **Shallow analysis** | Doesn't prevent recurrence | Ask "why" 5 times |
| **No action items** | Waste of time | Always have concrete next steps |
| **Unrealistic actions** | Never completed | Scope to achievable tasks |
| **No follow-up** | Actions forgotten | Track in ticketing system |

## Best Practices

### Do's
- **Start immediately** — Memory fades fast
- **Be specific** — Exact times, exact errors
- **Include graphs** — Visual evidence
- **Assign owners** — No orphan action items
- **Share widely** — Organizational learning

### Don'ts
- **Don't name and shame** — Ever
- **Don't skip small incidents** — They reveal patterns
- **Don't make it a blame doc** — That kills learning
- **Don't create busywork** — Actions should be meaningful
- **Don't skip follow-up** — Verify actions completed

## Resources

- [Google SRE - Postmortem Culture](https://sre.google/sre-book/postmortem-culture/)
- [Etsy's Blameless Postmortems](https://codeascraft.com/2012/05/22/blameless-postmortems/)
- [PagerDuty Postmortem Guide](https://postmortems.pagerduty.com/)

## Limitations

- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
