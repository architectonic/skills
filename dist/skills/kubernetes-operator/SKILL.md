---
name: Kubernetes Operator Development
description: Build Kubernetes Operators that reconcile correctly. Covers CRD design, reconcile-loop patterns, framework selection, and OperatorHub capability auditing.
tags: [devops, kubernetes, operator, crd, controller-runtime, kubebuilder, operator-sdk, devops]
type: Playbook
---

# Kubernetes Operator

Build operators that reconcile correctly. Most operator bugs are not Kubernetes bugs — they are reconcile-loop bugs: missing finalizers, blocking calls, no requeue on transient errors, status drift, RBAC over-grants.

## Source

Distilled from claude-skills (`engineering/kubernetes-operator`), MIT license, version 2.9.0.

## When to use

- Building a new Kubernetes Operator (controller for a CRD)
- Reviewing an existing operator for capability-level gaps
- Auditing a CRD spec for status/conditions/finalizer correctness
- Choosing a framework (controller-runtime / kubebuilder / operator-sdk / metacontroller / KOPF)
- Designing the API surface of a Custom Resource
- Hardening RBAC, leader election, or webhook validation

## When NOT to use

- Plain Helm chart packaging → use `devops/helm-chart-builder`
- Standard kubectl operations / blue-green deploys → use `devops/gitops-workflow`
- General k8s security posture → use `devops/cloud-security` (if exists)
- "I want to run a workload" — that's a Deployment / Job, not an operator

## Core principle: an operator is a reconcile loop, not a script

```
observe(actual) → desired = read(spec) → diff(actual, desired) → act → update(status)
                                                                          ↓
                                                                   requeue / done
```

Operators that fail are the ones that:
1. Treat reconcile as imperative (do this, then this, then this) instead of declarative (make actual=desired, idempotently)
2. Don't requeue transient failures
3. Don't use finalizers, leaving orphan resources
4. Mutate spec instead of status
5. Don't use the status subresource (status updates trigger spec reconciles → loop)
6. Block in reconcile (long HTTP calls, locks)
7. Forget leader election → split-brain on multi-replica deploys

## CRD design principles

1. **Status is the source of truth for the controller's view of the world.** Spec is what the user wants; status is what the controller observed.
2. **Use the status subresource.** Without it, status updates re-trigger reconcile (loop).
3. **Use Conditions.** `Ready`, `Reconciling`, `Degraded`. Each carries a reason and message.
4. **Add finalizers.** Without finalizers, deletion races the controller and orphans external resources.
5. **Version your CRD from day 1.** `v1alpha1` → `v1beta1` → `v1`. Plan a conversion webhook.
6. **Validate via OpenAPI v3 schema.** Don't rely on the controller for validation that should fail at admission.
7. **Use `additionalPrinterColumns` for `kubectl get`.** Show `Age`, `Phase`, `Ready` at minimum.
8. **Namespace your CRDs unless they manage cluster-scoped resources.**

## Reconcile loop principles

1. **Idempotent.** Reconciling the same state twice → same result, zero side effects.
2. **Read once, decide, act.** Don't observe the world repeatedly during reconcile.
3. **Update status, not spec.** Spec belongs to the user.
4. **Return errors that requeue.** Use `ctrl.Result{RequeueAfter: ...}` for known transient cases.
5. **Never block.** No `time.Sleep`. No long HTTP calls without context.
6. **Use the cache.** Read via the controller's cached client; only escape the cache for a specific reason.
7. **Leader-elect when running >1 replica.** Otherwise enable single-replica mode.
8. **Set OwnerReferences.** Cascading deletion is the operator pattern's free gift.

## Tooling landscape

| Framework | Language | Best for | Maintenance |
|---|---|---|---|
| **controller-runtime** | Go | Production-grade, low-level control | Active (sig-api-machinery) |
| **kubebuilder** | Go | Standard scaffolding, opinionated | Active (Kubernetes SIGs) |
| **operator-sdk** | Go / Helm / Ansible | OpenShift / mixed-paradigm teams | Active (Red Hat) |
| **metacontroller** | Any (webhook-based) | Polyglot teams, avoiding Go | Less active |
| **KOPF** | Python | Python shops, async-first | Active (community) |
| **java-operator-sdk** | Java | JVM shops | Active (Red Hat / Java SIG) |

Decision rules:
- New operator + Go shop → kubebuilder
- New operator + Python shop → KOPF
- New operator + can't pick a language → metacontroller
- OpenShift target → operator-sdk

## Workflows

### Workflow 1: Bootstrap a new operator (Go + kubebuilder)

```
1. Pick a Group/Version/Kind: e.g., apps.example.com/v1alpha1, kind=MyApp
2. kubebuilder init --domain example.com --repo github.com/org/myapp-operator
3. kubebuilder create api --group apps --version v1alpha1 --kind MyApp
4. Run crd_validator.py on config/crd/bases/apps.example.com_myapps.yaml
   → Fix every WARN before writing controller code
5. Implement the reconcile function (simplest correct version first)
6. Run reconcile_lint.py on controllers/myapp_controller.go
7. Run operator_capability_audit.py --operator-dir . — confirm L1
8. Test in a kind cluster: kubectl apply -f config/samples/
9. Add status conditions; aim for L2 in the same PR
```

### Workflow 2: Audit an existing operator

```
1. Run operator_capability_audit.py --operator-dir <path>
2. Run crd_validator.py --crd config/crd/
3. Run reconcile_lint.py --controller controllers/
4. Triage findings:
   - FAIL → block release; fix before next deploy
   - WARN → file an issue; fix in next 30 days
5. Document current capability level in README; commit
6. Plan one capability level advancement per quarter
```

## OperatorHub Capability Levels

- **L1 — Basic Install:** CRD defined, controller deploys it
- **L2 — Seamless Upgrades:** PDBs, conversion webhooks, version skew strategy
- **L3 — Full Lifecycle:** backups, restores, failure recovery
- **L4 — Deep Insights:** metrics endpoint, Prometheus rules, alerts
- **L5 — Auto Pilot:** auto-scaling, auto-tuning, anomaly detection

## Anti-patterns

- **`time.Sleep(30 * time.Second)` inside reconcile** — blocks other reconciles. Use `RequeueAfter`.
- **`r.Client.Update(ctx, obj)` to set status** — use `r.Status().Update(ctx, obj)` instead.
- **No leader election + 2+ replicas** — split-brain.
- **No finalizer** — external resources orphan on deletion.
- **CRD without status subresource** — status updates trigger spec reconciles (infinite loop).
- **Reconcile function > 200 lines** — extract reconcileXxx subroutines per condition.
- **`x-kubernetes-preserve-unknown-fields: true` on spec root** — defeats validation.
- **Imperative reconcile** — "if creating, do A; if updating, do B; if deleting, do C". Wrong shape. Reconcile = make actual=desired, regardless of how we got here.

## Verifiable success

A team using this skill should achieve:

- 100% of new CRDs pass `crd_validator.py` before merge
- All reconcile functions pass `reconcile_lint.py` strict mode
- Operators reach OperatorHub Capability Level 3 (Full Lifecycle) before public release
- Mean time to fix a reconcile bug: <1 day (no infinite loops in production)

## Cross-References

- Related: `devops/helm-chart-builder` — for Helm-based deployments
- Related: `devops/terraform-patterns` — for infrastructure provisioning
- Related: `devops/cloud-security` — for general k8s security posture
