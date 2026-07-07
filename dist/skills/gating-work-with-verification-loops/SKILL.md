---
name: gating-work-with-verification-loops
description: Gate agent work with validator loops and plan-validate-execute — draft, check against a deterministic validator, fix, and only proceed on pass; emit machine-checkable plan artifacts before batch or destructive operations. Use when output quality is critical, when a task mutates many files or records at once, or when an agent claims success without evidence.
tags: [verification, validation, feedback-loops, quality-gates, agent-operations, okf]
type: Playbook
domain: agent-operations
risk_level: low
requires_review: false
---

# Gating Work With Verification Loops

An unverified claim of success is the default failure mode of agent work. Every quality-critical task needs a loop where a checker — preferably deterministic — gates progression.

## The core loop

```text
draft → validate → (fail: read error, fix, re-validate) → pass → proceed
```

Rules:

- **Only proceed on pass.** No "validation mostly passed."
- The validator's error text is the repair context — make validators verbose and specific ("field `signature_date` not found; available: customer_name, order_total, signature_date_signed"), never boolean-silent.
- Deterministic checkers (scripts, schemas, test suites, linters) outrank LLM judges. Use an agentic grader only for inherently judgment-based qualities, and give it a written rubric.
- The checker must be separate from the producer: an agent grading its own output with the same context inherits its own blind spots.

## Plan-validate-execute (for batch or destructive work)

For operations that touch many targets or can't be cheaply undone, insert a verifiable intermediate artifact:

```text
analyze → write plan file (JSON/YAML) → validate plan with script → execute plan → verify result
```

Why it works: errors surface before anything is touched; the plan is machine-checkable and reviewable; the agent iterates on the plan without mutating originals; a human gate can approve the plan artifact itself. Use for: bulk edits, migrations, mass outreach, permission changes, deletions.

## Verification after mutation

After any state change, verify at the level the change claims to operate:

```text
code edit      → build + targeted test, not "file saved"
service change → end-to-end request against the running system
data write     → read back and compare
release        → install/run the shipped artifact, not the source tree
```

"Build completed" is not "system works" — restart-dependent systems need the restart *and* a probe. Report outcomes faithfully: failing checks are reported as failures with output attached, never rounded up to success.

## Checklists as loop scaffolding

For multi-step verified workflows, have the agent copy a checklist and tick items as validators pass — it prevents step-skipping under context pressure and makes progress auditable:

```text
- [ ] plan written          - [ ] plan validated
- [ ] changes applied       - [ ] result verified
- [ ] evidence recorded
```

## Wiring into loops and ledgers

In recurring loops, the validator gates the ledger: a status may flip to `done` only with the validator's evidence attached (command, output, artifact hash). This turns "the agent says it finished" into "the record shows it passed" — the difference between a log and a ledger.

## Related skills

- `engineering-loop-contracts` — the checker layer inside recurring loops.
- `authoring-agent-skills` — embedding these loops inside skills you write.
