---
name: construction-discipline
description: Code construction discipline from Steve McConnell's "Code Complete" — clarity, defect reduction, variable naming, control flow, error handling, and evidence-based quality as agent operating discipline.
tags: [agent-operations, code-complete, mcconnell, construction, clarity, defect-reduction, quality]
type: Playbook
---

# Construction Discipline

## When to Use

Apply when implementing, changing, reviewing, debugging, refactoring, or tuning production code where construction discipline must reduce defects and keep code easy to inspect.

## Core Principle

Construction quality is not accidental. Do not treat typing code, making it work once, or using a clever idiom as complete construction. Choose the option that lowers defect risk and makes the code easier to reason about.

## Decision Rules

1. **Verify upstream clarity before large construction** — Requirements, architecture, major risks, coding conventions, language constraints, error policy, data representation, reuse, integration, testing approach must be clear enough.
2. **Build a small validated slice when upstream uncertainty remains** — Instead of speculative code. Make expensive-to-reverse decisions deliberately.
3. **Optimize first for human readers** — Clarity, locality, explicitness, visible control flow, consistent conventions, practical correctness over cleverness or minimal keystrokes.
4. **Sketch pseudocode for complex routines** — At a consistent abstraction level, then convert to code. Keep only comments that explain intent, constraints, contracts, rationale.
5. **Keep routines cohesive, precisely named, small at interface, hard to misuse** — Separate setup, validation, computation, and side effects when conceptually different.
6. **Make variable and data meaning explicit** — Purpose-revealing names, small scope, deliberate initialization, named constants, stronger types, visible units.
7. **Choose data types that make invalid values harder to represent** — Booleans only for true binary meanings, enumerations for closed sets, records/maps only when shape communicates meaning.
8. **Keep control flow simple enough to verify** — Shallow nesting, named predicates for complex conditions, clear normal path, clear loop init/termination/update, no side-effect-dependent expressions.
9. **Table-driven logic only when clearer** — Stable explicit mappings, obvious, synchronized with rules, validated. Do not hide complex behavior in inscrutable encodings.
10. **Validate input at trust boundaries** — Assertions/invariant checks for programmer assumptions, validation/domain errors for expected external/business failures.
11. **Handle errors at the right abstraction** — Preserve diagnostic context, standardize similar failures, keep normal path readable, never silently continue from corrupted state.
12. **Keep classes/modules focused, cohesive, bounded by clear contracts** — Hide representation and internal bookkeeping, avoid mixed persistence/formatting/business/integration concerns.
13. **Rising complexity is defect risk** — Split tangled routines/modules, remove duplication that multiplies maintenance effort, reduce what a maintainer must keep in working memory.
14. **Build in small, verifiable increments** — Integrate often enough to expose conflicts, keep partial work from rotting.
15. **Match reviews/inspections/tests to defect risk** — Debug by reproducing, isolating, explaining, fixing, verifying root causes.
16. **Tune performance only when evidence justifies it** — Measure before and after, keep clarity unless explicit measured tradeoff warrants the cost.
17. **Use tools to reduce error-prone manual work** — Not to replace understanding.
18. **Prefer self-documenting structure first** — Comments should explain intent, assumptions, constraints, limitations, usage, or non-obvious facts.

## Trigger Rules

- Coding starts from a proposed solution → restate requirement, architecture fit, risks, conventions, success constraints
- Routine hard to name, mixes phases, has flag arguments, long parameters → redesign interface or split
- Readers must decode units/ranges/precision/encoding/ownership/magic values → move meaning into names/constants/types
- Input crosses a trust boundary → decide what is validated/rejected/recovered from/asserted/kept diagnosable
- Branches/loops/recursion/exits/exception paths hard to verify → simplify before adding logic
- Repeated branching maps stable categories → consider a validated table
- Class/module exposes representation, grows into god object, mixes responsibilities → restore abstraction boundary
- Tests cover only the happy path → add normal, boundary, invalid-input, defensive-check, edge cases
- Debugging begins from a guess → first make the failure repeatable, collect evidence, isolate the path
- Refactoring poorly understood code → add tests first, keep behavior changes separate
- Performance work begins → set a target, measure current behavior, change one thing, remeasure
- Comments restate obvious mechanics or go stale → rewrite the code or delete the comment
- Local style diverges → follow shared formatting, naming, file-structure conventions

## Final Checklist

- [ ] Requirements, architecture fit, risks, conventions clear enough?
- [ ] Names, routines, data, classes, layout, comments reduce reader effort?
- [ ] Inputs, errors, assertions, contracts, trust boundaries deliberate?
- [ ] Control flow, loops, tables, recursion, exception paths simple enough to inspect?
- [ ] Tests, reviews, debugging, refactoring, integration, tuning evidence-based?
- [ ] Change is small enough to verify and would stand up to careful review?
