---
type: Source Profile
title: Agent Skills Open Standard
description: Candidate source for the emerging Agent Skills package format and cross-runtime skill interoperability.
tags: [source-profile, skills, standard, claude, interoperability]
okf_version: "0.2"
source_url: https://agentskills.io
source_name: Agent Skills Open Standard
source_author: Anthropic / Agent Skills ecosystem
license: UNKNOWN
runtime_targets: [claude, vscode, github-copilot, cursor, goose, amp, opencode]
skill_format: agent-skill-package
risk_level: medium
ingestion_status: candidate
reviewed_at: 2026-07-02
---

# Agent Skills Open Standard

## What It Is

A public Agent Skills specification and ecosystem signal for packaging reusable instructions, scripts, and resources as interoperable agent skill bundles.

## Why It Matters

This repository is already an installable skills package. A reviewed source profile for the emerging Agent Skills format can help keep local package surfaces compatible with runtimes that consume skill bundles.

## Provenance

- Candidate specification URL: https://agentskills.io
- Public web sources on 2026-07-02 described the open specification and SDK as available at that URL, with adoption signals across VS Code, GitHub, Cursor, Goose, Amp, and OpenCode.

## License

Unknown from the Radar pass. Source Reviewer must inspect the specification, SDK repository, license, and redistribution terms before any normalization.

## Runtime Targets

- Claude / Claude Code style skills
- VS Code and GitHub agent integrations
- Cursor, Goose, Amp, OpenCode, and related coding agents
- Runtime-neutral skill package export

## Candidate Capabilities

- Skill directory layout comparison
- Metadata and package format alignment
- Installability and compatibility checks
- Cross-runtime export guidance

## Risks

- Medium risk because skill packages may include scripts, resources, dependency assumptions, and runtime-specific execution semantics.
- Avoid copying specification text; summarize only after license review.

## Ingestion Decision

Candidate only. Reference-only until reviewed.

## Next Action

Source Reviewer should verify the official specification URL, locate the license and SDK repository, inspect package structure expectations, and decide whether a Packager or Cataloger queue item is warranted.
