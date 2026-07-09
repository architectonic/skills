---
name: Building Attack Pattern Library from CTI Reports
description: Review-gated defensive guidance for turning authorized CTI reports into internal detection-engineering knowledge without operationalizing adversary procedures.
tags: [agent-skill, okf, cti-reports, attack-patterns, detection-engineering, mitre-attack, stix, sigma, defensive-security]
license: Apache-2.0
type: Playbook
domain: security-defensive
risk_level: high
requires_review: true
source_status: package-facing-risk-reviewed
review_status: authorized-defensive-cti-use-only
---

# Building Attack Pattern Library from CTI Reports

## Safety boundary

Use this skill only to organize authorized defensive threat-intelligence material for detection engineering, controls mapping, and analyst review. The output must reduce defensive ambiguity without reproducing instructions that enable intrusion, evasion, credential theft, lateral movement, command-and-control, malware operation, or offensive automation.

This skill is not a procedure generator. Do not transform CTI narratives into executable attack recipes, intrusion playbooks, exploit chains, payload logic, malware behavior implementations, or deployable offensive tooling.

## When to use

- Build an internal defensive library of behaviors described in licensed or public CTI.
- Map observed behaviors to defensive taxonomy such as ATT&CK tactics, techniques, data sources, and controls.
- Identify telemetry gaps and detection opportunities.
- Help analysts compare incidents against known behavioral patterns.

## Review requirements

Before adding a report or generated library entry, confirm:

1. The CTI source is public, licensed, or internally authorized for reuse.
2. Attribution and redistribution boundaries are clear.
3. Extracted details are defensive and do not preserve operational attack instructions.
4. Malware names, tool names, and procedure descriptions are necessary for detection context and not framed as how-to guidance.
5. Generated detection templates are analyst-reviewed before deployment.

## Safe workflow

### 1. Source intake

Record source metadata, license or permission status, publication date, confidence, and sensitivity. Do not ingest leaked, private, paywalled, or contract-restricted reports unless the repository is authorized to store derived notes.

### 2. Extract defensive observations

Summarize adversary behavior at a defensive abstraction level:

- tactic and technique category;
- observable behavior;
- affected platform or control plane;
- relevant telemetry source;
- defensive detection idea;
- confidence and source reference.

Avoid preserving command syntax, exploit steps, payload logic, credential material, infrastructure setup, or adversary tradecraft in operational sequence form.

### 3. Map to defensive controls

Map each behavior to detection and prevention controls, such as endpoint telemetry, identity logs, network logs, email security controls, cloud audit logs, hardening baselines, and response playbooks.

### 4. Draft detection hypotheses

Create non-executable hypotheses for analyst review. A hypothesis should state what behavior may be visible, where evidence may appear, and what false positives are expected. Do not publish deployable rules until tested in a controlled defensive environment.

### 5. Review before sharing

Before adding entries to a package-facing catalog or shared library, review for:

- source permission and attribution;
- absence of offensive procedure reproduction;
- removal of unnecessary malware/tool operational details;
- clear defensive purpose;
- analyst approval for any detection templates.

## Allowed outputs

- Defensive behavior summaries.
- ATT&CK mapping notes with confidence levels.
- Telemetry and data-source gap analysis.
- Detection hypotheses for analyst review.
- Internal control-improvement backlog items.

## Blocked package-facing content

This package-facing skill intentionally omits:

- executable CTI parsers or extraction scripts;
- hard-coded malware, tool, or command pattern lists intended to reconstruct adversary procedures;
- STIX bundle generation code;
- Sigma, YARA, Snort, or other rule-generation code;
- offensive sequence reconstruction;
- instructions that convert narratives into replayable attack chains.

Those may be appropriate only in a controlled internal detection-engineering repository with source rights, review controls, and deployment testing.

## Acceptance checklist

- Source rights and attribution are documented.
- Extracted entries are defensive abstractions.
- Operational attack instructions are excluded.
- Detection content is review-gated before deployment.
- The library improves analyst reviewability rather than enabling procedure reproduction.
