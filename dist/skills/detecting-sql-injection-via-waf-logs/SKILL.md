---
name: Detecting SQL Injection via WAF Logs
description: Analyze WAF (ModSecurity/AWS WAF/Cloudflare) logs to detect SQL injection
tags:
- security-defensive
- software-engineering
- skill
- okf
- waf-log-analysis
- sql-injection-detection
- modsecurity
- aws-waf
- cloudflare-waf
- web-application-security
- security
license: Apache-2.0
type: Playbook
title: Detecting SQL Injection via WAF Logs
domain: security-defensive
risk_level: medium
requires_review: true
source_family: agent-skills-standard
source_license: Apache-2.0
source_status: adapted
---

# Detecting SQL Injection via WAF Logs


## When to Use

- When investigating security incidents that require detecting sql injection via waf logs
- When building detection rules or threat hunting queries for this domain
- When SOC analysts need structured procedures for this analysis type
- When validating security monitoring coverage for related attack techniques

## Prerequisites

- Familiarity with security operations concepts and tools
- Access to a test or lab environment for safe execution
- Python 3.8+ with required dependencies installed
- Appropriate authorization for any testing activities

## Instructions

1. Install dependencies: `pip install requests`
2. Collect WAF logs (ModSecurity audit log, AWS WAF JSON logs, or Cloudflare firewall events).
3. Run the agent to parse and analyze:
   - Detect SQLi payloads via 15+ regex patterns
   - Classify attacks by OWASP injection type (classic, blind, time-based, UNION-based)
   - Identify persistent attackers by IP clustering
   - Correlate multi-request injection campaigns
   - Calculate attack success probability based on response codes

```bash
python scripts/agent.py --log-file /var/log/modsec_audit.log --format modsecurity --output sqli_report.json
```

## Examples

### ModSecurity SQLi Detection
```
Rule 942100 triggered: SQL Injection Attack Detected via libinjection
URI: /api/users?id=1' UNION SELECT username,password FROM users--
Source IP: 203.0.113.42 (47 requests in 5 minutes)
Classification: UNION-based SQLi campaign
```
