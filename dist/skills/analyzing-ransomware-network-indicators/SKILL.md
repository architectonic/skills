---
name: Analyzing Ransomware Network Indicators
description: Identify ransomware network indicators including C2 beaconing patterns,
tags:
- research
- agent-skill
- okf
- ransomware
- c2-beaconing
- zeek
- netflow
- tor
- exfiltration
- network-forensics
- security
license: Apache-2.0
type: Playbook
---

# Analyzing Ransomware Network Indicators


**Authorized-use only:** Use this skill only for owned systems, sanctioned lab environments, or engagements with explicit written permission. Document scope, preserve evidence, and follow applicable law, policy, and incident-response procedures.

## Overview

Before and during ransomware execution, adversaries establish C2 channels, exfiltrate data, and download encryption keys. This skill analyzes Zeek conn.log and NetFlow data to detect beaconing patterns (regular-interval callbacks), connections to known TOR exit nodes, large outbound data transfers, and suspicious DNS activity associated with ransomware families.


## When to Use

- When investigating security incidents that require analyzing ransomware network indicators
- When building detection rules or threat hunting queries for this domain
- When SOC analysts need structured procedures for this analysis type
- When validating security monitoring coverage for related attack techniques

## Prerequisites

- Zeek conn.log files or NetFlow CSV/JSON exports
- Python 3.8+ with standard library
- TOR exit node list (fetched from Tor Project or threat intel feeds)
- Optional: Known ransomware C2 IOC list

## Steps

1. **Parse Connection Logs** — Ingest Zeek conn.log (TSV) or NetFlow records into structured format
2. **Detect Beaconing Patterns** — Calculate connection interval statistics (mean, stddev, coefficient of variation) to identify periodic callbacks
3. **Check TOR Exit Node Connections** — Cross-reference destination IPs against current TOR exit node list
4. **Identify Data Exfiltration** — Flag connections with unusually high outbound byte ratios to external IPs
5. **Analyze DNS Patterns** — Detect DGA-like domain queries and high-entropy subdomains
6. **Score and Correlate** — Apply composite risk scoring across all indicator types
7. **Generate Report** — Produce structured report with timeline and MITRE ATT&CK mapping

## Expected Output

- JSON report with beaconing detections and interval statistics
- TOR exit node connection alerts
- Data exfiltration flow analysis
- Composite ransomware risk score with MITRE mapping (T1071, T1573, T1041)
