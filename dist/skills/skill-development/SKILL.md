---
name: Skill Development
description: Create, structure, and maintain effective agent skills. Use when the
  user wants to "create a skill", "add a skill to plugin", "write a new skill", "improve
  skill description", "organize skill content", or needs guidance on skill structure,
  progressive disclosure, or skill development best practices.
tags:
- agent-operations
- skill-management
- skill-creation
- skill-structure
- plugins
- okf
type: Playbook
title: Skill Development
domain: agent-operations
risk_level: medium
requires_review: true
source_family: agent-skills-standard
source_status: adapted
---

# Skill Development

Create effective skills that are compact, discoverable, and progressively disclosed.

## Sub-Skills

| Skill | When to Use |
|-------|-------------|
| [skill-structure](skill-structure.md) | Understand skill anatomy, frontmatter requirements, progressive disclosure layers |
| [skill-creation](skill-creation.md) | Walk through the full skill creation process (steps 1-6) |
| [skill-writing-style](skill-writing-style.md) | Check writing conventions (imperative form, description format, trigger phrases) |
| [skill-validation-checklist](skill-validation-checklist.md) | Validate a skill before publication |

## Core Principles

1. **Progressive disclosure**: metadata → body → resources (never load everything at once)
2. **Lean SKILL.md**: target 1,500-2,000 words; move detail to `references/`
3. **Trigger-first description**: write the description as "Use when..." with specific phrases
4. **Third-person + imperative**: "This skill should be used when..." / "Read the file first."
5. **Working examples**: executable, tested, complete
