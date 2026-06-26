---
name: refactoring-patterns
description: Behavior-preserving refactoring patterns from Martin Fowler's "Refactoring" — small-step structural improvements, named moves, and when to apply them.
tags: [software-development, refactoring, fowler, behavior-preserving, code-smells, design-improvement]
type: Playbook
---

# Refactoring Patterns

## When to Use

Apply when changing existing code, preparing a feature or bug fix, reviewing cleanup, or reducing structural friction without intending to change observable behavior.

## Core Principle

Refactoring is behavior-preserving design work in small steps. Do not turn cleanup into a rewrite, a hidden feature change, or speculative architecture.

## Decision Rules

1. **Preserve observable behavior** — Isolate behavior changes from structural changes. Never disguise a feature, migration, or redesign as cleanup.
2. **Work in small, reversible, buildable, testable, reviewable steps** — Split a patch when it is too large to reason about locally.
3. **Establish a safety net before risky refactoring** — Use characterization tests for unclear behavior. Never delete a failing test to finish cleanup.
4. **Preparatory and follow-up refactoring** — Identify what makes the requested change awkward, reshape that local structure first, make the behavior change, then clean debt introduced.
5. **Refactor the current blocking smell** — Not every smell in sight. Target: duplication, long functions, long parameter lists, globals, divergent change, shotgun surgery, feature envy, primitive obsession, repeated conditionals, temporary fields, middle men, speculative generality.
6. **Prefer the simplest named move** — Rename, extract, inline, move, split meanings, introduce parameter/value object, encapsulate field/collection, decompose conditionals, use guard clauses, substitute clearer algorithm.
7. **Names and functions reveal intent** — Rename before deeper work when bad names block understanding. Keep functions coherent, one abstraction level, tight variable scope, separated phases.
8. **Put behavior and state with the concept that owns them** — Split classes/modules with multiple reasons to change. Separate business policy from formatting, transport, persistence, I/O, frameworks.
9. **Simplify conditionals honestly** — Guard clauses, extracted predicates, lookup tables, state, strategy, polymorphism, null objects only when they reduce repeated branching or clarify variation.
10. **Abstraction only when current evidence justifies it** — Remove pass-through layers, vague utilities, middle men, unused hierarchy, just-in-case interfaces.
11. **Keep patch intent reviewable** — Group related refactorings, separate structural edits from behavior, avoid giant patches.
12. **Stop when the requested change is easy** — The blocking smell is gone, readability is better, and the next cleanup would be speculative.

## Named Moves Catalog

| Move | When |
|------|------|
| Rename | Name hides intent or overloads meaning |
| Extract Function | Code block needs a name, or is used in multiple places |
| Inline Function | Indirection adds no value |
| Move Function/Field | Behavior belongs to a different concept |
| Split Variable | One variable serves two purposes |
| Replace Temp with Query | Temporary used multiple times |
| Introduce Parameter Object | Group of parameters that travel together |
| Replace Conditional with Polymorphism | Repeated type-based switching |
| Decompose Conditional | Complex conditional expression |
| Consolidate Duplicate Conditional Fragments | Same code in all branches of a conditional |
| Replace Nested Conditional with Guard Clauses | Deep nesting obscures the main path |

## Trigger Rules

- Adding behavior → ask what structural friction blocks the change; refactor before the feature only when it makes it safer or simpler
- Fixing a bug in unclear code → characterize the current failure first, then refactor enough to make the fix visible
- Tests absent or weak → make the smallest structural move, improve testability before broader cleanup
- Same edit appears for a third time → remove duplication through clearer ownership
- Function mixes responsibilities/abstraction levels/phases → rename, extract, split before adding more logic
- One change forces edits across many files → centralize the knowledge or introduce a clearer boundary
- Repeated conditionals or type codes grow → decompose intent first; introduce polymorphism/state/strategy only when variation is real
- UI and domain behavior mix → move rules toward domain objects
- Patch mixes intents → split the change
- Tempted to rewrite → choose the next small behavior-preserving transformation

## Final Checklist

- [ ] Observable behavior preserved?
- [ ] Structural change, behavior change, and test updates separated?
- [ ] Safety net gap recorded?
- [ ] At least one real source of friction removed?
- [ ] Names, responsibilities, control flow, data ownership clearer?
- [ ] Patch still reviewable and runnable?
- [ ] Cleanup stopped before speculative abstraction?
