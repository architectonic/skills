# Catalog report — credential access, phishing, Kerberoasting, and lateral movement redaction verification

- Date: 2026-07-07
- Role: Cataloger
- Scheduled role: Reporter or Critic
- Selected role: Cataloger
- Override reason: The 23:00 cadence allows Reporter or Critic, but `catalog-refresh-after-credential-access-phishing-lateral-redaction-20260707` was the highest-priority open package-health queue item after a high-risk Risk Auditor redaction. Catalog/package health gates override Reporter/Critic while generated catalog and install surfaces need verification.
- Inspected ref/SHA: `main` at `0c7ecc51e98a58332d698566aab0e564a0017b67`
- Model requirement status: `model_setting_unverified`

## Doctrine followed

Read and followed:

- `operations/project-operator-prompt.md`
- `operations/aggregator-loop.md`
- `operations/operator-stability.md`
- `operations/action-runs/discover-skill-sources/README.md`
- `operations/scheduler-online-scout-contract.md`
- `operations/manual-discovery-review-fallback.md`
- `operations/daily/2026-07-07/status.json`
- `operations/daily/2026-07-07/queues.json`
- `operations/log.md`
- `reports/risk/2026-07-07-2213-credential-access-phishing-lateral-redaction.md`
- `dist/catalog.json`
- `dist/catalog.md`
- `dist/install-manifest.json`
- The four affected package-facing `dist/skills/**/SKILL.md` files.

`operations/action-runs/discover-skill-sources/latest.json` returned 404 on the default branch, so there was no discovery Action handoff to consume in this pass. This pass did not run online scouting because the open Cataloger package-health gate outranked discovery and fallback review work.

## Catalog queue consumed

Closed:

`catalog-refresh-after-credential-access-phishing-lateral-redaction-20260707`

The queue was created after Risk Auditor replaced four high-risk package-facing entries with review-gated defensive wrappers and noted generated catalog/install surfaces required role-owned verification.

## Verification results

`dist/catalog.json` and `dist/catalog.md` agree on:

- Skill count: 1182
- `security-offensive`: 16
- `uncategorized`: 567
- `high`: 13
- `medium`: 431
- `unspecified`: 729

`dist/install-manifest.json` remains coherent:

- package name: `architectonic-skills`
- install root: `dist/skills`
- discovery files: `README.md`, `dist/catalog.json`, `dist/catalog.md`, `dist/install-manifest.json`
- selection fields include `slug`, `title`, `domain`, `risk_level`, `tags`, and `requires_review`

The generated catalog includes all four redacted entries under `security-offensive`:

- `performing-credential-access-with-lazagne`
- `performing-initial-access-with-evilginx3`
- `performing-kerberoasting-attack`
- `moving-laterally-with-netexec`

## Package-facing entry verification

Verified each affected `dist/skills/**/SKILL.md` entry has:

- lowercase-hyphen `name`
- `domain: security-offensive`
- `risk_level: high`
- `requires_review: true`
- provenance metadata from `anthropic-cybersecurity-skills`
- package-facing body restricted to defensive review, authorization boundaries, detection mapping, evidence handling, remediation prompts, and explicit disallowed-use boundaries

The package-facing entries no longer expose copyable operational credential-access, phishing/session-capture, Kerberoasting/cracking, password-spraying, pass-the-hash, command-execution, credential-dumping, or lateral-movement procedures.

## Boundaries observed

- No third-party content was copied.
- No external repository was cloned, installed, imported, or executed.
- No live host, tenant, domain, network, account, credential, phishing, cracking, or lateral-movement command was run.
- No generated catalog files were hand-edited.
- No npm publication was attempted.

## Value-substance delta

Verified and closed the package-health blocker created by the 22:13 high-risk redaction. Catalog/install surfaces now consistently expose the four affected entries as high-risk, review-gated, package-facing defensive wrappers rather than executable offensive procedures.

## Next action

Critic can resume `metadata-backfill-uncategorized-and-unspecified-risk-20260707` in a bounded batch. Publication remains blocked by the standing metadata backlog and the absent discovery Action handoff.
