---
name: authoring-agent-skills
description: Author portable SKILL.md agent skills that trigger reliably and spend context wisely — frontmatter discipline, progressive disclosure, degrees of freedom, and a pre-publish checklist. Use when creating a new skill, reviewing or normalizing an existing skill, or deciding what belongs in a skill versus always-loaded instructions.
tags: [skills, skill-authoring, progressive-disclosure, agent-operations, okf]
type: Playbook
domain: agent-operations
risk_level: low
requires_review: false
---

# Authoring Agent Skills

A skill is a folder with a `SKILL.md` (frontmatter + instructions) plus optional `scripts/`, `references/`, and `assets/`. The format is an open standard (agentskills.io, originated by Anthropic) supported by Claude Code, Codex, Gemini CLI, Cursor, Copilot, Goose, OpenCode, and many others — author once, run anywhere.

## The three-stage contract

Agents load skills by progressive disclosure. Write for all three stages:

1. **Discovery** — only `name` + `description` are pre-loaded (~100 tokens). The description alone decides whether the skill ever fires.
2. **Activation** — the full SKILL.md body loads when relevant. Every token now competes with the live conversation.
3. **Execution** — referenced files load, and bundled scripts run, only as needed. Bundled material costs nothing until touched.

## Frontmatter rules

- `name`: ≤64 chars, lowercase letters/numbers/hyphens only. Prefer gerund or action form (`processing-pdfs`, `authoring-agent-skills`). Never vague (`helper`, `utils`).
- `description`: ≤1024 chars, non-empty, **third person**, and always two parts: *what it does* + *when to use it*, with the trigger words users actually say. Discovery matches against this text — missing trigger terms means the skill silently never activates.

## Body rules

- Keep the body **under 500 lines**; split anything more into referenced files.
- Assume the model is already smart: cut definitions of common concepts; every paragraph must justify its token cost.
- One recommended tool/approach with an escape hatch — not a menu of five options.
- Consistent terminology throughout (pick one word per concept and keep it).
- No time-sensitive facts in the main flow; park legacy behavior in an "old patterns" section.
- References go **one level deep** from SKILL.md — nested reference chains get partially read and silently truncated. Give reference files >100 lines a table of contents.
- Forward slashes in all paths.

## Set degrees of freedom deliberately

Match specificity to fragility:

- **High freedom** (heuristics, prose): many valid approaches; context decides. Example: code review guidance.
- **Medium freedom** (pseudocode, parameterized script): a preferred pattern with acceptable variation.
- **Low freedom** (exact script, "run exactly this, do not modify"): fragile or irreversible sequences — migrations, packaging, releases.

## Workflows and feedback loops

For multi-step tasks, provide a copyable checklist the agent ticks off, and build validator loops: draft → validate → fix → re-validate → only then proceed. For high-stakes batch operations use plan-validate-execute: emit a machine-checkable plan artifact, validate it with a script, then apply. See `gating-work-with-verification-loops`.

## Scripts

Prefer bundled utility scripts over asking the agent to regenerate code: more reliable, zero context cost until run. Scripts must solve, not punt — handle their own error cases, document every constant, state their dependencies explicitly. Mark intent clearly: "run `scripts/x.py`" (execute) vs "see `scripts/x.py` for the algorithm" (read).

## Pre-publish checklist

```text
- [ ] description = what + when, third person, includes trigger terms
- [ ] name lowercase-hyphen, action-oriented, ≤64 chars
- [ ] body <500 lines; details pushed to referenced files (one level deep)
- [ ] one default approach per decision, escape hatches only where needed
- [ ] degrees of freedom match task fragility
- [ ] validator/feedback loop present where quality matters
- [ ] scripts handle errors, no magic constants, dependencies stated
- [ ] no time-sensitive claims; consistent terminology; forward-slash paths
- [ ] ≥3 evaluation scenarios exist (see evaluating-skills-before-authoring)
```

## Related skills

- `evaluating-skills-before-authoring` — build evals before writing documentation.
- `gating-work-with-verification-loops` — validator-loop patterns referenced above.
- `validation-gated-skill-improvement` — governance for changing published skills.
