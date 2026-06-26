---
name: railway-deploy
description: Deploy and manage applications on Railway using the CLI. Use when the user asks to deploy to Railway, check deployment status, manage services, set environment variables, view logs, add databases, scale services, or rollback deployments. Complements existing vercel-deploy, cloudflare-deploy, netlify-deploy, and render-deploy skills.
tags: [devops, deploy, railway, paas, hosting, cli]
type: Playbook
---

# Railway Deploy

Deploy, manage, and monitor applications on Railway using the CLI. Full lifecycle: project setup → service configuration → env vars → deploy → scale → logs → rollback.

## When to use

- User asks to deploy to Railway
- User wants to check deployment status
- User needs to manage Railway services or set env vars
- User wants to view logs or rollback a deployment
- User needs to add a database (PostgreSQL, MySQL, Redis, MongoDB)

## Prerequisites

- Railway CLI installed: `npm i -g @railway/cli` or `brew install railway`
- Authenticated: `railway login` or `RAILWAY_TOKEN` env var

## Project Setup

```bash
# Check if already linked
railway status

# Create new project
railway init

# Link to existing project
railway link

# Token auth (CI/CD)
RAILWAY_TOKEN=xxx railway up
```

## Deployment

```bash
# Deploy and stream logs
railway up

# Deploy without waiting
railway up --detach

# Target specific service
railway up -s my-service

# Deploy to specific environment
railway up -e staging

# Remove latest deployment
railway down

# Redeploy (same code, fresh build)
railway redeploy

# Restart without rebuilding
railway restart
```

## Service Management

```bash
# Add service interactively
railway add

# Add database
railway add --database postgres   # also: mysql, redis, mongo

# Add service from GitHub repo
railway add --repo org/repo

# List services
railway service list

# Scale services
railway service update --replicas 3
```

## Environment Variables

```bash
# Set env vars
railway variables set API_KEY=secret
railway variables set DATABASE_URL=${{postgres.DATABASE_URL}}

# Import from .env
railway variables --env-file .env
```

## Monitoring

```bash
# View logs
railway logs

# View deployment logs
railway logs --deployment <id>

# Health check status
railway status
```

## Common Issues

- **Not authenticated**: Run `railway login` or set `RAILWAY_TOKEN`
- **Build fails**: Check build/start commands in project settings
- **Port binding**: Ensure app listens on `$PORT` (Railway injects this)
- **Database connection**: Use `${{service.VAR}}` syntax for cross-service references
