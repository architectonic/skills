---
name: docker-development
description: Docker and container development — Dockerfile optimization, docker-compose orchestration, multi-stage builds, and container security hardening. Use when: user wants to optimize a Dockerfile, create or improve docker-compose configurations, implement multi-stage builds, audit container security, reduce image size, or follow container best practices. Triggers on: Dockerfile, docker-compose, container, image size, build cache, Docker security, multi-stage build.
tags: [devops, docker, containers, security, optimization]
type: Playbook
---

# Docker Development

Smaller images. Faster builds. Secure containers. No guesswork.

Opinionated Docker workflow that turns bloated Dockerfiles into production-grade containers. Covers optimization, multi-stage builds, compose orchestration, and security hardening.

Not a Docker tutorial — a set of concrete decisions about how to build containers that don't waste time, space, or attack surface.

## Dockerfile Optimization Checklist

```
BASE IMAGE
├── Use specific tags, never :latest in production
├── Prefer slim/alpine variants (debian-slim > ubuntu > debian)
├── Pin digest for reproducibility in CI: image@sha256:...
└── Match base to runtime needs (don't use python:3.12 for a compiled binary)

LAYER OPTIMIZATION
├── Combine related RUN commands with && \
├── Order layers: least-changing first (deps before source code)
├── Clean package manager cache in the same RUN layer
├── Use .dockerignore to exclude unnecessary files
└── Separate build deps from runtime deps

BUILD CACHE
├── COPY dependency files before source code (package.json, requirements.txt, go.mod)
├── Install deps in a separate layer from code copy
├── Use BuildKit cache mounts: --mount=type=cache,target=/root/.cache
└── Avoid COPY . . before dependency installation

MULTI-STAGE BUILDS
├── Stage 1: build (full SDK, build tools, dev deps)
├── Stage 2: runtime (minimal base, only production artifacts)
├── COPY --from=builder only what's needed
└── Final image should have NO build tools, NO source code, NO dev deps
```

## Docker Compose Best Practices

```
SERVICES
├── Use depends_on with condition: service_healthy
├── Add healthchecks for every service
├── Set resource limits (mem_limit, cpus)
├── Use named volumes for persistent data
└── Pin image versions

NETWORKING
├── Create explicit networks (don't rely on default)
├── Separate frontend and backend networks
├── Only expose ports that need external access
└── Use internal: true for backend-only networks

ENVIRONMENT
├── Use env_file for secrets, not inline environment
├── Never commit .env files (add to .gitignore)
├── Use variable substitution: ${VAR:-default}
└── Document all required env vars

DEVELOPMENT vs PRODUCTION
├── Use compose profiles or override files
├── Dev: bind mounts for hot reload, debug ports exposed
├── Prod: named volumes, no debug ports, restart: unless-stopped
└── docker-compose.override.yml for dev-only config
```

## Container Security Audit

### Dockerfile Audit

| Check | Severity | Fix |
|---|---|---|
| Running as root | Critical | Add `USER nonroot` after creating user |
| Using :latest tag | High | Pin to specific version |
| Secrets in ENV/ARG | Critical | Use BuildKit secrets: `--mount=type=secret` |
| COPY with broad glob | Medium | Use specific paths, add .dockerignore |
| Unnecessary EXPOSE | Low | Only expose ports the app uses |
| No HEALTHCHECK | Medium | Add HEALTHCHECK with appropriate interval |
| Privileged instructions | High | Avoid `--privileged`, drop capabilities |
| Package manager cache retained | Low | Clean in same RUN layer |

### Runtime Security Checks

| Check | Severity | Fix |
|---|---|---|
| Container running as root | Critical | Set user in Dockerfile or compose |
| Writable root filesystem | Medium | Use `read_only: true` in compose |
| All capabilities retained | High | Drop all, add only needed: `cap_drop: [ALL]` |
| No resource limits | Medium | Set `mem_limit` and `cpus` |
| Host network mode | High | Use bridge or custom network |
| Sensitive mounts | Critical | Never mount /etc, /var/run/docker.sock in prod |
| No log driver configured | Low | Set `logging:` with size limits |

## Multi-Stage Build Patterns

### Compiled Language (Go, Rust, C++)

```dockerfile
# Build stage
FROM golang:1.22-alpine AS builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 go build -ldflags="-s -w" -o /app/server ./cmd/server

# Runtime stage
FROM gcr.io/distroless/static-debian12
COPY --from=builder /app/server /server
USER nonroot:nonroot
ENTRYPOINT ["/server"]
```

### Node.js / TypeScript

```dockerfile
# Dependencies stage
FROM node:20-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --production=false

# Build stage
FROM deps AS builder
COPY . .
RUN npm run build

# Runtime stage
FROM node:20-alpine
WORKDIR /app
RUN addgroup -g 1001 -S appgroup && adduser -S appuser -u 1001
COPY --from=builder /app/dist ./dist
COPY --from=deps /app/node_modules ./node_modules
COPY package.json ./
USER appuser
EXPOSE 3000
CMD ["node", "dist/index.js"]
```

### Python

```dockerfile
# Build stage
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Runtime stage
FROM python:3.12-slim
WORKDIR /app
RUN groupadd -r appgroup && useradd -r -g appgroup appuser
COPY --from=builder /install /usr/local
COPY . .
USER appuser
EXPOSE 8000
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Base Image Decision Tree

```
Is it a compiled binary (Go, Rust, C)?
├── Yes → distroless/static or scratch
└── No
    ├── Need a shell for debugging?
    │   ├── Yes → alpine variant (e.g., node:20-alpine)
    │   └── No → distroless variant
    ├── Need glibc (not musl)?
    │   ├── Yes → slim variant (e.g., python:3.12-slim)
    │   └── No → alpine variant
    └── Need specific OS packages?
        ├── Many → debian-slim
        └── Few → alpine + apk add
```

## Proactive Triggers

Flag these without being asked:

- **Dockerfile uses :latest** → Suggest pinning to a specific version tag.
- **No .dockerignore** → Create one. At minimum: `.git`, `node_modules`, `__pycache__`, `.env`.
- **COPY . . before dependency install** → Cache bust. Reorder to install deps first.
- **Running as root** → Add USER instruction. No exceptions for production.
- **Secrets in ENV or ARG** → Use BuildKit secret mounts. Never bake secrets into layers.
- **Image over 1GB** → Multi-stage build required. No reason for a production image this large.
- **No healthcheck** → Add one. Orchestrators (Compose, K8s) need it for proper lifecycle management.
- **apt-get without cleanup in same layer** → `rm -rf /var/lib/apt/lists/*` in the same RUN.

## Source Attribution

Derived from `claude-skills/engineering/docker-development` (MIT license, Alireza Rezvani / claude-skills project). Adapted for Hermes Agent by removing Claude-specific references, slash commands, and tool invocations.
