---
name: gitlab-ci-patterns
description: Build GitLab CI/CD pipelines with multi-stage workflows, caching, and deployment. Use when implementing GitLab CI/CD, optimizing pipeline performance, setting up automated testing/deployment, or implementing GitOps with GitLab.
type: Playbook
---

# GitLab CI Patterns

> Source: SWE-Skills-Bench — `skills/gitlab-ci-patterns/SKILL.md`

Comprehensive GitLab CI/CD pipeline patterns for automated testing, building, and deployment.

## When to Use

- Automating GitLab-based CI/CD
- Implementing multi-stage pipelines
- Deploying to Kubernetes from GitLab
- Implementing GitOps workflows
- Configuring GitLab Runners

## Basic Pipeline Structure

```yaml
stages: [build, test, deploy]

variables:
  DOCKER_DRIVER: overlay2
  DOCKER_TLS_CERTDIR: "/certs"

build:
  stage: build
  image: node:20
  script:
    - npm ci
    - npm run build
  artifacts:
    paths: [dist/]
    expire_in: 1 hour
  cache:
    key: ${CI_COMMIT_REF_SLUG}
    paths: [node_modules/]

test:
  stage: test
  image: node:20
  script:
    - npm ci
    - npm run lint
    - npm test
  coverage: '/Lines\s*:\s*(\d+\.\d+)%/'

deploy:
  stage: deploy
  image: bitnami/kubectl:latest
  script:
    - kubectl apply -f k8s/
    - kubectl rollout status deployment/my-app
  only: [main]
  environment:
    name: production
    url: https://app.example.com
```

## Docker Build and Push

```yaml
build-docker:
  stage: build
  image: docker:24
  services: [docker:24-dind]
  before_script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
  script:
    - docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA .
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
    - docker push $CI_REGISTRY_IMAGE:latest
  only: [main, tags]
```

## Multi-Environment Deployment

```yaml
.deploy_template: &deploy_template
  image: bitnami/kubectl:latest
  before_script:
    - kubectl config set-cluster k8s --server="$KUBE_URL" --insecure-skip-tls-verify=true
    - kubectl config set-credentials admin --token="$KUBE_TOKEN"
    - kubectl config set-context default --cluster=k8s --user=admin
    - kubectl config use-context default

deploy:staging:
  <<: *deploy_template
  stage: deploy
  script:
    - kubectl apply -f k8s/ -n staging
    - kubectl rollout status deployment/my-app -n staging
  environment:
    name: staging
    url: https://staging.example.com
  only: [develop]

deploy:production:
  <<: *deploy_template
  stage: deploy
  script:
    - kubectl apply -f k8s/ -n production
    - kubectl rollout status deployment/my-app -n production
  environment:
    name: production
    url: https://app.example.com
  when: manual
  only: [main]
```

## Terraform Pipeline

```yaml
stages: [validate, plan, apply]

variables:
  TF_ROOT: ${CI_PROJECT_DIR}/terraform
  TF_VERSION: "1.6.0"

.validate:
  before_script:
    - cd ${TF_ROOT}
    - terraform --version

validate:
  extends: .validate
  stage: validate
  image: hashicorp/terraform:${TF_VERSION}
  script:
    - terraform init -backend=false
    - terraform validate
    - terraform fmt -check

plan:
  extends: .validate
  stage: plan
  image: hashicorp/terraform:${TF_VERSION}
  script:
    - terraform init
    - terraform plan -out=tfplan
  artifacts:
    paths: [${TF_ROOT}/tfplan]
    expire_in: 1 day

apply:
  extends: .validate
  stage: apply
  image: hashicorp/terraform:${TF_VERSION}
  script:
    - terraform init
    - terraform apply -auto-approve tfplan
  when: manual
  only: [main]
```

## Security Scanning

```yaml
include:
  - template: Security/SAST.gitlab-ci.yml
  - template: Security/Dependency-Scanning.gitlab-ci.yml
  - template: Security/Container-Scanning.gitlab-ci.yml

trivy-scan:
  stage: test
  image: aquasec/trivy:latest
  script:
    - trivy image --exit-code 1 --severity HIGH,CRITICAL $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
  allow_failure: true
```

## Caching Strategies

```yaml
# Cache per branch
cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths: [node_modules/, .cache/]

# Different cache per job
build:
  cache:
    key: build-${CI_COMMIT_REF_SLUG}
    paths: [build/]
    policy: pull-push
```

## Dynamic Child Pipelines

```yaml
generate-pipeline:
  stage: build
  script:
    - python generate_pipeline.py > child-pipeline.yml
  artifacts:
    paths: [child-pipeline.yml]

trigger-child:
  stage: deploy
  trigger:
    include:
      - artifact: child-pipeline.yml
        job: generate-pipeline
    strategy: depend
```

## Best Practices

1. Use specific image tags (`node:20`, not `node:latest`)
2. Cache dependencies appropriately
3. Use artifacts for build outputs between stages
4. Implement manual gates for production (`when: manual`)
5. Use environments for deployment tracking
6. Enable merge request pipelines
7. Use pipeline schedules for recurring jobs
8. Include security scanning (SAST, dependency, container)
9. Use CI/CD variables for secrets (never hardcode)
10. Monitor pipeline performance and optimize slow stages
