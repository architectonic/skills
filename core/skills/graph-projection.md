---
type: Skill
title: Graph Projection
description: Use when relationships in canonical Markdown should be projected into a rebuildable graph for navigation, quality review, community analysis, or visualization.
tags: [architectonic, core-skill, graph, obsidian]
source_status: native
source_name: Architectonic reviewed core
source_license: Apache-2.0
risk_level: low
requires_review: false
status: reviewed
---

# Graph Projection

## Trigger

Use when links, dependencies, communities, missing bridges, or navigation cannot be understood reliably from a flat file tree.

## Inputs

Canonical Markdown, explicit links or relations, source identifiers, graph schema, optional extraction model, intended graph consumers, and review policy.

## Procedure

1. Keep canonical claims and source records in readable files independent of the graph engine.
2. Extract explicit Markdown links, wikilinks, and declared relations deterministically where possible.
3. Label model- or algorithm-proposed relations as inferred and retain method, model, date, confidence, source scope, and review status.
4. Generate a rebuildable projection rather than editing canonical content through graph side effects.
5. Check broken and ambiguous links, orphaned nodes, duplicate concepts, overloaded gravity wells, and missing bridges.
6. Use community detection or hierarchical summaries only as derived navigation aids.
7. Export through open formats such as JSON or DOT where practical.
8. Allow Obsidian, Graphify, GraphRAG, or another renderer to consume the projection without owning the source of truth.

## Verification

- Every edge is extracted or explicitly labeled inferred.
- The graph can be deleted and rebuilt from canonical material.
- Derived summaries preserve links to underlying nodes and sources.
- Ambiguous and broken relations are reported rather than silently resolved.
- Graph tooling is optional to reading and maintaining the corpus.

## Failure Modes

- Treating an inferred edge as established fact.
- Allowing graph identifiers to drift from canonical file identifiers.
- Making the database or visualization the only recoverable copy.
- Hiding ambiguity behind a single generated relation.
- Optimizing graph density instead of useful knowledge structure.
