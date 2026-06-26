---
name: migration-architect
description: Zero-downtime migration planning, compatibility validation, and rollback strategy generation. Tools for system, database, and infrastructure migrations with minimal business impact. Use when planning a database migration, infrastructure cutover, system replacement, or any high-risk transition that needs explicit rollback paths.
type: Playbook
---

# Migration Architect

Zero-downtime migration planning, compatibility validation, and rollback strategy generation for system, database, and infrastructure migrations.

**Source:** claude-skills/engineering/migration-architect/SKILL.md (Apache-2.0)

## Core Capabilities

1. **Migration Strategy Planning** — phased migration, risk assessment, timeline estimation
2. **Compatibility Analysis** — schema evolution, API versioning, data type validation
3. **Rollback Strategy Generation** — automated rollback plans, data recovery scripts, validation checkpoints

## Quick Start — plan → check compatibility → generate rollback

```bash
# 1. Generate the migration plan
python3 scripts/migration_planner.py --input migration_spec.json --format json -o migration_plan.json

# 2. Check schema/API compatibility (CI gate)
python3 scripts/compatibility_checker.py --before old_schema.json --after new_schema.json --type database --format json -o compatibility.json

# 3. Generate the rollback runbook
python3 scripts/rollback_generator.py --input migration_plan.json --format both -o rollback_runbook
```

**Gate:** migration is not approved until (a) compatibility checker exits 0 or every breaking item is explicitly accepted, and (b) a rollback runbook exists for every phase.

## Migration Patterns

### Database: Expand-Contract Pattern

1. **Expand** — Add new columns/tables alongside existing schema
2. **Dual Write** — Application writes to both old and new schema
3. **Migration** — Backfill historical data to new schema
4. **Contract** — Remove old columns/tables after validation

### Database: Parallel Schema Pattern

1. Run new schema in parallel with existing schema
2. Use feature flags to route traffic between schemas
3. Validate data consistency between parallel systems
4. Cutover when confidence is high

### Service: Strangler Fig Pattern

1. **Intercept Requests** — Route traffic through proxy/gateway
2. **Gradually Replace** — Implement new service functionality incrementally
3. **Legacy Retirement** — Remove old service components as new ones prove stable
4. **Monitoring** — Track performance and error rates throughout transition

### Service: Canary Deployment Pattern

1. **Limited Rollout** — Deploy new service to small percentage of users
2. **Monitoring** — Track key metrics (latency, errors, business KPIs)
3. **Gradual Increase** — Increase traffic percentage as confidence grows
4. **Full Rollout** — Complete migration once validation passes

## Rollback Strategies

### Database Rollback
- Maintain schema version control
- Use backward-compatible migrations when possible
- Keep rollback scripts for each migration step
- Point-in-time recovery using database backups

### Service Rollback
- **Blue-Green Deployment** — keep previous version running, switch back if issues
- **Rolling Rollback** — gradually shift traffic back, monitor system health

### Infrastructure Rollback
- Version control all infrastructure definitions (IaC)
- Maintain rollback terraform/CloudFormation templates
- Test rollback procedures in staging environments

## Risk Assessment Framework

| Risk Category | Examples | Mitigation |
|---|---|---|
| Technical | Data loss, downtime, integration failures | Gradual rollout, automated rollback, validation |
| Business | Revenue impact, customer experience | Stakeholder communication, business continuity |
| Operational | Knowledge gaps, insufficient testing | Runbooks, training, on-call planning |

## Migration Runbook Checklist

### Pre-Migration
- [ ] Migration plan reviewed and approved
- [ ] Rollback procedures tested and validated
- [ ] Monitoring and alerting configured
- [ ] Team roles and responsibilities defined
- [ ] Backup and recovery procedures verified
- [ ] Security review completed

### During Migration
- [ ] Execute migration phases in planned order
- [ ] Monitor key performance indicators continuously
- [ ] Validate data consistency at each checkpoint
- [ ] Communicate progress to stakeholders
- [ ] Execute rollback if success criteria not met

### Post-Migration
- [ ] Validate all success criteria met
- [ ] Perform comprehensive system health checks
- [ ] Execute data reconciliation procedures
- [ ] Monitor system performance over 72 hours
- [ ] Update documentation and runbooks
- [ ] Conduct post-migration retrospective

## Best Practices

1. **Design for Rollback** — Every migration step should have a tested rollback procedure
2. **Validate in Staging** — Execute full migration process in production-like environment
3. **Plan for Gradual Rollout** — Use feature flags and traffic routing for controlled migration
4. **Monitor Continuously** — Track both technical and business metrics throughout
5. **Automate Validation** — Use automated tools for data consistency and performance checks
6. **Document Everything** — Maintain detailed logs for post-migration analysis
