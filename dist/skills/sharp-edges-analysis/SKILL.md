---
name: Sharp Edges Analysis
description: "Identifies error-prone APIs, dangerous configurations, and footgun designs that enable security mistakes. Evaluates whether APIs follow 'secure by default' and 'pit of success' principles. Use when reviewing API designs, configuration schemas, cryptographic library ergonomics, or evaluating misuse resistance."
source: trailofbits-skills (MIT license, https://github.com/trailofbits/skills — plugins/sharp-edges/skills/sharp-edges/SKILL.md)
category: software-development
tags: [agent-operations, security, api-design, footgun, misuse-resistant, secure-defaults, usability]
type: Playbook
---

# Sharp Edges Analysis

Evaluates whether APIs, configurations, and interfaces are resistant to developer misuse. Identifies designs where the "easy path" leads to insecurity.

## Core Principle

**The pit of success**: Secure usage should be the path of least resistance. If developers must understand cryptography, read documentation carefully, or remember special rules to avoid vulnerabilities, the API has failed.

## When to Use

- Reviewing API or library design decisions
- Auditing configuration schemas for dangerous options
- Evaluating cryptographic API ergonomics
- Assessing authentication/authorization interfaces
- Reviewing any code that exposes security-relevant choices to developers

## When NOT to Use

- Implementation bugs (use standard code review)
- Business logic flaws (use domain-specific analysis)
- Performance optimization (different concern)

## Rationalizations to Reject

| Rationalization | Why It's Wrong |
|-----------------|----------------|
| "It's documented" | Developers don't read docs under deadline pressure |
| "Advanced users need flexibility" | Flexibility creates footguns; most "advanced" usage is copy-paste |
| "It's the developer's responsibility" | Blame-shifting; you designed the footgun |
| "Nobody would actually do that" | Developers do everything imaginable under pressure |
| "It's just a configuration option" | Config is code; wrong configs ship to production |
| "We need backwards compatibility" | Insecure defaults can't be grandfather-claused |

## Sharp Edge Categories

### 1. Algorithm/Mode Selection Footguns

APIs that let developers choose algorithms invite choosing wrong ones.

**Canonical example — JWT:**
- Header specifies algorithm: attacker can set `"alg": "none"` to bypass signatures
- Algorithm confusion: RSA public key used as HMAC secret when switching RS256→HS256
- Root cause: Letting untrusted input control security-critical decisions

**Detection patterns:**
- Function parameters like `algorithm`, `mode`, `cipher`, `hash_type`
- Enums/strings selecting cryptographic primitives
- Configuration options for security mechanisms

### 2. Dangerous Defaults

Defaults that are insecure, or zero/empty values that disable security.

**Detection patterns:**
- Timeouts/lifetimes that accept 0 (infinite? immediate expiry?)
- Empty strings that bypass checks
- Null values that skip validation
- Boolean defaults that disable security features
- Negative values with undefined semantics

**Key questions:**
- What happens with `timeout=0`? `max_attempts=0`? `key=""`?
- Is the default the most secure option?
- Can any default value disable security entirely?

### 3. Primitive vs. Semantic APIs

APIs that expose raw bytes instead of meaningful types invite type confusion.

**Detection patterns:**
- Functions taking `bytes`, `string`, `[]byte` for distinct security concepts
- Parameters that could be swapped without type errors
- Same type used for keys, nonces, ciphertexts, signatures

**The comparison footgun:**
```go
if hmac == expected { }           // BAD: timing attack
if hmac.Equal(mac, expected) { }  // Good: constant-time
// Same types, different security properties
```

### 4. Configuration Cliffs

One wrong setting creates catastrophic failure, with no warning.

**Detection patterns:**
- Boolean flags that disable security entirely
- String configs that aren't validated
- Combinations of settings that interact dangerously
- Environment variables that override security settings
- Constructor parameters with sensible defaults but no validation

### 5. Silent Failures

Errors that don't surface, or success that masks failure.

**Detection patterns:**
- Functions returning booleans instead of throwing on security failures
- Empty catch blocks around security operations
- Default values substituted on parse errors
- Verification functions that "succeed" on malformed input

### 6. Stringly-Typed Security

Security-critical values as plain strings enable injection and confusion.

**Detection patterns:**
- SQL/commands built from string concatenation
- Permissions as comma-separated strings
- Roles/scopes as arbitrary strings instead of enums
- URLs constructed by joining strings

## Analysis Workflow

### Phase 1: Surface Identification
1. Map security-relevant APIs: authentication, authorization, cryptography, session management, input validation
2. Identify developer choice points: algorithm selection, timeout configuration, mode selection
3. Find configuration schemas: environment variables, config files, constructor parameters

### Phase 2: Edge Case Probing
For each choice point, ask:
- **Zero/empty/null**: What happens with `0`, `""`, `null`, `[]`?
- **Negative values**: What does `-1` mean? Infinite? Error?
- **Type confusion**: Can different security concepts be swapped?
- **Default values**: Is the default secure? Is it documented?
- **Error paths**: What happens on invalid input? Silent acceptance?

### Phase 3: Threat Modeling
Consider three adversaries:
1. **The Scoundrel**: Can they disable security via configuration? Downgrade algorithms? Inject values?
2. **The Lazy Developer**: Will the first example they find be secure? Is the path of least resistance secure?
3. **The Confused Developer**: Can they swap parameters without type errors? Are failure modes obvious?

### Phase 4: Validate Findings
1. Reproduce the misuse: write minimal code demonstrating the footgun
2. Verify exploitability: does the misuse create a real vulnerability?
3. Check documentation: is the danger documented? (Doesn't excuse bad design)
4. Test mitigations: can the API be used safely with reasonable effort?

## Severity Classification

| Severity | Criteria | Examples |
|----------|----------|----------|
| Critical | Default or obvious usage is insecure | `verify: false` default; empty password allowed |
| High | Easy misconfiguration breaks security | Algorithm parameter accepts "none" |
| Medium | Unusual but possible misconfiguration | Negative timeout has unexpected meaning |
| Low | Requires deliberate misuse | Obscure parameter combination |

## Quality Checklist

- [ ] Probed all zero/empty/null edge cases
- [ ] Verified defaults are secure
- [ ] Checked for algorithm/mode selection footguns
- [ ] Tested type confusion between security concepts
- [ ] Considered all three adversary types
- [ ] Verified error paths don't bypass security
- [ ] Checked configuration validation
