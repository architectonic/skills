---
name: runaway-guard
title: Runaway Guard — $-Cost is the Third Complexity Dimension
description: 'Every loop has time complexity and space complexity. A loop that calls
  a paid API has a third: **dollars per execution**. The model tracks the first two
  automatically. It does not track the third, so it ships code where a single bug
  — a retry without bound, a stream reconnect storm, an agent that re-queues itself,
  a webhook that fires the same job twice — silently spends real money.'
type: Playbook
domain: software-engineering
tags:
- software-engineering
- okf
risk_level: medium
requires_review: true
---

# Runaway Guard — $-Cost is the Third Complexity Dimension

Every loop has time complexity and space complexity. A loop that calls a paid API has a third: **dollars per execution**. The model tracks the first two automatically. It does not track the third, so it ships code where a single bug — a retry without bound, a stream reconnect storm, an agent that re-queues itself, a webhook that fires the same job twice — silently spends real money.

## When to Use This Skill

- Writing or reviewing code that calls a paid AI/inference API in a loop, queue, retry path, agent step, webhook handler, or background job
- Importing or wrapping any paid-inference SDK: `@fal-ai/*`, `fal-client`, `@anthropic-ai/sdk`, `anthropic`, `openai`, `replicate`, `elevenlabs`, `together-ai`, `groq-sdk`, `cohere-ai`, `@mistralai/*`
- Designing an agent loop, fan-out pipeline, retry wrapper, polling job, stream reconnect, or self-rescheduling job that may call a billed endpoint
- Auditing a codebase/PR for unbounded fan-out, unbounded retries, missing idempotency keys, or missing provider-side spend caps
- Diagnosing an unexpected bill, runaway loop incident, or surprise overage

## The Iron Law

```
NO CALL TO A PAID API WITHOUT A WRITTEN $-CAP AT BOTH THE CODE AND PROVIDER LEVEL
```

A cap only in code can be bypassed by a bug in that code. A cap only at the provider can be hit during normal usage and degrade the product. You need both.

## Non-Negotiable Rules

1. **Every call site gets a one-line cost contract.** Before writing any paid-API call, state in one sentence:
   - **Max calls per run:** the strict upper bound on invocations in a single execution
   - **Max $ per run:** `max_calls × unit_cost` — compute it, don't estimate
   - **Max $ per day:** the provider-side hard cap that backstops the code-side bound

2. **Every loop calling a paid API gets an explicit iteration bound**, not just a termination argument. A concrete integer in code, not just "eventually terminates".

3. **Every retry path is bounded by attempts AND total elapsed cost**, not by time alone. Max attempts: 3-5 for transient errors, 1 for 4xx. 4xx errors do not retry. Period.

4. **Every fan-out path declares a concurrency limit.** Never an unbounded `Promise.all(items.map(...))` on a paid API. Use `p-limit`, semaphore, or batched chunks.

5. **Every paid API has a matching provider-side hard cap**, configured out of band. Defense in depth: if the code is wrong, the provider stops the bleeding.

   | Provider | Where to set the hard cap |
   |---|---|
   | **Fal.ai** | Dashboard → Billing → Spend Limit |
   | **Anthropic** | Console → Workspaces → Workspace Budget (hard limit) |
   | **OpenAI** | Org → Settings → Usage limits (org-level hard limit). ⚠️ Per-project monthly budgets are soft only. |
   | **Replicate** | Account → Billing → Spend limit |
   | **ElevenLabs** | Workspace → Usage limits per API key |

6. **Idempotency keys on every mutating or charging call.** A webhook that fires twice should bill once.

7. **Amplifier patterns are forbidden by default:**
   - Self-rescheduling jobs (no decrementing measure)
   - Webhook handlers that call the API that called the webhook (cycle)
   - Recursion over LLM output (no depth cap)
   - Polling without a deadline
   - Streaming reconnect storms (no backoff/attempt cap)
   - Cache-miss stampede on a paid call (use singleflight/request coalescing)

## The Pre-Write Protocol

Before producing code that calls a paid API, your message must contain:

1. **Provider + unit cost**
2. **Max calls per run** (literal integer constant)
3. **Max $ per run** (computed)
4. **Max $ per day** (provider hard cap)
5. **Concurrency limit** (code + queue + provider)
6. **Retry policy** (max attempts, error codes, idempotency)
7. **Amplifier audit** (rule 7 — declare "none apply" or address each)
8. **The code** with cost contract in a comment above the call site
9. **Self-check:** "in the worst case, this code bills $X and the provider cap stops it at $Y"

If any of 1-7 is missing, do not emit code.

## Common Runaway Patterns and Wallet Invariants

| Pattern | Wallet invariant to write | Hard cap to set |
|---|---|---|
| Fan-out over a list | `total_cost ≤ list_len × unit_cost ≤ MAX_$_PER_RUN` | provider daily spend limit |
| Retry on transient error | `total_cost ≤ attempts × unit_cost`, attempts ≤ 5 | provider daily spend limit |
| Agent loop | `total_cost ≤ MAX_STEPS × per_step_cost`, depth ≤ MAX_DEPTH | per-agent-run cost ceiling |
| Polling for job completion | `total_cost ≤ ceil(MAX_WAIT_MS / poll_interval) × poll_cost` | absolute deadline + alert |
| Webhook handler → API call | idempotency key required | provider rate limit per key |
| Stream reconnect | `attempts ≤ MAX_RECONNECTS`, exponential backoff with cap | provider connection cap |
| Cache miss stampede | singleflight → `cost ≤ 1 × unit_cost` per key per window | n/a (deduped in code) |

## Red Flags — STOP and Write the Cost Contract First

- About to write `await Promise.all(items.map(x => paidApi(x)))` with no `p-limit`
- About to write `while (!done) await paidApi(...)` with no integer bound
- About to write an agent loop with "the model decides when to stop"
- About to write a retry wrapper around a call already retried by queue/SDK/framework
- About to deploy a paid API key without first setting the provider dashboard cap
- About to handle a webhook that calls the API that produced the webhook

## Verification Checklist

Before shipping any code that calls a paid API:

- [ ] Cost contract comment exists above each call site (unit cost, max calls/run, max $/run, provider cap)
- [ ] The iteration/fan-out bound is a named integer constant
- [ ] Concurrency limit is set in code AND at the queue
- [ ] Retry policy is explicit: max attempts, 4xx → no retry, idempotency key
- [ ] Provider dashboard hard cap is set and documented in the file
- [ ] Per-environment API keys; dev keys have lower caps than prod
- [ ] Amplifier audit performed
- [ ] Tests exist for: empty input, oversized input rejected, 4xx not retried, idempotency dedup
- [ ] Worst case: code bills ≤ MAX_$_PER_RUN, provider cap stops loss at MAX_$_PER_DAY

## Limitations

- **Not a billing system.** Enforces intent at code-write time. Pair with provider hard cap and observability for runtime enforcement.
- **Provider-side caps may take minutes to enforce.** A pathological burst within a single window can still exceed the cap modestly.
- **No automated cost estimation for novel models.** Unit costs are inputs the author must look up.
- **Streaming/per-token pricing:** Adapt the protocol — replace `max calls per run` with `max tokens per run`.
- **Compute-billed providers:** Replace "calls" with "GPU-seconds" in the contract.

## The Thesis, in One Line

> **Time bounds prevent stalls. Space bounds prevent OOMs. Dollar bounds prevent $200 mornings. AI assistants enforce the first two by default and ignore the third. runaway-guard makes them reason about the wallet first.**
