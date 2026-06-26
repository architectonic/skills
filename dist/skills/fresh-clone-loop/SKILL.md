---
name: Fresh Clone Loop
description: Onboarding verification loop — clone a repo into a clean environment, follow the README exactly, fix every hidden setup assumption, and repeat until onboarding works from scratch. Use to test whether a repository's README really works for a new contributor.
tags: [loops, onboarding, readme, verification, disposable-environment]
type: Playbook
---

# Fresh Clone Loop

A disposable-environment workflow that follows the README from scratch, fixes every hidden setup assumption, and restarts until onboarding works cleanly.

## When to use

- Test whether a repository's onboarding instructions work for a new contributor
- Onboarding a new agent to a codebase
- Verifying CI-style environment setup
- Finding hidden assumptions in setup documentation

## How to run

1. **Create disposable environment**: No project dependencies or configuration carried over from another checkout.
2. **Fresh-clone**: Clone the repository and follow ONLY the README. Record every missing step, hidden assumption, and failure.
3. **Fix smallest gap**: Fix the setup or documentation to remove the assumption.
4. **Discard and restart**: Destroy the environment completely. Begin again from a fresh clone.
5. **Repeat** until one clean run reaches the running app without intervention.

## Tracking

Keep a short log of each gap and how you closed it, so it does not return:
- Missing prerequisites not stated in README
- Environment assumptions (specific OS tools, version managers)
- Configuration that must exist before setup commands work
- Credential-dependent steps that the README does not mention

## Verify / stop

A clean environment reaches a running app using only the README. The final from-scratch run is uninterrupted and needs no unstated step, preinstalled tool, configuration, or manual repair.

## Why it works

Destroying the environment after each repair prevents local state from hiding the next problem. The final uninterrupted run is direct evidence that the README, not the operator's memory, is sufficient.

## Key rules

- Never carry dependencies, config, credentials, or manual fixes from one attempt to the next
- Fix the smallest change that removes the assumption (don't rewrite the whole README)
- Use isolated disposable environments (containers, worktrees, VMs)
- Never copy personal credentials into the test environment
- Finish with the exact commands a new contributor now runs from scratch
