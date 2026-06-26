---
name: architecture-review-loop
description: Scan a codebase for deepening opportunities, present findings as a visual HTML report, then grill through the chosen candidate. Use when the user wants to improve codebase architecture, find deepening opportunities, turn shallow modules into deep ones, or review architectural friction. Covers deep-module vocabulary (module, interface, depth, seam, adapter, leverage, locality), the deletion test, and the design-it-twice pattern.
tags: [loops, software-development, architecture, deep-modules, review-loop]
type: Playbook
---

# architecture-review-loop

Scan a codebase for **deepening opportunities** — refactors that turn shallow modules into deep ones. Extracted from mattpocock/skills `improve-codebase-architecture` (MIT license, https://github.com/mattpocock/skills).

## Deep Module Vocabulary

Use these terms exactly:

- **Module** — anything with an interface and an implementation (function, class, package, tier-spanning slice)
- **Interface** — everything a caller must know to use the module (type signature + invariants + ordering constraints + error modes + required config + performance characteristics)
- **Implementation** — what's inside a module
- **Depth** — leverage at the interface: behavior per unit of interface a caller must learn
- **Seam** — a place where you can alter behavior without editing in that place (Michael Feathers)
- **Adapter** — a concrete thing that satisfies an interface at a seam
- **Leverage** — what callers get from depth: more capability per unit of interface learned
- **Locality** — what maintainers get from depth: change/bugs/knowledge concentrate in one place

## Deep vs Shallow

**Deep module** = small interface + lots of implementation (leverage)
**Shallow module** = large interface + little implementation (avoid)

## Key Principles

- **Depth is a property of the interface, not the implementation.** A deep module can be internally composed of small, mockable, swappable parts.
- **The deletion test.** Imagine deleting the module. If complexity vanishes, it was a pass-through. If complexity reappears across N callers, it was earning its keep.
- **The interface is the test surface.** Callers and tests cross the same seam.
- **One adapter means a hypothetical seam. Two adapters means a real one.** Don't introduce a seam unless something actually varies across it.

## Process

### 1. Explore

Read the project's domain glossary (`CONTEXT.md`) and any ADRs first. Then explore the codebase organically, noting friction:

- Where does understanding one concept require bouncing between many small modules?
- Where are modules **shallow** — interface nearly as complex as the implementation?
- Where have pure functions been extracted just for testability, but real bugs hide in how they're called?
- Where do tightly-coupled modules leak across their seams?
- Which parts are untested or hard to test through their current interface?

Apply the **deletion test** to anything you suspect is shallow.

### 2. Present Candidates as HTML Report

Write a self-contained HTML file to the OS temp directory. For each candidate, render a card with:

- **Files** — which files/modules are involved
- **Problem** — why current architecture causes friction
- **Solution** — what would change
- **Benefits** — in terms of locality and leverage, and how tests would improve
- **Before / After diagram** — side-by-side
- **Recommendation strength** — `Strong`, `Worth exploring`, or `Speculative`

End with a **Top recommendation** section.

### 3. Grilling Loop

Once the user picks a candidate, run a grilling session to walk the design tree: constraints, dependencies, the shape of the deepened module, what sits behind the seam, what tests survive.

Update the domain model inline as decisions crystallize:
- Naming a deepened module after a concept not in `CONTEXT.md`? Add it.
- Sharpening a fuzzy term? Update `CONTEXT.md` right there.
- User rejects with a load-bearing reason? Offer an ADR.

### 4. Design-It-Twice (Optional)

For critical seams, spin up parallel sub-agents to design the interface several radically different ways, then compare on depth, locality, and seam placement.

## Designing for Testability

1. **Accept dependencies, don't create them.** Functions that accept a gateway parameter are testable; functions that instantiate their own are not.
2. **Return results, don't produce side effects.** Pure functions are easier to test than void mutators.
3. **Small surface area.** Fewer methods = fewer tests needed.

## Relationships

- A **Module** has exactly one **Interface**
- **Depth** is a property of a **Module**, measured against its **Interface**
- A **Seam** is where a **Module**'s **Interface** lives
- An **Adapter** sits at a **Seam** and satisfies the **Interface**
- **Depth** produces **Leverage** for callers and **Locality** for maintainers
