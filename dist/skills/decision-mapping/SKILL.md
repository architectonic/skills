---
name: decision-mapping
description: Turn a loose idea into a sequenced map of investigation tickets, then drive them to resolution one at a time. Use when a multi-session planning effort has open questions that need research, prototyping, or discussion before implementation can begin.
type: Playbook
---

# Decision Mapping

Turn a loose idea into a **stateful decision map** — a compact, git-tracked markdown file that drives a sequence of investigation tickets to resolution.

## When to Use

- A loose idea requires more than one agent session to turn into a plan
- There are open questions that need research, prototyping, or discussion
- The path forward has "fog of war" — unknowns that must be resolved before implementation

## When NOT to Use

- The idea is clear enough to implement directly → use `/to-prd` or implement
- The grilling session resolves everything inline → skip the map

## The Decision Map

A single compact Markdown file, one per planning effort, git-tracked alongside the project. **The whole map is loaded as context into every session**, so it must stay compact.

Assets created during tickets should be linked from the map, not duplicated within it.

### Structure

Numbered entries ("tickets"), each its own section:

```markdown
## #1: Relational Or Non-Relational Database?

Blocked by: #<ticket-number>, #<ticket-number>
Type: Research | Prototype | Discuss

### Question

<question-here>

### Answer

<answer-here>
```

Each ticket must be sized to one ~100K token agent session.

## Ticket Types

- **Research**: Reading docs, APIs, knowledge bases. Creates a markdown summary. Use when knowledge outside the current working directory is required.
- **Prototype**: Writing code to test a hypothesis or explore a design space. Creates a prototype asset. Use when "how should it look/behave" is the key question.
- **Discuss**: Conversation with the agent. Uses grilling and domain-modeling. The default case.

## Fog of War

The map is deliberately incomplete beyond the frontier. Your job is to investigate the frontier and resolve tickets to push it forward — one node at a time.

When the fog has been pushed back far enough that the path to the finish line is clear, the map is done.

## Invocation

### Bootstrap

User invokes with a loose idea.

1. Run grilling and domain-modeling to surface open decisions
2. Write a new decision map — mostly fog, frontier identified, trivially-decidable entries resolved inline
3. **Stop.** Map-building is one session's work; do not also resolve tickets.

### Resume

User invokes with a path to an existing map and a ticket number.

1. Load the **whole map** as context
2. Run a session to resolve the ticket, invoking skills as needed
3. Record what was resolved in the ticket's body
4. Add newly-discovered tickets (with correct `blocked_by` edges)
5. **Stop.**

If decisions made invalidate other parts of the map, update or delete those nodes.

## Parallelism

The user may choose to run tickets in parallel, so expect other agents to make changes to the map.

## Skipping the Decision Map

If the initial grilling results in no fog of war — no unresolved tickets — offer the user the chance to skip the decision map. Recommend either implementing directly or using a PRD synthesis skill.
