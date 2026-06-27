---
name: skill-quality-gate
description: Validate, lint, and score agent skills before promotion into the skill
  library. Use when evaluating a candidate skill for quality, safety, and completeness.
  Covers schema validation, frontmatter checks, content quality, and scoring dimensions.
tags:
- agent-operations
- skill-management
- quality-gate
- validation
- okf
type: Playbook
title: skill-quality-gate
domain: agent-operations
risk_level: medium
requires_review: true
source_family: agent-skills-standard
source_status: adapted
---

# skill-quality-gate

Validate, lint, and score agent skills before promotion into the skill library.

## When to use

- A candidate skill is proposed for addition to the kit
- An existing skill is being revised or consolidated
- Periodic review of the skill library health

## Validation checks

### Schema validity
- Directory structure follows `<category>/<skill>.md` layout
- File uses `.md` extension
- Frontmatter parses as YAML
- Required fields present: `type`, `title`, `description`, `tags`
- `type` is one of: Skill, Playbook, Policy, Index, Runbook, Source Profile, Decision, Memory Model
- `description` ≤ 1024 characters
- File starts with `---` at byte 0
- Non-empty body after closing `---`

### Frontmatter completeness
- `title` is concise and descriptive
- `description` starts with a verb and explains when to use the skill
- `tags` are lowercase, hyphenated, meaningful
- No agent-specific runtime tags (e.g., `hermes`, `codex`, `cursor`)
- No `timestamp`, `source_status`, `source_name`, `source_runtime` fields (these are provenance metadata, not skill content)

### Content quality
- No hardcoded local paths (e.g., `C:\\Users\alan`, `/home/oai/`)
- No secrets, API keys, tokens, or credentials
- No agent-specific tool references unless the skill is explicitly about that tool
- Trigger conditions are clear and specific
- Procedures are actionable, not vague
- Verification steps are included
- Failure modes or pitfalls are documented

### Content quality analysis (from skill-validator)
- **Word count:** skill body should be 50-500 words (lean main file)
- **Code block ratio:** < 30% of total content (move long scripts to `scripts/`)
- **Imperative ratio:** > 60% of sentences use imperative mood (commands, not descriptions)
- **Information density:** every sentence teaches something (no filler)
- **Instruction specificity:** uses concrete file paths, commands, and examples
- **Section count:** 3-8 sections (enough structure, not too fragmented)
- **Cross-language contamination:** skill doesn't mix unrelated tool ecosystems
- **Internal links resolve:** all relative links point to existing files
- **Token budget:** skill should fit in < 2000 tokens of context window

### Scoring dimensions

| Dimension | Criteria |
|-----------|----------|
| **Trigger clarity** | When to use is unambiguous |
| **Procedure quality** | Steps are concrete, ordered, actionable |
| **Verification** | Success criteria are defined |
| **Safety** | No external mutation without explicit approval |
| **Portability** | Works across agent runtimes |
| **Token efficiency** | No unnecessary verbosity |
| **Progressive disclosure** | Main skill is lean; details in references |
| **Content density** | High information per word |
| **Actionability** | Every step is executable |
| **Novelty** | Adds value beyond existing skills |

## Risk classification

| Class | Effect | Promotion posture |
|-------|--------|-------------------|
| Read-only local | Reads local files or repo context | Medium review |
| Read-only external | Queries external APIs or browser | High review |
| Local mutation | Edits files, runs formatters, changes git state | High review |
| External mutation | Sends email, deploys, trades, posts to cloud | Blocked until harness controls exist |
| Security-sensitive | Credentials, scanners, offensive security, crypto | Blocked by default |

## Promotion gate

Promote only if:
- Schema is valid
- Frontmatter is complete
- Content passes quality checks
- Risk classification is acceptable
- No secrets or hardcoded paths
- Trigger is specific enough to avoid false matches
- Verification steps exist

## Output
## Output
Each evaluated skill gets a receipt:
- Schema: pass/fail
- Quality score per dimension (1-5)
- Risk class
- Promotion decision: `promote` / `revise` / `merge` / `prune` / `block`
- Reviewer notes

## CI integration (from skill-validator)

For automated quality checks in CI pipelines:

```bash
# Install
go install github.com/agent-ecosystem/skill-validator/cmd/skill-validator@latest

# Run all checks on skills directory
skill-validator check skills/ --strict

# Validate structure only
skill-validator validate structure skills/ --strict

# Analyze content quality
skill-validator analyze content skills/

# Score with LLM-as-judge (requires API key)
skill-validator score evaluate skills/ --model gpt-4o
```

Exit codes: 0=pass, 1=errors, 2=warnings, 3=CLI error

## Sources
- agent-ecosystem/skill-validator — structure, content, contamination, link validation
- skill-tools/skill-tools — ESLint/Lighthouse-style quality rules
- skillops-2026 (arxiv) — skill library as software ecosystem with tech debt diagnostics
- SkillOpt (microsoft) — bounded skill text optimization with validation gates
