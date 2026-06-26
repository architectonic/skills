---
name: ci-fix-workflow
description: Debug and fix failing GitHub PR checks (GitHub Actions) using gh CLI. Use when PR checks are failing and the user wants to inspect logs, understand failures, and apply fixes with explicit approval before implementing.
tags: [devops, github, ci, actions, debugging, pr-checks]
source: openai/skills gh-fix-ci
type: Playbook
---

# CI Fix Workflow

Debug and fix failing GitHub PR checks (GitHub Actions only) using `gh` CLI.

## When to use
- PR checks are failing and the user wants to understand why
- User wants a fix plan before implementing changes
- External providers (Buildkite, etc.) are out of scope — report only the details URL

## Prerequisites
- `gh` CLI authenticated with repo + workflow scopes
- Run `gh auth status` to verify

## Workflow

### 1. Resolve the PR
```bash
# Current branch PR
gh pr view --json number,url

# Or use explicit PR number/URL
```

### 2. Inspect failing checks
```bash
# Preferred: bundled script (handles field drift and job-log fallbacks)
python scripts/inspect_pr_checks.py --repo . --pr <number-or-url>

# Machine-readable output
python scripts/inspect_pr_checks.py --repo . --pr <number-or-url> --json

# Manual fallback
gh pr checks <pr> --json name,state,bucket,link,startedAt,completedAt,workflow
```

For each failing check, extract the run ID and fetch logs:
```bash
gh run view <run_id> --json name,workflowName,conclusion,status,url
gh run view <run_id> --log
```

### 3. Scope non-GitHub Actions checks
- If `detailsUrl` is not a GitHub Actions run, label it as external
- Only report the URL — do not attempt Buildkite or other providers

### 4. Summarize failures
For each failing check, provide:
- Failing check name
- Run URL (if any)
- Concise log snippet
- Missing logs explicitly called out

### 5. Create a fix plan
- Draft a concise plan and request approval before implementing
- If a plan-oriented skill is available, use it

### 6. Implement after approval
- Apply the approved plan
- Summarize diffs/tests
- Ask about opening a PR

### 7. Recheck status
```bash
gh pr checks <pr>
```

## Guardrails
- Always get explicit user approval before implementing fixes
- Only inspect GitHub Actions logs — external CI providers are read-only
- Summarize before acting; never implement without a plan
