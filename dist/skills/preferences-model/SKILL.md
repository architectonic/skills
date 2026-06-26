---
name: Preferences Model
description: Template for recording project or team working preferences without turning personality into doctrine. Use when setting up working preferences, defining team conventions, or documenting communication style.
tags: [agent-operations, agent-operations, preferences, template, collaboration]
type: Reference
---

# Preferences Model

Use this model to record project or team working preferences without turning personality into doctrine.

Preferences are defaults. They do not override correctness, safety, source evidence, or explicit current instructions.

## Preferences Template

```md
# Working Preferences

## Communication

- Preferred response length:
- Preferred level of detail:
- Preferred review style:

## Engineering

- Code style:
- Testing expectations:
- Dependency policy:
- Refactor policy:

## Collaboration

- When to ask:
- When to proceed:
- How to report completion:

## Boundaries

Preferences do not override:
- security;
- privacy;
- source artifacts;
- user instruction;
- project ontology.
```

## Rules

- Keep preferences generic and task-relevant.
- Do not include private identity details in public repos.
- Do not infer preferences from one frustrated exchange.
- Treat preferences as revisable defaults.

## Trigger

Use this skill when:
- Setting up a new project with team preferences
- Documenting communication or engineering conventions
- Deciding whether a preference should be recorded or is temporary

## Procedure

1. Identify the preference area (communication, engineering, collaboration).
2. State the preference as a default, not a rule.
3. Explicitly note what the preference does NOT override.
4. Review periodically — preferences should evolve with the project.

## Verification

- Preferences are stated as defaults, not absolutes.
- No private identity details are included.
- The "Boundaries" section is present and complete.

## Failure Modes

- Treating preferences as rules (overriding source evidence)
- Inferring preferences from a single exchange (overfitting)
- Including private details in public repos (privacy leak)
- Never updating preferences (stale defaults)
