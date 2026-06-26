---
name: clean-code-discipline
description: Clean code principles from Robert C. Martin's "Clean Code" — readability, naming, function design, error handling, and boundary separation as agent operating discipline.
tags: [software-development, clean-code, readability, naming, refactoring, code-quality, robert-martin]
type: Playbook
---

# Clean Code Discipline

## When to Use

Apply when readability, local reasoning, and maintainable code shape are the main concerns — especially during everyday implementation and review.

## Core Principle

Working code is not automatically clean code. Treat cleanliness as part of delivery.

## Decision Rules

1. **Write for local reasoning** — A reader should understand the path without reconstructing hidden state, wide jumps, or naming trivia.
2. **Use precise names, one term per concept** — Rename code when vocabulary hides intent, overloads meaning, or forces comments to compensate.
3. **Keep functions small, focused, one abstraction level** — Tell the story top-down so intent appears before detail.
4. **Keep parameters few and meaningful** — Avoid boolean flags, output parameters, grab-bag argument lists; model the concept instead.
5. **Separate commands from queries** — A function that answers should not also mutate behind the reader's back.
6. **Keep the happy path readable** — Isolate error handling, invalid-state handling, cleanup; prefer explicit optionality or typed results over null-like sentinel flow.
7. **Expose behavior, not raw representation** — Avoid train-wreck access, utility dumping grounds, classes/modules with mixed responsibilities.
8. **Make public APIs small, explicit, hard to misuse** — Encode boundary logic, required order, likely changes where readers can see them.
9. **Comments for rationale only** — Use for constraints, warnings, external contracts. Do not narrate code instead of improving it.
10. **Tests are production code** — Readable, deterministic, aligned with behavior or contract they protect.
11. **Let design emerge** — Through tests, duplication removal, expressiveness, minimal structure. Do not add needless abstractions.
12. **When touching code, remove the smell** — That most increases change cost, but do not silently broaden the task.

## Trigger Rules

- Function mixes setup/validation/computation/side effects → split phases
- Comment explains control flow → simplify names or structure first
- Function both mutates and answers → separate responsibilities
- Duplication, repeated switches, primitive clusters → name the concept
- Boundary leaks framework/vendor/persistence inward → add/strengthen adapter
- Async/concurrency enters → isolate threading policy, minimize shared mutable state
- Fixing a bug → add/update the test that protects the intended contract
- Cleanup spreading into unrelated areas → cut back to smallest safe refactor

## Final Checklist

- [ ] Can a reader follow the change locally?
- [ ] Are names and APIs carrying meaning without narration?
- [ ] Is mutation explicit and the happy path still clear?
- [ ] Did framework/persistence/vendor details stay behind boundaries?
- [ ] Did I remove at least one smell from the touched area?
- [ ] Do tests protect the changed behavior or contract?
- [ ] Did I actually run the relevant tests or checks?
