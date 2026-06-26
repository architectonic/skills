---
name: gui-skill-action-graph
description: Compose GUI agent skills as composable action graphs for computer-use tasks. Use when building GUI automation skills, designing multi-step desktop workflows, or integrating with GUI agent frameworks. Covers action retrieval, DAG-like composition, vision grounding, and execution budgets.
tags: [autonomous-ai-agents, autonomous-ai-agents, gui-agent, action-graph, computer-use, skill-composition]
---

# gui-skill-action-graph

Compose GUI agent skills as composable action graphs for computer-use tasks.

## When to use

- Building a GUI automation skill for desktop or web applications
- Designing multi-step workflows that require screen grounding
- Integrating with GUI agent frameworks (CUA, Playwright, etc.)
- Skills need reusable action components rather than monolithic instructions

## Core Pattern (from Microsoft CUA)

```text
intent
→ retrieve reusable skill/action graph
→ instantiate arguments
→ ground against current UI
→ execute action
→ update memory
→ continue until done or budget expires
```

## Design Principles

### Composability
- Keep action modules small enough to compose
- Each action module: one atomic GUI operation (click, type, scroll, drag)
- Multi-step workflows: explicit execution DAG, not free-form instructions

### Retrieval
- Combine symbolic/keyword and semantic matching when skills are numerous
- Match by application context (which app/window is active)
- Match by UI element type (button, text field, menu)

### Grounding
- Always ground actions against the observed screen, not prior documentation
- Use vision-based element detection for dynamic UIs
- Fall back to accessibility tree or OCR when vision is unreliable

### Memory
- Track outcomes of each action (success, failure, unexpected state)
- Maintain memory of which actions have been attempted
- Maximum-step or wall-time budgets for long-horizon tasks

## Skill Structure for GUI Actions

```yaml
---
type: Playbook
title: <gui-skill-name>
description: <what this GUI skill does>
tags: [gui, <app-name>, <action-type>]
---

# <gui-skill-name>

## Target Application
- App: <name>
- Version constraints: <optional>
- OS: <windows/macos/linux>

## Action Graph
1. <step-1> → on failure: <fallback>
2. <step-2> → on failure: <fallback>
3. ...

## Grounding Strategy
- Primary: <vision/a11y-tree/ocr>
- Fallback: <alternative>

## Budget
- Max steps: <N>
- Wall time: <seconds>
- Stop condition: <what success looks like>
```

## Risk Classification

GUI skills are **high-review** because they:
- Interact with live desktop state
- May trigger unintended actions (clicks, keystrokes)
- Can cause data loss if misapplied

Promote GUI skills only with:
- Explicit stop conditions
- Reversible actions or rollback paths
- Dry-run or report-only mode
- Human confirmation for destructive operations

## Sources

- microsoft/cua_skill — skill-based autonomous GUI agent framework with action graphs
- loop-engineering.md — bounded loop design for GUI agent cycles
