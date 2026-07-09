---
name: Building Identity Federation with SAML Azure AD
description: Review-gated defensive governance guidance for SAML and Microsoft Entra ID federation without exposing tenant mutation commands, signing-certificate operations, or production account-control procedures.
tags: [security-defensive, identity, saml, azure-ad, entra-id, federation, sso, adfs, hybrid-identity, governance, review-gated]
license: Apache-2.0
type: Playbook
domain: security-defensive
risk_level: high
requires_review: true
source_status: package_risk_reviewed
reviewed_at: 2026-07-09
reviewed_by: Skills Value Operator
---

# Building Identity Federation with SAML Azure AD

## Purpose

Use this skill to review or plan SAML federation between on-premises identity infrastructure, AD FS or a third-party IdP, and Microsoft Entra ID. It is intentionally review-gated because federation changes authentication authority, tenant/domain state, relying-party trusts, claims issuance, signing material, metadata endpoints, and production SSO/account-control behavior.

This package-facing version is a defensive governance wrapper. It does not provide AD FS farm installation commands, Microsoft Graph tenant mutation commands, federation conversion payloads, relying-party trust scripts, claims-rule mutation snippets, token-signing certificate rotation/removal commands, or public endpoint deployment steps.

## Allowed Use

Use this skill when you need to:

- scope a defensive identity-federation review;
- identify approval gates before changing federation, SAML, tenant, domain, claims, certificates, or SSO behavior;
- compare managed, pass-through, federated, and third-party IdP models at an architecture level;
- document safe rollout, rollback, monitoring, and disaster-recovery requirements;
- review whether a proposed federation change has the right owners, test plan, audit trail, and break-glass path.

Do not use this skill to make live tenant, domain, AD FS, Microsoft Graph, certificate, DNS, claims-rule, or account-control changes without explicit authorization, change control, tested rollback, and a qualified identity administrator.

## Risk Classification

High-risk surfaces requiring review:

- AD FS role installation, farm creation, federation-service configuration, or proxy exposure;
- Microsoft Graph permissions such as domain write scopes or any tenant/domain mutation authority;
- converting a domain between managed, pass-through, and federated authentication;
- relying-party trust creation or mutation for Microsoft 365, Entra ID, or SaaS applications;
- claims-rule design that changes identifiers, NameID, UPN, email, group, role, or authorization claims;
- token-signing, token-decrypting, TLS, and metadata-signing certificate lifecycle operations;
- public federation metadata, MEX, sign-in, sign-out, and assertion consumer endpoints;
- conditional-access, MFA, smart-lockout, extranet-lockout, break-glass, and fallback-account behavior;
- any production SSO change that can lock out users, weaken authentication, or redirect authentication trust.

## Safe Design Principles

1. **Preserve change control.** Treat federation changes as production identity changes requiring approval, maintenance windows, rollback, and owner sign-off.
2. **Separate planning from execution.** Architecture review, test plans, and runbooks should be reviewed before any administrator runs tenant or AD FS commands.
3. **Prefer least privilege.** Use scoped, time-bound administrative access and avoid persistent broad tenant/domain write permissions.
4. **Keep break-glass independent.** Emergency access accounts should remain outside the federation dependency chain and be monitored separately.
5. **Stage before production.** Validate claims, certificates, metadata, MFA, lockout, fallback, and user experience in a non-production or pilot scope first.
6. **Protect signing material.** Certificate private keys, thumbprints, rollover timing, and metadata publication should be handled as sensitive operational material.
7. **Audit decisions, not secrets.** Record approvers, scope, timestamps, test results, rollback state, and affected domains without embedding credentials or private key material.
8. **Monitor both sides of trust.** Identity-provider health, Entra sign-in logs, certificate expiry, metadata reachability, lockout events, and relying-party errors should all be visible before rollout.

## Review Checklist

Before a SAML or Entra federation change is approved, confirm:

- the business reason and affected domains, applications, users, and administrators are documented;
- identity, security, operations, and application owners have approved the change;
- non-production or pilot validation covers login, logout, MFA, claims, session lifetime, and failure modes;
- break-glass accounts are tested and excluded from the federation dependency chain;
- claims mapping has been reviewed for privacy, authorization, and application compatibility;
- certificate ownership, expiry, rollover, backup, and rollback responsibilities are assigned;
- DNS, TLS, public endpoint, and metadata dependencies are mapped and monitored;
- conditional access, smart lockout, extranet lockout, and audit logging are configured according to policy;
- rollback to a known-good authentication model is documented and tested;
- the implementation plan avoids storing credentials, tenant tokens, private keys, or raw production payloads in skill content, tickets, or logs.

## Recommended Governance Flow

A safe federation program should be staged as follows:

1. **Scope:** identify the domain, identity provider, relying parties, user groups, and applications affected.
2. **Classify:** mark the change as production identity/account-control work and assign risk owners.
3. **Design:** document the intended federation model, claims, certificates, endpoints, fallback, and monitoring.
4. **Review:** require security and identity-administration approval before any live change.
5. **Pilot:** validate with constrained users and noncritical applications before broad rollout.
6. **Deploy:** execute only through an approved runbook by authorized administrators.
7. **Observe:** monitor sign-in success, failures, lockouts, certificate status, metadata reachability, and application errors.
8. **Rollback:** keep an approved path to restore managed/pass-through authentication or alternate access if federation fails.

## Disallowed Package-Facing Content

Do not include the following in this distributable skill without a separate reviewed implementation package:

- AD FS installation or farm configuration commands;
- Microsoft Graph connection examples with tenant/domain write permissions;
- managed-to-federated or federated-to-managed domain mutation payloads;
- relying-party trust creation scripts;
- claims-rule scripts or production claim transformation code;
- token-signing certificate promotion, removal, or private-key handling commands;
- public federation endpoint deployment steps;
- instructions that disable, redirect, or weaken production authentication controls.

## References

- Microsoft Entra federation documentation: https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/whatis-fed
- AD FS design guidance: https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/design/ad-fs-design-guide
- OASIS SAML 2.0 specification: https://docs.oasis-open.org/security/saml/v2.0/
