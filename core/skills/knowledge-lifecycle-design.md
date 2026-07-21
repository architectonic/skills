---
type: Skill
title: Knowledge Lifecycle Design
description: Use when choosing between memory, ordinary knowledge, and living knowledge and defining how claims are sourced, reviewed, revised, and retired.
tags: [architectonic, core-skill, knowledge, living-knowledge]
source_status: native
source_name: Architectonic reviewed core
source_license: Apache-2.0
risk_level: low
requires_review: false
status: reviewed
---

# Knowledge Lifecycle Design

## Trigger

Use when creating or repairing a corpus, wiki, research system, operational catalog, regulatory knowledge base, or second brain.

## Inputs

The claims to preserve, canonical sources, expected source-change rate, maintainers, freshness requirements, contradiction policy, review authority, publication boundary, and downstream uses.

## Procedure

1. Separate memory traces, recoverable sources, claims, synthesis, inference, and derived outputs.
2. Use ordinary knowledge when updates occur through deliberate curation and external change does not routinely invalidate correctness.
3. Add living knowledge only when correctness decays as external sources change.
4. For living knowledge, define the watch boundary, freshness rule, comparison method, verification standard, publication gate, destructive-change gate, budget, and stop condition.
5. Preserve contradictions and known unknowns rather than flattening them.
6. Keep large or operational datasets external through manifests, schemas, samples, access rules, and query recipes.
7. Define how stale, superseded, rejected, and archived material becomes quiet without losing provenance.
8. Evaluate retrieval and synthesis against representative questions and source trails.

## Verification

- Every durable claim can be traced to a source, explicit decision, or labeled assumption.
- Living maintenance has an external-change justification and bounded operating contract.
- Operational inventories and retrieval scores are not treated as evidence.
- Derived outputs remain reproducible from canonical material.
- Stale and contradictory material is visible.

## Failure Modes

- Calling a transcript or generated summary knowledge by default.
- Adding living maintenance to a stable corpus.
- Running endless source scans without publication or stopping gates.
- Copying large mutable datasets into prose.
- Treating semantic similarity as factual support.
