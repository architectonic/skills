---
name: pragmatic-engineering
description: Pragmatic engineering practices from Hunt & Thomas "The Pragmatic Programmer" — orthogonality, tracer bullets, prototyping, automation, and broken windows as agent operating discipline.
tags: [agent-operations, pragmatic, hunt-thomas, orthogonality, tracer-bullets, automation, broken-windows]
type: Playbook
---

# Pragmatic Engineering

## When to Use

Apply as a general engineering operating style when the goal is accountable delivery, adaptability, fast feedback, and code that remains easy to change.

## Core Principle

Do not optimize only for the local edit, requested feature, or familiar ritual. Own the outcome by reducing duplicated knowledge, keeping concerns independent, proving assumptions early, automating repeated work, and making intent clear.

## Decision Rules

1. **Be pragmatic, not dogmatic** — Choose the practice, formality, quality level, and stopping point that improves real outcomes.
2. **Own the result** — Surface tradeoffs, risks, uncertainty, and avoidable design costs instead of blaming tools, frameworks, schedule pressure, or existing style.
3. **Think beyond the local edit** — Quick fixes that multiply future maintenance cost are usually a bad bargain. Leave touched areas better where the cost is low.
4. **One authoritative representation per fact** — Business rules, validation, status semantics, mappings, calculations, schemas, configuration meaning should derive from or trace to one owner.
5. **Preserve orthogonality** — Keep components independent, responsibilities non-overlapping, interfaces narrow, collaborator knowledge small, and policy/mechanism/data/presentation separated.
6. **Keep volatile decisions reversible** — Do not hard-code vendors, platforms, databases, deployment environments, or requirements before evidence justifies the commitment.
7. **Tracer bullets over isolated pieces** — Prefer thin end-to-end slices over piles of isolated components. Keep the first slice simple but real enough to validate architecture and assumptions.
8. **Prototypes to learn, not to pretend** — State what the prototype proves, what it does not prove, and which shortcuts must be discarded or hardened.
9. **Dig for real requirements** — Separate durable needs and constraints from current implementation details, proposed solutions, and unresolved team hesitation.
10. **Automate repetitive work** — Builds, tests, linting, formatting, packaging, deployment, setup, validation, release should be reproducible and aligned with shared automation.
11. **Shorten feedback loops** — Relevant tests, automated checks, visible failures, cheap early signals before late expensive surprises.
12. **Make contracts and assumptions explicit** — Invariants, responsibilities, caller/callee obligations close to the abstraction they protect.
13. **Distinguish error types** — Programmer errors, contract violations, impossible states, expected domain failures, retryable failures, recoverable failures, permanent failures. Preserve diagnostic context.
14. **Resource ownership is a contract** — Release every acquired allocation, handle, lock, or resource on success and failure paths, preferably opposite acquisition order.
15. **Prefer inspectable plain text and open formats** — When longevity, diffability, automation, migration, or interoperability matter.
16. **Shared mutable state, globals, temporal coupling are costs** — That must earn themselves and be made visible.
17. **Debug from reproduced facts** — Observe, isolate, explain, fix, verify before guessing or blaming compilers, OS, libraries, vendors.
18. **Broken windows rule** — Fix or visibly contain small quality decay before bad code, unclear ownership, weak design, or broken process becomes normal.

## Trigger Rules

- Same fact in multiple artifacts → choose one owner, derive/validate/trace the rest
- One change requires edits in many unrelated places → repair missing boundary or hidden coupling
- Volatile details are hard-coded → move to validated, versioned configuration or explicit abstraction
- Uncertainty is high or decision is hard to reverse → reduce risk with tracer feedback, prototype, smaller reversible step
- Prototype/generated/tool output becoming production truth → inspect, understand, harden, replace, or reject deliberately
- Prose specs growing without reducing uncertainty → build a working slice that forces feedback
- Hidden assumptions in comments/folklore → move into code, contracts, tests, scripts, checked configuration
- Error or resource crosses a boundary → decide who can recover, what context survives, who owns cleanup
- Shared state/async/locks/ordering appears → make ownership, synchronization, cleanup explicit
- Repeated manual steps → automate and version them
- Tests slow/flaky/environment-dependent → improve the feedback path
- Human finds a bug → add or improve an automatic regression test
- Code works for reasons nobody can explain → stop and prove the behavior with data
- Local decay in touched code → fix if cheap or leave explicit containment/cleanup path

## Final Checklist

- [ ] One authoritative owner for each system fact?
- [ ] Unrelated concerns independent and volatile choices reversible?
- [ ] Working feedback exists for risky assumptions?
- [ ] Prototype/generated/tool-derived behavior deliberately accepted?
- [ ] Contracts, failures, diagnostics, resources, cleanup explicit?
- [ ] State, concurrency, ordering, coupling visible?
- [ ] Repeatable work automated and versioned?
- [ ] Tests automatic, relevant, and run before calling the change done?
- [ ] Names, comments, docs, scripts, tests, commits communicate intent?
- [ ] Touched area better or explicitly contained?
