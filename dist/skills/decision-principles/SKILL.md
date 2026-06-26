---
name: Decision Principles
description: Structured framework for choosing between implementation paths, tools, architectures, or product directions. Use when evaluating technical options or making architecture decisions.
tags: [agent-operations, agent-operations, decision-making, architecture, tradeoffs]
type: Playbook
---

# Decision Principles

## Purpose

Provide a structured procedure for making technical decisions that are scoped, reversible when possible, source-grounded, and explicit about tradeoffs.

## Decision Procedure

1. Define the actual problem.
2. Identify evidence that the problem exists.
3. Identify constraints.
4. List realistic options.
5. Compare consequences.
6. Prefer the smallest coherent next move.
7. Define what would prove the decision wrong.
8. Record the decision if future agents must preserve it.

## Good Decisions

Good decisions are:

- scoped;
- reversible when possible;
- source-grounded;
- explicit about tradeoffs;
- tied to a verification method.

## Bad Decisions

Bad decisions often:

- optimize for aesthetics without solving the problem;
- add abstraction before need is proven;
- preserve broken behavior by default;
- ignore maintenance cost;
- hide assumptions.

## Trigger

Use this skill when:
- Choosing between two or more implementation approaches
- Evaluating whether to add a new dependency or tool
- Deciding on architecture patterns for a new feature
- Prioritizing between competing technical directions

## Procedure

1. **Define the problem.** State what actually needs to change, not just the symptom.
2. **Gather evidence.** What source confirms this is a real problem? (tests, logs, user reports)
3. **Identify constraints.** What are the non-negotiable requirements? (performance, compatibility, security, license)
4. **List options.** What are the realistic paths? (ignore theoretically possible but impractical options)
5. **Compare consequences.** For each option: what is the maintenance cost? What does it enable? What does it foreclose?
6. **Choose the smallest move.** Prefer the option that solves the problem with the least structural change.
7. **Define falsification.** What observation would prove this decision wrong? (e.g., "if latency exceeds 200ms, reconsider")
8. **Record if durable.** If future agents are likely to revisit this decision, record it in the decision log.

## Verification

- The chosen option addresses the defined problem.
- The decision is no larger than necessary.
- Tradeoffs are documented.
- A falsification condition is defined.
- If the decision is durable, it is recorded in the decision log.

## Failure Modes

- Agent chooses based on familiarity rather than evidence.
- Agent optimizes for code aesthetics over functional need.
- Agent adds abstraction layers before the problem warrants them.
- Agent makes irreversible decisions without acknowledging the irreversibility.
- Agent hides assumptions instead of stating them explicitly.

## Security Notes

- Low risk: this is a decision framework, not an execution tool.
- Indirect risk: poor decision discipline leads to accumulated technical debt that makes systems harder to secure and maintain.

## Sources

- curator/legacy/cognition/decision_principles.md — decision procedure and quality criteria
