---
name: prompt-governance
description: Use when managing prompts in production at scale — versioning prompts, running A/B tests on prompts, building prompt registries, preventing prompt regressions, or creating eval pipelines for production AI features. Triggers: "manage prompts in production", "prompt versioning", "prompt regression", "prompt A/B test", "prompt registry", "eval pipeline". NOT for writing or improving individual prompts.
tags: [agent-operations, prompt-engineering, production-ai, prompt-registry, eval-pipeline, a-b-testing, ai-governance]
type: Playbook
---

# Prompt Governance

Treat prompts as first-class infrastructure — versioned, tested, evaluated, and deployed with the same rigor as application code. Prevent quality regressions, enable safe iteration, and give teams confidence that prompt changes will not break production.

Prompts are code. They change behavior in production. Ship them like code.

## Modes

### Mode 1: Build Prompt Registry
No centralized prompt management today. Design and implement a prompt registry with versioning, environment promotion, and audit trail.

### Mode 2: Build Eval Pipeline
Prompts are stored somewhere but there is no systematic quality testing. Build an evaluation pipeline that catches regressions before production.

### Mode 3: Governed Iteration
Registry and evals exist. Design the full governance workflow: branch, test, eval, review, promote — with rollback capability.

## Mode 1: Build Prompt Registry

**Minimum Viable Registry (File-Based)** — for small teams, structured files in version control:

```
prompts/
  registry.yaml          # Index of all prompts
  summarizer/
    v1.0.0.md            # Prompt content
    v1.1.0.md
  classifier/
    v1.0.0.md
```

Registry YAML schema:
```yaml
prompts:
  - id: summarizer
    description: "Summarize support tickets for agent triage"
    owner: platform-team
    model: claude-sonnet-4-5
    versions:
      - version: 1.1.0
        file: summarizer/v1.1.0.md
        status: production
        promoted_at: 2026-03-15
        promoted_by: eng@company.com
      - version: 1.0.0
        file: summarizer/v1.0.0.md
        status: archived
```

**Production Registry (Database-Backed)** — for larger teams: API-accessible registry with tables for prompts and prompt_versions tracking slug, content, model, environment, eval_score, and promotion metadata.

## Mode 2: Build Eval Pipeline

### Eval Types

| Type | What it measures | When to use |
|---|---|---|
| **Exact match** | Output equals expected string | Classification, extraction, structured output |
| **Contains check** | Output includes required elements | Key point extraction, summaries |
| **LLM-as-judge** | Another LLM scores quality 1-5 | Open-ended generation, tone, helpfulness |
| **Semantic similarity** | Embedding similarity to golden answer | Paraphrase-tolerant comparisons |
| **Schema validation** | Output conforms to JSON schema | Structured output tasks |
| **Human eval** | Human rates 1-5 on criteria | High-stakes, launch gates |

### Golden Dataset Design

Every prompt needs a golden dataset: a fixed set of input/expected-output pairs defining correct behavior.

Requirements:
- Minimum 20 examples for basic coverage, 100+ for production confidence
- Cover edge cases and failure modes, not just happy path
- Reviewed and approved by domain expert, not just the engineer who wrote the prompt
- Versioned alongside the prompt

### Pass Thresholds

- Classification/extraction: 95%+ exact match
- Summarization: 0.85+ LLM-as-judge score
- Structured output: 100% schema validation
- Open-ended generation: 80%+ human eval approval

## Mode 3: Governed Iteration

The full prompt deployment lifecycle:

```
1. BRANCH  — Create feature branch for prompt change
2. DEVELOP — Edit prompt in dev environment, manual testing
3. EVAL    — Run eval pipeline vs. golden dataset (automated in CI)
4. COMPARE — Compare new prompt eval score vs. current production score
5. REVIEW  — PR review: eval results plus diff of prompt changes
6. PROMOTE — Staging to Production with approval gate
7. MONITOR — Watch production metrics for 24-48h post-deploy
8. ROLLBACK — One-command rollback to previous version if needed
```

### A/B Testing Prompts

- Use stable assignment (same user always gets same variant, based on user_id hash)
- Log every assignment with user_id, prompt_slug, and variant
- Define success metric before starting (not after)
- Run for minimum 1 week or 1,000 requests per variant
- Check for novelty effect (first-day engagement spike)
- Statistical significance: p<0.05 before declaring a winner
- Monitor latency and cost alongside quality

### Rollback Playbook

One-command rollback promotes the previous version back to production status in the registry. Verify by re-running evals against the restored version.

## Proactive Triggers

- **Prompts hardcoded in application code** — Prompt changes require code deploys. Flag immediately.
- **No golden dataset for production prompts** — You are flying blind.
- **Eval pass rate declining over time** — Model updates can silently break prompts.
- **No prompt rollback capability** — If a bad prompt reaches production, the team is stuck.
- **One person owns all prompt knowledge** — Bus factor risk.
- **Prompt changes deployed without eval** — Every uneval'd deploy is a bet.

## Anti-Patterns

| Anti-Pattern | Why It Fails | Better Approach |
|---|---|---|
| Hardcoding prompts in source code | Changes require code deploys | Versioned registry separate from code |
| Deploying without running evals | Silent quality regressions | Gate on eval pass before promotion |
| Single golden dataset forever | Drifts from real usage | Review quarterly, add edge cases |
| One person owns all prompt knowledge | Bus factor of 1 | Registry with ownership + rationale |
| A/B testing without pre-defined metric | Post-hoc bias | Define success metric before starting |
| Skipping rollback capability | Bad prompt = emergency deploy | One-command rollback always available |
