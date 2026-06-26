---
name: codebase-automation-recommender
description: Analyze a codebase and recommend agent automations (hooks, subagents, skills, MCP servers). Use when the user asks for automation recommendations, wants to optimize their agent setup, mentions improving agent workflows, asks how to first set up an agent for a project, or wants to know what agent features they should use. Adapted from anthropic-claude-plugins-official/claude-automation-recommender.
type: Playbook
---

# Codebase Automation Recommender

Analyze codebase patterns to recommend tailored agent automations across all extensibility options.

**This skill is read-only.** It analyzes the codebase and outputs recommendations. It does NOT create or modify any files. Users implement the recommendations themselves or ask the agent separately to help build them.

## Output Guidelines

- **Recommend 1-2 of each type**: Don't overwhelm — surface the top 1-2 most valuable automations per category.
- **If user asks for a specific type**: Focus only on that type and provide 3-5 recommendations.
- **Go beyond the reference lists**: Use web search to find recommendations specific to the codebase's tools, frameworks, and libraries.
- **Tell users they can ask for more**: End by noting they can request more recommendations for any specific category.

## Automation Types Overview

| Type | Best For |
|------|----------|
| **Hooks** | Automatic actions on tool events (format on save, lint, block edits) |
| **Subagents** | Specialized reviewers/analyzers that run in parallel |
| **Skills** | Packaged expertise, workflows, and repeatable tasks |
| **Plugins** | Collections of skills that can be installed |
| **MCP Servers** | External tool integrations (databases, APIs, browsers, docs) |

## Workflow

### Phase 1: Codebase Analysis

Gather project context:

```bash
# Detect project type and tools
ls -la package.json pyproject.toml Cargo.toml go.mod pom.xml 2>/dev/null
cat package.json 2>/dev/null | head -50

# Check dependencies for MCP server recommendations
cat package.json 2>/dev/null | grep -E '"(react|vue|angular|next|express|fastapi|django|prisma|supabase|convex|stripe)"'

# Check for existing agent config
ls -la .hermes/ AGENTS.md CLAUDE.md 2>/dev/null

# Analyze project structure
ls -la src/ app/ lib/ tests/ components/ pages/ api/ 2>/dev/null
```

**Key Indicators to Capture:**

| Category | What to Look For | Informs Recommendations For |
|----------|------------------|----------------------------|
| Language/Framework | package.json, pyproject.toml, import patterns | Hooks, MCP servers, skills |
| Frontend stack | React, Vue, Angular, Next.js | Playwright MCP, frontend skills |
| Backend stack | Express, FastAPI, Django | API documentation tools |
| Database | Prisma, Supabase, Convex, raw SQL | Database MCP servers |
| External APIs | Stripe, OpenAI, AWS SDKs | context7 MCP for docs |
| Testing | Jest, pytest, Playwright configs | Testing hooks, subagents |
| CI/CD | GitHub Actions, CircleCI | GitHub MCP server |
| Issue tracking | Linear, Jira references | Issue tracker MCP |
| Docs patterns | OpenAPI, JSDoc, docstrings | Documentation skills |

### Phase 2: Generate Recommendations

Based on analysis, generate recommendations across all categories:

#### A. MCP Server Recommendations

| Codebase Signal | Recommended MCP Server |
|-----------------|------------------------|
| Uses popular libraries (React, Express, etc.) | **context7** — Live documentation lookup |
| Frontend with UI testing needs | **Playwright** — Browser automation/testing |
| Uses Supabase | **Supabase MCP** — Direct database operations |
| Uses Convex | **Convex MCP** — Live deployment introspection |
| PostgreSQL/MySQL database | **Database MCP** — Query and schema tools |
| GitHub repository | **GitHub MCP** — Issues, PRs, actions |
| Uses Linear for issues | **Linear MCP** — Issue management |
| AWS infrastructure | **AWS MCP** — Cloud resource management |
| Slack workspace | **Slack MCP** — Team notifications |
| Memory/context persistence | **Memory MCP** — Cross-session memory |
| Sentry error tracking | **Sentry MCP** — Error investigation |
| Docker containers | **Docker MCP** — Container management |

#### B. Skills Recommendations

| Codebase Signal | Skill to Create | Invocation |
|-----------------|-----------------|------------|
| API routes | **api-doc** (with OpenAPI template) | Both |
| Database project | **create-migration** (with validation script) | User-only |
| Test suite | **gen-test** (with example tests) | User-only |
| Component library | **new-component** (with templates) | User-only |
| PR workflow | **pr-check** (with checklist) | User-only |
| Releases | **release-notes** (with git context) | User-only |
| Code style | **project-conventions** | Agent-only |
| Onboarding | **setup-dev** (with prereq script) | User-only |

#### C. Hooks Recommendations

| Codebase Signal | Recommended Hook |
|-----------------|------------------|
| Prettier configured | PostToolUse: auto-format on edit |
| ESLint/Ruff configured | PostToolUse: auto-lint on edit |
| TypeScript project | PostToolUse: type-check on edit |
| Tests directory exists | PostToolUse: run related tests |
| `.env` files present | PreToolUse: block `.env` edits |
| Lock files present | PreToolUse: block lock file edits |
| Security-sensitive code | PreToolUse: require confirmation |

#### D. Subagent Recommendations

| Codebase Signal | Recommended Subagent |
|-----------------|---------------------|
| Large codebase (>500 files) | **code-reviewer** — Parallel code review |
| Auth/payments code | **security-reviewer** — Security audits |
| API project | **api-documenter** — OpenAPI generation |
| Performance critical | **performance-analyzer** — Bottleneck detection |
| Frontend heavy | **ui-reviewer** — Accessibility review |
| Needs more tests | **test-writer** — Test generation |

### Phase 3: Output Recommendations Report

Format recommendations clearly. **Only include 1-2 recommendations per category** — the most valuable ones for this specific codebase. Skip categories that aren't relevant.

```markdown
## Agent Automation Recommendations

I've analyzed your codebase and identified the top automations for each category.

### Codebase Profile
- **Type**: [detected language/runtime]
- **Framework**: [detected framework]
- **Key Libraries**: [relevant libraries detected]

---

### 🔌 MCP Servers

#### context7
**Why**: [specific reason based on detected libraries]
**Install**: `claude mcp add context7` (or equivalent for your agent runtime)

---

### 🎯 Skills

#### [skill name]
**Why**: [specific reason]
**Create**: `skills/<category>/<name>.md`

---

### ⚡ Hooks

#### [hook name]
**Why**: [specific reason based on detected config]

---

### 🤖 Subagents

#### [agent name]
**Why**: [specific reason based on codebase patterns]

---

**Want more?** Ask for additional recommendations for any specific category.
```

## Decision Framework

### When to Recommend MCP Servers
- External service integration needed (databases, APIs)
- Documentation lookup for libraries/SDKs
- Browser automation or testing
- Team tool integration (GitHub, Linear, Slack)
- Cloud infrastructure management

### When to Recommend Skills
- Frequently repeated prompts or workflows
- Project-specific tasks with arguments
- Applying templates or scripts to tasks
- Quick actions invoked by the agent
- Workflows that should run in isolation

### When to Recommend Hooks
- Repetitive post-edit actions (formatting, linting)
- Protection rules (block sensitive file edits)
- Validation checks (tests, type checks)

### When to Recommend Subagents
- Specialized expertise needed (security, performance)
- Parallel review workflows
- Background quality checks

## Source

Adapted from: `anthropic-claude-plugins-official/plugins/claude-code-setup/skills/claude-automation-recommender/SKILL.md`
Original license: MIT
