---
name: terraform-patterns
description: Terraform infrastructure-as-code discipline — module design, state management, provider patterns, security hardening, and CI/CD workflows. Use when designing Terraform modules, managing state backends, reviewing Terraform security, implementing multi-region deployments, or following IaC best practices.
tags: [terraform, iac, infrastructure, devops, modules, state]
type: Playbook
---

# Terraform Patterns

Predictable infrastructure. Secure state. Modules that compose. No drift.

Opinionated Terraform workflow for well-structured, secure, production-grade infrastructure code. Not a Terraform tutorial — concrete decisions about infrastructure code that doesn't break at 3 AM.

## When to Use This Skill

Use this skill when:
- Designing or refactoring Terraform modules
- Setting up remote state backends
- Reviewing Terraform code for anti-patterns or security issues
- Implementing multi-region or multi-account deployments
- Building Terraform CI/CD pipelines
- Implementing policy-as-code (Sentinel/OPA)

## Core Workflows

### 1. Module Design

**Flat Module (small projects)**
```
infrastructure/
├── main.tf          # All resources
├── variables.tf     # All inputs
├── outputs.tf       # All outputs
├── versions.tf      # Provider requirements
└── backend.tf       # Remote state configuration
```

**Nested Modules (medium/large projects)**
```
infrastructure/
├── environments/
│   ├── dev/         # Calls modules with dev params
│   ├── staging/
│   └── prod/
├── modules/
│   ├── networking/
│   ├── compute/
│   └── database/
└── versions.tf
```

**Module Checklist:**
- Variables have descriptions and type constraints
- Outputs expose only what consumers need
- Resources use consistent naming: `{provider}_{type}_{purpose}`
- Locals used for computed values and DRY expressions
- No hardcoded values — everything parameterized

### 2. State Management

**Backend decision tree:**
- Single developer, small project → Local state (migrate to remote ASAP)
- Using Terraform Cloud → TF Cloud native backend (built-in locking, encryption, RBAC)
- AWS → S3 + DynamoDB (encryption, locking, versioning)
- GCP → GCS bucket (native locking, encryption)
- Azure → Azure Blob Storage (native locking, encryption)

**Environment isolation:** Separate state files per environment (directories preferred over workspaces).

### 3. Security Audit Checklist

| Check | Severity | Fix |
|-------|----------|-----|
| Hardcoded secrets in `.tf` files | Critical | Use variables with `sensitive = true` or vault |
| IAM policy with `*` actions | Critical | Scope to specific actions and resources |
| Security group 0.0.0.0/0 on SSH/RDP | Critical | Restrict to known CIDR or bastion |
| S3 bucket without encryption | High | Add `server_side_encryption_configuration` |
| S3 bucket public access | High | Add `aws_s3_bucket_public_access_block` |
| RDS without encryption | High | Set `storage_encrypted = true` |
| RDS publicly accessible | High | Set `publicly_accessible = false` |
| Variables without `sensitive = true` | Medium | Mark secret variables as sensitive |

### 4. Provider Configuration

```hcl
# Version pinning with pessimistic operator
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"    # Allow 5.x, block 6.0
    }
  }
}

# Multi-region with aliases
provider "aws" {
  alias  = "west"
  region = "us-west-2"
}
```

### 5. CI/CD Integration

GitHub Actions plan/apply pattern:
```yaml
# .github/workflows/terraform.yml
# plan job on PRs, apply job on main push
# Key steps: terraform init → validate → plan → (manual approval) → apply
```

Drift detection: schedule `terraform plan -detailed-exitcode` to detect configuration drift.

## Proactive Triggers

Flag these without being asked:
- No remote backend configured → Migrate to encrypted remote backend
- Provider without version constraint → Add `version = "~> X.0"`
- Hardcoded secrets in .tf files → Use `sensitive = true` variables
- IAM policy with `"Action": "*"` → Scope to specific actions
- Security group open to 0.0.0.0/0 on SSH/RDP → Restrict CIDR
- No state locking → Enable DynamoDB for S3 backend
- Resources without tags → Add `default_tags` in provider block
- Missing `prevent_destroy` on databases/storage → Add lifecycle block

## Anti-Patterns

- **Local state in production** — State file contains secrets; must be remote + encrypted
- **No version constraints** — Provider upgrades break everything
- **Hardcoded values** — Every environment-specific value must be a variable
- **Single state file for all environments** — Blast radius too large
- **Provider config in child modules** — Providers belong in root module
- **Outputting entire resources** — Output specific attributes only
