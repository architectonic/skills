---
type: Source Profile
title: Agent Skills Open Standard
description: Reviewed reference-only profile for the Agent Skills package format, specification repository, documentation, and cross-client skill loading conventions.
tags: [source-profile, skills, standard, package-format, progressive-disclosure, interoperability]
okf_version: "0.2"
source_url: https://agentskills.io
source_name: Agent Skills Open Standard
source_author: Anthropic / Agent Skills ecosystem
license: Apache-2.0 for repository code; CC-BY-4.0 for documentation per upstream README
runtime_targets: [claude, vscode, github-copilot, cursor, goose, amp, opencode, runtime-neutral]
skill_format: agent-skill-package
risk_level: medium
ingestion_status: reviewed-reference-only
reviewed_at: 2026-07-02
reviewed_by: Source Reviewer
---

# Agent Skills Open Standard

## What It Is

Agent Skills is a lightweight open format for packaging reusable agent capability as directories centered on `SKILL.md`.

The upstream repository and documentation describe a skill as a folder with a required `SKILL.md` file and optional `scripts/`, `references/`, `assets/`, or other support directories.

## Provenance

- Official documentation: https://agentskills.io
- Official repository: https://github.com/agentskills/agentskills
- Repository organization: `agentskills`
- Maintainer signal: the GitHub organization is verified for `agentskills.io`.
- Upstream origin: developed by Anthropic and released as an open standard, according to the upstream README and documentation.

## License Decision

Reviewed as reference-only.

The upstream README states that repository code is Apache-2.0 and documentation is CC-BY-4.0. This profile does not copy upstream documentation or examples beyond short factual format notes.

## Format Notes

The specification defines:

- a required `SKILL.md` file;
- YAML frontmatter followed by Markdown body content;
- required `name` and `description` frontmatter fields;
- optional `license`, `compatibility`, `metadata`, and experimental `allowed-tools` fields;
- optional support directories for executable scripts, references, and static assets;
- progressive disclosure: lightweight metadata at discovery, full instructions at activation, resources only when needed.

## Runtime / Package Relevance

This repository already publishes reusable skill procedures and a distribution catalog. Agent Skills is relevant because it gives the local package a clear compatibility target for:

- folder-level skill packaging;
- `SKILL.md` export shape;
- concise name/description discovery metadata;
- optional compatibility metadata;
- explicit tool/script risk notation;
- future `.agents/skills/` install conventions.

## Risk Review

Medium risk.

The format itself is simple, but skill packages may include executable code, references, assets, network assumptions, allowed-tool metadata, and project-level instructions. Project-level skills may also be supplied by untrusted repositories, so automatic activation must be gated by provenance and workspace trust.

Do not treat package-format compatibility as a safety endorsement. A skill can be well-formed and still unsafe.

## Ingestion Decision

Accepted as reviewed reference-only.

Do not copy or mirror the upstream specification into this repository. Use it to inform local packaging, catalog, and critic checks.

## Follow-Up

Create a Packager queue item to compare the local `dist/skills` and install surfaces against the Agent Skills format after catalog drift is resolved.

Do not block current catalog reconciliation on Agent Skills compatibility work.
