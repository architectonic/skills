---
name: Resolving Merge Conflicts
description: Use when you need to resolve an in-progress git merge/rebase conflict. Provides a disciplined approach to understanding both sides of a conflict and resolving it without losing intent.
source: mattpocock/skills (MIT license, https://github.com/mattpocock/skills)
category: software-development
tags: [software-development, git, merge, rebase, conflict-resolution, version-control]
type: Playbook
---

# Resolving Merge Conflicts

## Overview

Merge conflicts are not errors — they're a signal that two changes need to be reconciled. This skill provides a disciplined approach to understanding both sides of a conflict and resolving it without losing intent.

## When to Use

- You encounter a git merge or rebase conflict
- You need to reconcile divergent branches
- A rebase is in progress with conflicting commits

## Process

### 1. See the Current State

Check git history and the conflicting files:

```bash
git status                    # See which files conflict
git log --oneline --graph     # Understand the branch structure
git diff --name-only --diff-filter=U  # List unmerged files
```

### 2. Find the Primary Sources for Each Conflict

Understand deeply why each change was made, and what the original intent was:

```bash
git log --all --oneline -- <file>     # History of the conflicting file
git show <commit>                      # See what a specific commit changed
# Check PRs, issues, tickets referenced in commit messages
```

Don't just look at the conflict markers — understand the *intent* behind each side.

### 3. Resolve Each Hunk

- **Preserve both intents where possible.** Most conflicts can be resolved by keeping both changes.
- **Where incompatible, pick the one matching the merge's stated goal** and note the trade-off.
- **Do NOT invent new behaviour.** You're reconciling existing changes, not adding new ones.
- **Always resolve; never `--abort`.** If you're stuck, ask for help rather than aborting.

For each conflict hunk:
```
1. Read both sides of the conflict marker
2. Understand what each side was trying to achieve
3. Determine if both can coexist or if one must win
4. Write the resolved code (removing all conflict markers)
5. Verify the resolved code makes sense in context
```

### 4. Run Automated Checks

Discover the project's automated checks and run them — typically typecheck, then tests, then format. Fix anything the merge broke:

```bash
# Common checks (adapt to the project)
npm run typecheck    # or: tsc --noEmit
npm test
npm run lint
```

### 5. Finish the Merge/Rebase

```bash
# For merges:
git add <resolved-files>
git commit  # Use the default merge commit message or improve it

# For rebases:
git add <resolved-files>
git rebase --continue
# Continue until all commits are rebased
```

## Red Flags

- Resolving a conflict without understanding both sides
- Choosing "theirs" or "ours" blindly for the entire file
- Aborting a merge/rebase because conflicts are hard
- Not running tests after resolving conflicts
- Leaving conflict markers in committed code
- Inventing new behavior during conflict resolution
