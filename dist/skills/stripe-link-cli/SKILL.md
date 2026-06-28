---
name: stripe-link-cli
description: "Agent payments via Stripe Link — virtual cards, Shared Payment Tokens, in-app approval flow."
tags: [payments, stripe, link, checkout, mpp, okf]
type: Playbook
---

# Stripe Link CLI

Pay merchants on the user's behalf via `@stripe/link-cli`. Supports one-time-use web checkout (card) and HTTP 402 Shared Payment Token (SPT) flows. Every spend requires in-app approval — Hermes cannot self-approve.

US-only (Link account requirement). Windows unsupported by upstream CLI.

## Trigger

- user says "buy X", "pay for X", "make a purchase", "complete checkout"
- user asks for a card, payment method, or to connect Link wallet
- HTTP 402 response with `www-authenticate: ... method="stripe"`

## Inputs

- Node.js 20+ on `PATH`
- US-based (Link account requirement)
- Link account, payment method, and approval app (CLI walks through on first run)

## Procedure

1. Check / establish auth:
   ```
   link-cli auth status
   ```
   If not authenticated:
   ```
   link-cli auth login --client-name "Hermes" --interval 5 --timeout 300
   ```
   **Do not proceed until `auth status` confirms login.**

2. Evaluate the merchant:

   | Merchant surface | `--credential-type` |
   |---|---|
   | Web checkout / Stripe Elements | `card` (default) |
   | HTTP 402 with `method="stripe"` | `shared_payment_token` |
   | HTTP 402 without `method="stripe"` | unsupported — stop |

   Decode 402 challenge:
   ```
   link-cli mpp decode --challenge '<WWW-Authenticate header>'
   ```

3. List payment methods + shipping:
   ```
   link-cli payment-methods list
   link-cli shipping-address list
   ```

4. Create spend request (confirm total with user first — amounts in cents):
   ```
   link-cli spend-request create \
     --payment-method-id <pm_id> \
     --merchant-name "<name>" \
     --merchant-url "<url>" \
     --context "<what is being purchased>" \
     --amount <cents> \
     --line-item "name:<item>,unit_amount:<cents>,quantity:1" \
     --total "type:total,display_text:Total,amount:<cents>" \
     --request-approval
   ```
   `--request-approval` polls Link app until user approves/denies. Non-zero exit on deny/timeout.
   Add `--credential-type shared_payment_token` for MPP merchants.

5. Retrieve credential SECURELY:
   ```
   link-cli spend-request retrieve <lsrq_id> \
     --include card \
     --output-file /tmp/link-card.json \
     --format json
   ```
   **Never print PAN to stdout.** File written 0600.

6. Use the credential:
   - Web checkout: hand file path to user or browser tool
   - MPP merchants:
     ```
     link-cli mpp pay <merchant-url> \
       --spend-request-id <lsrq_id> \
       --method POST \
       --data '<json body>'
     ```

7. Clean up:
   ```
   rm -f /tmp/link-card.json
   ```

## Optional: MCP Server

```
hermes mcp add stripe-link --command "npx" --args "@stripe/link-cli --mcp"
```

MCP does NOT bypass Link approval.

## Verification

```
link-cli --version && link-cli auth status
```

## Failure Modes

- US-only — `auth login` fails outside US. Tell user, don't retry.
- Card PAN must never enter agent context — use `--output-file` every time.
- `--request-approval` blocks until user acts. Set expectations.
- Some commands return `_next.command` — prefer inline polling flags (`--interval`/`--timeout`).
- Non-TTY defaults to `toon` output. Pass `--format json` when structured fields needed.
- Don't default to `card` — evaluate merchant first (step 2).
