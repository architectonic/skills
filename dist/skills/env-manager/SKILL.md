---
name: Environment Manager
description: Manage environment variables and secrets across development, staging, and production environments. Use when auditing env vars, syncing secrets between environments, detecting missing or mismatched variables, rotating credentials, or setting up a new environment.
tags: [environment-variables, secrets, configuration, devops, security]
source: terminal-skills (terminalskills.io)
license: Apache-2.0
distilled: 2026-06-22
type: Playbook
---

# Environment Manager

## Overview

Manage environment variables and secrets across multiple environments (development, staging, production). Detect missing variables, identify mismatches, audit for exposed secrets, and rotate credentials without downtime.

## Auditing Environment Variables

1. **Find all env var references in code:**
   ```bash
   # Node.js/TypeScript
   grep -rn "process\.env\." src/ --include="*.ts" --include="*.js" | \
     sed 's/.*process\.env\.\([A-Z_]*\).*/\1/' | sort -u
   # Python
   grep -rn "os\.environ\|os\.getenv" src/ --include="*.py" | \
     sed 's/.*os\.\(environ\["\|getenv("\)\([A-Z_]*\).*/\2/' | sort -u
   ```

2. **Compare against what's defined:**
   ```bash
   grep -v '^#' .env.example | grep '=' | cut -d'=' -f1 | sort -u
   ```

3. **Flag issues:**
   - Referenced in code but missing from `.env.example` → undocumented
   - In `.env.example` but never referenced → possibly stale
   - No default and no validation → app will crash if missing

## Comparing Environments

Build a comparison matrix across dev/staging/prod:
- Variable present in staging but missing in production → likely deployment bug
- Same secret value across dev and prod → security risk
- Public-prefixed variables with secret values → exposed to client

## Secret Rotation

1. Identify the secret to rotate
2. Check where it's used across code, CI/CD, Docker, configs
3. Generate rotation plan:
   - **API keys**: Create new key → update all environments → verify → revoke old
   - **Database passwords**: Update password → update connection strings → restart services
   - **JWT secrets**: Implement dual-key validation → deploy → set new primary → remove old
4. Verify no hardcoded values exist (all should reference env vars)

## Setting Up a New Environment

1. Start from `.env.example` as the template
2. Categorize each variable:
   - **Shared config** (feature flags, API URLs) → copy and adjust
   - **Secrets** (API keys, passwords) → generate new ones, never copy
   - **Infrastructure** (DB URLs, Redis URLs) → get from new env's infra
3. Validate: app starts without missing var errors

## Guidelines

- Never print or log actual secret values — show only variable names and metadata
- Flag identical secrets across environments as a security concern
- Always check for `NEXT_PUBLIC_` / `VITE_` prefixed vars containing actual secrets
- Recommend `.env.example` as the source of truth, committed to git (without values)
- For rotation, always plan for zero-downtime: new key → deploy → verify → revoke old
- Check CI/CD pipeline configs too — secrets there often go stale after renames
- Suggest validation libraries (envalid, zod) to catch missing vars at startup, not runtime
