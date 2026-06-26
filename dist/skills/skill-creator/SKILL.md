---
name: skill-creator
description: Create, improve, test, and optimize skills. Use when the user wants a new skill, wants to revise an existing skill, wants help with skill structure or trigger wording, or wants to validate a skill against realistic examples.
tags: [skill-management, agent-skill]
type: Playbook
---

# skill-creator

Use this skill to build skills that actually help future agent runs.

## Core workflow
1. Capture intent: what the skill should do, when it should trigger, and what output is expected.
2. Decide the right level of detail: keep the main instructions lean and move supporting material into references, scripts, or assets when needed.
3. Write a clear name and a strong description that includes both what the skill does and when to use it.
4. Keep instructions in imperative form and avoid unnecessary explanation.
5. Add examples, templates, or helper scripts only when they materially improve reliability.
6. Validate the skill against realistic prompts or artifacts.
7. Iterate from feedback and observed failure modes.

## Skill writing rules
- Put the trigger logic in the description, not only in the body.
- Keep the main skill body focused on procedure, judgment, and guardrails.
- Move detailed documentation, schemas, and long examples into references.
- Put executable helpers into scripts when the same steps repeat or need deterministic output.
- Preserve user-provided wording verbatim when they explicitly ask for exact text.

## Validation workflow
When the skill is concrete enough to test:
1. Write realistic prompts or artifacts that match real user requests.
2. Run the skill on those prompts and compare output quality.
3. Check whether the skill triggers too often or too rarely.
4. Tighten the description if the skill under-triggers.
5. Keep iterating until the skill generalizes beyond the first example set.

## Good practices
- Prefer concrete triggers over vague ones.
- Keep the skill focused on one domain or one workflow family.
- Move repetitive or fragile logic into deterministic scripts.
- Keep references one level deep and easy to find.
- Use concise examples that teach the pattern without bloating the skill.

## Authoring guidance
- Ask what the skill should enable, when it should trigger, and what the expected output should look like.
- Ask for edge cases, dependencies, and example inputs when the workflow is fragile.
- Use the smallest amount of structure that still makes the skill reliable.
- If the user already has a draft, improve that draft instead of rewriting the workflow from scratch.

## Common mistakes
- Overwriting user intent with generic advice.
- Making the skill too long or too broad.
- Mixing process notes with the actual skill body.
- Leaving unclear triggers or unsupported edge cases.

## Safety and quality gates
Before promoting a skill, run the skill-quality-gate:

1. **Schema check:** Valid YAML frontmatter, required fields present, no agent-specific runtime tags.
2. **Content check:** No hardcoded local paths, no secrets/keys/tokens, no agent-specific tool references unless the skill is about that tool.
3. **Trigger check:** Description starts with a verb, explains when to use, specific enough to avoid false matches.
4. **Risk classification:** Classify as read-only-local, read-only-external, local-mutation, external-mutation, or security-sensitive. Block external-mutation and security-sensitive by default.
5. **Verification check:** Skill includes verification steps and failure modes.
6. **Portability check:** Works across agent runtimes, not tied to a specific agent's tool names.

## Provenance requirements
Every skill must include:
- Source attribution (which upstream sources support this entry)
- License status (can we redistribute this?)
- Divergence notes (what was changed from upstream)
- Risk level (low/medium/high based on tool powers)

## Promotion decision
| Decision | Meaning |
|----------|---------|
| `promote` | Skill has clear net utility and bounded permissions |
| `revise` | Skill has useful signal but weak wording, excessive scope, or missing gates |
| `merge` | Skill duplicates an existing skill family — merge into the representative |
| `prune` | Skill is stale, redundant, or no longer improves outcomes |
| `block` | Skill is unsafe, unlicensed, unverifiable, or too mutation-heavy |
