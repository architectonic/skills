---
name: Project Onboarding
description: Onboard an existing repository with the Agent Memory Ops Kit. Use when adding the kit to a new project, setting up agent context for a repo, or establishing the initial operating memory for a codebase.
tags: [agent-operations, agent-operations, onboarding, setup, repo-contract]
type: Playbook
---

# Project Onboarding

## Purpose

Add the Agent Memory Ops Kit to an existing repository in a way that gives future agents the context they need to work safely and coherently.

## Trigger

Use when:
- Adding the kit to a new repository
- Setting up agent context for an unfamiliar project
- Establishing initial operating memory for a codebase

## Procedure

1. **Read the repository README and top-level docs.**
   - Understand what the project does, who uses it, and how it's structured.

2. **Identify key artifacts.**
   - Package manifests, build scripts, test scripts, deployment config.
   - Note their locations for the repo contract.

3. **Fill in `repo_contract.md`.**
   - Project identity, source-of-truth locations, agent permissions, done criteria, non-goals.
   - Only record what is supported by source artifacts or human confirmation.

4. **Add known decisions to `decision_log.md`.**
   - Only when supported by source or human confirmation. No guessing.

5. **Add current work state to `handoff_log.md`.**
   - Only when useful for continuation.

6. **Customize `qa_gauntlet.md`.**
   - Add actual project commands (build, test, lint, deploy).

7. **Customize `security_review.md`.**
   - Adjust for the project's specific risk profile.

8. **Remove files that do not apply.**
   - If a template has no relevant content, remove it rather than leaving it empty.

## Output

The onboarded repo should answer:
- What the project is
- How to run it
- How to test it
- What the agent may change
- What the agent must not touch without permission
- Where decisions and handoffs live

## Avoid

- Filling unknowns with guesses
- Copying every template without pruning
- Adding private notes to public repos
- Treating this kit as a substitute for reading the actual code

## Verification

- `repo_contract.md` is populated with project-specific information
- `qa_gauntlet.md` contains actual project commands
- Irrelevant templates have been removed
- No private context has been added to public repos

## Failure Modes

- Onboarding without reading the code → agent works from wrong assumptions
- Filling every template with placeholder text → noise, not signal
- Skipping the security review customization → agent misses project-specific risks
