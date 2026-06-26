---
name: Security Review
description: Security gate checklist for reviewing agent-made changes and third-party agent skill ingestion. Use before merging, shipping, or promoting any skill or code change that touches sensitive surfaces.
tags: [agent-operations, agent-operations, security, review, gate, okf]
type: Playbook
---

# Security Review

## Purpose

Catch security-sensitive issues before they ship. This is a compact gate, not a full audit. Use it before merging or promoting any change that touches repositories, skills, or external systems.

## Trigger

Use before:
- merging agent-made changes
- shipping code to production or shared branches
- promoting a third-party skill to canonical status
- onboarding a new skill library entry

## Scope Checks

### Repository Safety
- [ ] Examples use placeholders, not live account material
- [ ] Local configuration files are not committed
- [ ] No private user data was added
- [ ] No client-sensitive or proprietary context was added
- [ ] Logs, screenshots, and fixtures are sanitized

### Access Control
- [ ] Authentication behavior was not changed accidentally
- [ ] Authorization checks were preserved
- [ ] Admin-only operations remain protected
- [ ] Public routes do not expose private data

### Dependency Safety
- [ ] New dependencies are necessary
- [ ] Package names are verified
- [ ] Install scripts or binaries are treated cautiously
- [ ] License impact is understood for production use

### Third-Party Skill Ingestion
Before adapting a public skill or workflow:
- [ ] Source URL is recorded
- [ ] Upstream author or organization is recorded
- [ ] License is recorded
- [ ] Redistribution status is clear
- [ ] Content is summarized or rewritten unless copying is explicitly allowed
- [ ] Any executable component is excluded unless reviewed
- [ ] Any instruction that changes files, external systems, accounts, packages, browsers, or network resources is marked
- [ ] Prompt-injection risk is considered
- [ ] The normalized OKF file states source status: `native`, `summarized`, `adapted`, `verbatim`, or `reference-only`

### Destructive Operations
Ask before changing anything involving:
- deletion
- migrations
- production data
- billing
- deployment configuration
- auth configuration
- security policies

## Security Note Template

```
Sensitive area touched:
Risk:
Mitigation:
Verification:
```

## Failure Modes
- Skipping the review when the change is "small" — small changes to auth or config can be high-risk
- Checking boxes without reading the actual diff
- Treating third-party skills as safe because they are popular

## Output
A pass/fail report with named risks and any required mitigations before proceeding.
