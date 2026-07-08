# Risk report — credential access, phishing, Kerberoasting, and lateral movement redaction

- Date: 2026-07-07
- Role: Risk Auditor
- Scheduled role: Critic
- Selected role: Risk Auditor
- Override reason: The 22:00 cadence selected Critic, but `risk-review-credential-access-phishing-lateral-movement-skills-20260707` was the highest-priority open queue item. Safety review outranks Critic metadata backfill, catalog/package work, publication, and discovery.
- Inspected ref/SHA: `main` at `50015279a56cf1ee7c5f075ccf4703e48cfe0768`
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
- `reports/critic/2026-07-07-2111-credential-access-phishing-lateral-risk-triage.md`
- The four affected package-facing `dist/skills/**/SKILL.md` files.

`operations/action-runs/discover-skill-sources/latest.json` returned 404 on the default branch, so there was no discovery Action handoff to consume in this pass. This pass did not run manual discovery because the open high-priority risk queue outranked broad discovery and metadata fallback.

## Risk queue consumed

Closed:

`risk-review-credential-access-phishing-lateral-movement-skills-20260707`

The queue was created by the prior Critic pass after direct package-facing inspection found concrete procedure detail for credential extraction, adversary-in-the-middle phishing/session capture, Kerberoasting/offline cracking, password spraying, pass-the-hash, remote command execution, credential dumping, and lateral movement.

## Decisions

### `dist/skills/performing-credential-access-with-lazagne/SKILL.md`

Decision: replaced the default installed credential-access procedure with a high-risk, review-gated defensive wrapper.

Rationale: the previous package-facing body included tool acquisition/execution, credential extraction modules, output parsing, credential prioritization, and credential validation guidance. That is not suitable as default installed automation.

Allowed package-facing value after redaction: authorization review, defensive scope planning, credential-store exposure mapping, detection prompts, evidence-handling boundaries, and remediation prompts.

### `dist/skills/performing-initial-access-with-evilginx3/SKILL.md`

Decision: replaced the default installed AiTM phishing/session-capture procedure with a high-risk, review-gated defensive wrapper.

Rationale: the previous package-facing body included phishing infrastructure setup, phishlet/lure setup, delivery guidance, session monitoring, cookie extraction, session hijack validation, and post-access activity guidance. That is not suitable as default installed automation.

Allowed package-facing value after redaction: identity-control review, phishing-resistant MFA planning, session-security detection prompts, certificate/domain monitoring prompts, incident-response boundaries, and remediation prompts.

### `dist/skills/performing-kerberoasting-attack/SKILL.md`

Decision: replaced the default installed Kerberoasting procedure with a high-risk, review-gated defensive wrapper.

Rationale: the previous package-facing body included SPN enumeration, ticket request/extraction, offline cracking mode guidance, credential validation, and privilege/path mapping. That is not suitable as default installed automation.

Allowed package-facing value after redaction: service-account hygiene review, Kerberos telemetry planning, encryption/password-policy risk prompts, evidence boundaries, and remediation prompts.

### `dist/skills/moving-laterally-with-netexec/SKILL.md`

Decision: replaced the default installed NetExec lateral-movement procedure with a high-risk, review-gated defensive wrapper.

Rationale: the previous package-facing body included password spraying, credential validation, pass-the-hash, remote command execution, credential dumping, attack-module usage, and lateral-movement workflows. That is not suitable as default installed automation.

Allowed package-facing value after redaction: defensive scope planning, remote-service exposure review, lockout-safety boundaries, detection prompts, identity hardening, segmentation review, and remediation prompts.

## Queue action

Created Cataloger queue item:

`catalog-refresh-after-credential-access-phishing-lateral-redaction-20260707`

Cataloger should verify or rebuild `dist/catalog.json`, `dist/catalog.md`, and `dist/install-manifest.json` after the four `dist/skills/**` changes, then confirm the affected entries are high risk, require review, and expose only defensive review-gated wrappers.

## Boundaries observed

- No third-party content was copied.
- No external repository was cloned, installed, imported, or executed.
- No live host, tenant, domain, network, account, credential, phishing, cracking, or lateral-movement command was run.
- No generated catalog files were hand-edited.
- No npm publication was attempted.

## Value-substance delta

Removed default installed procedure bodies for four high-risk security entries and converted them into package-facing review-gated defensive wrappers. This preserves defensive planning value while removing copyable offensive credential-access, phishing/session-hijack, Kerberoasting/cracking, and lateral-movement automation from the default install surface.
