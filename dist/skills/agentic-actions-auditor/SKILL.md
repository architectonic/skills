---
name: agentic-actions-auditor
description: "Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations (Claude Code Action, Gemini CLI, OpenAI Codex, GitHub AI Inference). Detects 9 attack vectors where attacker-controlled input reaches AI agents in CI/CD pipelines. Use when reviewing workflow files that invoke AI coding agents, auditing CI/CD pipeline security for prompt injection risks, or evaluating agentic action configurations."
source: trailofbits-skills (MIT license, https://github.com/trailofbits/skills — plugins/agentic-actions-auditor/skills/agentic-actions-auditor/SKILL.md)
category: software-development
tags: [agent-operations, security, ci-cd, github-actions, ai-agent, prompt-injection, static-analysis]
type: Playbook
domain: security-defensive
risk_level: medium
requires_review: true
source_family: trailofbits-skills
source_license: MIT
source_status: adapted
---

# Agentic Actions Auditor

Static security analysis for GitHub Actions workflows that invoke AI coding agents. Detects attack vectors where attacker-controlled input reaches an AI agent running in CI/CD.

## When to Use

- Auditing a repository's GitHub Actions workflows for AI agent security
- Reviewing CI/CD configurations that invoke Claude Code Action, Gemini CLI, or OpenAI Codex
- Checking whether attacker-controlled input can reach AI agent prompts
- Evaluating agentic action configurations (sandbox settings, tool permissions, user allowlists)
- Assessing trigger events that expose workflows to external input (`pull_request_target`, `issue_comment`, etc.)

## When NOT to Use

- Analyzing workflows that do NOT use any AI agent actions
- Runtime prompt injection testing (this is static analysis only)
- Auditing non-GitHub CI/CD systems (Jenkins, GitLab CI, CircleCI)
- Auto-fixing or modifying workflow files (reports findings only)

## Rationalizations to Reject

| Rationalization | Why It's Wrong |
|-----------------|----------------|
| "It only runs on PRs from maintainers" | `pull_request_target` and `issue_comment` expose actions to any external contributor |
| "We use allowed_tools to restrict what it can do" | Even `echo` can exfiltrate via `echo $(env)`. Limited tools != safe tools. |
| "There's no ${{ }} in the prompt, so it's safe" | Env var intermediary pattern: data flows through `env:` blocks with zero visible expressions |
| "The sandbox prevents any real damage" | `danger-full-access`, `Bash(*)`, `--yolo` disable protections entirely |

## Audit Methodology

### Step 0: Determine Analysis Mode

**Local mode:** Scan `.github/workflows/*.yml` and `.github/workflows/*.yaml` in the local repo.

**Remote mode:** If given a `owner/repo` or GitHub URL, fetch workflows via `gh api`:
```bash
gh api repos/{owner}/{repo}/contents/.github/workflows --paginate --jq '.[].name'
gh api repos/{owner}/{repo}/contents/.github/workflows/{filename} --jq '.content | @base64d'
```

### Step 1: Identify AI Action Steps

Check each step's `uses:` field against known AI action references:

| Action Reference | Type |
|-----------------|------|
| `anthropics/claude-code-action` | Claude Code Action |
| `google-github-actions/run-gemini-cli` | Gemini CLI |
| `google-gemini/gemini-cli-action` | Gemini CLI (legacy) |
| `openai/codex-action` | OpenAI Codex |
| `actions/ai-inference` | GitHub AI Inference |

Also resolve cross-file references: local composite actions (`./path/to/action`) and job-level reusable workflows (one level deep).

### Step 2: Capture Security Context

For each AI action step, capture:

**Step-level config** (`with:` block):
- Claude: `prompt`, `claude_args`, `allowed_non_write_users`, `allowed_bots`, `settings`
- Gemini: `prompt`, `settings`, `gemini_model`, `extensions`
- Codex: `prompt`, `prompt-file`, `sandbox`, `safety-strategy`, `allow-users`, `allow-bots`

**Workflow-level context:**
- Trigger events: flag `pull_request_target`, `issue_comment`, `issues` as security-relevant
- Environment variables: check all `env:` blocks for `${{ github.event.* }}` expressions
- Permissions: flag overly broad `contents: write`, `pull-requests: write` combined with AI agents

### Step 3: Analyze for Attack Vectors

| Vector | Name | Quick Check |
|--------|------|-------------|
| A | Env Var Intermediary | `env:` block with `${{ github.event.* }}` + prompt reads that env var |
| B | Direct Expression Injection | `${{ github.event.* }}` inside prompt or system-prompt field |
| C | CLI Data Fetch | `gh issue view`, `gh pr view`, or `gh api` commands in prompt text |
| D | PR Target + Checkout | `pull_request_target` trigger + checkout with `ref:` pointing to PR head |
| E | Error Log Injection | CI logs, build output, or `workflow_dispatch` inputs passed to AI prompt |
| F | Subshell Expansion | Tool restriction list includes commands supporting `$()` expansion |
| G | Eval of AI Output | `eval`, `exec`, or `$()` in `run:` step consuming `steps.*.outputs.*` |
| H | Dangerous Sandbox Configs | `danger-full-access`, `Bash(*)`, `--yolo`, `safety-strategy: unsafe` |
| I | Wildcard Allowlists | `allowed_non_write_users: "*"`, `allow-users: "*"` |

Vectors H and I are configuration weaknesses that amplify co-occurring injection vectors (A–G). Without a co-occurring injection vector, they are Info/Low severity.

### Step 4: Report Findings

Each finding includes:
- **Title:** Vector name (e.g., "Env Var Intermediary")
- **Severity:** High / Medium / Low / Low / Info (context-dependent)
- **File:** Workflow file path with line reference
- **Impact:** One sentence stating what an attacker can achieve
- **Evidence:** YAML code snippet showing the vulnerable pattern
- **Data Flow:** Numbered trace from attacker-controlled source to AI agent consequence
- **Remediation:** Action-specific guidance

**Severity factors:** Trigger event exposure, sandbox/tool config, user allowlist scope, data flow directness, permissions/secrets exposure, execution context trust.

**Report structure:**
1. Executive summary: `Analyzed X workflows containing Y AI action instances. Found Z findings: N High, M Medium, P Low, Q Info.`
2. Summary table: Workflow File | Findings | Highest Severity
3. Findings grouped by workflow, ordered by severity descending

## Quality Checklist

- [ ] All workflow files in `.github/workflows/` scanned
- [ ] All AI action steps identified (including cross-file references)
- [ ] All 9 attack vectors checked against each AI action instance
- [ ] Data flow traces start from attacker-controlled source (not YAML line)
- [ ] Severity justified by context (not just vector type)
- [ ] Remediation guidance is actionable
