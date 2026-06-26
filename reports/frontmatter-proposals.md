# Frontmatter Proposals Summary

Total proposals: **1143**

This file is proposal-only. No files have been modified.

## Fields proposed

- `name`
- `title`
- `description`
- `type`
- `tags` (deduplicated, normalized)
- `domain` (derived)
- `risk_level` (derived)
- `requires_review` (derived)
- `source_family` (inferred)

## Next steps

1. Review this report
2. Approve or adjust proposals
3. Run apply_frontmatter_patches.py (not yet written)

## Sample proposals (first 20)

```json
{
  "path": "a11y-audit\\SKILL.md",
  "proposed_frontmatter": {
    "name": "a11y-audit",
    "title": "a11y-audit",
    "description": "WCAG 2.2 accessibility audit pipeline — scan, fix, and verify Level A/AA compliance across React, Next.js, Vue, Angular, Svelte, and plain HTML. Use when auditing accessibility, fixing a11y violations, checking color contrast, generating compliance reports, or integrating a11y checks into CI/CD.",
    "type": "Playbook",
    "tags": [],
    "domain": "design",
    "risk_level": "medium",
    "requires_review": true,
    "source_family": "vercel-skills"
  },
  "current_frontmatter": {
    "type": "Playbook",
    "tags": [],
    "source_status": "",
    "risk_level": "medium",
    "requires_review": true
  }
}
---
{
  "path": "abusing-dpapi-for-credential-access\\SKILL.md",
  "proposed_frontmatter": {
    "name": "abusing-dpapi-for-credential-access",
    "title": "Abusing DPAPI for Credential Access",
    "description": "Extract DPAPI-protected secrets such as credentials and browser data offline and online.",
    "type": "Playbook",
    "tags": [
      "software-engineering",
      "agent-operations",
      "okf",
      "red-team",
      "credential-access",
      "dpapi",
      "sharpdpapi",
      "post-exploitation",
      "active-directory",
      "windows",
      "mimikatz",
      "security"
    ],
    "domain": "security-offensive",
    "risk_level": "high",
    "requires_review": true,
    "source_family": "anthropic-cybersecurity-skills"
  },
  "current_frontmatter": {
    "type": "Playbook",
    "tags": [
      "software-engineering",
      "agent-operations",
      "okf",
      "red-team",
      "credential-access",
      "dpapi",
      "sharpdpapi",
      "post-exploitation",
      "active-directory",
      "windows",
      "mimikatz",
      "security"
    ],
    "source_status": "",
    "risk_level": "high",
    "requires_review": true
  }
}
---
{
  "path": "abusing-shadow-credentials-for-privesc\\SKILL.md",
  "proposed_frontmatter": {
    "name": "abusing-shadow-credentials-for-privesc",
    "title": "Abusing Shadow Credentials for Privilege Escalation",
    "description": "Take over Active Directory user and computer accounts by writing alternate certificate keys to msDS-KeyCredentialLink (Shadow Credentials) with pyWhisker, Whisker, and Certipy, then authenticate via PKINIT.",
    "type": "Playbook",
    "tags": [
      "software-engineering",
      "agent-operations",
      "okf",
      "red-team",
      "active-directory",
      "shadow-credentials",
      "pywhisker",
      "certipy",
      "pkinit",
      "key-credential-link",
      "privilege-escalation",
      "security"
    ],
    "domain": "security-offensive",
    "risk_level": "high",
    "requires_review": true,
    "source_family": "anthropic-cybersecurity-skills"
  },
  "current_frontmatter": {
    "type": "Playbook",
    "tags": [
      "software-engineering",
      "agent-operations",
      "okf",
      "red-team",
      "active-directory",
      "shadow-credentials",
      "pywhisker",
      "certipy",
      "pkinit",
      "key-credential-link",
      "privilege-escalation",
      "security"
    ],
    "source_status": "",
    "risk_level": "high",
    "requires_review": true
  }
}
---
{
  "path": "academic-research\\SKILL.md",
  "proposed_frontmatter": {
    "name": "academic-research",
    "title": "academic-research",
    "description": "Search, review, synthesize, and write academic research. Use for arXiv paper search, paper review, systematic literature reviews, consulting analysis reports, and full research paper writing (NeurIPS/ICML/ICLR). Covers the full research lifecycle from discovery to publication.",
    "type": "Playbook",
    "tags": [
      "research",
      "agent-operations"
    ],
    "domain": "research",
    "risk_level": "medium",
    "requires_review": true,
    "source_family": "agent-skills-standard"
  },
  "current_frontmatter": {
    "type": "Playbook",
    "tags": [
      "research",
      "agent-operations"
    ],
    "source_status": "",
    "risk_level": "medium",
    "requires_review": true
  }
}
---
{
  "path": "acceptance-orchestrator\\SKILL.md",
  "proposed_frontmatter": {
    "name": "acceptance-orchestrator",
    "title": "acceptance-orchestrator",
    "description": "",
    "type": "Playbook",
    "tags": [],
    "domain": "business",
    "risk_level": "medium",
    "requires_review": true,
    "source_family": "unknown"
  },
  "current_frontmatter": {
    "type": "",
    "tags": [],
    "source_status": "",
    "risk_level": "medium",
    "requires_review": true
  }
}
---
{
  "path": "achieving-cmmc-level-2-compliance\\SKILL.md",
  "proposed_frontmatter": {
    "name": "achieving-cmmc-level-2-compliance",
    "title": "Achieving CMMC Level 2 Compliance",
    "description": "",
    "type": "Playbook",
    "tags": [
      "software-engineering",
      "agent-operations",
      "okf",
      "cmmc",
      "nist-800-171",
      "cui",
      "sprs",
      "dfars",
      "c3pao",
      "poam",
      "compliance",
      "governance",
      "defense-industrial-base",
      "security"
    ],
    "domain": "business",
    "risk_level": "medium",
    "requires_review": true,
    "source_family": "agent-skills-standard"
  },
  "current_frontmatter": {
    "type": "Playbook",
    "tags": [
      "software-engineering",
      "agent-operations",
      "okf",
      "cmmc",
      "nist-800-171",
      "cui",
      "sprs",
      "dfars",
      "c3pao",
      "poam",
      "compliance",
      "governance",
      "defense-industrial-base",
      "security"
    ],
    "source_status": "",
    "risk_level": "medium",
    "requires_review": true
  }
}
---
{
  "path": "acquiring-disk-image-with-dd-and-dcfldd\\SKILL.md",
  "proposed_frontmatter": {
    "name": "acquiring-disk-image-with-dd-and-dcfldd",
    "title": "Acquiring Disk Image with dd and dcfldd",
    "description": "Create forensically sound bit-for-bit disk images using dd and dcfldd",
    "type": "Playbook",
    "tags": [
      "software-engineering",
      "agent-operations",
      "okf",
      "forensics",
      "disk-imaging",
      "evidence-acquisition",
      "dd",
      "dcfldd",
      "hash-verification",
      "security"
    ],
    "domain": "forensics",
    "risk_level": "medium",
    "requires_review": true,
    "source_family": "agent-skills-standard"
  },
  "current_frontmatter": {
    "type": "Playbook",
    "tags": [
      "software-engineering",
      "agent-operations",
      "okf",
      "forensics",
      "disk-imaging",
      "evidence-acquisition",
      "dd",
      "dcfldd",
      "hash-verification",
      "security"
    ],
    "source_status": "",
    "risk_level": "medium",
    "requires_review": true
  }
}
---
{
  "path": "agent-context-validation\\SKILL.md",
  "proposed_frontmatter": {
    "name": "agent-context-validation",
    "title": "Agent Context Validation",
    "description": "Validate any artifact that changes what an agent reads, installs, executes, or treats as authority. Use when reviewing skills, prompts, MCP configs, hooks, subagent definitions, or runtime adapters before promotion.",
    "type": "Playbook",
    "tags": [
      "agent-operations",
      "validation",
      "safety",
      "linting",
      "skills",
      "mcp"
    ],
    "domain": "agent-operations",
    "risk_level": "medium",
    "requires_review": true,
    "source_family": "unknown"
  },
  "current_frontmatter": {
    "type": "Playbook",
    "tags": [
      "agent-operations",
      "validation",
      "safety",
      "linting",
      "skills",
      "mcp"
    ],
    "source_status": "",
    "risk_level": "medium",
    "requires_review": true
  }
}
---
{
  "path": "agent-development\\SKILL.md",
  "proposed_frontmatter": {
    "name": "agent-development",
    "title": "agent-development",
    "description": "Create autonomous agent configurations for Claude Code plugins. Use when building subagents, designing agent frontmatter, writing system prompts, defining triggering conditions, or structuring agent files. Covers agent file format, description writing, tool restriction, model selection, and validation rules.",
    "type": "Playbook",
    "tags": [],
    "domain": "agent-operations",
    "risk_level": "medium",
    "requires_review": true,
    "source_family": "unknown"
  },
  "current_frontmatter": {
    "type": "Playbook",
    "tags": [],
    "source_status": "",
    "risk_level": "medium",
    "requires_review": true
  }
}
---
{
  "path": "agent-handoff\\SKILL.md",
  "proposed_frontmatter": {
    "name": "agent-handoff",
    "title": "Agent Handoff",
    "description": "Compact the current conversation into a handoff document for another agent to pick up. Use when work must be transferred to a fresh session or a different agent. Covers summarization, context preservation, and redaction of sensitive information.",
    "type": "Playbook",
    "tags": [
      "agent-operations",
      "handoff",
      "context",
      "cross-session"
    ],
    "domain": "agent-operations",
    "risk_level": "medium",
    "requires_review": true,
    "source_family": "unknown"
  },
  "current_frontmatter": {
    "type": "Playbook",
    "tags": [
      "agent-operations",
      "handoff",
      "context",
      "cross-session"
    ],
    "source_status": "",
    "risk_level": "medium",
    "requires_review": true
  }
}
---
{
  "path": "agent-memory-system\\SKILL.md",
  "proposed_frontmatter": {
    "name": "agent-memory-system",
    "title": "agent-memory-system",
    "description": "Design and maintain agent memory systems. Use when setting up agent memory, designing memory schemas, implementing memory lifecycle management, or reconciling memory across sessions. Covers memory classes, lifecycle states, demotion rules, and canonicalization.",
    "type": "Playbook",
    "tags": [
      "agent-operations",
      "memory",
      "self-improvement"
    ],
    "domain": "agent-operations",
    "risk_level": "medium",
    "requires_review": true,
    "source_family": "unknown"
  },
  "current_frontmatter": {
    "type": "Playbook",
    "tags": [
      "agent-operations",
      "memory",
      "self-improvement"
    ],
    "source_status": "",
    "risk_level": "medium",
    "requires_review": true
  }
}
---
{
  "path": "agent-operating-loop\\SKILL.md",
  "proposed_frontmatter": {
    "name": "agent-operating-loop",
    "title": "Agent Operating Loop",
    "description": "The canonical Read → Classify → Inspect → Plan → Act → Verify → Reconcile → Handoff cycle that governs how an agent should approach any task. Use as the default procedure before starting work.",
    "type": "Playbook",
    "tags": [
      "loops",
      "agent-operations",
      "operating-loop",
      "modus-operandi",
      "safety"
    ],
    "domain": "agent-operations",
    "risk_level": "medium",
    "requires_review": true,
    "source_family": "unknown"
  },
  "current_frontmatter": {
    "type": "Playbook",
    "tags": [
      "loops",
      "agent-operations",
      "operating-loop",
      "modus-operandi",
      "safety"
    ],
    "source_status": "",
    "risk_level": "medium",
    "requires_review": true
  }
}
---
{
  "path": "agent-skill-configuration\\SKILL.md",
  "proposed_frontmatter": {
    "name": "agent-skill-configuration",
    "title": "agent-skill-configuration",
    "description": "Research on configuring and optimizing agent skills in agentic coding workflows.",
    "type": "Playbook",
    "tags": [
      "research",
      "skill-configuration",
      "agentic-coding",
      "agent-setup",
      "tool-integration"
    ],
    "domain": "agent-operations",
    "risk_level": "medium",
    "requires_review": true,
    "source_family": "agent-skills-standard"
  },
  "current_frontmatter": {
    "type": "Playbook",
    "tags": [
      "research",
      "skill-configuration",
      "agentic-coding",
      "agent-setup",
      "tool-integration"
    ],
    "source_status": "",
    "risk_level": "medium",
    "requires_review": true
  }
}
---
{
  "path": "agent-skill-portability\\SKILL.md",
  "proposed_frontmatter": {
    "name": "agent-skill-portability",
    "title": "agent-skill-portability",
    "description": "Research on agent skill portability, security implications, and cross-agent compatibility challenges.",
    "type": "Playbook",
    "tags": [
      "research",
      "skill-portability",
      "security",
      "cross-agent",
      "compatibility",
      "agent-ecosystem"
    ],
    "domain": "agent-operations",
    "risk_level": "medium",
    "requires_review": true,
    "source_family": "agent-skills-standard"
  },
  "current_frontmatter": {
    "type": "Playbook",
    "tags": [
      "research",
      "skill-portability",
      "security",
      "cross-agent",
      "compatibility",
      "agent-ecosystem"
    ],
    "source_status": "",
    "risk_level": "medium",
    "requires_review": true
  }
}
---
{
  "path": "agentic-actions-auditor\\SKILL.md",
  "proposed_frontmatter": {
    "name": "agentic-actions-auditor",
    "title": "Agentic Actions Auditor",
    "description": "Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations (Claude Code Action, Gemini CLI, OpenAI Codex, GitHub AI Inference). Detects 9 attack vectors where attacker-controlled input reaches AI agents in CI/CD pipelines. Use when reviewing workflow files that invoke AI coding agents, auditing CI/CD pipeline security for prompt injection risks, or evaluating agentic action configurations.",
    "type": "Playbook",
    "tags": [
      "agent-operations",
      "security",
      "ci-cd",
      "github-actions",
      "ai-agent",
      "prompt-injection",
      "static-analysis"
    ],
    "domain": "software-engineering",
    "risk_level": "medium",
    "requires_review": true,
    "source_family": "unknown"
  },
  "current_frontmatter": {
    "type": "Playbook",
    "tags": [
      "agent-operations",
      "security",
      "ci-cd",
      "github-actions",
      "ai-agent",
      "prompt-injection",
      "static-analysis"
    ],
    "source_status": "",
    "risk_level": "medium",
    "requires_review": true
  }
}
---
{
  "path": "agents-md-improver\\SKILL.md",
  "proposed_frontmatter": {
    "name": "agents-md-improver",
    "title": "agents-md-improver",
    "description": "Audit and improve AGENTS.md / CLAUDE.md / SOUL.md files in repositories. Use when the user asks to check, audit, update, improve, or fix agent instruction files. Scans for all agent instruction files, evaluates quality against a rubric, outputs quality report, then makes targeted updates. Also use when the user mentions \"agent instruction maintenance\", \"project memory optimization\", or \"rules file audit\". Adapted from anthropic-claude-plugins-official/claude-md-improver.",
    "type": "Playbook",
    "tags": [],
    "domain": "software-engineering",
    "risk_level": "medium",
    "requires_review": true,
    "source_family": "unknown"
  },
  "current_frontmatter": {
    "type": "Playbook",
    "tags": [],
    "source_status": "",
    "risk_level": "medium",
    "requires_review": true
  }
}
---
{
  "path": "ai-native-cli\\SKILL.md",
  "proposed_frontmatter": {
    "name": "ai-native-cli",
    "title": "ai-native-cli",
    "description": "Design spec with 98 rules for building CLI tools that AI agents can safely use. Covers structured JSON output, error handling, input contracts, safety guardrails, exit codes, and agent self-description.",
    "type": "Playbook",
    "tags": [
      "agent-operations",
      "cli",
      "agent-safety",
      "json-output",
      "error-handling",
      "spec"
    ],
    "domain": "agent-operations",
    "risk_level": "medium",
    "requires_review": true,
    "source_family": "unknown"
  },
  "current_frontmatter": {
    "type": "Playbook",
    "tags": [
      "agent-operations",
      "cli",
      "agent-safety",
      "json-output",
      "error-handling",
      "spec"
    ],
    "source_status": "",
    "risk_level": "medium",
    "requires_review": true
  }
}
---
{
  "path": "ai-seo\\SKILL.md",
  "proposed_frontmatter": {
    "name": "ai-seo",
    "title": "ai-seo",
    "description": "Optimize content for AI search and LLM citations across AI Overviews, ChatGPT, Perplexity, Claude, Gemini, and similar systems. Covers AI visibility audit, three-pillar optimization strategy (structure/authority/presence), and monitoring.",
    "type": "Reference",
    "tags": [
      "productivity",
      "seo",
      "ai-search",
      "llm-citations",
      "geo",
      "aeo",
      "content-optimization"
    ],
    "domain": "writing",
    "risk_level": "medium",
    "requires_review": true,
    "source_family": "unknown"
  },
  "current_frontmatter": {
    "type": "Reference",
    "tags": [
      "productivity",
      "seo",
      "ai-search",
      "llm-citations",
      "geo",
      "aeo",
      "content-optimization"
    ],
    "source_status": "",
    "risk_level": "medium",
    "requires_review": true
  }
}
---
{
  "path": "alert-optimizer\\SKILL.md",
  "proposed_frontmatter": {
    "name": "alert-optimizer",
    "title": "Alert Optimizer",
    "description": "Restructure and optimize alert rules for monitoring platforms (Sentry, PagerDuty, Datadog, OpsGenie). Use when reducing alert noise, fixing alert fatigue, creating alert rules, setting up escalation policies, tuning alerting thresholds, or creating on-call runbooks.",
    "type": "Playbook",
    "tags": [
      "devops",
      "alerting",
      "on-call",
      "pagerduty",
      "datadog",
      "sentry",
      "incident-response",
      "observability"
    ],
    "domain": "design",
    "risk_level": "medium",
    "requires_review": true,
    "source_family": "unknown"
  },
  "current_frontmatter": {
    "type": "Playbook",
    "tags": [
      "devops",
      "alerting",
      "on-call",
      "pagerduty",
      "datadog",
      "sentry",
      "incident-response",
      "observability"
    ],
    "source_status": "",
    "risk_level": "medium",
    "requires_review": true
  }
}
---
{
  "path": "algorithmic-art\\SKILL.md",
  "proposed_frontmatter": {
    "name": "algorithmic-art",
    "title": "algorithmic-art",
    "description": "Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use when users request creating art using code, generative art, algorithmic art, flow fields, or particle systems. Create original algorithmic art rather than copying existing artists' work to avoid copyright violations.",
    "type": "Playbook",
    "tags": [],
    "domain": "design",
    "risk_level": "medium",
    "requires_review": true,
    "source_family": "unknown"
  },
  "current_frontmatter": {
    "type": "Playbook",
    "tags": [],
    "source_status": "",
    "risk_level": "medium",
    "requires_review": true
  }
}
---
```