---
name: mpp-agent
description: "Pay HTTP 402 APIs via Machine Payments Protocol — mppx, Tempo Wallet, Privy, AgentCash."
tags: [payments, mpp, http-402, stripe, tempo, okf]
type: Playbook
---

# MPP Agent

Pay HTTP 402 APIs via Machine Payments Protocol (MPP). Multiple client options available.

## Trigger

- merchant API returns `HTTP 402` with `www-authenticate` header
- user says "pay per request", "set up agent wallet", "use Tempo/Privy/AgentCash"
- user wants to discover MPP-priced services

## Inputs

- Node.js 20+ on `PATH`
- Funded wallet (Tempo / Privy / AgentCash) OR `mppx` account
- For wallet onboarding, fetch the vendor's SKILL.md via `web_extract`

## Client Selection

| Tool | When | Setup |
|---|---|---|
| `link-cli` | User has Stripe Link or 402 advertises `method="stripe"` | `stripe-link-cli` skill |
| Tempo Wallet | MPP services with spend controls, service discovery | `tempo wallet login` |
| Privy Agent CLI | Multi-chain wallets, browser-based funding | `privy-agent-wallets login` |
| AgentCash | 300+ pre-priced APIs via one USDC.e balance | `npx agentcash onboard` |
| `mppx` | Dev + debugging, smallest dep surface | `npm install -g mppx` |

Default: use `link-cli mpp pay` if Stripe Link configured; otherwise `mppx` for one-off calls.

## Procedure (mppx, fastest path)

1. Install + create account:
   ```
   npm install -g mppx
   mppx account create
   ```
   CLI writes credentials under its own config dir.

2. Inspect the 402 challenge:
   ```
   curl -i <merchant_url>
   ```
   Real MPP 402:
   ```
   HTTP/1.1 402 Payment Required
   www-authenticate: tempo amount=0.1 currency=...
   ```

3. Pay:
   ```
   mppx <merchant_url>
   ```
   With body:
   ```
   mppx <merchant_url> --method POST --data '<json>'
   ```

4. Verify receipt:
   ```
   mppx <merchant_url> -v
   ```

## Procedure (Tempo Wallet)

Fetch https://tempo.xyz/SKILL.md for canonical reference. Headline:
```
tempo wallet login
tempo wallet pay <url>
```

## Verification

```
mppx --version && mppx account list
```

## Failure Modes

- HTTP 402 without `method="stripe"` cannot use Stripe Link. Use `mppx` or matching wallet.
- Multiple challenges in one header (`tempo, stripe`) — Link picks Stripe, `mppx` picks Tempo. Match to user's funded wallet.
- Zero-amount challenges (`$0.00`) work without funded wallet. Don't refuse as broken.
- Wallet keys never enter agent context. Don't `cat` them.
- Server-side MPP (adding 402 to your own API) is a different skill — see https://mpp.dev/quickstart/server.
