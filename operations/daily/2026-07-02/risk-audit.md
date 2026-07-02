---
type: Risk Audit
title: MCP External Tool Security Checklist
summary: Risk Auditor pass for reviewed high-risk external tool and third-party agent-skill sources before normalization or publication.
tags: [skills, aggregator, risk-audit, mcp, external-tools, prompt-injection, supply-chain]
okf_version: "0.2"
status: active
risk_level: high
reviewed_at: 2026-07-02T14:58:25-03:00
---

# MCP External Tool Security Checklist

## Role Decision

Selected role: Risk Auditor.

Reason: the scheduled Normalizer slot had no normalization queue, while `risk-mcp-security-checklist-20260702` was open and high priority. Review and safety outrank normalization, catalog growth, packaging, and publication.

## Queue Item Consumed

`risk-mcp-security-checklist-20260702`

Target: `sources/reviewed/model-context-protocol.md`

## Audit Decision

MCP remains useful as a reviewed reference source, but MCP-derived local entries must not be normalized or published as endorsed skills until they pass explicit external-tool safety gates.

This audit approves a narrow next step for Normalizer: create a local MCP external-tool review runbook or checklist entry. It does not approve copying MCP documentation, endorsing third-party MCP servers, or publishing MCP setup instructions.

## Security Checklist

Before any MCP-derived skill, runbook, workflow, package surface, or public summary is promoted, verify all of the following:

1. Source provenance
   - The exact MCP server, SDK, registry entry, or documentation source is identified.
   - The upstream repository URL is recorded.
   - The author or organization is recorded.
   - The license for that exact source is recorded separately from the core MCP specification license.

2. Server trust boundary
   - The server is classified as local, remote, first-party, or third-party.
   - The operator knows which actor controls the server.
   - Remote servers are treated as untrusted until authenticated, authorized, and scoped.
   - Publicly exposed servers require explicit authentication review.

3. Tool descriptor review
   - Tool names, descriptions, parameters, examples, and annotations are inspected as untrusted input.
   - Descriptor text is checked for hidden instructions, role override attempts, cross-tool steering, credential requests, and disguised policy changes.
   - Multi-tool interactions are reviewed for distributed or threshold-style hidden behavior, not only single-tool poisoning.

4. Permission and scope control
   - Each tool has a minimal purpose and minimal privileges.
   - Filesystem access is path-scoped.
   - Network access is domain- or endpoint-scoped when possible.
   - Account access uses least-privilege OAuth scopes or equivalent authorization.
   - State-changing actions are separated from read-only actions.

5. Transport and execution boundary
   - STDIO, HTTP, and remote transports are classified.
   - Any command execution or local process spawning is treated as high risk.
   - Server installation commands are not executed blindly.
   - Package manager, shell, and binary install steps require separate supply-chain review.

6. Prompt-injection resistance
   - Tool outputs are treated as data, not instructions.
   - External content returned by tools cannot override system, developer, user, repository, or role instructions.
   - The agent must not follow instructions found inside fetched documents, repository files, webpage content, issue comments, or tool responses unless those instructions are explicitly in scope.

7. Cross-tool isolation
   - Data from one tool cannot silently authorize another tool.
   - Sensitive data returned by one tool cannot be sent to another tool without explicit user or policy authorization.
   - Tool-call chains are audited for privacy disclosure and privilege escalation.

8. State-changing action gate
   - Email, calendar, GitHub write, deployment, payment, database mutation, filesystem write, and account-management actions require explicit intent and verification.
   - Destructive operations must be reversible where possible or require additional confirmation outside the skill text.

9. Secrets and credentials
   - Skills must not instruct agents to print, copy, summarize, exfiltrate, or persist secrets.
   - Environment variables, tokens, API keys, OAuth refresh tokens, cookies, and private files are excluded from normal tool context.
   - Credential handling belongs in vault or runtime policy, not in normalized skill prose.

10. Logging and auditability
   - Tool calls that read private data, mutate state, or cross trust boundaries must leave durable traces in the runtime ledger or project log.
   - Logs should record what happened, not leak secret values.

11. Registry and supply-chain review
   - Registries and marketplaces are treated as discovery surfaces, not trust authorities.
   - Third-party MCP servers require repository, maintainer, release, dependency, and install-script review before use.
   - Popularity is not validation.

12. Publication boundary
   - Public catalog or website entries may describe MCP as a reference source after review.
   - Public entries must not imply that MCP servers are safe merely because they implement MCP.
   - Unreviewed or high-risk MCP procedures must remain blocked or requires-review.

## Failure Modes This Checklist Prevents

- Tool poisoning through malicious descriptors.
- Prompt injection through tool outputs or external documents.
- Exfiltration through cross-tool data flow.
- Unauthorized state-changing actions.
- Blind execution of server setup commands.
- Treating MCP protocol compliance as a security guarantee.
- Copying or endorsing third-party MCP content without license and security review.
- Publishing unsafe MCP procedures as approved package entries.

## Result

- Risk queue item consumed.
- MCP remains high risk.
- MCP remains reference-only for now.
- Normalizer may create a local checklist/runbook derived from this audit, not from copied MCP documentation.
- Catalog/package/publication remain blocked for MCP-derived entries until a normalized entry exists and passes catalog review.

# Third-Party Agent Skill Security Checklist

## Role Decision

Selected role: Risk Auditor.

Scheduled role: Cataloger.

