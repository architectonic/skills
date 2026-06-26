---
name: Project Skill Audit
description: Analyze a project and recommend highest-value skills to create or update. Use when auditing project skills, getting skill recommendations, or reviewing existing skill coverage.
tags: [skill-management, skill-management, audit, project-analysis, recommendations]
source: terminal-skills (terminalskills.io)
license: Apache-2.0
distilled: 2026-06-22
type: Playbook
---

# Project Skill Audit

## Overview

Audit the project's real recurring workflows before recommending skills. Prefer evidence from memory, session history, existing skill folders, and current repo conventions over generic brainstorming.

Recommend updates before new skills when an existing project skill is already close to the needed behavior.

## Workflow

1. **Map the current project surface.**
   Identify the repo root and read the most relevant project guidance first: `AGENTS.md`, `README.md`, roadmap/ledger files, and local docs that define workflows or validation expectations.

2. **Build the memory/session path first.**
   - Check memory for project name, basename, and important module/file names
   - Read the 1-3 most relevant past session summaries for this project
   - Fall back to raw session transcripts only when summaries lack needed evidence

3. **Scan existing project-local skills before suggesting anything new.**
   Check these locations relative to the repo root:
   - `.agents/skills/`
   - `.hermes/skills/`
   - `skills/`
   - `.codex/skills/`

4. **Compare project-local skills against recurring work.**
   Look for repeated patterns in past sessions:
   - Repeated validation sequences
   - Repeated failure shields
   - Recurring ownership boundaries
   - Repeated root-cause categories
   - Workflows that repeatedly require the same repo-specific context

5. **Separate `new skill` from `update existing skill`.**
   - Recommend an **update** when an existing skill is the right bucket but has stale triggers, missing guardrails, outdated paths, or weak validation instructions
   - Recommend a **new skill** only when the workflow is distinct enough that stretching an existing skill would make it vague

6. **Check for overlap with global skills only after reviewing project-local skills.**
   Don't reject a project-local skill just because a global skill exists — project-specific guardrails can still justify a local specialization.

## Recommendation Rules

- **Recommend a new skill** when the same repo-specific workflow or failure mode appears multiple times across sessions, success depends on project-specific paths/scripts/ownership/validation, or the workflow benefits from strong defaults
- **Recommend an update** when an existing project-local skill already covers most of the need but has drifted
- **Do not recommend a skill** when the pattern is a one-off bug, a generic global skill already fits, or the workflow hasn't recurred enough to justify maintenance

## Output Format

Return a compact audit with:

1. **Existing skills** — list project-local skills found and the main workflow each covers
2. **Suggested updates** — skill name, why incomplete/stale, highest-value change
3. **Suggested new skills** — name, justification, triggers, core workflow
4. **Priority order** — rank by expected value

## Failure Shields

- Do not invent recurring patterns without session or repo evidence
- Do not recommend duplicate skills when an update would suffice
- Do not rely on a single memory note if the repo has clearly evolved
- Do not recommend skills from themes alone — recommendations must come from repeated procedures, validation flows, or failure modes
