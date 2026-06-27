---
name: skill-creation
title: Skill Creation Process
description: Six steps to create an effective skill.
type: Playbook
domain: agent-operations
tags:
- agent-operations
- okf
risk_level: medium
requires_review: false
---

# Skill Creation Process

Six steps to create an effective skill.

## Step 1: Understand with Concrete Examples

Identify specific usage scenarios. Ask:
- "What should the skill support?"
- "What would a user say that should trigger this skill?"
- "What scripts/references/assets would help?"

Conclude when you have concrete examples.

## Step 2: Plan Reusable Resources

For each example:
1. Consider executing from scratch
2. Identify which scripts, references, and assets would help
3. Plan the `scripts/`, `references/`, and `assets/` contents

## Step 3: Create Structure

```bash
mkdir -p skills/skill-name/{references,examples,scripts}
touch skills/skill-name/SKILL.md
```

## Step 4: Write

**SKILL.md body — answer these questions:**
1. What is the purpose?
2. When should it be used?
3. How should the agent use it (reference resources)?

**Reference resources in SKILL.md:**
```markdown
## Additional Resources
### Reference Files
- `references/patterns.md` — Detailed patterns
### Examples
- `examples/script.sh` — Working example
```

## Step 5: Validate and Test

- [ ] SKILL.md exists with valid frontmatter
- [ ] Description uses third person with trigger phrases
- [ ] Body uses imperative/infinitive form
- [ ] SKILL.md is lean (1,500-2,000 words)
- [ ] Referenced files exist
- [ ] Examples are complete and correct
- [ ] Scripts are executable

## Step 6: Iterate

After using the skill on real tasks:
1. Notice struggles or inefficiencies
2. Identify updates to SKILL.md or resources
3. Implement changes and test again

**Common improvements:**
- Strengthen trigger phrases
- Move long sections to references/
- Add missing examples or scripts
- Clarify ambiguous instructions
