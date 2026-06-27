---
name: Skill Writing Style
description: Follow writing conventions for agent skills — imperative voice, third-person
  description, trigger phrases, and progressive disclosure. Use when writing or reviewing
  any skill document.
tags:
- writing
- skill-management
- writing-style
- conventions
- voice
- okf
type: Playbook
title: Skill Writing Style
domain: writing
risk_level: medium
requires_review: true
source_family: agent-skills-standard
source_status: adapted
---

# Skill Writing Style

Conventions for skill documents that agents can parse and use effectively.

## Description (Frontmatter)

**Third person with trigger phrases:**
```yaml
description: This skill should be used when the user asks to "create a hook", "add a PreToolUse hook", "validate tool use", or mentions hook events.
```

**Bad examples:**
- `Use this skill when working with hooks.` — wrong person, vague
- `Load when user needs hook help.` — not third person
- `Provides hook guidance.` — no trigger phrases

## Body Content

**Imperative/infinitive form (verb-first):**
```
Read the configuration file.
Validate the input before processing.
Use the grep tool to search for patterns.
```

**NOT second person:**
```
You should read the configuration file.
You need to validate the input.
You can use the grep tool.
```

## Objective Language

Focus on what to do, not who should do it:
```
Parse the frontmatter using sed.
Extract fields with grep.
Validate values before use.
```

NOT:
```
You can parse the frontmatter...
Claude should extract fields...
The user might validate values...
```

## Progressive Disclosure

**SKILL.md (always loaded when skill triggers):**
- Core concepts and overview
- Essential procedures and workflows
- Quick reference tables
- Pointers to references/examples/scripts
- Most common use cases

**references/ (loaded as needed):**
- Detailed patterns and advanced techniques
- Comprehensive API documentation
- Migration guides
- Edge cases and troubleshooting
- Extensive examples and walkthroughs

**examples/ (working code):**
- Complete, runnable scripts
- Configuration files
- Template files
- Real-world usage examples

**scripts/ (utilities):**
- Validation tools
- Testing helpers
- Parsing utilities
- Automation scripts
