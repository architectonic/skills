---
name: skills-keep
title: Keep Skills Healthy
description: Use when maintaining a drifted skill library so reusable procedures stay normalized, categorized, packageable, and safe for progressive discovery. Prevents growth-without-quality.
type: Playbook
domain: agent-operations
tags:
- agent-operations
- okf
- upkeep
- maintenance
- quality
- distribution
source_name: TeleAgent skills distribution scripts + skills-upkeep doctrine
source_url: https://github.com/architectonic/teleagent/tree/main/skills
source_license: Apache-2.0
source_status: native
risk_level: medium
requires_review: false
runtime_targets: [hermes]
capabilities: [read-files, edit-files, run-tests]
---

# skills-keep — Keep a Skill Library Health

This skill turns the `skills-upkeep` playbook into a concrete, repeatable checklist you can run on demand. It targets a library that already exists and has drifted.

## Trigger

Run this skill when:
- new skills were bulk-imported and haven't been validated
- `uncategorized` or `unspecified` counts in `dist/catalog.md` are growing
- skill metadata (descriptions, tags, risk levels, source_status) drifts from the actual content
- overlap or duplicate skills make discovery harder than just writing the procedure yourself
- risk markers, provenance, or licensing on high-attribution skills are missing
- packaging artifacts (catalog, inventories, bundle docs) need regenerating after structural changes

## Inputs

- the current skills corpus (`dist/skills/<skill>/SKILL.md`)
- frontmatter rules from `doctrine/okf-frontmatter.md`
- ingestion policy from `doctrine/ingestion-policy.md`
- current catalog and inventory artifacts
- enrichment reports, quality-gate reports, source metadata
- license/provenance signals per skill

## Procedure

1. **Generate an inventory** — walk every skill directory, parse YAML frontmatter (with `name`, `type`, `title`, `domain`, `tags`, `risk_level`, `requires_review`, `source_*`), emit a JSON index.
2. **Normalize frontmatter** — for each skill:
   - set `type` correctly (`Skill`/`Playbook`/`Reference` per OKF rules)
   - `description` is trigger-oriented ("Use when …"), not a prose summary
   - `risk_level` matches the actual procedure (medium if it edits files, high if it touches shell/installs/network/account access)
   - `requires_review: true` on anything high-risk or security-related
   - `source_name`, `source_url`, `source_license`, `source_status` are set
   - `runtime_targets` lists actual runtime/client it targets (`[hermes, codex, cursor, claude-code, generic]` etc.)
3. **Reclassify uncategorized and miscategorized skills** using the canonical domain vocabulary from `doctrine/ingestion-policy.md` and `skills-catalog`'s domain list. Every skill must end up in a real domain; `uncategorized` is a staging zone.
4. **Detect overlap** — group skills by trigger similarity, not just filename. Flag:
   - duplicate skills (same trigger, different filename)
   - skills that were merged from multi-source scrapes with slight naming variance
   - siblings where one is clearly richer and the other is redundant
   - low-signal entries that teach no actionable procedure
5. **Prune or quarantine** low-value skills. For each flagged skill, pick one action:
   - **merge** — fold the unique bits from the worse file into the better one, delete the loser
   - **rewrite** — salvage the trigger but replace the body with a real procedure
   - **archive** (keep the file but remove from the distributable catalog)
   - **delete** if nothing salvageable
6. **Refresh packaging artifacts** — regenerate:
   - `dist/catalog.md` with updated domain and risk count tables
   - `reports/dist-skills-inventory.json`, `reports/dist-skills-enriched-inventory.json`
   - `reports/dist-skills-report.md`, `reports/dist-skills-domain-report.md`, `reports/dist-skills-risk-report.md`
   - `skills-lock.json` if your installer uses it
7. **Verify distributions remain installable** — each skill stays in its own directory at `dist/skills/<name>/`, and the catalog/inventory counts agree with the file tree.

## Verification
- `dist/catalog.md` domain and risk counts match the live `ls dist/skills` output
- no skill stays in `uncategorized` longer than a single maintenance pass
- no skill has `risk_level: unspecified` after classification
- inventory JSON fields are every skill's actual frontmatter, not stale mirrors
- high-risk skills have `requires_review: true`
- packaging manifests regenerate cleanly from the current library state

## Failure Modes
- growth outpaces categorization — the library becomes a pile of stuff, not a reusable map
- risk_level is left `unspecified` because nobody wants to label things — this silently auto-promotes them to "trusted"
- uncategorized grows unbounded — discovery quality collapses
- stale inventory vs real files — the bundle manifests lie about the library
- merge preference over pruning — the library keeps growing past usefulness

## Quick Reference

| Artifact | Rebuild Trigger |
|---|---|
| `dist/catalog.md` | After any skill add/remove/reclassify |
| `reports/dist-skills-inventory.json` | After any skill add/remove/frontmatter change |
| `reports/dist-skills-enriched-inventory.json` | After ingestion reviews or provenance updates |
| `reports/dist-skills-risk-report.md` | After risk classification pass |
| `reports/dist-skills-domain-report.md` | After domain classification pass |
| Discovered skills | On restart of the agent/package loader — no hot-reload |
