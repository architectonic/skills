---
type: SourceReviewReport
title: Design Skill Consolidation
date: 2026-07-22
status: validation_pending
branch: agent/design-skill-consolidation
sources: [Hallmark, Taste Skill, Transitions.dev]
tags: [skills, design, source-review, deduplication, lifecycle, validation]
okf_version: "0.2"
---

# Design Skill Consolidation

## Decision

Replace wholesale import pressure with a small first-party composition:

1. `interface-design` for bounded implementation and redesign;
2. `interface-quality-audit` for evidence-backed critique without mutation;
3. `interface-transition-review` for state-based motion decisions;
4. `frontend-ui-engineering` retained conditionally for implementation mechanics;
5. `canvas-design` retained conditionally for static visual work.

Do not recommend the existing packaged `frontend-design` entry. Preserve its imported body as evidence and mark it superseded by `skills/interface-design.md`.

## Evidence

### Hallmark

- Reviewed commit: `aeb42fb354ff4efa36ab475773a082315a3af2ce`
- Reviewed skill blob: `e0715e9d8bf5fd12c6a31f677b181a212b4f2cf1`
- Upstream version: `1.1.0`
- License: MIT
- Use: source of bounded redesign, audit separation, preservation rails, truthful-content checks, token discipline, and pre-emit critique.
- Decision: distill; do not vendor wholesale.

### Taste Skill

- Reviewed commit: `98565e65bc3274ddf6eb0838734341714057178b`
- Reviewed skill blob: `b72132fcd466da605623ffe96e370b3991fc5285`
- Upstream default: v2 experimental
- License: MIT
- Use: source of brief inference, audience and regulatory constraints, design-system selection, dependency checks, and audit-first redesign.
- Decision: distill; do not vendor wholesale.

### Transitions.dev

- Reviewed commit: `047d036a79cc2ddecd868e7f1e3aa04b495644b2`
- Reviewed skill blob: `f39bc0538a612700638da314bd26fdd240c64d49`
- Root license: not found
- Root package license declaration: absent
- Use: source of state-based motion review, reduced-motion discipline, interruption checks, and usage-based motion tokens.
- Decision: reference only. Do not copy CSS snippets or implementation payloads until upstream licensing is explicit.

## Existing registry finding

`frontend-design` is not an acceptable shared default because its body:

- requires every output to use an `index.html` entry file regardless of project structure;
- mandates an external `Created By Deerflow` link in every generated interface;
- proposes branded watermarks, badges, signatures, and interaction effects;
- encourages visual escalation without a sufficiently strict preservation boundary.

The catalog decision is therefore:

```text
lifecycle_status: superseded
install_recommendation: do-not-install
requires_review: true
superseded_by: skills/interface-design.md
```

The imported body is not deleted or rewritten.

## Local skill decisions

### `interface-design`

Added as a first-party working skill with:

- component/section/page/flow/application scope resolution;
- inspection of existing project and design-system boundaries;
- concise evidence-based design read;
- preservation boundary before redesign;
- structure before surface styling;
- truthful content and proof;
- no forced framework, font, icon family, file layout, attribution, watermark, or aesthetic preset;
- applicable state coverage rather than impossible universal state requirements;
- motion delegated to `interface-transition-review`;
- rendered, responsive, accessibility, and functional verification.

### `interface-quality-audit`

Retained and upgraded from candidate provenance to exact reviewed Hallmark/Taste revisions. Still awaiting utility evaluation before core consideration.

### `interface-transition-review`

Retained and upgraded to the exact Transitions.dev revision. The source remains reference-only because upstream licensing is unclear. No CSS implementation or source body was copied.

## Catalog architecture

Added `operations/catalog-decisions.json` for body-level lifecycle decisions separate from metadata classification.

Added `scripts/apply_catalog_decisions.py` to expose:

- `lifecycle_status`;
- `install_recommendation`;
- `superseded_by`;
- `decision_evidence`;
- `catalog_decision` disclosure;
- lifecycle and recommendation summary counts.

The builder remains responsible for inventory and classification. The decision processor runs afterward so generated catalog rebuilds cannot erase reviewed body-level decisions.

## Boundaries

- No external skill was copied wholesale.
- No Transitions.dev CSS snippet was copied.
- No imported `dist/skills/**/SKILL.md` body was mutated.
- No candidate was added to `core/manifest.json`.
- No package or npm publication was attempted.
- No application, browser session, dependency, MCP server, or external account was invoked.

## Acceptance tests

| Test | Expected |
|---|---|
| Hallmark, Taste, and Transitions exact revisions are recorded | Pass in PR validation |
| Hallmark and Taste MIT licenses are recorded | Pass by source evidence |
| Transitions unclear-license boundary is explicit | Pass in PR validation |
| `frontend-design` is superseded and `do-not-install` | Pass in PR validation |
| `frontend-ui-engineering` and `canvas-design` remain conditional | Pass in PR validation |
| Local design skills have required contract sections | Pass in PR validation |
| Catalog generation preserves classification batch metrics | Pass in PR validation |
| No imported skill body is modified | Pass by construction |

## Next justified action

After validation and merge:

1. run small comparative evaluations for greenfield, redesign, audit-only, component, and motion tasks;
2. promote only the local procedures that show measurable improvement and acceptable token cost;
3. continue with Remotion/HyperFrames as the next source-review cluster;
4. continue metadata repair independently in bounded semantic batches.
