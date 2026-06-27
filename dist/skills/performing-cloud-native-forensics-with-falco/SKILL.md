---
name: Performing Cloud Native Forensics with Falco
description: Uses Falco YAML rules for runtime threat detection in containers and
tags:
- security-defensive
- software-engineering
- skill
- okf
- cloud-security
- falco
- runtime-threat-detection
- container-forensics
- kubernetes-security
- syscall-monitoring
- security
license: Apache-2.0
type: Playbook
title: Performing Cloud Native Forensics with Falco
domain: security-defensive
risk_level: medium
requires_review: true
source_family: agent-skills-standard
source_license: Apache-2.0
source_status: adapted
---

# Performing Cloud Native Forensics with Falco


## When to Use

- When conducting security assessments that involve performing cloud native forensics with falco
- When following incident response procedures for related security events
- When performing scheduled security testing or auditing activities
- When validating security controls through hands-on testing

## Prerequisites

- Familiarity with cloud security concepts and tools
- Access to a test or lab environment for safe execution
- Python 3.8+ with required dependencies installed
- Appropriate authorization for any testing activities

## Instructions

Deploy and manage Falco rules for runtime security detection in containerized
environments. Parse Falco alerts for incident response.

```yaml
# Custom Falco rule for detecting shell in container
- rule: Shell Spawned in Container
  desc: Detect shell process started in a container
  condition: >
    spawned_process and container
    and proc.name in (bash, sh, zsh, dash, csh)
    and not proc.pname in (docker-entrypo, supervisord)
  output: >
    Shell spawned in container
    (user=%user.name command=%proc.cmdline container=%container.name
     image=%container.image.repository)
  priority: WARNING
  tags: [container, shell, mitre_execution]
```

Key detection rules:
1. Shell spawn in non-interactive containers
2. Sensitive file access (/etc/shadow, /etc/passwd)
3. Outbound connections from unexpected containers
4. Privilege escalation via setuid/setgid
5. Container escape via mount or ptrace

## Examples

```bash
# Run Falco with custom rules
falco -r /etc/falco/custom_rules.yaml -o json_output=true
# Parse JSON alerts
cat /var/log/falco/alerts.json | python3 -c "import json,sys; [print(json.loads(l)['output']) for l in sys.stdin]"
```
