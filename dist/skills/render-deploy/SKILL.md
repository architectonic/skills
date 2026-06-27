---
name: render-deploy
description: Deploy applications to Render using Git-backed Blueprints (render.yaml).
  Use when the user wants to deploy, host, publish, or set up their application on
  Render's cloud platform. Complements existing vercel-deploy, cloudflare-deploy,
  and netlify-deploy skills.
tags:
- software-engineering
- devops
- deploy
- render
- hosting
- blueprint
- iac
- okf
type: Playbook
title: Deploy to Render
domain: software-engineering
risk_level: medium
requires_review: true
source_family: vercel-skills
source_status: adapted
---

# Deploy to Render

Render supports **Git-backed** services (via `render.yaml` Blueprints) and **prebuilt Docker image** services. This skill covers the Git-backed flow.

## When to use

- User asks to deploy an app to Render
- User wants to create a `render.yaml` Blueprint
- User needs to set up databases, cron jobs, or workers on Render
- User wants Infrastructure-as-Code deployment

## Prerequisites

- Git repository pushed to GitHub, GitLab, or Bitbucket
- Render account (dashboard.render.com)
- When sandboxing blocks deployment network calls, rerun with escalated permissions

## Deployment Methods

| Method | Best For | Pros |
|--------|----------|------|
| **Blueprint** (render.yaml) | Multi-service apps, IaC workflows | Version controlled, reproducible |
| **Direct Creation** | Single services, quick deploys | Instant, no file needed |

## Blueprint Method (Recommended)

### 1. Create `render.yaml` in repo root

```yaml
services:
  - type: web
    name: my-app
    env: node
    buildCommand: npm install && npm run build
    startCommand: npm start
    healthCheckPath: /health
    envVars:
      - key: NODE_VERSION
        value: "20"
      - key: DATABASE_URL
        fromDatabase:
          name: my-db
          property: connectionString

databases:
  - name: my-db
    databaseName: myapp
    user: myuser
```

### 2. Connect repo in Render Dashboard

1. Go to dashboard.render.com → New → Web Service
2. Connect your Git repository
3. Render auto-detects `render.yaml` if present

### 3. Deploy via Dashboard or CLI

Render auto-deploys on push when connected. For manual deploys:
- Dashboard: Service → Deploy → Deploy latest commit
- CLI: `render deploy` (if using render CLI)

## Common Service Types

| `type` | Description |
|--------|-------------|
| `web` | HTTP service (Node, Python, Go, etc.) |
| `worker` | Background worker process |
| `cron` | Scheduled job |
| `static` | Static site hosting |

## Framework Detection

Render auto-detects frameworks. Common patterns:

| Framework | Env | Build | Start |
|-----------|-----|-------|-------|
| Next.js | `node` | `npm run build` | `npm start` |
| Express | `node` | `npm install` | `node index.js` |
| Django | `python` | `pip install -r requirements.txt` | `gunicorn myapp.wsgi` |
| FastAPI | `python` | `pip install -r requirements.txt` | `uvicorn main:app` |
| Go | `go` | `go build` | `./main` |

## Environment Variables

```yaml
envVars:
  - key: API_KEY
    value: "your-...  # Plain value
  - key: DATABASE_URL
    fromDatabase:       # Reference another service
      name: my-db
      property: connectionString
  - key: SECRET_KEY
    sync: false         # Set manually in dashboard
```

## Databases on Render

```yaml
databases:
  - name: my-db
    databaseName: myapp
    user: myuser
    plan: free  # free, starter, professional
```

Supported: PostgreSQL, Redis (Valkey), MySQL.

## Prebuilt Docker Images

For image-backed services:
1. Push image to a registry (Docker Hub, GHCR)
2. In Render Dashboard → New → Web Service → Image
3. Provide image URL and registry auth if private

## Common Issues

- **Build fails**: Check `buildCommand` matches your framework
- **Health check fails**: Verify `healthCheckPath` returns 200
- **Missing env vars**: Mark `sync: false` for secrets set in dashboard
- **Blueprint not detected**: Ensure `render.yaml` is in repo root
