---
title: AI SDK Provider Tool Safety
description: Design provider-agnostic AI features with explicit tool, sandbox, model, and runtime boundaries before implementation.
domain: software-engineering
risk_level: medium
requires_review: true
source_profile: sources/profiles/2026-07-08/vercel-ai.json
source_attribution: vercel/ai, Apache-2.0; original guidance only, no copied examples or implementation content
review_gate: tool-and-sandbox-boundary-review
---

# AI SDK Provider Tool Safety

Use this skill when an agent or developer is designing an AI feature that combines model providers, tool calls, streaming output, application UI, sandboxed execution, or provider routing. The goal is to keep provider abstraction useful without letting tools, secrets, accounts, files, or deployment surfaces become implicit ambient authority.

This is original package-facing guidance derived from a reviewed source profile for the Vercel AI SDK. It does not copy README examples, prompts, code snippets, or implementation content.

## Operating rule

Separate four decisions before writing feature code:

1. which model provider or gateway may be called;
2. which tools may be invoked;
3. where tool effects are allowed to land;
4. what the user must approve before irreversible or external effects occur.

A provider abstraction should make model choice portable. It must not make tool authority portable by accident.

## Fit

Use this skill for:

- chat or agent features that may switch between model providers;
- features that expose tools to a model;
- applications with streaming responses and tool results;
- model gateway or provider-fallback design;
- sandboxed code, shell, browser, file, repository, or deployment workflows;
- package guidance that needs to stay implementation-agnostic.

Do not use this skill as a substitute for a security review of production code, provider credentials, hosted sandboxes, browser automation, payment, email, account mutation, or deployment workflows.

## Required boundaries

### Provider boundary

Document the provider surface separately from the tool surface.

A safe provider boundary records:

- allowed provider or gateway names;
- model selection policy;
- fallback policy;
- data classes allowed to leave the application;
- logging and retention expectations;
- budget or rate-limit owner;
- failure behavior when a provider is unavailable.

The provider boundary should be changeable without changing tool permissions.

### Tool boundary

Every tool must have a declared effect class:

- read-only local context;
- read-only external fetch;
- local file write;
- repository mutation;
- account or workspace mutation;
- network action;
- paid action;
- deployment or publication action.

Default to no external mutation. A tool that can mutate external state needs an explicit approval checkpoint and a durable audit record.

### Sandbox boundary

Sandboxed execution is not a generic permission grant. Record:

- what filesystem paths are mounted;
- whether network access is available;
- whether secrets are present;
- whether subprocesses are allowed;
- where generated artifacts are written;
- how execution is timed out and logged;
- who can inspect the result.

If a sandbox has network, secrets, browser control, repository access, or deployment credentials, classify the feature as at least medium risk and require review.

### UI boundary

Streaming and tool-result UI must distinguish:

- model text;
- tool input requested by the model;
- tool output returned by the system;
- user approval prompts;
- committed side effects.

Do not present a model-generated plan as if the tool action has already happened. Do not hide tool failures behind fluent text.

## Review checklist

Before implementation, answer these questions in the ticket, spec, or PR:

1. What providers may be called, and what data may be sent to them?
2. What tools exist, and which are read-only versus mutating?
3. Which tools require human approval?
4. What secrets are available to the runtime, if any?
5. Can the model access files, shell, browser, network, repositories, accounts, billing, email, or deployment surfaces?
6. What logs prove what the model requested, what the tool did, and who approved it?
7. How does the application behave if the provider, tool, or sandbox fails?
8. What must never be included in prompts, tool arguments, traces, or UI output?

If any answer is unknown, block package or publication endorsement until the boundary is explicit.

## Approval gates

Require explicit human approval for:

- sending email or messages;
- modifying accounts, permissions, billing, or credentials;
- writing to repositories or shared documents;
- publishing packages, posts, pages, or deployments;
- running browser automation against authenticated sessions;
- running shell commands outside a constrained sandbox;
- spending money or consuming paid resources beyond a fixed budget.

The approval prompt should name the target, effect, cost/risk, and rollback path. Generic approval such as “continue” is not enough for mutating actions.

## Failure handling

Provider and tool failures should be visible as structured states, not smoothed over by the model. Record:

- provider unavailable;
- provider timeout;
- tool rejected by policy;
- tool failed before side effect;
- tool produced partial side effect;
- approval denied;
- sandbox timeout;
- budget or rate limit exceeded.

The agent may summarize these states, but the application should keep the structured event as source of truth.

## Package-facing metadata guidance

Classify AI SDK provider/tool guidance as:

- `domain: software-engineering` when it is about application architecture;
- `risk_level: medium` when it discusses tools, sandboxes, provider routing, or runtime effects;
- `requires_review: true` when any shell, browser, account, deployment, payment, messaging, credential, or external mutation surface is in scope.

Escalate to high risk if the material includes executable account/browser workflows, credential handling, security testing, SSRF/internal probing, offensive behavior, deployment mutation, payment mutation, or unattended external actions.

## Done definition

The work is done when:

- provider, tool, sandbox, and UI boundaries are explicit;
- mutating actions have approval gates;
- secrets and logs are accounted for;
- failure states are structured;
- package metadata reflects risk and review requirements;
- no third-party examples or implementation content were copied into the skill.
