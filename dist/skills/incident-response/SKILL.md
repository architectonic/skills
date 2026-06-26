---
name: incident-response
description: >
type: Playbook
---

# Incident Response

Full lifecycle security incident triage: classify, escalate, collect evidence, notify regulators.

**This is NOT operational incident management** — for outages/degradations, use `incident-commander`. This skill is exclusively for security events.

## Incident Classification (14 Types)

| Type | Default SEV | Response SLA |
|------|-------------|--------------|
| ransomware | SEV1 | 15 minutes |
| data_exfiltration | SEV1 | 15 minutes |
| apt_intrusion | SEV1 | 15 minutes |
| supply_chain_compromise | SEV1 | 15 minutes |
| domain_controller_breach | SEV1 | 15 minutes |
| credential_compromise | SEV2 | 1 hour |
| lateral_movement | SEV2 | 1 hour |
| malware_infection | SEV2 | 1 hour |
| cloud_account_compromise | SEV2 | 1 hour |
| unauthorized_access | SEV3 | 4 hours |
| policy_violation | SEV3 | 4 hours |
| phishing_attempt | SEV4 | 24 hours |

**Auto-escalation triggers:** Ransomware note found, active exfiltration confirmed, CloudTrail/SIEM disabled, domain controller access, second system compromised → all become SEV1.

## Severity Framework

- **SEV1 (Critical):** Confirmed ransomware, active PII/PHI exfiltration (>10K records), DC breach → SOC Lead → CISO → CEO → Board
- **SEV2 (High):** Unauthorized access to sensitive systems, credential compromise with lateral movement → SOC Lead → CISO
- **SEV3 (Medium):** Suspected unauthorized access, contained malware → SOC Lead → Security Manager
- **SEV4 (Low):** No confirmed impact, policy violation without data risk → L3 Analyst queue

## False Positive Filters

1. CI/CD agent activity (jenkins, github-actions, circleci)
2. Test environment tagging (test-, staging-, dev-)
3. Scheduled job patterns (cron, backup_)
4. Whitelisted identities (svc_monitoring, datadog-agent)
5. Known scanners (nessus, qualys, aws_inspector)

A confirmed false positive suppresses escalation and logs the suppression reason for audit.

## Forensic Evidence Collection (DFRWS Framework)

### Six Phases
1. **Identification** — What evidence exists and where
2. **Preservation** — Prevent modification (write-block, snapshot, legal hold)
3. **Collection** — Acquire in order of volatility
4. **Examination** — Technical analysis (within 2 hours)
5. **Analysis** — Interpret findings (within 4 hours)
6. **Presentation** — Findings report with chain of custody

### Volatile Evidence (Collect First)
1. Live memory (RAM dump) — lost on reboot
2. Running processes and open network connections
3. Logged-in users and active sessions
4. System uptime (timeline anchoring)
5. Environment variables and loaded kernel modules

### Chain of Custody
Every evidence item requires: SHA-256 hash, UTC timestamp, tool provenance, investigator identity, transfer log.

## Regulatory Notification Deadlines

| Framework | Incident Type | Deadline |
|-----------|--------------|----------|
| GDPR | Personal data breach | 72 hours |
| PCI-DSS v4.0 | Cardholder data breach | 24 hours to acquirer |
| HIPAA | PHI breach (>500 individuals) | 60 days |
| NY DFS 500 | Cybersecurity event | 72 hours |
| SEC Rule | Material cybersecurity incident | 4 business days |
| NIS2 | Significant incident (essential services) | 24h early warning, 72h notification |

**Operational rule:** If scope is unclear at declaration, assume the most restrictive applicable deadline.

## Anti-Patterns

1. Starting notification clock at investigation completion (not discovery)
2. Containing before collecting volatile evidence (destroys RAM/processes)
3. Skipping false positive verification before escalation
4. Undocumented incident command decisions
5. Treating incident closure as investigation completion
6. Single-source classification (require 2+ independent signals for SEV1)
7. Automated containment without human approval gates
