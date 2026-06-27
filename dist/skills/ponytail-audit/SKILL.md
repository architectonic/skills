---
name: Ponytail Audit — Repo-Wide Over-Engineering Scan
description: Audit the whole repo for over-engineering. A ranked list of what to delete,
  simplify, or replace with stdlib or native features.
tags:
- design
- skill
- okf
- software-engineering
- code-review
- yagni
- simplicity
- audit
source: https://github.com/DietrichGebert/ponytail
license: MIT
risk: low
type: Playbook
title: Ponytail Audit — Repo-Wide Over-Engineering Scan
domain: design
risk_level: medium
requires_review: true
source_family: agent-skills-standard
source_license: MIT
source_status: adapted
---

# Ponytail Audit — Repo-Wide Over-Engineering Scan

Audit the whole repo for over-engineering. Scan the whole tree instead of a diff. Rank findings biggest cut first.

## Tags

- `delete:` dead code, unused flexibility, speculative feature. Replacement: nothing.
- `stdlib:` hand-rolled thing the standard library ships. Name the function.
- `native:` dependency or code doing what the platform already does. Name the feature.
- `yagni:` abstraction with one implementation, config nobody sets, layer with one caller.
- `shrink:` same logic, fewer lines. Show the shorter form.

## Hunt

Deps the stdlib or platform already ships, single-implementation interfaces, factories with one product, wrappers that only delegate, files exporting one thing, dead flags and config, hand-rolled stdlib.

## Output

One line per finding, ranked: `<tag> <what to cut>. <replacement>. [path]`. End with `net: -<N> lines, -<M> deps possible.` Nothing to cut: `Lean already. Ship.`

## Boundaries

Scope: over-engineering and complexity only. Correctness bugs, security holes, and performance are explicitly out of scope. Route them to a normal review pass. Lists findings, applies nothing. One-shot. "stop ponytail-audit" or "normal mode" to revert.
