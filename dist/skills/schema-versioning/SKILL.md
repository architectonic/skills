---
name: Schema Versioning
description: Set up and manage database schema versioning with migration files, automated rollback capabilities, and CI/CD integration. Use when you need to version database changes, generate migration files from schema diffs, safely roll back failed deployments, or audit schema history.
tags: [devops, database, migrations, schema, rollback]
source: terminal-skills (terminalskills.io)
license: Apache-2.0
distilled: 2026-06-22
type: Playbook
---

# Schema Versioning

## Overview

Establish a reliable database schema versioning workflow: generating timestamped migration files, testing against a shadow database, integrating schema checks into CI/CD, and rolling back safely. Works with any migration tool (Prisma, Knex, TypeORM, Flyway, Alembic) — patterns, not vendor lock-in.

## Core Rules

- **Every migration must have a working `down` function** — untested rollbacks fail when you need them most
- **Never modify a migration applied to any shared environment** — create a new migration instead
- **Use transactions** for DDL when your database supports it (PostgreSQL does, MySQL does not for most DDL)
- **Test the full sequence**: migrate up, roll back, migrate up again — catches hidden state dependencies
- **Keep migrations small** — one logical change per file. A 500-line migration is a red flag
- **Add indexes in separate migrations** from table creation to avoid long locks on large tables
- **Timestamp migration filenames** — sequential integers cause merge conflicts in teams

## Workflow

### 1. Initialize Migration Infrastructure

Set up migration directory structure for your tool (Prisma, Knex, Alembic, etc.).

Create a shadow database for testing migrations before applying to production:
```yaml
# docker-compose.shadow-db.yml
services:
  shadow-db:
    image: postgres:16
    environment:
      POSTGRES_DB: app_shadow
      POSTGRES_PASSWORD: shadow_test
    ports:
      - "5433:5432"
```

### 2. Generate Migrations from Schema Changes

Each migration gets a timestamped filename with `up` and `down` functions. Include data backfill logic in the migration when needed (run in batches to avoid locking).

### 3. Test Migrations Safely

```bash
# Apply all pending migrations to shadow database
npx knex migrate:latest
# Verify rollback works
npx knex migrate:rollback --all
# Re-apply to confirm clean state
npx knex migrate:latest
```

### 4. Zero-Downtime Renames

For renaming tables/columns without breaking the app:
1. Migration 1: Create new table, add trigger to sync writes
2. Migration 2: Backfill existing data
3. Migration 3: Create view for backwards compatibility
4. Migration 4: Drop old table/view after all code references new name

## CI/CD Integration

```yaml
- name: Apply all migrations from scratch
  run: npx knex migrate:latest
- name: Verify rollback works
  run: npx knex migrate:rollback --all
- name: Re-apply to confirm clean state
  run: npx knex migrate:latest
```
