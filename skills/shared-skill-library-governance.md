---
type: Skill
name: shared-skill-library-governance
title: Shared Skill Library Governance
description: Use when designing or operating a shared repository of agent skills so reusable skills stay canonical, reviewed, scoped to named collections, and exposed safely to each runtime.
tags: [skill, skill-library, governance, agent-runtime, collections, registry, agent-operations]
domain: agent-operations
timestamp: 2026-07-06T20:13:00-03:00
last_reviewed: 2026-07-07
okf_version: "0.2"
source_status: normalized
source_name: MagicSkills source-profile synthesis
source_url: https://github.com/Narwhal-Lab/MagicSkills
source_profile: sources/reviewed/magicskills.md
license: MIT reference source; this normalized skill is original Architectonic procedure text
risk_level: medium
requires_review: true
---

# Shared Skill Library Governance

## Trigger

Use this when an agent, team, runtime, installer, or repository needs to share reusable skills without copying every skill into every project or exposing unreviewed capabilities to every agent.

Do not use this for one-off prompt snippets, private skill dumps, unlicensed skill packs, or runtime-specific installer instructions that have not passed source and risk review.

## Inputs

- Canonical skill pool location: repository, package, directory, registry, or artifact store.
- Skill metadata requirements: name, source, license, review status, risk level, domain, runtime targets, version or commit reference, and install surface.
- Named collection targets: team, project, agent role, runtime, workflow, or deployment environment.
- Runtime exposure method: documentation include, AGENTS-style instruction block, package manifest, CLI/tool dispatch, MCP/tool registry, or manual install list.
- Trust boundary: what may be listed, read, synced, installed, executed, uploaded, or modified.
- Collision policy for duplicate names, aliases, moved skills, and deprecated skills.
- Review gates for provenance, licensing, safety, hidden instructions, filesystem/network behavior, and state-changing actions.

## Procedure

1. Keep one canonical physical skill pool. Do not duplicate skill bodies into every project unless the distribution format requires a generated copy.
2. Treat collections as references to reviewed skills, not as independent skill content. A collection should name which skills are exposed and why.
3. Define collection scope before exposure: target runtime, users or agents, allowed tasks, disallowed tasks, and risk level ceiling.
4. Separate visibility from execution:
   - listing means a skill can be discovered;
   - reading means the skill body can enter context;
   - syncing means the skill can modify runtime instruction surfaces;
   - installing means files or package state can change;
   - executing means commands, tools, scripts, network calls, or external actions may run.
5. Require stronger review for each higher trust level. A skill that is safe to list is not automatically safe to sync, install, or execute.
6. Use explicit runtime adapters. Document-driven runtimes may receive curated instruction blocks; tool-capable runtimes may receive narrow tool descriptors; package installers may receive immutable catalog metadata.
7. Preserve provenance in every surfaced entry: canonical path, source profile, license, review status, risk level, and last reviewed date.
8. Resolve duplicate skill names by requiring canonical paths or stable identifiers. Do not guess between ambiguous names.
9. Persist registry state as metadata references. Avoid storing duplicated skill bodies inside collection records unless the copy is generated, traceable, and refreshable.
10. When a skill changes under `skills/` or `dist/skills/`, create a Cataloger queue item before publication, packaging endorsement, or runtime rollout.
11. Record drift explicitly: missing canonical source, stale generated copy, unreviewed source, unsafe exposure surface, duplicate name, broken install manifest, or runtime-specific mismatch.
12. Roll out changes by collection. Start with a review-only or read-only collection before enabling sync, installation, tool dispatch, or execution.

## Verification

A valid shared-skill library pass has all of the following:

- The canonical skill pool and generated distribution surfaces are distinct and traceable.
- Each named collection has a stated purpose, runtime target, and risk ceiling.
- Every exposed skill has source, license, review status, risk level, and canonical path metadata.
- Listing, reading, syncing, installing, and executing are treated as separate permissions.
- Duplicate names require explicit canonical identifiers.
- Runtime-specific exposure does not bypass repository review gates.
- Any new or changed skill creates a catalog/package follow-up before publication or runtime endorsement.
- Registry state can be rebuilt from canonical skills and metadata rather than becoming a second source of truth.

## Failure Modes

- Copying skill bodies into multiple project folders until no canonical source remains.
- Treating a named collection as reviewed because the underlying repository is public.
- Syncing skill text into runtime instruction files without provenance, risk level, or review status.
- Letting a CLI/tool dispatcher execute skills that were only reviewed for reading.
- Resolving duplicate skill names by whichever match appears first.
- Publishing generated catalogs after a skill change without verifying counts, metadata, and install manifest pointers.
- Mixing private team skills, third-party public skills, and generated distribution copies in one undifferentiated pool.
- Allowing collection membership to drift from the canonical registry.

## Boundaries

- Do not clone, install, import, or execute third-party skill-library managers during scheduler runs.
- Do not copy upstream prose, code, examples, templates, command documentation, package metadata, or skill bodies into this repository.
- Do not expose private, leaked, unlicensed, or unreviewed skills through public catalogs or runtime instruction files.
- Do not grant execution, filesystem, network, credential, upload, or account-action capabilities merely because a skill is present in a collection.
- Do not let generated distribution files become the canonical source for authoring.

## Provenance Note

This skill was normalized from the reviewed `MagicSkills` source profile as original Architectonic procedure text. The reusable lesson is the governance model: a canonical skill pool, named collections, runtime-specific exposure surfaces, registry references, collision handling, and separate trust levels for listing, reading, syncing, installing, and executing. It is not an import of upstream wording, code, examples, package metadata, command documentation, templates, or skill bodies.
