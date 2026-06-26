---
name: invariant-guard
description: Correctness-first coding: force writing function contracts, loop invariants, termination arguments, and edge cases BEFORE code. Use when writing or reviewing algorithms where the obvious implementation is subtly wrong (binary search, Boyer-Moore, QuickSelect, in-place mutation, recursion).
tags: [software-development, correctness, algorithms, loop-invariants, contracts, verification, software-development]
type: Playbook
---

# Invariant-Guard — Correctness-First Coding

The model knows what a loop invariant is. It knows recursion needs a base case. It knows about empty lists, integer overflow, and the difference between `<` and `≤`. It just does not write these down before producing code — so it ships subtle correctness bugs that tests do not catch.

**Thesis: Tests verify examples. Invariants verify behavior. AI assistants ship example-correct, behavior-wrong code by default. invariant-guard makes them reason about behavior first.**

## When to Use

Use when writing or reviewing algorithms where the obvious implementation is subtly wrong:

- Postcondition stronger than the loop's natural invariant (Boyer-Moore, Floyd's cycle, leftmost binary search, QuickSelect)
- In-place mutation with read+write pointers (dedup, partition, rotate)
- Recursion with multiple parameters or accumulator state
- Off-by-one suspects with duplicates, empty inputs, boundary values
- Iterative refinements that must terminate (fixed-point, Newton, EM)
- Any function where you catch yourself thinking "I know this algorithm" — the trap is usually in the contract

## The Iron Law

**NO LOOP OR RECURSION WITHOUT A WRITTEN INVARIANT AND TERMINATION ARGUMENT**

If you cannot write the invariant in one sentence, you have not designed the loop.

## Non-Negotiable Rules

1. **Every loop gets a one-line invariant.** Before writing any loop, state what is true at the top of every iteration.
   - "At loop top: `result` contains the sum of `a[0..i)`."
   - "At loop top: `lo ≤ target_position ≤ hi`."

2. **Every loop gets a one-line termination argument.** Name the quantity that strictly decreases each iteration.
   - "`hi − lo` strictly decreases each iteration."
   - "`i` increases by 1 and is bounded above by `n`."

3. **Every recursion gets an explicit base case and measure.** State the smallest inputs that return without recursing, and a non-negative integer that strictly decreases on every call.

4. **List edge cases before writing, not after.** For every function operating on a collection or number, list which apply: empty, singleton, all-equal, sorted, reversed, duplicates, negative, zero, boundary values, overflow, NaN/Inf.

5. **Make illegal states unreachable, not just unhandled.** Prefer sum types, newtypes, non-empty types, parse-don't-validate.

## The Pre-Write Protocol

Before producing non-trivial code with loops, recursion, or non-trivial state, emit in this order:

1. **Function contract** — preconditions, postconditions, return value (one line each)
2. **Loop invariants** — one per loop
3. **Termination arguments** — one per loop or recursion
4. **Base cases and measure** — for recursion
5. **Edge case table** — bullets with expected behavior
6. **Illegal states made unrepresentable** — types or asserts
7. **The code**
8. **Self-check** — one line per loop confirming invariant holds

If any of 1–6 is missing, do not emit code.

## Canonical Trap: Boyer-Moore Majority Vote

The voting loop is correct. The postcondition is wrong.

```typescript
// BUG: returns candidate even when no majority exists
function findMajority(arr: number[]): number | null {
  let candidate = arr[0], count = 0;
  for (const x of arr) {
    if (count === 0) candidate = x;
    if (x === candidate) count++; else count--;
  }
  return candidate; // FAILS on [1,2,3] → returns 3, expected null
}
```

**Why the protocol catches it:** Writing the function contract forces the postcondition: "Returns `x` iff `count(x, arr) > arr.length / 2`; else `null`." Writing the loop invariant forces: "If a strict majority exists in `arr`, it equals `candidate`." These are not equivalent — the loop invariant is strictly weaker. The gap reveals the need for a verification pass.

## Canonical Trap: Leftmost Binary Search

Most "I know binary search" implementations return *any* match. The trap is the postcondition.

```typescript
// Returns ANY occurrence, not leftmost
if (a[mid] === target) return mid;  // early return abandons search
```

The fix: maintain the invariant that every index `< lo` has `a[i] < target`, and narrow until `lo === hi`.

## Common Invariant Patterns

| Loop Shape | Canonical Invariant | Termination |
|---|---|---|
| Linear scan | `acc = f(a[0..i))` | `i` increases by 1 |
| Two-pointer | `target (if any) ∈ a[lo..hi]` | `hi − lo` decreases |
| Binary search | `target (if present) ∈ a[lo..hi]` | `hi − lo` halves |
| Sliding window | window `[l..r)` satisfies constraint | `r` advances |
| BFS | nodes at distance < d popped | node count decreases |
| DFS/recursion | result = combine(children results) | depth decreases |
| In-place partition | `a[0..i)` < pivot; `a[i..j)` ≥ pivot | `n − j` decreases |

## Edge Case Checklist

| Input Shape | Cases to Check |
|---|---|
| Array/list | empty, singleton, all-equal, sorted, reversed, duplicates |
| String | empty, single char, whitespace, unicode |
| Integer | 0, 1, −1, MIN, MAX, overflow, division by 0 |
| Float | 0.0, −0.0, NaN, ±Inf, denormal |
| Map/dict | empty, missing key |
| Tree/graph | empty, single node, cycle, disconnected |
| Stream | empty, infinite, exception mid-iteration |

## Verification Checklist

Before claiming correctness:

- [ ] Every loop has a one-line `// inv:` comment
- [ ] Every loop has a termination argument
- [ ] Every recursion names base case and measure
- [ ] Postcondition is written and implied by exit state
- [ ] Every applicable edge case has a test or delegation note
- [ ] At least one test exercises each non-trivial boundary
- [ ] Illegal states are unrepresentable or asserted at entry

## Red Flags — STOP and Write the Invariant First

- About to write `while (...)` without having stated what is true on entry
- About to write `if (i === n − 1)` or `if (i === n)` — boundary suspicious
- About to recurse without naming the base case
- About to write `// TODO: handle empty`
- About to use `==` on floats
- Tests pass but you did not state what the function guarantees
- "It works on the examples I tried"

## Rationalizations to Watch For

| Excuse | Reality |
|---|---|
| "I know this algorithm" | Knowing the loop ≠ knowing the contract |
| "I traced it in my head" | Mental tracing skips edge cases |
| "Edge cases are obvious" | Then write them down in 30 seconds |
| "Tests will catch it" | Tests catch the examples you thought of |
| "The postcondition is implied" | If it were, the invariant would equal it |

## Integration

Pairs with:
- `software-development/test-driven-development` — invariants complement tests
- `software-development/code-review-excellence` — review for missing invariants
- `software-development/debugging-discipline` — invariants help isolate bugs

---

## Limitations

- Not an automated prover — requires the author to write invariants
- Concurrency is out of scope by default (single-threaded assumption)
- Float/overflow edge cases are language-specific
- Will slow down trivial code — reserve for non-trivial loops and recursion