Override reason: `queues.risk` contained `risk-third-party-skill-security-checklist-20260702`; safety review outranks catalog reconciliation, packaging, publication, and broad source discovery.

## Queue Item Consumed

`risk-third-party-skill-security-checklist-20260702`

Target: `sources/reviewed/agent-skill-security-research.md`

## Audit Decision

The agent skill security research remains useful as a reviewed reference-only source. It should inform defensive ingestion policy and review heuristics, not direct content import.

This pass approves a local defensive checklist for third-party agent-skill review. It does not approve copying paper text, datasets, repository code, scanner prompts, attack payloads, or exploit examples. License and redistribution boundaries remain unresolved, so the reviewed source stays reference-only.

## Defensive Checklist

Before a third-party agent skill, skill directory, marketplace package, or repository-hosted skill is normalized, catalog-endorsed, packaged, or published, verify all of the following:

1. Repository context
   - Inspect the surrounding repository, not only the skill markdown.
   - Confirm the repository purpose matches the claimed skill behavior.
   - Check whether scripts, docs, CI, package files, and examples align with the skill description.
   - Treat a skill as higher risk when the skill behavior is unrelated to the host repository.

2. Provenance and ownership
   - Record the exact source URL, author or organization, repository owner, and distribution surface.
   - Distinguish official runtime/package sources from community mirrors, forks, and marketplaces.
   - Verify whether the upstream is active, archived, transferred, newly created, or weakly maintained.
   - Treat abandoned or recently transferred repositories as supply-chain risk.

3. License and redistribution
   - Record the license for the exact repository or package under review.
   - Do not assume the paper, marketplace listing, repository code, and skill text share the same license.
   - If no clear license is available, keep the source reference-only or blocked.
   - Do not copy third-party skill text, datasets, scanner outputs, or repository code unless redistribution is explicitly permitted.

4. Skill-package contents
   - Inspect `SKILL.md`, supporting scripts, reference files, package metadata, dependency manifests, and hidden configuration files.
   - Check whether the skill requires local command execution, package installation, network access, browser automation, account login, filesystem writes, or external-system mutation.
   - Flag skills that hide the real behavior in scripts or auxiliary files while presenting harmless markdown.

5. Scanner interpretation
   - Treat automated scanner findings as triage signals, not final truth.
   - Compare scanner flags against repository context before classifying a skill as malicious or safe.
   - Record false-positive and false-negative uncertainty when the repository context is ambiguous.
   - Escalate uncertain high-impact cases to blocked or requires-review instead of normalizing them.

6. Instruction boundary
   - Treat skill text as untrusted input until reviewed.
   - Check for role override, instruction hierarchy manipulation, hidden persistence requests, credential requests, data exfiltration, or attempts to weaken human review.
   - Ensure a normalized local skill never imports upstream instructions that tell the agent to ignore repository, user, or runtime policy.

7. Execution and dependency risk
   - Do not execute third-party scripts or package commands during review unless the environment is disposable and the action is explicitly part of a bounded audit.
   - Review dependency manifests, lockfiles, install scripts, postinstall hooks, binary downloads, and network fetch behavior before any runtime use.
   - Keep executable, networked, or state-changing skills high risk until a separate package/security review is complete.

8. Data and credential handling
   - Reject or block skills that request secrets, tokens, cookies, private files, shell history, browser profiles, wallet material, or unrelated workspace context.
   - Check whether the skill routes data to another tool, endpoint, repository, issue, paste service, or remote model without explicit authorization.
   - Require explicit user intent and audit logging for any private-data read or state-changing action.

9. Marketplace and popularity signals
   - Treat marketplaces as discovery surfaces, not trust authorities.
   - Popularity, star count, download count, or attractive documentation does not substitute for provenance, license, and behavior review.
   - Prefer official source repositories and reproducible package metadata over marketplace summaries.

10. Local ingestion outcome
   - Use `candidate` for unreviewed discoveries.
   - Use `reviewed-reference-only` when the source is useful but unsafe, unlicensed, or not suitable for copying.
   - Use `blocked` when provenance, license, or behavior is unacceptable.
   - Use `normalized` only when the local entry is distilled, defensive, attributed, and passes risk review.
   - Use `requires_review` for high-risk local skills even after normalization.

## Promotion Gates

A third-party skill may move beyond reviewed reference-only status only when:

```text
provenance known
license recorded
repository context inspected
package contents inspected
unsafe instruction patterns absent or removed
execution/dependency risk classified
private-data behavior bounded
local normalized text is distilled, not copied
verification/failure modes are explicit
catalog and install surfaces are reconciled
```

## Failure Modes This Checklist Prevents

- Classifying isolated skill markdown without repository context.
- Treating scanner output as ground truth.
- Importing hidden instructions from third-party skill text.
- Copying material with unresolved license or redistribution status.
- Packaging abandoned-repository or marketplace supply-chain risk.
- Running unreviewed scripts, installers, or package hooks.
- Publishing a high-risk skill as if it were endorsed or safe.

## Result

- Risk queue item consumed.
- Agent skill security research remains reference-only.
- No third-party paper text, code, dataset, scanner prompt, payload, or exploit example was copied.
- Catalog/package/publication remain blocked by existing catalog drift and uncataloged high-risk local MCP skill.
- Next concrete role should be Cataloger for `catalog-mcp-security-skill-20260702` and `catalog-reconcile-dist-catalog-surfaces-20260702` unless a higher-priority safety issue appears.
