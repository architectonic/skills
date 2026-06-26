---
name: vertical-slice-issues
description: Break a plan, spec, or PRD into independently-grabbable issues using tracer-bullet vertical slices. Use when you have a plan that needs to be split into issues for an issue tracker, especially when work will be done across multiple sessions or by different agents. Each slice cuts through ALL integration layers end-to-end (schema, API, UI, tests), not a horizontal slice of one layer.
tags: [agent-operations, software-development, planning, issue-tracking, vertical-slices]
source: mattpocock/skills — skills/engineering/to-issues/SKILL.md (MIT license)
type: Playbook
---

# Vertical Slice Issues

Break a plan into independently-grabbable issues using vertical slices (tracer bullets).

## When to Use

- You have a PRD, spec, or plan that needs to become tracked issues
- Work will be split across multiple sessions or agents
- You need each issue to be independently demoable/verifiable
- You want to parallelize work without coupling

## Prerequisites

The issue tracker and triage label vocabulary should already be configured for the project.

## Process

### 1. Gather context

Work from whatever is already in the conversation context. If the user passes an issue reference (issue number, URL, or path) as an argument, fetch it from the issue tracker and read its full body and comments.

### 2. Explore the codebase (optional)

If you have not already explored the codebase, do so to understand the current state. Issue titles and descriptions should use the project's domain glossary vocabulary and respect ADRs in the area you're touching.

Look for opportunities to prefactor the code to make the implementation easier. "Make the change easy, then make the easy change."

### 3. Draft vertical slices

Break the plan into **tracer bullet** issues. Each issue is a thin vertical slice that cuts through ALL integration layers end-to-end, NOT a horizontal slice of one layer.

**Vertical slice rules:**
- Each slice delivers a narrow but COMPLETE path through every layer (schema, API, UI, tests)
- A completed slice is demoable or verifiable on its own
- Any prefactoring should be done first

### 4. Quiz the user

Present the proposed breakdown as a numbered list. For each slice, show:

- **Title**: short descriptive name
- **Blocked by**: which other slices (if any) must complete first
- **User stories covered**: which user stories this addresses (if the source material has them)

Ask the user:
- Does the granularity feel right? (too coarse / too fine)
- Are the dependency relationships correct?
- Should any slices be merged or split further?

Iterate until the user approves the breakdown.

### 5. Publish the issues to the issue tracker

For each approved slice, publish a new issue. These issues are considered ready for AFK agents.

Publish issues in dependency order (blockers first) so you can reference real issue identifiers in the "Blocked by" field.

**Issue body template:**

```
## Parent

A reference to the parent issue on the issue tracker (if the source was an existing issue, otherwise omit this section).

## What to build

A concise description of this vertical slice. Describe the end-to-end behavior, not layer-by-layer implementation.

Avoid specific file paths or code snippets — they go stale fast. Exception: if a prototype produced a snippet that encodes a decision more precisely than prose can (state machine, reducer, schema, type shape), inline it here and note briefly that it came from a prototype. Trim to the decision-rich parts — not a working demo, just the important bits.

## Acceptance criteria

- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Blocked by

- A reference to the blocking ticket (if any)

Or "None - can start immediately" if no blockers.
```

Do NOT close or modify any parent issue.

## Key Principles

- **Vertical over horizontal**: A slice goes through all layers (DB → API → UI → test), not one layer across all features
- **Independently demoable**: Each slice delivers visible, testable value on its own
- **Dependency-aware**: Publish in order so blockers are real issue references
- **Agent-ready**: Issues should be clear enough for an agent to pick up without the original context
