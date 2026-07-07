---
name: engineering-loop-contracts
description: Design safe recurring agent loops with explicit triggers, context, actions, verification, state, stopping conditions, and human checkpoints — the loop contract that replaces turn-by-turn prompting. Use when creating a scheduled or autonomous agent loop, reviewing an existing loop for runaway or staleness risk, or converting repeated manual work into automation.
tags: [loops, loop-engineering, agent-operations, scheduling, verification, okf]
type: Playbook
domain: agent-operations
risk_level: low
requires_review: false
---

# Engineering Loop Contracts

Loop engineering designs the system that prompts the agent, instead of a human typing each prompt. The prompt becomes one component inside a contract with seven parts. A loop missing any part is not ready to run unattended.

## The loop contract

```text
1. TRIGGER      when may the loop run? (schedule, queue item, event, heartbeat)
2. CONTEXT     what durable state does it read first? (ledger, queues, logs)
3. ACTION      what one bounded unit of work does it perform this run?
4. VERIFICATION how is the result checked before it counts? (deterministic > agentic grader)
5. STATE       what does it persist so the next run knows what happened?
6. STOP        testable termination + failure exits (never "until done")
7. CHECKPOINT  which outcomes require a human before taking effect?
```

## Layered safety (operator loop stack)

Evaluate any loop bottom-up; each layer assumes the ones below:

```text
harness      → sandbox, permissions, tool budget (see engineering-agent-harnesses)
loop contract → the seven parts above
state layer  → ledger + queues as durable memory between runs
checker      → validator that gates status flips (evidence, not claims)
human gate   → approval artifact for irreversible/outward actions
```

## Proven operating pattern (single coordinator)

Many independent recurring jobs drift: duplicated plans, conflicting priorities, stale state, no single account of what happened. Prefer:

```text
single coordinator, many roles, shared daily ledger, queue-aware execution
```

The coordinator reads durable state, selects **exactly one role** for the run, acts within that role's boundary, records an evidence-bearing ledger entry, updates queues, and stops cleanly. Time decides *when* it may run; queues decide *whether* meaningful work exists — an empty queue is a valid no-op run, not a failure.

## Ledger entry minimum

Every run persists, at minimum:

```text
run id + timestamp        selected role + override reason if scheduled role skipped
inspected ref/commit      what was consumed (queue item) and produced (files, commit)
verification outcome      boundary check (what was deliberately NOT done)
next action               blockers, honestly recorded
```

Honest failure records beat fabricated progress: a run that records "source unavailable, no data written" is a *successful* run.

## Stopping conditions and failure exits

- Termination must be testable: "queue empty", "phase exit conditions met", "N items processed" — never "when finished".
- Cap retries; after the cap, write a blocker to the ledger and stop rather than looping.
- Bound each run's work (one role, one queue item) so a bad run has bounded blast radius.
- Watch for the three chronic loop diseases: **stale state** (loop trusts its own outdated notes — re-inspect source each run), **weak checks** (grader passes everything — make validators verbose and specific), **unsafe authority** (loop can spend/send/delete without a checkpoint — move those behind human gates).

## Verification design

Prefer deterministic graders (scripts, schema checks, test suites) over LLM judges; use an agentic grader only where judgment is inherent, and give it a written rubric. The checker gates the ledger: status flips only with evidence attached.

## Related skills

- `agent-operating-loop` — the within-run cycle (Read → … → Handoff); this skill governs *between* runs.
- `gating-work-with-verification-loops` — validator patterns used by the checker layer.
- `engineering-agent-harnesses` — the layer beneath the loop contract.
