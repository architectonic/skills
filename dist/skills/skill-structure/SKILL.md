---
name: Skill Structure
description: Understand the anatomy of an agent skill — directory layout, frontmatter fields, progressive disclosure layers, and bundled resources. Use when designing a new skill, reviewing an existing skill's structure, or deciding what content goes in SKILL.md vs references/.
tags: [skill-management, skill-management, skill-structure, anatomy, frontmatter]
type: Playbook
---

# Skill Structure

Every skill consists of a required SKILL.md file and optional bundled resources.

## Directory Layout

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (required)
│   └── Markdown instructions (required)
└── Bundled Resources (optional)
    ├── scripts/          - Executable code (Python/Bash/etc.)
    ├── references/       - Documentation loaded into context as needed
    └── assets/           - Files used in output (templates, icons, fonts)
```

## Frontmatter Fields

| Field | Required | Notes |
|-------|----------|-------|
| `name` | Yes | Lowercase, hyphens, matches directory name |
| `description` | Yes | Third-person trigger: "This skill should be used when..." |
| `version` | No | Semantic version |

## Progressive Disclosure

1. **Metadata (name + description)** — always in context (~100 words)
2. **SKILL.md body** — loaded when skill triggers (<5k words recommended)
3. **Bundled resources** — loaded as needed (unlimited)

## Bundled Resources

### scripts/
Executable code for deterministic reliability. When the same code is rewritten repeatedly.

### references/
Documentation loaded into context as needed. Use for schemas, API docs, domain knowledge, detailed patterns.

### assets/
Files used in output, not loaded into context. Templates, images, fonts, boilerplate.

## Writing Style

- **Imperative/infinitive form**: "Read the file" not "You should read the file"
- **Third-person description**: "This skill should be used when..." not "Use this skill when..."
- **Lean SKILL.md**: 1,500-2,000 words ideal, <5k max
- **Move detail to references/**: Keep SKILL.md focused on core procedures
