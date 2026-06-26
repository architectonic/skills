---
name: git-worktree-manager
description: Run parallel feature work safely with Git worktrees. Standardizes branch isolation, port allocation, environment sync, and cleanup so each worktree behaves like an independent local app. Optimized for multi-agent workflows where each agent or terminal session owns one worktree. Use when running multiple feature branches simultaneously, isolating experimental work, or coordinating multi-agent development across the same repo.
type: Playbook
---

# Git Worktree Manager

Run parallel feature work safely with Git worktrees. Standardizes branch isolation, port allocation, environment sync, and cleanup so each worktree behaves like an independent local app.

**Source:** claude-skills/engineering/git-worktree-manager/SKILL.md (Apache-2.0)

This skill is optimized for multi-agent workflows where each agent or terminal session owns one worktree.

## Core Capabilities

- Create worktrees from new or existing branches with deterministic naming
- Auto-allocate non-conflicting ports per worktree and persist assignments
- Copy local environment files (`.env*`) from main repo to new worktree
- Optionally install dependencies based on lockfile detection
- Detect stale worktrees and uncommitted changes before cleanup
- Identify merged branches and safely remove outdated worktrees

## When to Use

- You need 2+ concurrent branches open locally
- You want isolated dev servers for feature, hotfix, and PR validation
- You are working with multiple agents that must not share a branch
- Your current branch is blocked but you need to ship a quick fix now
- You want repeatable cleanup instead of ad-hoc `rm -rf` operations

## Key Workflows

### 1. Create a Fully-Prepared Worktree

```bash
python scripts/worktree_manager.py \
  --repo . \
  --branch feature/new-auth \
  --name wt-auth \
  --base-branch main \
  --install-deps \
  --format text
```

For JSON automation:
```bash
python scripts/worktree_manager.py --input config.json --format json
```

### 2. Run Parallel Sessions

- Main repo: integration branch (`main`/`develop`) on default port
- Worktree A: feature branch + offset ports
- Worktree B: hotfix branch + next offset

Each worktree contains `.worktree-ports.json` with assigned ports.

### 3. Cleanup with Safety Checks

```bash
python scripts/worktree_cleanup.py --repo . --stale-days 14 --format text
python scripts/worktree_cleanup.py --repo . --remove-merged --format text
```

### 4. Port Allocation Strategy

Default: `base + (index * stride)` with collision checks:
- App: `3000`, Postgres: `5432`, Redis: `6379`, Stride: `10`

## Decision Matrix

| Need | Action |
|---|---|
| Isolated dependencies and server ports | Create a new worktree |
| Quick local diff review | Stay on current tree |
| Hotfix while feature branch is dirty | Create dedicated hotfix worktree |
| Ephemeral reproduction bug triage | Create temporary worktree, cleanup same day |

## Common Pitfalls

1. Creating worktrees inside the main repo directory
2. Reusing `localhost:3000` across all branches
3. Sharing one database URL across isolated feature branches
4. Removing a worktree with uncommitted changes
5. Forgetting to prune old metadata after branch deletion
6. Assuming merged status without checking against the target branch

## Best Practices

1. One branch per worktree, one agent per worktree
2. Keep worktrees short-lived; remove after merge
3. Use deterministic naming pattern (`wt-<topic>`)
4. Persist port mappings in file, not memory
5. Run cleanup scan weekly in active repos
6. Use `--format json` for machine flows and `--format text` for human review
7. Never force-remove dirty worktrees unless changes are intentionally discarded

## Validation Checklist

**Before creation:**
1. Main repo has clean baseline or intentional WIP commits
2. Target branch naming convention confirmed
3. No reserved local ports occupied by non-repo services

**After creation:**
1. `git worktree list` shows expected path + branch
2. `.worktree-ports.json` exists with unique ports
3. App boots on allocated port

**Before removal:**
1. Branch has upstream and is merged when intended
2. No uncommitted files remain
3. No running containers/processes depend on this worktree path
