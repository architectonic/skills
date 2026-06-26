---
name: skill-factory-review
description: Review and govern skill generation factories, templates, and automated skill builders. Use when evaluating repositories or tools that produce skills automatically, generate agents/prompts/hooks from templates, or scaffold skill directories. Covers factory output review, template safety, and generated-artifact promotion gates.
tags: [skill-management, skill-management, skill-factory, generation, review, templates]
type: Playbook
---

# skill-factory-review

Review and govern skill generation factories, templates, and automated skill builders.

## When to use

- A repository or tool proposes to generate skills automatically
- A factory produces agents, prompts, hooks, or slash commands from templates
- A scaffold command creates new skill directories
- Generated artifacts are proposed for promotion into the skill library

## Why it matters

Skill factories multiply the ingestion surface. A single unsafe template can produce many unsafe skills. Factory outputs must be treated as high-review even when the factory itself is trusted.

## Factory classification

| Factory type | Risk posture |
|---|---|
| Template-only (produces markdown scaffolds) | Medium review |
| LLM-generated skill content | High review |
| OpenAPI / MCP → skill converter | High review |
| Agent / prompt / hook generator | High review |
| Full pipeline (generate + install + execute) | Critical review |

## Review dimensions

### Template safety
- Do templates embed hardcoded paths, secrets, or local assumptions?
- Do templates include agent-specific runtime tags?
- Do templates separate executable content from instruction content?
- Do templates include verification steps and failure modes?

### Generated output review
- Each generated skill must pass skill-quality-gate independently
- Generated skills must pass skill-safety-review before promotion
- Generated skills must not embed factory-internal paths or assumptions
- Generated skills must have clear provenance (which factory, which template, which inputs)

### Hook and command risk
- Hooks may execute on file save, git commit, or session start
- Slash commands may trigger external tools or APIs
- Generated commands must be reviewed for external mutation surface
- Hooks that run automatically are higher risk than on-demand commands

### Installer risk
- Factories that auto-install into agent directories are high-risk
- Symlink creation, global install scope, and recursive discovery must be reviewed
- Anonymous telemetry in installers must be disclosed

## Review workflow

```
Inspect factory source
→ Review templates for safety
→ Generate sample outputs
→ Run skill-quality-gate on samples
→ Run skill-safety-review on samples
→ Classify factory risk tier
→ Decide: allow / allow-with-review / block
```

## Promotion gate

Generated skills are promoted only if:
- Factory source is reviewed and classified
- Templates pass safety review
- Each generated skill passes skill-quality-gate
- Each generated skill passes skill-safety-review
- Provenance is preserved (factory, template, inputs, date)
- No auto-install without explicit approval

## Anti-patterns

- Promoting factory output because the factory is from a trusted source
- Bulk-importing generated skills without individual review
- Treating generated skills as lower-risk than hand-written ones
- Allowing factories to auto-install into production agent directories

## Sources

- alirezarezvani/claude-code-skill-factory — Claude Code skill/agent/prompt/hook generator
- yccm/SkillGen — verified inference-time skill synthesis with paired evaluation
- skill-tools/skill-tools — ESLint/Lighthouse-style skill quality toolkit
- claude-code-skill-factory (graphify-corpus source profile)
