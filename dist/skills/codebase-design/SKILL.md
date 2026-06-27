---
name: codebase-design
title: Codebase Design — Deep Modules
description: 'Design **deep modules**: a lot of behaviour behind a small interface,
  placed at a clean seam, testable through that interface. Use this language and these
  principles wherever code is being designed or restructured.'
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

# Codebase Design — Deep Modules

## Purpose

Design **deep modules**: a lot of behaviour behind a small interface, placed at a clean seam, testable through that interface. Use this language and these principles wherever code is being designed or restructured.

The aim is **leverage** for callers, **locality** for maintainers, and **testability** for everyone.

## Trigger

Use when:
- Designing or improving a module's interface
- Finding opportunities to deepen modules
- Deciding where a seam goes
- Making code more testable or AI-navigable
- Another skill needs the deep-module vocabulary

## Glossary

Use these terms exactly — don't substitute "component," "service," "API," or "boundary."

**Module** — anything with an interface and an implementation. Scale-agnostic: function, class, package, or tier-spanning slice. *Avoid*: unit, component, service.

**Interface** — everything a caller must know to use the module correctly: type signature, invariants, ordering constraints, error modes, required configuration, performance characteristics. *Avoid*: API, signature (too narrow).

**Implementation** — what's inside a module. Distinct from **Adapter**: a thing can be a small adapter with large implementation (Postgres repo) or large adapter with small implementation (in-memory fake). Reach for "adapter" when the seam is the topic; "implementation" otherwise.

**Depth** — leverage at the interface: behaviour per unit of interface a caller must learn. **Deep** = large behaviour behind small interface. **Shallow** = interface nearly as complex as implementation.

**Seam** (Michael Feathers) — a place where you can alter behaviour without editing in that place; the *location* at which a module's interface lives. *Avoid*: boundary (overloaded with DDD's bounded context).

**Adapter** — a concrete thing that satisfies an interface at a seam. Describes *role* (what slot it fills), not *substance* (what's inside).

**Leverage** — what callers get from depth: more capability per unit of interface learned. One implementation pays back across N call sites and M tests.

**Locality** — what maintainers get from depth: change, bugs, knowledge concentrate in one place. Fix once, fixed everywhere.

## Deep vs Shallow

```
Deep Module:                 Shallow Module (avoid):
┌─────────────────────┐      ┌─────────────────────────────────┐
│   Small Interface   │      │       Large Interface           │
├─────────────────────┤      ├─────────────────────────────────┤
│                     │      │  Thin Implementation            │
│  Deep Implementation│      │                                 │
│                     │      └─────────────────────────────────┘
└─────────────────────┘
```

When designing an interface, ask:
- Can I reduce the number of methods?
- Can I simplify the parameters?
- Can I hide more complexity inside?

## Principles

1. **Depth is a property of the interface, not the implementation.** A deep module can be internally composed of small, mockable, swappable parts — they just aren't part of the interface. A module can have **internal seams** (private, used by its own tests) as well as the **external seam**.

2. **The deletion test.** Imagine deleting the module. If complexity vanishes, it was a pass-through. If complexity reappears across N callers, it was earning its keep.

3. **The interface is the test surface.** Callers and tests cross the same seam. If you want to test *past* the interface, the module is probably the wrong shape.

4. **One adapter means a hypothetical seam. Two adapters means a real one.** Don't introduce a seam unless something actually varies across it.

5. **Accept dependencies, don't create them.** Functions that accept dependencies as parameters are testable; functions that instantiate dependencies internally are not.

6. **Return results, don't produce side effects.** Functions that return values are testable; functions that mutate state are harder to test.

## Designing for Testability

```typescript
// Testable: accepts dependency, returns result
function processOrder(order, paymentGateway): Result {}

// Hard to test: creates dependency internally, mutates state
function processOrder(order) {
  const gateway = new StripeGateway();
  order.total -= discount;
}
```

## Relationships

- A **Module** has exactly one **Interface** (surface presented to callers and tests)
- **Depth** is a property of a **Module**, measured against its **Interface**
- An **Adapter** satisfies an **Interface** at a **Seam**

## Verification

- [ ] Module has a single, small interface
- [ ] Implementation complexity is hidden behind the interface
- [ ] Dependencies are accepted, not created internally
- [ ] Functions return results rather than producing side effects
- [ ] Seams are real (two+ adapters), not hypothetical
- [ ] Tests cross the same seam as callers
- [ ] Vocabulary is consistent: module, interface, depth, seam, adapter, leverage, locality
