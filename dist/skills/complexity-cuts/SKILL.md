---
name: complexity-cuts
title: complexity-cuts — Lower Big-O on Existing Code
description: Lower time/space complexity on existing code via a one-transformation-at-a-time
  playbook with verify-revert-stop.
type: Playbook
domain: software-engineering
tags:
- software-engineering
- okf
risk_level: medium
requires_review: true
source_family: agent-skills-standard
source_status: adapted
---

# complexity-cuts — Lower Big-O on Existing Code

Lower time/space complexity on existing code via a one-transformation-at-a-time playbook with verify-revert-stop.

**Source:** Distilled from `antigravity-awesome-skills/skills/complexity-cuts/SKILL.md` by morsechimwai (Apache-2.0).

## When to Use This Skill

Use **complexity-cuts** when refactoring existing code that has poor Big-O:

- Nested loops, `O(n²)` or worse scans, repeated work, redundant allocations, blown memory.
- Stated symptoms: "this is slow on large inputs", "times out", "OOM", "too much memory", "reduce complexity", "optimize this algorithm".
- N+1 query patterns in ORMs (Prisma, Drizzle, SQLAlchemy, Django, ActiveRecord).
- `await` inside `for` over independent items causing serial latency.

For *preventing* bad complexity before code is written, use a prevention-focused skill. For math-level optimizations (Bloom, HLL, FFT, JL projection), escalate to a math-focused skill.

## The Iron Law

```
NO TRANSFORMATION WITHOUT EXISTING TESTS GREEN BEFORE AND AFTER
```

If the code has no tests, write a characterization test first (golden input → current output). Then transform. Then verify the test still passes.

## Non-negotiable Rules

1. **State current and target Big-O before touching code.** In one line:
   - Current: `time = O(?)`, `space = O(?)`
   - Target: `time = O(?)`, `space = O(?)`
   - Dominant input dimension (n = what, how large in practice)

2. **Identify the bottleneck, do not guess.** Point to the exact line(s) responsible for the dominant term.

3. **One transformation at a time, with a verify-revert-stop loop:**
   1. Apply exactly one transformation from the playbook.
   2. Run the existing test suite.
   3. If any test breaks: **revert immediately.** Do not patch the test.
   4. Count reverts. If **3 reverts in a row**, STOP. Escalate to invariant analysis.
   5. Only after green: pick the next transformation.

4. **Preserve semantics exactly.** Lower complexity must not change outputs, ordering guarantees, stability, or error behavior.

5. **No invented numbers.** Never write "10x faster" without measuring. Write `<measured: TBD>` or actually measure.

6. **Always report the measured speedup ratio after a transformation lands:**
   ```
   p50:  186 ms → 1.1 ms   (169× faster, n=20,000, 200 samples)
   ```

## The Transformation Playbook

### Time-Complexity Reductions

| Smell | Fix | Typical Win |
|-------|-----|-------------|
| `for x in A: if x in B` where B is list | Convert B to `Set`/`Map` once | O(n·m) → O(n+m) |
| Nested loop computing pairs/joins | Hash-join on the key | O(n·m) → O(n+m) |
| Repeated `.find`/`.indexOf` inside loop | Precompute index `Map<key, item>` | O(n²) → O(n) |
| Repeated recomputation of same value | Memoize / cache by input key | O(n·f(n)) → O(n + f(n)) |
| Sort inside a loop | Sort once outside | O(n² log n) → O(n log n) |
| Recursive recomputation (naive Fibonacci) | Memoize or convert to iterative DP | exponential → O(n) |
| `await` inside `for` over independent items | `Promise.all` / batched concurrency | wall-clock O(n·latency) → O(latency) |
| ORM query inside a loop (N+1) | `IN (...)` / `select_related` / bulk fetch | O(n) round-trips → O(1) |

### Space-Complexity Reductions

| Smell | Fix | Typical Win |
|-------|-----|-------------|
| Materializing whole list just to iterate | Generator / iterator / stream | O(n) → O(1) |
| Building intermediate arrays via chained `.map().filter()` | Single-pass loop or lazy pipeline | k·O(n) → O(n) |
| Caching every intermediate result of recursion | Rolling window (keep last k states) | O(n) → O(k) |
| Reading entire file before processing | Stream line-by-line / chunked | O(file) → O(chunk) |
| Loading full result set from DB | Cursor / pagination / streaming query | O(rows) → O(page) |

### When You Cannot Lower Asymptotic Big-O

Sometimes O(n log n) really is the floor. Then move to constant-factor wins:
- Replace pointer-chasing structures with contiguous arrays (cache locality)
- Hoist invariants out of loops
- Avoid allocation in the hot loop (reuse buffers)
- Batch syscalls / I/O

State explicitly: "Asymptotic floor is O(n log n); applying constant-factor optimizations only."

## Required Workflow

For each piece of code you optimize:

1. **Measure or estimate current Big-O.** Write it down.
2. **Identify the bottleneck line(s).** Point at them.
3. **Pick one transformation from the playbook.** Name it.
4. **Apply it.** One change.
5. **Verify behavior.** Tests pass, or outputs match on a representative input.
6. **State new Big-O.** Time and space.
7. **Repeat if more wins exist and are worth the complexity cost.**

## Output Discipline

When proposing or applying an optimization, your message must contain — in this order:

1. **Bottleneck** — file:line and one-sentence reason.
2. **Current complexity** — `time = O(?)`, `space = O(?)`.
3. **Transformation** — name from the playbook.
4. **New complexity** — `time = O(?)`, `space = O(?)`.
5. **Semantic risk** — anything callers might notice. "None" is valid if true.
6. **Measured speedup** — `before → after · N× faster` (or `asymptotic only`).
7. **The diff.**

## Stop Conditions

Do not optimize further when:
- Asymptotic Big-O already matches a known lower bound for the problem.
- The input is provably small and bounded (n < ~100 and not on a hot path).
- The optimization would obscure correctness without a measured win.
- The bottleneck is I/O or external service latency, not CPU/memory.

## Verification Checklist

Before claiming an optimization is complete:

- [ ] Existing tests were green BEFORE the transformation
- [ ] Exactly one transformation was applied
- [ ] Tests are green AFTER the transformation
- [ ] No test was modified, weakened, or skipped
- [ ] Current and target Big-O are stated
- [ ] Semantic risk is written down
- [ ] Measured speedup ratio is reported
- [ ] Revert count on this code is < 3

## Red Flags — STOP

- Optimizing without stating current Big-O
- "This should be faster" without identifying a specific bottleneck line
- Stacking multiple transformations before verifying any one of them
- Claiming a speedup without measuring or without an asymptotic argument
- Lowering complexity by silently changing output semantics
- Rewriting code that runs once at startup with n = 12

## Limitations

- **Requires existing tests or a written characterization test.** Without one, you cannot detect silent semantic regressions.
- **Asymptotic wins only; constant-factor work is a separate mode** (clearly labeled).
- **Single-process scope.** Distributed-system bottlenecks are out of scope.
- **3-revert rule is firm.** If three transformations failed, escalate — do not try a fourth.
- **Measurement is on the author.** You must produce a representative input.
- **Won't help I/O-bound code.** If the dominant term is network latency or disk, fix the I/O pattern instead.

## The Thesis

> Existing code earned its slowness one shortcut at a time. complexity-cuts removes them one transformation at a time — and refuses to ship the optimization without a green test.
