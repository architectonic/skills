---
name: x-api-mcp
title: X API via XMCP
description: Use the official XMCP server to call X API endpoints (post, search, read, like, follow) from any MCP client. Run locally; connect any MCP-compatible agent.
type: Playbook
domain: runtime-tools
tags:
- runtime-tools
- mcp
- x
- twitter
- okf
- api
source_name: xdevplatform/xmcp
source_url: https://docs.x.com/tools/mcp
source_license: Apache-2.0
source_status: distilled
risk_level: high
requires_review: true
runtime_targets: [hermes, cursor, windsurf, generic]
capabilities: [network, oauth, account-access, mcp]
---

# x-api-mcp — X API via the Official MCP Server

Use the official XMCP server (from the X Developer Platform team) to call X API endpoints from any MCP-compatible agent. XMCP exposes 200+ tools auto-generated from the X API OpenAPI spec and uses OAuth 1.0a with a browser-based consent flow.

This is NOT the `xurl` CLI (use that for HTTP/xurl CLI calls without MCP). XMCP is a local MCP server for agent-driven X workflows.

## Trigger

Use when the user wants to:
- connect an MCP client to the X API (post, search, read, like, follow)
- integrate X capabilities via Model Context Protocol
- allow-list restrict what actions a client can perform on X

## Inputs

- X Developer Console app credentials (OAuth consumer key, consumer secret, bearer token)
- registered callback URL in the Developer Console (e.g. `http://127.0.0.1:8976/oauth/callback`)
- Python 3.9+ installed locally

## Procedure

1. Clone and install:
   ```bash
   git clone https://github.com/xdevplatform/xmcp && cd xmcp
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. Copy `env.example` to `.env` and fill in `X_API_CONSUMER_KEY`, `X_API_CONSUMER_SECRET`, `X_API_BEARER_TOKEN`, `X_API_CALLBACK_URL`.
3. Start the server — defaults to `http://127.0.0.1:8000/mcp`:
   ```bash
   python server.py
   ```
4. (Optional) Restrict tools with the `X_API_TOOL_ALLOWLIST` env var:
   ```bash
   export X_API_TOOL_ALLOWLIST="createPosts,getUsersByUsername,searchPostsRecent,likePost"
   ```
5. Connect an MCP client to `http://127.0.0.1:8000/mcp`.
6. For documentation lookup, also connect the hosted Docs MCP at `https://docs.x.com/mcp`.

## Verification

```bash
curl -s http://127.0.0.1:8000/mcp -X POST \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}'
```

The response JSON includes a `tools` array with X API operations (`createPost`, `searchPostsRecent`, etc.). Empty or error means the server isn't running, `.env` is misconfigured, or OAuth wasn't completed.

## Failure Modes

- Callback URL mismatch with Developer Console registration — auth fails silently with 401.
- Spec fetched at startup only — restart XMCP to pick up new X API endpoints.
- Tokens are in-memory only — lost on server restart; re-authenticate via browser after each restart.
- No streaming/webhook endpoints — persistent-connection X endpoints (filtered stream) are incompatible with MCP's request/response model.
- `--verbose`-style logging on XMCP may leak tokens; only allow-list read tools for high-trust sessions.

## Quick Reference

| Item | Value |
|---|---|
| Local endpoint | `http://127.0.0.1:8000/mcp` |
| Docs MCP endpoint | `https://docs.x.com/mcp` |
| OpenAPI spec | `https://api.x.com/2/openapi.json` |
| GitHub | https://github.com/xdevplatform/xmcp |
| Developer Console | https://console.x.com |
| Tool allow-list env | `X_API_TOOL_ALLOWLIST` |
| Auth method | OAuth 1.0a (browser consent) |
| Doc MCP tools | `search_x`, `get_page_x` |
