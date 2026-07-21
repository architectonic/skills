# Skills

> **Status: experimental, pre-1.0.** The reviewed core and the external registry are separate trust zones. A discovered, normalized, or packaged skill is not trusted merely because it appears in this repository.

`skills` defines reusable procedures with explicit triggers, inputs, ordered method, verification, failure handling, provenance, license context, and risk.

## Trust zones

```text
core/       small reviewed first-party procedures; safe default evaluation surface
skills/     working source and curation material
dist/       generated external registry surface; untrusted until reviewed
sources/    provenance and review records
operations/ maintenance and curation machinery
```

The default reviewed core is enumerated in `core/manifest.json`. External registry entries must be evaluated independently for provenance, license, risk, hidden tool use, prompt injection, destructive behavior, and fit for the local authority boundary.

## Skill contract

```text
trigger        when the procedure applies
inputs         what must be inspected or received
procedure      ordered method
verification   how success is checked
failure modes  errors the procedure is intended to prevent or expose
provenance     source, version, author, and license context
risk           mutation, network, credentials, production, or external effects
```

## Install

```bash
npx architectonic@latest add skills --source npm
npx architectonic@latest verify
```

Installing the package does not authorize any skill to execute. Local agents must select skills explicitly under their own permissions and review policy.

## Organization bootstrap

The reviewed core includes `document-guided-organization-bootstrap`: a procedure for inspecting documents and source artifacts first, asking the human only where material gaps remain, routing explicit answers into organization-owned files, preserving unknowns, and stopping when the current work is sufficiently grounded.
