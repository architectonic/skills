---
name: netlify-deploy
description: Deploy web projects to Netlify using the Netlify CLI. Use when the user asks to deploy, host, publish, or link a site/repo on Netlify, including preview and production deploys. Complements existing vercel-deploy and cloudflare-deploy skills.
tags: [devops, deploy, netlify, hosting, cli]
type: Playbook
---

# Netlify Deployment

Deploy web projects to Netlify using `npx netlify` CLI with intelligent project detection.

## When to use

- User asks to deploy a site to Netlify
- User wants preview deployment for a PR
- User wants to link an existing site to Netlify
- User needs production deployment with environment variables

## Prerequisites

- `npx netlify` (no global install required)
- Netlify account with active login session
- Valid web project in current directory
- When sandboxing blocks deployment network calls, rerun with escalated permissions

## Authentication

```bash
# Check status
npx netlify status

# Login (opens browser for OAuth)
npx netlify login

# Alternative: API key
export NETLIFY_AUTH_TOKEN=<your-token>
```

## Deployment Workflow

### 1. Detect project configuration

Inspect `package.json` for build commands and output directories. Common frameworks:

| Framework | Build command | Output directory |
|-----------|--------------|------------------|
| Next.js | `next build` | `.next` |
| React (Vite) | `vite build` | `dist` |
| Gatsby | `gatsby build` | `public` |
| Static HTML | (none) | `.` or `public` |
| Hugo | `hugo` | `public` |

### 2. Deploy to preview

```bash
npx netlify deploy
```

This creates a unique preview URL for the current branch/state.

### 3. Deploy to production

```bash
npx netlify deploy --prod
```

### 4. Link to existing site

```bash
# Link to a site already on Netlify
npx netlify link

# Then deploy to it
npx netlify deploy --site=<site-name>
```

## Configuration File

Create `netlify.toml` for reproducible deploys:

```toml
[build]
  command = "npm run build"
  publish = "dist"

[build.environment]
  NODE_VERSION = "20"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

## Environment Variables

```bash
# Set env vars via CLI
npx netlify env:set API_KEY <value>

# Or via netlify.toml
[build.environment]
  API_KEY = "your-key-here"
```

## Common Issues

- **Auth expired**: Re-run `npx netlify login`
- **Build fails**: Check build command matches your framework
- **Wrong output dir**: Verify `publish` directory in config
- **Deploy not triggering**: Ensure Git remote is connected
