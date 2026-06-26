---
name: github-actions-templates
description: Create production-ready GitHub Actions workflows for automated testing, building, and deploying. Use when setting up CI/CD with GitHub Actions, automating development workflows, or creating reusable workflow templates.
type: Playbook
---

# GitHub Actions Templates

> Source: SWE-Skills-Bench — `skills/github-actions-templates/SKILL.md`

Production-ready GitHub Actions workflow patterns for testing, building, and deploying applications.

## When to Use

- Automating testing and deployment
- Building and pushing Docker images
- Deploying to Kubernetes
- Running security scans
- Implementing matrix builds

## Pattern 1: Test Workflow with Matrix

```yaml
name: Test
on:
  push: {branches: [main, develop]}
  pull_request: {branches: [main]}

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [18.x, 20.x]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
          cache: "npm"
      - run: npm ci
      - run: npm run lint
      - run: npm test
      - uses: codecov/codecov-action@v3
        with: {files: ./coverage/lcov.info}
```

## Pattern 2: Build and Push Docker Image

```yaml
name: Build and Push
on:
  push:
    branches: [main]
    tags: ["v*"]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
    steps:
      - uses: actions/checkout@v4
      - uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - id: meta
        uses: docker/metadata-action@v5
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=ref,event=branch
            type=semver,pattern={{version}}
      - uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

## Pattern 3: Deploy to Kubernetes

```yaml
name: Deploy
on:
  push: {branches: [main]}

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-west-2
      - run: aws eks update-kubeconfig --name production-cluster --region us-west-2
      - run: |
          kubectl apply -f k8s/
          kubectl rollout status deployment/my-app -n production
```

## Pattern 4: Reusable Workflows

```yaml
# .github/workflows/reusable-test.yml
name: Reusable Test
on:
  workflow_call:
    inputs:
      node-version: {required: true, type: string}
    secrets:
      NPM_TOKEN: {required: true}

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: {node-version: ${{ inputs.node-version }}}
      - run: npm ci
      - run: npm test
```

```yaml
# Call it from another workflow
jobs:
  call-test:
    uses: ./.github/workflows/reusable-test.yml
    with: {node-version: "20.x"}
    secrets: {NPM_TOKEN: ${{ secrets.NPM_TOKEN }}}
```

## Pattern 5: Security Scanning

```yaml
name: Security Scan
on:
  push: {branches: [main]}
  pull_request: {branches: [main]}

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: aquasecurity/trivy-action@master
        with:
          scan-type: "fs"
          format: "sarif"
          output: "trivy-results.sarif"
      - uses: github/codeql-action/upload-sarif@v2
        with: {sarif_file: "trivy-results.sarif"}
```

## Pattern 6: Production Deployment with Approvals

```yaml
name: Deploy to Production
on:
  push: {tags: ["v*"]}

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: production
      url: https://app.example.com
    steps:
      - uses: actions/checkout@v4
      - run: ./deploy.sh production
      - if: success()
        uses: slackapi/slack-github-action@v1
        with:
          webhook-url: ${{ secrets.SLACK_WEBHOOK }}
          payload: '{"text": "Production deployment complete ✅"}'
```

## Best Practices

1. **Pin action versions** (`@v4`, not `@latest`)
2. **Cache dependencies** to speed up builds
3. **Use secrets** for all sensitive data (never hardcode)
4. **Set minimal permissions** per job (principle of least privilege)
5. **Use matrix builds** for multi-version testing
6. **Implement approval gates** for production environments
7. **Use reusable workflows** for shared patterns
8. **Add notifications** for failures
9. **Use branch protection rules** with required status checks
10. **Leverage GitHub Actions cache** (`type=gha`) for Docker builds
