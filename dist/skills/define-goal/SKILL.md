---
name: Define Goal
description: Help the user define a concrete, measurable goal before starting work, especially when they ask to create a goal, set an objective, clarify success criteria, or turn a fuzzy intention into a quantitative outcome. Use for goal creation and goal refinement only.
source: openai-skills (MIT license, https://github.com/openai/skills)
category: agent-operations
tags: [agent-operations, goal, objective, success-criteria, planning, measurement]
type: Playbook
---

# Define Goal

## Overview

Shape the user's intent into an objective an agent can pursue honestly. Prefer measurable outcomes, explicit evidence, and bounded scope over activity descriptions.

## When to Use

- The user asks to create or set a goal
- The user wants help turning an intention into a clear objective
- The user wants to clarify success criteria
- Requirements are fuzzy and need to be made concrete

**When NOT to use:**
- The user only asks for ordinary implementation work — do the work directly instead of forcing goal creation
- The goal is already clear and measurable

## Workflow

### 1. Confirm Goal Definition Is Needed

Use this skill when the user asks for goal definition explicitly. If the user just wants work done, do the work directly.

### 2. Restate the Goal in Concrete Terms

A usable goal names:

- The specific outcome that will be true
- The main artifact, system, repo, environment, or user-facing behavior involved
- How completion will be verified
- What is in scope
- What is out of scope when ambiguity would matter
- The stop condition for asking the user instead of grinding

### 3. Make It Quantitative

Prefer numbers that represent real success, not decorative precision:

```
BAD:  "Make the app faster"
GOOD: "Reduce p95 API latency from 500ms to 200ms for the checkout endpoint"

BAD:  "Improve the codebase"
GOOD: "Reduce cyclomatic complexity of payment module from 45 to under 20"

BAD:  "Add tests"
GOOD: "Increase code coverage of auth module from 40% to 80%"
```

### 4. Define Verification

How will we know the goal is met?

- **Automated verification:** Tests pass, metrics hit thresholds, build succeeds
- **Manual verification:** User confirms behavior, visual inspection
- **Evidence-based:** Logs show expected behavior, monitoring shows improvement

### 5. Set Boundaries

Explicitly state what's out of scope to prevent scope creep:

```
IN SCOPE:
- Checkout endpoint latency optimization
- Database query optimization for payment flow

OUT OF SCOPE:
- Other endpoints
- Frontend performance
- Infrastructure changes
```

## Goal Template

```markdown
## Goal: [Concrete, measurable objective]

### Success Criteria
- [ ] [Criterion 1 — measurable]
- [ ] [Criterion 2 — measurable]

### In Scope
- [What's included]

### Out of Scope
- [What's explicitly excluded]

### Verification
- [How we'll know it's done]

### Stop Condition
- [When to ask the user instead of continuing]
```

## Red Flags

- Goals that describe activity instead of outcomes ("work on X" vs. "deliver X")
- Goals with no way to verify completion
- Goals that are too broad to achieve in a single session
- Goals that conflict with each other
