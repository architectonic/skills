---
name: Insecure Defaults Detection
description: "Detects fail-open insecure defaults (hardcoded secrets, weak auth, permissive security) that allow apps to run insecurely in production. Distinguishes fail-open from fail-secure patterns. Use when auditing security, reviewing config management, or analyzing environment variable handling."
source: trailofbits-skills (MIT license, https://github.com/trailofbits/skills — plugins/insecure-defaults/skills/insecure-defaults/SKILL.md)
category: software-development
tags: [software-development, security, insecure-defaults, fail-open, configuration, secrets, audit]
type: Playbook
---

# Insecure Defaults Detection

Finds **fail-open** vulnerabilities where apps run insecurely with missing configuration. Distinguishes exploitable defaults from fail-secure patterns that crash safely.

**Fail-open (CRITICAL):** `SECRET = env.get('KEY') or 'default'` → App runs with weak secret
**Fail-secure (SAFE):** `SECRET = env['KEY']` → App crashes if missing

## When to Use

- Security audits of production applications (auth, crypto, API security)
- Configuration review of deployment files, IaC templates, Docker configs
- Code review of environment variable handling and secrets management
- Pre-deployment checks for hardcoded credentials or weak defaults

## When NOT to Use

- Test fixtures explicitly scoped to test environments (`test/`, `spec/`, `__tests__/`)
- Example/template files (`.example`, `.template`, `.sample` suffixes)
- Development-only tools (local Docker Compose for dev, debug scripts)
- Documentation examples in README.md or docs/ directories
- Build-time configuration that gets replaced during deployment
- Crash-on-missing behavior (fail-secure patterns)

## Rationalizations to Reject

| Rationalization | Why It's Wrong |
|-----------------|----------------|
| "It's just a development default" | If it reaches production code, it's a finding |
| "The production config overrides it" | Verify prod config exists; code-level vulnerability remains |
| "This would never run without proper config" | Prove it with code trace; many apps fail silently |
| "It's behind authentication" | Defense in depth; compromised session still exploits weak defaults |
| "We'll fix it before release" | Document now; "later" rarely comes |

## Workflow

### 1. Search: Find Insecure Defaults

Determine language, framework, and project conventions first. Then search for:

**Fallback secrets:**
```bash
grep -rn "getenv.*) or ['\"]" --include="*.py" --include="*.js" --include="*.ts" .
grep -rn "process\.env\.[A-Z_]+ || ['\"]" --include="*.js" --include="*.ts" .
grep -rn "ENV\.fetch.*default:" --include="*.rb" .
```

**Hardcoded credentials:**
```bash
grep -rn "password.*=.*['\"][^'\"]{8,}['\"]" --include="*.py" --include="*.js" --include="*.yml" .
grep -rn "api[_-]?key.*=.*['\"][^'\"]+['\"]" --include="*.py" --include="*.js" --include="*.yml" .
```

**Weak defaults:**
```bash
grep -rn "DEBUG.*=.*true" --include="*.py" --include="*.js" --include="*.yml" .
grep -rn "AUTH.*=.*false" --include="*.py" --include="*.js" .
grep -rn "CORS.*=.*\*" --include="*.py" --include="*.js" --include="*.yml" .
```

**Weak crypto:**
```bash
grep -rn "MD5\|SHA1\|DES\|RC4\|ECB" --include="*.py" --include="*.js" --include="*.go" --include="*.java" .
```

Focus on production-reachable code, not test fixtures or example files.

### 2. Verify: Actual Behavior

For each match, trace the code path:
- When is this code executed? (Startup vs. runtime)
- What happens if a configuration variable is missing?
- Is there validation that enforces secure configuration?

### 3. Confirm: Production Impact

- If production config provides the variable → Lower severity (but still a code-level vulnerability)
- If production config missing or uses default → CRITICAL

### 4. Report with Evidence

```
Finding: Hardcoded JWT Secret Fallback
Location: src/auth/jwt.ts:15
Pattern: const secret = process.env.JWT_SECRET || 'default';
Verification: App starts without JWT_SECRET; secret used in jwt.sign() at line 42
Production Impact: Dockerfile missing JWT_SECRET
Exploitation: Attacker forges JWTs using 'default', gains unauthorized access
```

## Quick Verification Checklist

**Fallback Secrets:** `SECRET = env.get(X) or Y`
→ Verify: App starts without env var? Secret used in crypto/auth?
→ Skip: Test fixtures, example files

**Default Credentials:** Hardcoded username/password pairs
→ Verify: Active in deployed config? No runtime override?
→ Skip: Disabled accounts, documentation examples

**Fail-Open Security:** `AUTH_REQUIRED = env.get(X, 'false')`
→ Verify: Default is insecure (false/disabled/permissive)?
→ Safe: App crashes or default is secure (true/enabled/restricted)

**Weak Crypto:** MD5/SHA1/DES/RC4/ECB in security contexts
→ Verify: Used for passwords, encryption, or tokens?
→ Skip: Checksums, non-security hashing

**Permissive Access:** CORS `*`, permissions `0777`, public-by-default
→ Verify: Default allows unauthorized access?
→ Skip: Explicitly configured permissiveness with justification

**Debug Features:** Stack traces, introspection, verbose errors
→ Verify: Enabled by default? Exposed in responses?
→ Skip: Logging-only, not user-facing
