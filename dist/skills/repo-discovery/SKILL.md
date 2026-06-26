---
name: repo discovery
description: Repo Discovery Skill. Use when the agent needs to repo discovery.
tags: [agent-operations, agent-operations]
type: Playbook
---

## Trigger

Use when entering an unfamiliar repository.

## Inputs

- Repository access.
- User-stated task.
- Existing docs and manifests.

## Procedure

1. Read `README.md`, `AGENTS.md`, and `START_HERE.md` if present.
2. Identify package manifests and scripts.
3. Identify source entry points.
4. Identify test commands.
5. Identify deployment or runtime config.
6. Identify domain concepts from source, not assumptions.
7. Report known facts, inferred facts, and open questions.

## Verification

- Point to the files that support each major claim.
- Do not infer project goals from folder names alone.

## Failure Modes

- Inventing architecture from familiar stack patterns.
- Missing project-specific conventions.
- Ignoring test/deploy scripts.
- Writing before understanding the repo boundary.
