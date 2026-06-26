---
name: Database Backup & Disaster Recovery
description: Set up automated database backup, restore, and disaster recovery procedures for PostgreSQL, MySQL, MongoDB, and Redis. Use when implementing backup schedules, point-in-time recovery, cross-region replication, backup verification, or disaster recovery runbooks.
tags: [devops, database, backup, disaster-recovery, postgresql, mysql, mongodb, redis, devops]
source_repo: terminal-skills
source_path: skills/db-backup/SKILL.md
distilled_at: 2026-08-03
type: Playbook
---

# Database Backup & Disaster Recovery

## Overview

Implement comprehensive database backup and disaster recovery strategies. Covers automated backup scheduling, storage management, backup verification, point-in-time recovery, and disaster recovery runbooks for PostgreSQL, MySQL, MongoDB, and Redis.

## When to Use

- Setting up automated database backups
- Implementing point-in-time recovery (PITR)
- Creating disaster recovery runbooks
- Configuring backup verification and restore testing
- Planning cross-region backup replication

## Instructions

### 1. Assess Requirements

Determine the backup strategy based on:
- **RPO** (Recovery Point Objective): How much data loss is acceptable? (minutes → WAL/binlog streaming, hours → periodic dumps)
- **RTO** (Recovery Time Objective): How fast must recovery complete? (minutes → hot standby, hours → restore from backup)
- **Database size**: Small (<10GB) → full dumps; Large (>100GB) → incremental/WAL archiving
- **Compliance**: Retention requirements (30 days, 1 year, 7 years for financial data)

### 2. Implement Backup Strategy

#### PostgreSQL

```bash
# Full logical backup (small-medium databases)
pg_dump -Fc --no-owner --no-acl -h $DB_HOST -U $DB_USER $DB_NAME | \
  gzip | aws s3 cp - s3://backups/pg/$(date +%Y%m%d_%H%M%S).dump.gz

# WAL archiving for point-in-time recovery (large databases)
# postgresql.conf:
#   archive_mode = on
#   archive_command = 'aws s3 cp %p s3://backups/pg-wal/%f'

# Base backup + WAL for PITR
pg_basebackup -D /backups/base -Ft -z -P -h $DB_HOST -U replication
```

#### MySQL

```bash
# Full logical backup
mysqldump --single-transaction --routines --triggers --all-databases \
  -h $DB_HOST -u $DB_USER -p$DB_PASS | gzip > backup_$(date +%Y%m%d).sql.gz

# Binary log for point-in-time recovery
mysqlbinlog --read-from-remote-server --host=$DB_HOST --raw binlog.000001
```

#### MongoDB

```bash
# Full backup with oplog for PITR
mongodump --uri="$MONGO_URI" --oplog --gzip --archive | \
  aws s3 cp - s3://backups/mongo/$(date +%Y%m%d_%H%M%S).archive.gz
```

#### Redis

```bash
# RDB snapshot (built-in)
redis-cli BGSAVE
# Copy the dump.rdb file to backup storage

# For AOF persistence
redis-cli BGREWRITEAOF
```

### 3. Backup Rotation Policy

Implement grandfather-father-son rotation:
- **Daily**: Keep last 7 days
- **Weekly**: Keep last 4 Sundays
- **Monthly**: Keep last 12 first-of-months
- **Yearly**: Keep indefinitely (or per compliance)

### 4. Backup Verification

Every backup strategy **must** include automated verification:

```bash
# Download latest backup
# Restore to temporary database
# Run integrity checks (row counts, checksum of critical tables)
# Compare against production counts
# Alert if variance > 0.1%
# Tear down temporary database
```

An untested backup is not a backup. Test restores monthly.

### 5. Disaster Recovery Runbook

Generate a step-by-step runbook covering:
- How to identify which backup to restore
- Exact restore commands with parameters
- How to verify the restored data
- How to redirect application traffic to the restored instance
- Communication template for stakeholders
- Post-incident review checklist

## Guidelines

- Always encrypt backups at rest (S3 SSE-KMS, or gpg before upload)
- Test restores monthly — an untested backup is not a backup
- Store backups in a different region than production
- Use separate IAM credentials for backup operations with minimal permissions
- Monitor backup job completion — alert immediately if a backup fails
- Document the restore process so any team member can execute it under pressure
- For databases over 500GB, prefer incremental backups (pgBackRest, Percona XtraBackup)
- Keep backup credentials in a secrets manager, never in scripts
- Calculate actual RTO by running restore drills — estimated RTO is usually optimistic

## Examples

### PostgreSQL backup with S3 and verification

```bash
#!/bin/bash
# scripts/backup-postgres.sh
set -euo pipefail

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
S3_BUCKET="s3://myapp-backups/postgres"
DB_HOST="${DB_HOST:?required}"
DB_NAME="${DB_NAME:?required}"

echo "[$(date)] Starting backup of ${DB_NAME}..."

# Create base backup with checksums
pg_basebackup \
  -h "$DB_HOST" -U replication \
  -D /tmp/backup_${TIMESTAMP} \
  -Ft -z -P --checkpoint=fast --wal-method=stream

# Upload to S3
aws s3 cp /tmp/backup_${TIMESTAMP}/base.tar.gz \
  "${S3_BUCKET}/base/${TIMESTAMP}/base.tar.gz" \
  --storage-class STANDARD_IA

# Upload WAL files
aws s3 sync /tmp/backup_${TIMESTAMP}/pg_wal/ \
  "${S3_BUCKET}/base/${TIMESTAMP}/pg_wal/"

# Cleanup local
rm -rf /tmp/backup_${TIMESTAMP}

echo "[$(date)] Backup complete: ${TIMESTAMP}"
```
