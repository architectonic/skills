---
name: agents-md-improver
description: Audit and improve AGENTS.md / CLAUDE.md / SOUL.md files in repositories. Use when the user asks to check, audit, update, improve, or fix agent instruction files. Scans for all agent instruction files, evaluates quality against a rubric, outputs quality report, then makes targeted updates. Also use when the user mentions "agent instruction maintenance", "project memory optimization", or "rules file audit". Adapted from anthropic-claude-plugins-official/claude-md-improver.
type: Playbook
domain: agent-operations
risk_level: medium
requires_review: true
source_family: anthropic-claude-plugins-official
source_license: MIT
source_status: adapted
---

# Agent Instruction File Improver

Audit, evaluate, and improve agent instruction files (AGENTS.md, CLAUDE.md, SOUL.md, MEMORY.md) across a codebase to ensure agents have optimal project context.

**This skill can write to instruction files.** After presenting a quality report and getting user approval, it updates files with targeted improvements.

## Workflow

### Phase 1: Discovery

Find all agent instruction files in the repository:

```bash
find . -name "AGENTS.md" -o -name "CLAUDE.md" -o -name "SOUL.md" -o -name ".claude.md" -o -name ".claude.local.md" -o -name ".cursorrules" 2>/dev/null | head -50
```

**File Types & Locations:**

| Type | Location | Purpose |
|------|----------|---------|
| Project root | `./AGENTS.md` | Primary project context (checked into git, shared with team) |
| Hermes profile | `~/.hermes/profiles/<name>/AGENTS.md` | Profile-specific rules |
| Local overrides | `./.claude.local.md` | Personal/local settings (gitignored, not shared) |
| Global defaults | `~/.hermes/AGENTS.md` | User-wide defaults across all projects |
| Package-specific | `./packages/*/AGENTS.md` | Module-level context in monorepos |
| Subdirectory | Any nested location | Feature/domain-specific context |

### Phase 2: Quality Assessment

For each instruction file, evaluate against quality criteria.

**Quick Assessment Checklist:**

| Criterion | Weight | Check |
|-----------|--------|-------|
| Commands/workflows documented | High | Are build/test/deploy commands present? |
| Architecture clarity | High | Can the agent understand the codebase structure? |
| Non-obvious patterns | Medium | Are gotchas and quirks documented? |
| Conciseness | Medium | No verbose explanations or obvious info? |
| Currency | High | Does it reflect current codebase state? |
| Actionability | High | Are instructions executable, not vague? |
| Source hierarchy | High | Does it define what overrides what? |

**Quality Scores:**

- **A (90-100)**: Comprehensive, current, actionable
- **B (70-89)**: Good coverage, minor gaps
- **C (50-69)**: Basic info, missing key sections
- **D (30-49)**: Sparse or outdated
- **F (0-29)**: Missing or severely outdated

### Phase 3: Quality Report Output

**ALWAYS output the quality report BEFORE making any updates.**

Format:

```
## Agent Instruction Quality Report

### Summary
- Files found: X
- Average score: X/100
- Files needing update: X

### File-by-File Assessment

#### 1. ./AGENTS.md (Project Root)
**Score: XX/100 (Grade: X)**

| Criterion | Score | Notes |
|-----------|-------|-------|
| Commands/workflows | X/20 | ... |
| Architecture clarity | X/20 | ... |
| Non-obvious patterns | X/15 | ... |
| Conciseness | X/15 | ... |
| Currency | X/15 | ... |
| Actionability | X/15 | ... |

**Issues:**
- [List specific problems]

**Recommended additions:**
- [List what should be added]
```

### Phase 4: Targeted Updates

After outputting the quality report, ask user for confirmation before updating.

**Update Guidelines (Critical):**

1. **Propose targeted additions only** — Focus on genuinely useful info:
   - Commands or workflows discovered during analysis
   - Gotchas or non-obvious patterns found in code
   - Package relationships that weren't clear
   - Testing approaches that work
   - Configuration quirks

2. **Keep it minimal** — Avoid:
   - Restating what's obvious from the code
   - Generic best practices already covered
   - One-off fixes unlikely to recur
   - Verbose explanations when a one-liner suffices

3. **Show diffs** — For each change, show:
   - Which file to update
   - The specific addition (as a diff or quoted block)
   - Brief explanation of why this helps future sessions

### Phase 5: Apply Updates

After user approval, apply changes. Preserve existing content structure.

## Common Issues to Flag

1. **Stale commands**: Build commands that no longer work
2. **Missing dependencies**: Required tools not mentioned
3. **Outdated architecture**: File structure that's changed
4. **Missing environment setup**: Required env vars or config
5. **Broken test commands**: Test scripts that have changed
6. **Undocumented gotchas**: Non-obvious patterns not captured
7. **Missing source hierarchy**: No clear ordering of what overrides what

## What Makes a Great Agent Instruction File

**Key principles:**
- Concise and human-readable
- Actionable commands that can be copy-pasted
- Project-specific patterns, not generic advice
- Non-obvious gotchas and warnings
- Clear source hierarchy (what overrides what)

**Recommended sections** (use only what's relevant):
- Commands (build, test, dev, lint)
- Architecture (directory structure)
- Key Files (entry points, config)
- Code Style (project conventions)
- Environment (required vars, setup)
- Testing (commands, patterns)
- Gotchas (quirks, common mistakes)
- Workflow (when to do what)
- Source Hierarchy (what overrides what)
- Privacy (what not to record)

## Source

Adapted from: `anthropic-claude-plugins-official/plugins/claude-md-management/skills/claude-md-improver/SKILL.md`
Original license: MIT
