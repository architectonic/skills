---
name: vendor-skill-packaging
description: Package and maintain vendor-maintained skill libraries for multi-runtime agent compatibility. Use when creating skills intended for multiple agent runtimes, when reviewing vendor skill packs for ingestion, or when publishing skills to marketplaces. Covers skill family grouping, install/discover workflows, and deployment classification.
tags: [skill-management, skill-management, packaging, vendor, multi-runtime, marketplace]
type: Playbook
---

# vendor-skill-packaging

Package skills for multi-runtime compatibility and marketplace distribution.

## When to use

- Creating skills that should work across Claude Code, Codex, Cursor, and other runtimes
- Reviewing a vendor skill pack for potential ingestion
- Publishing skills to a marketplace or registry
- Classifying skills as safe for automated installation

## Core Pattern (from Vercel Labs + Google Stitch)

```text
product/vendor knowledge
→ packaged as focused SKILL.md modules
→ discoverable through marketplace/registry
→ installable into multiple coding-agent runtimes
→ optionally backed by scripts and references
```

## Packaging Principles

### Family Grouping
- Group skills by capability family (e.g., web-performance, react-patterns, deployment)
- Each skill should be focused — one clear capability per module
- Use consistent naming within a family (e.g., `web-audit-*`, `react-*`, `deploy-*`)

### Multi-Runtime Compatibility
- Avoid runtime-specific tool references in the main skill body
- Use `tags` to indicate compatible runtimes
- Keep the main SKILL.md portable; put runtime-specific details in `references/`
- Test installation path on at least 2 runtimes

### Discover Skills
- Provide explicit install/use documentation
- Include a "when to use" section with clear triggers
- Document what the skill does NOT do (scope boundaries)

### Deployment Classification
Skills that trigger deployments (Vercel, Netlify, etc.) must be classified as **external mutation**:
- Require explicit human approval before execution
- Produce receipts for every mutation
- Support dry-run mode

## Skill Package Structure

```
skills/<family>/
  <skill-name>/
    SKILL.md              # Main skill (portable, lean)
    references/           # Detailed reference docs
    scripts/              # Optional automation scripts
    tests/                # Validation/verification tests
```

## Ingestion Review Checklist

When reviewing a vendor skill pack for AOMK ingestion:
- [ ] License allows summarization and pattern extraction
- [ ] No hardcoded secrets, credentials, or API keys
- [ ] Skill bodies are focused (not kitchen-sink)
- [ ] Trigger conditions are specific enough to avoid false matches
- [ ] External mutation is clearly documented
- [ ] Dependencies are declared

## Sources

- vercel-labs/agent-skills — vendor-maintained skill packaging for web engineering
- google-labs-code/stitch-skills — multi-runtime plugin marketplace with baton-loop pattern
- skill-quality-gate.md — validation before promotion
