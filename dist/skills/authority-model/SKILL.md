---
name: Authority Model
description: Rank sources by authority level and resolve conflicting information. Use when two sources disagree, when evaluating evidence strength, or when deciding what to trust for sensitive changes.
tags: [agent-operations, agent-operations, authority, conflict-resolution, epistemic-hygiene]
type: Playbook
---

# Authority Model

Defines how an agent should rank sources when working in a repository and how to resolve conflicts.

## Authority Hierarchy

When sources conflict, use this order:

```
1.  Current user instruction
2.  Current repository source files
3.  Tests, typechecks, build output, CI, and runtime evidence
4.  Repo-local AGENTS.md
5.  Repo contract
6.  Accepted decision records
7.  Current handoff
8.  Memory facts with recoverable sources
9.  Assumptions explicitly labeled as assumptions
10. Agent inference
11. Model prior knowledge
```

The hierarchy does not remove judgment. It prevents weaker sources from silently overruling stronger ones.

## Source Classes

### Current User Instruction
Defines the task and may override previous plans. Does not automatically rewrite durable project decisions unless explicitly requested.

### Source Files
Strongest evidence for how the system currently behaves. Read source files before changing them. When source files contradict memory, trust the source files and update the memory.

### Tests and Runtime Evidence
Passing tests, failing tests, logs, build output, and runtime behavior are evidence. They can reveal that both source comments and memory are stale.

### AGENTS.md
Defines repository-local agent behavior. Read before substantial work.

### Repo Contract
Defines project identity, source-of-truth locations, agent permissions, definition of done, and non-goals.

### Decision Records
Accepted decisions should not be accidentally undone. A decision record may be superseded, but make that status explicit.

### Handoffs
Useful for continuation. Not proof of current state. Should guide inspection, not replace it.

### Memory Facts
Should be backed by a recoverable source when possible. Unsourced facts are weaker than sourced facts.

### Assumptions
Provisional. Must remain labeled until verified, rejected, or deleted.

### Inference
Allowed, but must be named as inference when it affects decisions.

### Model Prior Knowledge
Weakest source. May help generate hypotheses, but must not override repository evidence.

## Conflict Resolution

When two sources disagree:

1. Identify both sources.
2. Rank them by authority.
3. Inspect the strongest available source.
4. State the conflict if it affects the task.
5. Update, demote, or delete stale memory when appropriate.

**Do not average conflicting sources into a compromise claim.**

## Sensitive Changes

Before making a sensitive change, identify the highest-authority source that permits the change. Sensitive changes include: authentication, authorization, billing, payments, secrets, production deployment, data deletion, public API contracts, legal or compliance text.

If no sufficient authority exists, ask before acting.

## Private Context Rule
Private memory, personal context, raw transcripts, hidden system state, or external private repositories must not be treated as publishable source material.

## Trigger
Use when:
- Two sources disagree about project behavior or decisions
- An agent must decide which source to trust
- Evaluating whether memory or source files take precedence
- Making sensitive changes that require authority verification

## Procedure
1. Identify the conflicting sources.
2. Classify each source using the authority hierarchy.
3. Inspect the highest-ranked source first.
4. Read actual source artifacts — do not rely on memory or inference.
5. State the conflict explicitly in the output.
6. Update or demote stale memory.
7. If the conflict affects a decision, record it in the decision log.

## Verification
- Conflict is explicitly named, not silently resolved.
- The chosen source is higher in the authority hierarchy.
- Stale memory has been updated or marked for deletion.

## Failure Modes
- Silently merging contradictions into a compromise claim.
- Treating model prior knowledge as authoritative.
- Using handoffs as proof of current state.
- Letting stale memory override current source files.
