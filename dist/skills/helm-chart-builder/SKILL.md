---
name: helm-chart-builder
description: Production-grade Helm chart development — chart scaffolding, values design, template patterns, dependency management, security hardening, and chart testing. Use when creating or improving Helm charts, designing values.yaml, implementing template helpers, auditing chart security (RBAC, network policies, pod security), managing subcharts, or running helm lint/test.
tags: [devops, helm, kubernetes, k8s, charts, packaging, deployment]
type: Playbook
---

# Helm Chart Builder

Production-grade Helm charts. Sensible defaults. Secure by design. No cargo-culting.

Opinionated Helm workflow that turns ad-hoc Kubernetes manifests into maintainable, testable, reusable charts. Not a Helm tutorial — concrete decisions about how to build charts that operators trust.

## When to Use This Skill

Use this skill when:
- Creating a new Helm chart from scratch
- Reviewing an existing Helm chart for issues
- Designing values.yaml structure
- Implementing template helpers and named templates
- Managing subchart dependencies
- Auditing chart security (RBAC, pod security, network policies)
- Setting up helm lint/test workflows

## Chart Scaffolding

### Standard Chart Structure

```
mychart/
├── Chart.yaml              # Chart metadata and dependencies
├── values.yaml             # Default configuration
├── values.schema.json      # Optional: JSON Schema for values validation
├── .helmignore             # Files to exclude from packaging
├── templates/
│   ├── _helpers.tpl        # Named templates and helper functions
│   ├── deployment.yaml     # Workload resource
│   ├── service.yaml        # Service exposure
│   ├── ingress.yaml        # Ingress (if applicable)
│   ├── serviceaccount.yaml # ServiceAccount
│   ├── hpa.yaml            # HorizontalPodAutoscaler
│   ├── pdb.yaml            # PodDisruptionBudget
│   ├── networkpolicy.yaml  # NetworkPolicy
│   ├── configmap.yaml      # ConfigMap (if needed)
│   ├── secret.yaml         # Secret (if needed)
│   ├── NOTES.txt           # Post-install usage instructions
│   └── tests/
│       └── test-connection.yaml
└── charts/                 # Subcharts (dependencies)
```

### Chart.yaml Best Practices

- `apiVersion: v2` (Helm 3 only — never v1)
- `name` matches directory name exactly
- `version`: semver (chart version, not app version)
- `appVersion`: application version string
- Pin dependency versions with `~X.Y.Z` (patch-level float)
- Use `condition` field to make subcharts optional

### Values Design Principles

- **Flat over nested** — `image.tag` > `container.spec.image.tag`
- **Group by resource** — `service.*`, `ingress.*`, `resources.*`
- **Use `enabled: true/false`** for optional resources
- **Document every key** with inline YAML comments
- **Sensible development defaults** — chart works without overrides
- **No hardcoded cluster-specific values** (image registry, domain, storage class)
- **No secrets as default values** — use placeholders with comments

## Security Hardening

### Pod Security

| Check | Severity | Fix |
|-------|----------|-----|
| No securityContext | Critical | Add runAsNonRoot, readOnlyRootFilesystem |
| Running as root | Critical | Set `runAsNonRoot: true`, `runAsUser: 1000` |
| Writable root filesystem | High | Set `readOnlyRootFilesystem: true` + emptyDir for tmp |
| All capabilities retained | High | Drop ALL, add only specific needed caps |
| Privileged container | Critical | Set `privileged: false` |
| allowPrivilegeEscalation true | High | Set `allowPrivilegeEscalation: false` |

### RBAC

| Check | Severity | Fix |
|-------|----------|-----|
| No ServiceAccount | Medium | Create dedicated SA, don't use default |
| automountServiceAccountToken true | Medium | Set to false unless pod needs K8s API |
| ClusterRole instead of Role | Medium | Use namespace-scoped Role unless cluster-wide needed |
| Wildcard permissions | Critical | Use specific resource names and verbs |

### Network and Secrets

| Check | Severity | Fix |
|-------|----------|-----|
| No NetworkPolicy | Medium | Add default-deny ingress + explicit allow rules |
| Secrets in values.yaml | Critical | Use external secrets operator or sealed-secrets |
| No PodDisruptionBudget | Medium | Add PDB with minAvailable for HA workloads |
| hostNetwork: true | High | Remove unless absolutely required |

## Template Patterns

### Standard Labels (_helpers.tpl)

```yaml
{{- define "mychart.labels" -}}
helm.sh/chart: {{ include "mychart.chart" . }}
app.kubernetes.io/name: {{ include "mychart.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}
```

### Security-Hardened Pod Spec

```yaml
spec:
  automountServiceAccountToken: false
  securityContext:
    runAsNonRoot: true
    runAsUser: 1000
    seccompProfile:
      type: RuntimeDefault
  containers:
    - name: {{ .Chart.Name }}
      securityContext:
        allowPrivilegeEscalation: false
        readOnlyRootFilesystem: true
        capabilities:
          drop: ["ALL"]
```

## Dependency Management

- Use Chart.yaml dependencies (not requirements.yaml — Helm 3)
- Pin versions: `version: ~15.x.x` (patch float)
- Use `condition:` to make subcharts optional
- Use `alias:` for multiple instances of same subchart
- Override subchart values under subchart name key in values.yaml
- Run `helm dependency update` before packaging

## Proactive Triggers

Flag these without being asked:
- **No _helpers.tpl** → Create one with standard labels and fullname helpers
- **Hardcoded image tag** → Extract to values.yaml
- **No resource requests/limits** → Add them with defaults in values.yaml
- **Running as root** → Add securityContext
- **No NOTES.txt** → Add post-install instructions
- **Secrets in values.yaml defaults** → Remove, use placeholders
- **No liveness/readiness probes** → Add with configurable paths
- **Missing app.kubernetes.io labels** → Add via _helpers.tpl

## Validation

```bash
helm lint mychart/
helm template mychart/ --debug
helm test mychart/
```
