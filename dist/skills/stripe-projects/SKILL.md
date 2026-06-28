---
name: stripe-projects
description: "Provision SaaS services and sync credentials via Stripe Projects CLI."
tags: [payments, stripe, projects, provisioning, infrastructure, okf]
type: Playbook
---

# Stripe Projects

Provision SaaS services (Neon, Twilio, Vercel, etc.), generate/sync credentials into `.env`, and manage billing across providers from one Stripe Projects vault.

## Trigger

- user says "set up ", "provision ", "create a database"
- user asks for providers, credentials, key rotation, plan upgrades
- user wants to link an existing provider resource

## Inputs

- Stripe CLI installed (`stripe`)
- Stripe Projects plugin installed (`stripe plugin install projects`)
- Stripe account (CLI guides sign-in on first run)

## Procedure

1. Initialize the project:
   ```
   cd <project_dir>
   stripe projects init
   ```
   Creates `.projects/vault/vault.json` (encrypted credential store).

2. Discover available providers:
   ```
   stripe projects catalog
   ```

3. Add a service:
   ```
   stripe projects add <provider>/<service>
   ```
   Examples:
   - `stripe projects add neon/postgres`
   - `stripe projects add twilio/sms`
   - `stripe projects add runloop/sandbox`

   CLI provisions the service, generates credentials, syncs to `.env`, records in vault.

4. Verify:
   ```
   stripe projects list
   ```

5. Manage / upgrade / remove:
   ```
   stripe projects upgrade <provider>/<service>
   stripe projects remove <provider>/<service>
   stripe projects rotate <provider>/<service>
   ```

## Verification

```
stripe projects --version && stripe projects list
```

Exit code 0 inside an initialized project means healthy.

## Failure Modes

- `.env` writes are real writes — check `.gitignore` first or keys land in VCS.
- Per-project state: same service in two projects = two resources + two bills.
- Billing happens on Stripe side — tier prompts during `add`/`upgrade` are real charges. Surface before confirming.
- Provider catalog changes — `stripe projects catalog | grep <name>` before `add`.
- Removing a service does NOT always destroy the underlying resource. Check provider dashboard after `remove` for high-cost services.
- Credentials in vault are encrypted; `.env` is plaintext. Standard `.env` hygiene applies.
