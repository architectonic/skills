# Critic report — credential access, phishing, and lateral movement risk triage

- Date: 2026-07-07
- Role: Critic
- Scheduled role: Cataloger
- Selected role: Critic
- Override reason: The 21:00 cadence selected Cataloger, but no catalog queue was open and generated catalog/package surfaces were already coherent at 1182 skills. The concrete open queue was `metadata-backfill-uncategorized-and-unspecified-risk-20260707`; direct inspection found high-risk installed security playbooks where safety review must precede routine metadata backfill or publication endorsement.
- Inspected ref/SHA: `main` at `b51304f08329d1349412c3b7d39666657dc15857`
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
- `dist/catalog.json`
- `dist/catalog.md`
- `dist/install-manifest.json`

`operations/action-runs/discover-skill-sources/latest.json` returned 404 on the default branch, so there was no Action handoff to consume in this pass.

## Package/catalog state observed

- `dist/catalog.json`: 1182 skills; 571 `uncategorized`; 733 `unspecified`; 9 `high`; 431 `medium`.
- `dist/catalog.md`: same summary counts.
- `dist/install-manifest.json`: still points runtime installers to `README.md`, `dist/catalog.json`, `dist/catalog.md`, and `dist/install-manifest.json`.

No catalog/package files were edited in this Critic pass.

## Directly inspected package-facing skills

### `dist/skills/performing-credential-access-with-lazagne/SKILL.md`

Finding: installed package-facing body contains concrete credential-access procedure detail, including tool acquisition/execution and credential extraction workflows. This is not safe for routine metadata backfill as an ordinary medium-risk skill.

Decision: route to Risk Auditor before classification/publication endorsement.

### `dist/skills/performing-initial-access-with-evilginx3/SKILL.md`

Finding: installed package-facing body contains adversary-in-the-middle phishing/session-token capture procedure detail, including phishing infrastructure setup, lure generation, session monitoring, and session hijack guidance.

Decision: route to Risk Auditor before classification/publication endorsement.

### `dist/skills/performing-kerberoasting-attack/SKILL.md`

Finding: installed package-facing body contains Active Directory credential-attack procedure detail, including SPN enumeration, TGS request/extraction, offline cracking, and credential validation steps.

Decision: route to Risk Auditor before classification/publication endorsement.

### `dist/skills/moving-laterally-with-netexec/SKILL.md`

Finding: installed package-facing body contains lateral-movement and credential-abuse procedure detail, including password spraying, pass-the-hash, command execution, credential dumping, and attack-module usage.

Decision: route to Risk Auditor before classification/publication endorsement.

## Queue action

Created high-priority risk queue item:

`risk-review-credential-access-phishing-lateral-movement-skills-20260707`

Risk Auditor should inspect the four package-facing entries and decide whether to redact them into review-gated defensive wrappers, preserve only detection/authorization/audit guidance, mark them reference-only, or block package endorsement.

## Boundaries observed

- No third-party content was copied.
- No external repository was cloned, installed, imported, or executed.
- No live host, tenant, credential, phishing, cracking, or lateral-movement command was run.
- No generated catalog files were hand-edited.
- No npm publication was attempted.

## Value-substance delta

Stopped routine metadata backfill on four high-risk installed package entries and converted the finding into a concrete Risk Auditor queue before classification, catalog endorsement, packaging, or publication. This removes a safety blocker from the metadata backlog by making the risk decision explicit and actionable.