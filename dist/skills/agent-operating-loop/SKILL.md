---
name: Agent Operating Loop
description: The canonical Read → Classify → Inspect → Plan → Act → Verify → Reconcile → Handoff cycle that governs how an agent should approach any task. Use as the default procedure before starting work.
tags: [loops, agent-operations, operating-loop, modus-operandi, safety]
type: Playbook
---

# Agent Operating Loop

The canonical operating cycle for agents. Do not skip directly from instruction to edit.

## Loop Stages

### 1. Read

Read the local operating context before changing files.

Minimum read order:
```
AGENTS.md
START_HERE.md
memory_ops_doctrine.md
authority.md
repo_contract.md
memory_model.md
decision_log.md
handoff_log.md
```

Then read the source files relevant to the task.

Memory tells the agent where to look first. Source files tell the agent what is currently true.

### 2. Classify

Classify the work before touching files.

Use these classes:
```
local reversible change
feature work
bug fix
refactor
security-sensitive change
data-sensitive change
production-sensitive change
research task
destructive operation
```

Escalate caution when the task touches: authentication, authorization, secrets, cryptography, billing, payments, user data, production deployment, dependency supply chain, public API contracts, destructive scripts, vulnerability discovery or exploitation.

### 3. Inspect

Inspect the strongest available sources before proposing changes.

Prefer:
```
source code
tests
runtime output
CI output
logs
accepted decisions
repo contract
```

Do not rely on prior memory, old handoffs, or model knowledge when current source evidence is available.

### 4. Plan

Make the smallest coherent plan.

A good plan names: target files, expected behavior, verification method, safety boundary, rollback path when relevant.

Avoid broad rewrites unless the user explicitly requested them or source evidence proves they are necessary.

### 5. Act

Change only what the task requires.

Prefer direct fixes over new abstraction. Do not introduce frameworks, services, dependencies, config systems, or architectural patterns unless the task requires them.

Do not silently change public contracts, auth behavior, data models, or deployment behavior.

### 6. Verify

Verification is mandatory. Use the strongest practical verification available:

```
typecheck
unit tests
integration tests
build
lint
runtime smoke test
manual source review
security checklist
```

If a check cannot run, state why. Do not imply verification that did not happen.

### 7. Reconcile

After substantial work, reconcile memory.

Ask:
```
What became true?
What was disproved?
What decision changed?
What should future agents know?
What should be deleted as stale?
```

Update memory only when the information is durable and useful. Most task-local details should not become memory.

### 8. Handoff

If work remains, write a compact handoff.

A handoff should let the next agent continue without guessing. It should include:

```
task
current state
completed work
changed files
verification
open questions
risks
next step
```

## Security-Sensitive Mode

When the task touches security-sensitive surfaces, become more conservative.

Use this mode for: auth flows, permissions, cryptography, secrets, OAuth, payment systems, API keys, data deletion, production infrastructure, vulnerability research, exploitability analysis.

Security-sensitive mode requires:
1. explicit scope
2. source-grounded claims
3. no speculative exploit instructions beyond defensive need
4. no secret exposure
5. no destructive actions without permission
6. verification or stated inability to verify
7. memory reconciliation for durable security decisions

## Research Mode

When doing research, distinguish:
```
source quote
source-backed summary
inference
hypothesis
unknown
```

Use citations or source pointers when possible. Do not let a polished report hide uncertainty. Do not treat third-party summaries as equal to primary sources.

## Autonomy Boundary

The agent may proceed autonomously when: scope is clear, change is local and reversible, affected files are known, verification method is known, no sensitive boundary is touched.

The agent should ask or stop when: scope is ambiguous, action is destructive, sensitive systems are touched, requirements conflict, evidence is insufficient, the agent would need to invent product policy.

## Sources

- curator/legacy/root-meta/modus_operandi.md — full operating discipline
- curator/legacy/root-meta/memory_ops_doctrine.md — memory ops doctrine
- curator/legacy/root-meta/authority.md — authority hierarchy
- curator/legacy/cognition/reasoning_principles.md — reasoning guardrails
