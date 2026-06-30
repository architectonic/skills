---
name: skills-catalog
title: Catalog and Categorize Agent Skills
description: Use when inventorying, classifying, or recategorizing a skill library. Assigns domain tags, risk levels, source metadata, and catalog entries to skills at scale.
type: Playbook
domain: agent-operations
tags:
- agent-operations
- okf
- catalog
- categorization
- metadata
source_name: TeleAgent skills distribution scripts
source_url: https://github.com/architectonic/teleagent/tree/main/skills
source_license: Apache-2.0
source_status: native
risk_level: medium
requires_review: false
runtime_targets: [hermes]
capabilities: [read-files, edit-files, run-tests]
---

# skills-catalog — Catalog and Categorize Agent Skills

This skill classifies and catalogs skills so a large library remains progressively discoverable, not just technically present. It covers how every skill gets frontmatter, a domain, a risk marker, a type/category, and an entry in the distribution catalog.

## Trigger

Use when:
- a new skill is imported or created and needs frontmatter normalized
- the library has uncategorized or miscategorized entries
- you are refreshing packaging artifacts (catalog.md, inventory JSON, manifests)
- you need to audit whether every skill's metadata still matches its content

## Inputs

- the current skills corpus (`dist/skills/<skill>/SKILL.md`)
- the current catalog metadata (`dist/catalog.md`, `reports/dist-skills-inventory.json`, `reports/dist-skills-enriched-inventory.json`)
- known license/provenance info per skill
- the OKF frontmatter rules in `doctrine/okf-frontmatter.md`

## Procedure

1. **Inventory** — list every skill directory and gather frontmatter fields (`name`, `type`, `title`, `domain`, `tags`, `risk_level`, `requires_review`, `source_*`).
2. **Normalize frontmatter** — confirm each skill:
   - has the required `type` field (one of `Skill`, `Playbook`, `Reference`, `API Endpoint`, `Metric`, `BigQuery Table`, `Dataset`, or `Playbook`/`Reference` as used in TeleAgent)
   - includes trigger-oriented `description` specifying when to use it
   - has risk-appropriate `risk_level`
   - records source provenance (`source_name`, `source_url`, `source_license`, `source_status`)
   - declares `runtime_targets` matching the agents and CLIs it actually touches
3. **Assign each skill to a domain** using the canonical domain vocabulary:
   - `agent-operations` — workflow, memory, delegation, orchestration, skill lifecycle
   - `business` — GTM, commercial ops, pricing, partnerships
   - `cloud-security` — cloud hardening, compliance frameworks, CSPM
   - `design` — UX, visual design, diagram generation, creative direction
   - `forensics` — incident response, evidence collection, IOCs
   - `media` — audio, video, image generation, multimodal prompting
   - `research` — literature review, experimental design, data science, survey methodology
   - `runtime-tools` — CLI tools, MCP servers, API clients, SDK integrations
   - `security-defensive` — defensive-only controls, assessment, architecture review
   - `security-offensive` — pentesting, C2 simulation, exploit research (skip — never import without explicit opt-in)
   - `software-engineering` — frontend, backend, DevOps, SRE, testing, databases
   - `writing` — communication strategy, copy, editorial workflow
   - `uncategorized` — only until classified; never ship a library with many uncategorized entries
4. **Mark risk level** honestly per OKF rules: `low` (read/reason only), `medium` (edits files, runs tests, uses local tools), `high` (shell, installs, network, browser automation, account access, external systems, production mutation), `blocked` (unclear license, unsafe behavior, private data, unverifiable provenance).
5. **Detect overlap** — flag duplicate skills, skills that merged from multi-source scrapes, skills whose trigger has split across multiple entries. Merge or prune; don't let the catalog grow by name collision alone.
6. **Refresh catalog artifacts** — regenerate:
   - `dist/catalog.md` (domain + risk distribution tables)
   - `reports/dist-skills-inventory.json` (machine-readable index)
   - `reports/dist-skills-enriched-inventory.json` (with source metadata layered in)
   - any summary reports (`reports/dist-skills-report.md`, `reports/dist-skills-domain-report.md`, `reports/dist-skills-risk-report.md`)
7. **Verify** — recount by domain and risk_level and confirm the generated counts match the actual file tree.

## Verification
- every skill directory contains a `SKILL.md` with valid OKF frontmatter
- no skill stays in `uncategorized` after classification
- `dist/catalog.md` domain and risk tables match the live counts
- skill count totals (`skills-lock.json`, catalog, inventory JSON) agree
- high-risk or `requires_review: true` skills are explicitly marked, not silently auto-promoted

## Failure Modes
- `uncategorized` grows without bound, defeating progressive discovery
- frontmatter diverges from actual content (e.g., `risk_level: low` on a shell runner)
- inventory counts go stale as new skills are added but not reindexed
- skills with identical triggers but slightly different names fracture discoverability
- skipping the defensive review gate when ingesting offensive/security content

## Quick Reference

| Artifact | Path |
|---|---|
| Distribution catalog | `dist/catalog.md` |
| Inventory (raw) | `reports/dist-skills-inventory.json` |
| Inventory (with source metadata) | `reports/dist-skills-enriched-inventory.json` |
| Risk report | `reports/dist-skills-risk-report.md` |
| Domain report | `reports/dist-skills-domain-report.md` |
| Skill frontmatter rules | `doctrine/okf-frontmatter.md` |
| Skill doctrine | `doctrine/skill.md` |
| Ingestion policy | `doctrine/ingestion-policy.md` |
