---
name: Skill Validation Checklist
description: Validate a skill before publication. Use when reviewing a skill for structure, description quality, content organization, progressive disclosure, and common mistakes.
tags: [skill-management, skill-management, validation, quality, review]
type: Playbook
---

# Skill Validation Checklist

Before publishing or promoting any skill, verify:

## Structure
- [ ] SKILL.md exists with valid YAML frontmatter
- [ ] Frontmatter has `name` and `description` fields
- [ ] Markdown body is present and substantial
- [ ] Referenced files actually exist

## Description Quality
- [ ] Uses third person ("This skill should be used when...")
- [ ] Includes specific trigger phrases users would say
- [ ] Lists concrete scenarios ("create X", "configure Y")
- [ ] Not vague or generic

## Content Quality
- [ ] SKILL.md body uses imperative/infinitive form
- [ ] Body is focused and lean (1,500-2,000 words ideal, <5k max)
- [ ] Detailed content moved to references/
- [ ] Examples are complete and working
- [ ] Scripts are executable and documented

## Progressive Disclosure
- [ ] Core concepts in SKILL.md
- [ ] Detailed docs in references/
- [ ] Working code in examples/
- [ ] Utilities in scripts/
- [ ] SKILL.md references these resources

## Testing
- [ ] Skill triggers on expected user queries
- [ ] Content is helpful for intended tasks
- [ ] No duplicated information across files
- [ ] References load when needed

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Weak trigger description: "Provides guidance for X" | Add specific phrases: "when user asks to 'create X', 'configure Y'" |
| Everything in SKILL.md (>3,000 words) | Move detail to references/, keep core in SKILL.md |
| Second person: "You should..." | Imperative: "Read the file..." |
| Missing resource references | Add "Additional Resources" section in SKILL.md |
| Vague: "Use this skill when working with X" | Concrete: "Use when user asks to 'X', 'Y', 'Z'" |
