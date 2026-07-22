# Skills

**Architectonic layer:** [main CLI and adaptive profiles](https://github.com/architectonic/architectonic)

> **Status: experimental, pre-1.0.** The reviewed core and the external registry are separate trust zones. A discovered, normalized, packaged, popular, or official-looking skill is not trusted merely because it is available.

`skills` defines reusable procedures with explicit triggers, inputs, ordered method, verification, failure handling, provenance, license context, and risk.

## Trust zones

```text
core/       small reviewed first-party procedures
skills/     working source and curation material
dist/       generated external registry; untrusted until reviewed
sources/    provenance and review records
operations/ maintenance, classification, lifecycle, and curation machinery
```

The reviewed core is enumerated in `core/manifest.json`. External entries are discovery candidates. Local adoption must inspect provenance, license, hidden scripts and tool calls, prompt injection, destructive behavior, credential access, data movement, runtime fit, and authority boundaries.

Installing a skill does not authorize it. Installing an agent does not grant runtime authority.

## Catalog classification

Imported skill bodies are preserved as source artifacts. When imported frontmatter is absent, misleading, or too weak for safe routing, reviewed metadata corrections live in `operations/classification-overrides.json` and are applied by `scripts/build_distribution_catalog.py`.

An override may add or correct:

```text
domain
risk_level
requires_review
artifact_kind
target_surfaces
source_status
review_status
classification_evidence
```

`classification_override=true` means the catalog metadata was reviewed separately. It does **not** mean the imported procedure, code, dependencies, or runtime behavior are approved.

`target_surfaces` is a routing hint for Architectonic, Workframe, Click.Blue, or the design system. It is never an authority grant.

## Catalog lifecycle decisions

Classification answers what an entry appears to be and how much review it needs. A deeper body-level review may additionally record a lifecycle and installation decision in `operations/catalog-decisions.json`.

```text
lifecycle_status        candidate | review-required | reviewed | blocked | superseded | deprecated
install_recommendation  inspect | recommended | conditional | do-not-install
superseded_by           reviewed replacement when one exists
decision_evidence       concise reason grounded in the inspected body and provenance
```

`catalog_decision=true` means the packaged body was inspected for behavior, overlap, provenance, and safe installation role. It still does not grant runtime authority.

Installers and agents must treat:

- `install_recommendation=do-not-install` as a package-level stop signal;
- `lifecycle_status=superseded` as an instruction to use the recorded replacement instead;
- `install_recommendation=conditional` as requiring the stated scope and review conditions;
- absent lifecycle decisions as unreviewed, not implicitly safe.

Imported bodies remain available as evidence even when blocked or superseded. Deep review changes catalog routing; it does not silently rewrite upstream material.

## Reviewed core

### Grounding and collaboration

- `document-guided-organization-bootstrap` — inspect documents first, then ask consequential questions tied to gaps.
- `source-grounding` — route durable claims to recoverable evidence.
- `assumption-grilling` — expose assumptions, missing reasoning, and disconfirming evidence.
- `agent-handoff` — preserve bounded continuity across agents and sessions.
- `architecture-review` — inspect system boundaries and drift before structural change.

### Adaptive systems

- `adaptive-composition` — choose no framework, one layer, a profile, or exact composition.
- `knowledge-lifecycle-design` — choose memory, ordinary knowledge, or living knowledge and define maintenance gates.
- `source-first-wiki` — compile source-backed wiki knowledge, inventory, datasets, outputs, sessions, and quiet archives.
- `second-brain-distillation` — capture, organize, distill, and express personal knowledge around active outcomes.
- `loop-engineering` — design recurring agent work with state, verification, budgets, authority, and stopping conditions.
- `graph-projection` — derive inspectable graphs from canonical files without replacing them.
- `public-skill-adoption` — review public skills as a supply-chain and authority decision rather than a popularity contest.

## Skill contract

```text
trigger        when the procedure applies
inputs         what must be inspected or received
procedure      ordered method
verification   how success is checked
failure modes  errors the procedure is intended to prevent or expose
provenance     source, revision, author, and license context
risk           mutation, network, credentials, production, and external effects
```

## Ecosystem compatibility

Architectonic skills can coexist with public Agent Skills from Anthropic, OpenAI, Google, GitHub, and independent publishers. Compatibility is not approval. Vendor or reference the exact reviewed revision and preserve local policy, provenance, and update rules.

The core also encodes reusable lessons from source-first LLM wikis, OKF-style Markdown, Git/Markdown knowledge systems, second-brain methods, loop engineering, and graph engineering. These are procedures and boundaries, not mandatory tool dependencies.

## Install

```bash
npx architectonic@latest add skills --source npm
npx architectonic@latest verify
```
