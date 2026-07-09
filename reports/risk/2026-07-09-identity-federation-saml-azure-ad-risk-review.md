---
type: RiskReview
title: Identity Federation SAML Azure AD Risk Review
status: complete
date: 2026-07-09
ticket: skills-risk-review-identity-federation-saml-azure-ad-001
role: Risk Auditor
---

# Identity Federation SAML Azure AD Risk Review

## Ticket consumed

- Board ticket: `skills-risk-review-identity-federation-saml-azure-ad-001`
- Selected role: `Risk Auditor`
- Inspected ref/SHA: `main` at `42faade63f0879f9e0e216a39d7f4d4adabd36cd`
- External source/action use: none beyond GitHub repository reads/writes

## Inputs reviewed directly

- `operations/heartbeat.md`
- `operations/board.json`
- `operations/gates.md`
- `operations/value-ledger.json`
- `operations/action-runs/discover-skill-sources/latest.json` attempted and absent
- `operations/daily/2026-07-09/status.json`
- `operations/daily/2026-07-09/queues.json`
- `operations/daily/2026-07-09/report.md`
- `operations/log.md`
- `dist/catalog.json`
- `dist/catalog.md`
- `dist/install-manifest.json`
- `dist/skills/building-identity-federation-with-saml-azure-ad/SKILL.md`
- `reports/critic/2026-07-09-metadata-backfill-batch-007.md`

## Risk surfaces classified

Direct review found legitimate enterprise identity-administration material that is unsafe as ungated package-facing skill content:

- AD FS role installation, farm creation, federation-service configuration, and federation endpoint exposure.
- Microsoft Graph `Domain.ReadWrite.All` style tenant/domain mutation authority.
- Managed-domain to federated-domain conversion and federation configuration payloads.
- AD FS relying-party trust creation and claims-rule mutation for Microsoft 365 / Entra federation.
- Token-signing certificate promotion, rollover, removal, and related signing material operations.
- Public federation metadata, MEX, passive sign-in, sign-out, and SSO endpoint dependencies.
- Production SSO, MFA, conditional-access, smart-lockout, extranet-lockout, break-glass, and account-control boundaries.

These surfaces can lock out users, redirect authentication authority, weaken authentication, expose signing material, or mutate tenant/domain identity state. They require explicit review before implementation, package endorsement, or publication.

## Package-facing remediation

Converted `dist/skills/building-identity-federation-with-saml-azure-ad/SKILL.md` into a high-risk, `requires_review: true`, defensive governance wrapper.

Removed or review-gated package-facing:

- AD FS installation and farm configuration commands.
- Microsoft Graph connection and domain-write command examples.
- Federated-domain conversion payloads.
- Relying-party trust scripts.
- Claims-rule mutation snippets.
- Token-signing certificate rotation/removal commands.
- Public endpoint setup instructions.
- Production tenant/account-control implementation steps.

Preserved useful safe material:

- identity federation purpose and model framing;
- high-level risk classification;
- defensive planning, approval, rollback, and monitoring guidance;
- break-glass, certificate lifecycle, claims review, and pilot-validation checklists;
- references to primary public documentation without copying implementation content.

## Acceptance tests

| Test | Result | Evidence |
|---|---|---|
| AD FS farm setup and federation service configuration surfaces are classified | Pass | AD FS farm/service setup and public federation endpoint exposure are explicitly classified as high-risk and removed from package-facing implementation steps. |
| Microsoft Graph `Domain.ReadWrite.All` and federated-domain mutation surfaces are classified | Pass | Tenant/domain mutation authority and managed/federated conversion payloads are classified and removed from executable guidance. |
| Relying-party trust, claims-rule, token-signing certificate, metadata endpoint, and production SSO/account-control boundaries are classified | Pass | Trusts, claims, signing material, metadata endpoints, SSO, MFA, lockout, break-glass, and account-control surfaces are listed as high-risk review-gated boundaries. |
| Safe defensive identity-governance guidance is preserved or bounded | Pass | The rewritten skill retains governance flow, review checklist, design principles, monitoring, rollback, and approved-use boundaries. |
| Catalog refresh remains blocked until review completes | Pass | No generated catalog file was edited in this ticket; catalog parity is queued as the next board ticket. |

## Decision

- `skills-risk-review-identity-federation-saml-azure-ad-001`: done.
- Risk queue: clear.
- Catalog parity is required next because the skill frontmatter now declares `domain: security-defensive`, `risk_level: high`, and `requires_review: true`.
- No package, npm, registry, publication, Azure, Microsoft Graph, AD FS, tenant, DNS, certificate, or account-control external action occurred.

## Value delta

Removed the identity-federation/account-control package risk blocker while preserving safe defensive governance guidance.

## Next action

Cataloger should consume `skills-catalog-refresh-after-metadata-backfill-007` before any further metadata backlog cleanup, package endorsement, or publication work.
