---
name: Prompt Injection Detection
description: Detect prompt injection attacks targeting LLM-based applications. Use
  when sanitizing user inputs, building input validation for AI agents, or scanning
  for prompt injection vulnerabilities. Covers direct injections (system prompt overrides,
  role-play escapes) and indirect injections (encoded payloads, multi-language obfuscation).
tags:
- red-teaming
- prompt-injection
- llm-security
- input-validation
- owasp
type: Playbook
---

# Prompt Injection Detection


**Authorized-use only:** Use this skill only for owned systems, sanctioned lab environments, or engagements with explicit written permission. Document scope, preserve evidence, and follow applicable law, policy, and incident-response procedures.

Detect prompt injection attacks targeting LLM-based applications using multi-layered defense.

## Attack categories

### Direct injections
- System prompt overrides ("ignore previous instructions")
- Role-play escapes ("you are now DAN")
- Instruction hijacking (embedded instructions in user input)
- Delimiter escapes (breaking out of context boundaries)

### Indirect injections
- Encoded payloads (base64, URL encoding, unicode tricks)
- Multi-language obfuscation (mixed-language attacks)
- Context window stuffing (overwhelming to hide payloads)
- Data exfiltration via tool calls

## Detection layers

### Layer 1 — Pattern matching
- Regex signatures for known attack patterns
- Keyword blacklists (common jailbreak phrases)
- Structural anomalies (unusual formatting, excessive length)

### Layer 2 — Heuristic scoring
- Input entropy analysis (encoded payloads have high entropy)
- Instruction density (too many imperative sentences)
- Role confusion markers (attempts to redefine agent persona)

### Layer 3 — Classifier-based
- Transformer-based classification (e.g., DeBERTa fine-tuned on injection data)
- Semantic similarity to known attack patterns
- Anomaly detection on embedding space

## Integration points

- **PreToolUse hook**: Scan tool inputs before execution
- **Input sanitization**: Clean user inputs before they reach the LLM
- **Output validation**: Check agent responses for data exfiltration
- **Audit logging**: Record detected attempts for security review

## Key principles

- Defense in depth: no single layer is sufficient
- Fail closed: when in doubt, block the input
- Never echo the injection back to the user (reveals detection)
- Log all detections for security monitoring
- Update signatures regularly as attack patterns evolve

## OWASP LLM Top 10 reference

- LLM01:2025 — Prompt Injection (primary)
- LLM02:2025 — Insecure Output Handling (related)
- LLM06:2025 — Excessive Agency (tool call abuse)
