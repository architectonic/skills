---
type: Source Profile
title: MagicSkills
description: Reviewed reference-only profile for Narwhal-Lab MagicSkills, a local-first skill collection manager for SKILL.md libraries and agent runtime exposure.
tags: [source-profile, skills, skill-library, registry, agents-md, reference-only]
okf_version: "0.2"
source_url: https://github.com/Narwhal-Lab/MagicSkills
source_name: MagicSkills
source_author: Narwhal-Lab
license: MIT
runtime_targets: [claude-code, cursor, windsurf, aider, codex, autogen, crewai, langchain, langgraph, semantic-kernel, llamaindex, generic-agent]
skill_format: skill-directory-with-SKILL-md-and-collection-registry
risk_level: medium
ingestion_status: reference-only
reviewed_at: 2026-07-06
---

# MagicSkills

## What It Is

MagicSkills is a public Narwhal-Lab repository for managing reusable `SKILL.md` skill directories across multiple agent apps and agent frameworks. It separates a physical skill pool from named runtime-specific skill collections and can expose those collections either by syncing an `AGENTS.md` block or by dispatching through a CLI/Python tool interface.

The source is relevant to this repository because it treats skills as reusable operational units rather than loose prompt snippets. The reusable idea is not its implementation code. The reusable idea is the governance model: install skills once, select only the subset a runtime should see, persist collection membership, and choose the exposure surface according to the target runtime.

## Provenance

- Repository: `Narwhal-Lab/MagicSkills`
- Default branch inspected: `main`
- Repository maintainer shown in README: Narwhal-Lab / Peking University
- Package metadata inspected: `pyproject.toml`, package name `MagicSkills`, version `1.1.0`, Python `>=3.10,<3.14`
- License file inspected directly: MIT
- Evidence inspected: `README.md`, `LICENSE`, `pyproject.toml`, `doc/cli.md`, `doc/python-api.md`, and `src/magicskills/cli.py`

## License

MIT license found in the repository license file. This permits reuse under the license terms, but this profile remains reference-only. No upstream code, docs, examples, screenshots, package data, skill templates, or CLI implementation are copied into Architectonic skills in this pass.

## Runtime Targets

Observed targets include agent apps that can read `AGENTS.md` and framework/tool-call integrations that need CLI or Python dispatch. The reviewed design also names Claude Code, Cursor, Windsurf, Aider, Codex, AutoGen, CrewAI, LangChain, LangGraph, Haystack, Semantic Kernel, smolagents, and LlamaIndex as examples.

These are integration surfaces, not endorsement targets. Any future normalization should describe a runtime-neutral pattern and not assume the package is installed or safe to execute inside scheduled runs.

## Candidate Capabilities

Useful concepts for future normalization, if converted narrowly and with attribution:

1. Shared skill pool: keep physical skills in one canonical storage root rather than copying them into every agent project.
2. Named collections: expose only the subset of skills that a given agent, team, or workflow needs.
3. Surface-specific sync: use `AGENTS.md` for document-driven agents and tool/CLI dispatch for function-call or framework integrations.
4. Registry persistence: persist collection metadata as references, not full duplicated skill contents.
5. Collision handling: when skill names conflict, require explicit paths instead of ambiguous names.
6. Execution separation: listing, reading, syncing, and executing skills are different capabilities and should not share one implicit trust level.

## Risks

- Execution risk: the CLI exposes command execution and skill execution surfaces. Scheduler runs must not execute candidate tools or installed upstream skills.
- Installation risk: the package can install skills from repositories or paths. This repository should not run installer commands or import upstream skills without separate source/risk review.
- Upload/account-flow risk: upload flows may use GitHub CLI/authenticated account operations. Scheduler runs must not perform account actions or PR/upload flows from this source.
- Context-injection risk: syncing generated skill blocks into `AGENTS.md` can alter future agent behavior; any local equivalent needs provenance and review gates.
- Collection drift risk: registry references can point to mutable filesystem content; normalized doctrine should require explicit source, version, and review metadata.

## Ingestion Decision

Decision: `reference-only_with_normalizer_follow_up`.

Rationale: MagicSkills is licensed and directly relevant to multi-agent skill governance, but immediate safe value is a reviewed source profile and a narrow original normalizer queue item. No third-party content or executable surface should be ingested in this pass.

## Next Action

Queue a Normalizer pass for an original Architectonic skill or playbook on shared skill-library governance. It should teach the collection model, runtime exposure decision, review gates, and failure modes without copying upstream prose, command examples, code, or templates.
