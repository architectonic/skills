# MCP Tool Poisoning / SSRF Skill Risk Review — 2026-07-08

## Decision

Ticket `skills-risk-review-mcp-tool-poisoning-001` is **done with package-facing wrapper required**.

The skill can remain in the package only as a high-risk, authorized-use-only defensive review playbook. The package-facing body was rewritten to remove default executable probing recipes, explicit internal/metadata/loopback target examples, unauthenticated endpoint probing commands, and executable MCP server call snippets.

## Inspected state

- Repository: `architectonic/skills`
- Inspected ref: `main`
- Inspected SHA before this ticket's content write: `f3d8e7fed190f8da6471f427bf906b048d90cf4f`
- Model requirement status: `model_setting_unverified`
- Daily ledger present: yes
- Missing-ledger initialization: no
- Discovery Action handoff: `operations/action-runs/discover-skill-sources/latest.json` absent on default branch
- Online searches used: none
- External connector used: GitHub only

## Files inspected directly

- `operations/heartbeat.md`
- `operations/board.json`
- `operations/gates.md`
- `operations/value-ledger.json`
- `operations/daily/2026-07-08/status.json`
- `operations/daily/2026-07-08/queues.json`
- `operations/daily/2026-07-08/report.md`
- `operations/log.md`
- `dist/catalog.json`
- `dist/install-manifest.json`
- `dist/catalog.md`
- `dist/skills/auditing-mcp-servers-for-tool-poisoning/SKILL.md`
- `reports/critic/2026-07-08-0912-mcp-tool-poisoning-ssrf-risk-triage.md`

## Risk classification

| Field | Result |
|---|---|
| Risk level | `high` |
| Requires review | `true` |
| Domain | `security-defensive` |
| Package state | Allowed only as authorization-gated defensive wrapper |
| Publication state | Still blocked until catalog parity is refreshed and discovery/risk gates are clean |

## Findings

### 1. Default package-facing body included executable probing detail

The previous package-facing skill contained direct commands and code snippets for scanning MCP configs, enumerating tool descriptions, calling MCP tools programmatically, probing SSRF-sensitive targets, and checking unauthenticated network exposure.

That content has defensive value, but as a package-facing skill it created an unsafe default: consumers could run active tests against systems without explicit authorization or copy reusable target probes into inappropriate contexts.

**Resolution:** replaced the body with a high-risk defensive review wrapper that requires authorization, static/design review first, owner-controlled evidence, and explicit test depth before any active validation.

### 2. SSRF testing needed to be reframed

The previous body listed concrete internal/metadata/loopback/file targets. Those examples were removed from the package-facing artifact.

**Resolution:** the revised skill now requires design review of URL-fetching controls first and limits active validation to owner-approved environments using benign owner-controlled canary endpoints. It avoids reusable target payload lists.

### 3. Unauthenticated exposure checks needed authorization gating

The previous body included direct network commands for endpoint exposure checks. Those were removed from the package-facing artifact.

**Resolution:** the revised skill now instructs reviewers to use configuration, gateway policy, deployment manifests, owner-provided evidence, or explicitly authorized minimal checks.

### 4. Prompt-injection/tool-poisoning inspection remains useful

Tool-description review is still valuable and remains in the playbook, but malicious excerpts should be short and evidence-scoped rather than copied wholesale.

**Resolution:** the revised skill keeps static metadata inspection, fingerprinting, severity scoring, and remediation reporting.

## Package-facing changes made

Updated `dist/skills/auditing-mcp-servers-for-tool-poisoning/SKILL.md`:

- added `domain: security-defensive`;
- added `risk_level: high`;
- added `requires_review: true`;
- added `review_gate: authorized-security-review-only`;
- removed duplicate `software-development` tag;
- reframed the description as authorized, non-exploitative evidence collection;
- removed default executable snippets for MCP server calls and SSRF probing;
- removed internal/metadata/loopback/file target examples;
- removed direct unauthenticated endpoint probing commands;
- preserved defensive audit workflow, threat taxonomy, fingerprinting, reporting, and remediation structure.

## Acceptance tests

| Test | Result | Evidence |
|---|---|---|
| Classifies risk level and `requires_review` | Pass | Frontmatter now includes `risk_level: high` and `requires_review: true`. |
| Removes default executable SSRF/probing detail if unsafe | Pass | Package-facing body no longer includes SSRF target lists, executable MCP tool-call scripts, or default unauthenticated endpoint probe commands. |
| Preserves defensive audit framing | Pass | Revised workflow retains authorization scope, static tool-description review, fingerprinting, SSRF design review, auth/exposure review, runtime guardrail assessment, and remediation reporting. |
| Creates catalog-refresh ticket if package-facing metadata changed | Pass | `skills-catalog-refresh-after-risk-review-001` is promoted to ready because skill frontmatter changed and generated catalog surfaces were not hand-edited in this pass. |

## Boundaries preserved

- No third-party content was copied.
- No repository was cloned.
- No code, MCP server, scanner, curl command, or endpoint probe was executed.
- No online search was used.
- No generated catalog surface was hand-edited.
- No package publication or npm action was attempted.

## Value-substance delta

Removed a live package-facing risk blocker by converting a high-risk MCP/tool-poisoning and SSRF audit skill into a review-gated defensive wrapper. This is substantive package-safety value, not status churn.

## Next action

Cataloger should consume `skills-catalog-refresh-after-risk-review-001` and refresh or verify `dist/catalog.json`, `dist/catalog.md`, and `dist/install-manifest.json` after the skill metadata/body change.
