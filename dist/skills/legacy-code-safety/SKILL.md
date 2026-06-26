---
name: legacy-code-safety
description: Safe change techniques for legacy/untested code from Michael Feathers' "Working Effectively with Legacy Code" — seams, characterization tests, dependency breaking, and sprout/wrap patterns.
tags: [agent-operations, legacy-code, feathers, characterization-tests, seams, dependency-breaking, safety]
type: Playbook
---

# Legacy Code Safety

## When to Use

Apply when changing code that is expensive to change safely because behavior is unclear, tests are weak or missing, dependencies are hidden, or runtime/framework setup blocks local feedback.

## Core Principle

Gain control before improving design. Understand current behavior, protect what must stay, create the smallest useful seam, break the dependency that blocks feedback, make the requested change, then leave the area more testable.

## The Legacy Loop

1. **Identify the change point** — Where does the behavior need to change?
2. **Check existing protection** — What tests already cover this area?
3. **Add characterization where possible** — Capture current behavior before changing it.
4. **Find or create a seam** — The smallest point that allows substitution, observation, or interception.
5. **Break the blocking dependency** — Expose hidden inputs, hard outputs, globals, statics, framework callbacks.
6. **Change behavior** — Make the requested change with tests protecting it.
7. **Refactor locally** — Leave the area more testable.

## Decision Rules

1. **Treat any area without trustworthy tests as legacy code** — Do not start with rewrite or module-wide cleanup.
2. **State the behavior delta** — Before editing, state the requested change AND the current behavior that must remain.
3. **Characterize uncertain behavior** — Instead of silently fixing suspicious behavior, write characterization tests that capture what it actually does.
4. **Prefer fast, focused tests around the slice being changed** — Use broader integration tests only when they are the safest first observation point.
5. **Choose test points by tracing effects outward** — From the change point through values, calls, fields, outputs, collaborators, interception points, pinch points.
6. **Use the smallest seam that allows substitution/observation** — Make clear whether the seam is for sensing, separation, or both.
7. **Break dependencies deliberately** — Expose hidden inputs, hard outputs, globals, statics, ambient context, framework callbacks only where they block testing or safe change.
8. **Keep behavior changes, structural refactorings, and cleanup separate** — Verify small steps. Avoid checking in exploratory restructuring.
9. **Sprout and wrap for risky edits** — Add behavior with sprout method/class, wrap method/class, extract-and-override. Fold temporary structure into better design when tests support it.
10. **Split construction from use** — Extract side effects behind collaborators, carve pure computation first, isolate policy from runtime/persistence/UI/framework.
11. **Dependency-breaking techniques by barrier** — Adapt narrow parameters, extract interfaces, parameterize constructors/methods, encapsulate globals, introduce instance delegators, override factories/calls, use link/preprocessing seams only when ordinary object seams are impractical.
12. **Leave the touched area easier to understand, test, or change** — Do not mistake test-only seams, wrappers, subclass tricks for design improvement.

## Seam Types

| Seam | Purpose | Cleanup Obligation |
|------|---------|-------------------|
| Object seam | Substitute implementation via interface | Low — standard OOP |
| Preprocessor seam | Conditional compilation | Medium — remove when safer structure exists |
| Link seam | Substitute at link time | Medium — remove when safer structure exists |
| Probe/sensing variable | Observe internal state | High — remove after adding real tests |

## Trigger Rules

- Behavior is uncertain → add characterization before changing semantics
- Tests require too much setup → break the first real barrier (constructor work, hidden allocation, global state)
- Time/randomness/environment blocks repeatable tests → wrap or inject that boundary
- Large method defeats local reasoning → sketch effects, find interception points, extract pure computation first
- Database/UI/framework-bound code → separate policy from query/mapping/persistence
- Seam is magical/temporary/public-for-test → add cleanup obligation, remove once safer structure exists
- Repeated edits cluster → remove duplication incrementally under tests
- Rewrite feels tempting → choose the smallest sprout/wrap/seam/characterization step

## Final Checklist

- [ ] Untested area treated as legacy risk?
- [ ] Behavior delta and behavior-to-preserve stated?
- [ ] Uncertain current behavior characterized?
- [ ] Tests close enough and fast enough to diagnose the change?
- [ ] Smallest useful seam chosen (sensing vs separation clear)?
- [ ] Blocking dependency reduced without expanding hidden ones?
- [ ] Behavior change, refactoring, and cleanup kept separate?
- [ ] Temporary seam has a cleanup path?
- [ ] Touched area is more understandable, testable, or changeable?
