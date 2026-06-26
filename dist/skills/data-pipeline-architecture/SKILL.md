---
name: data-pipeline-architecture
description: Design and implement scalable, reliable data pipelines for batch and streaming processing. Covers ETL/ELT, Lambda, Kappa, Lakehouse architectures, workflow orchestration (Airflow/Prefect), dbt transformations, Delta Lake/Iceberg storage, and data quality frameworks.
type: Playbook
---

# Data Pipeline Architecture

Design and implement scalable, reliable, and cost-effective data pipelines for batch and streaming data processing.

## Use this skill when

- Designing batch or streaming data pipelines
- Building data warehouses or lakehouse architectures
- Implementing workflow orchestration with Airflow/Prefect
- Transforming data using dbt and Spark
- Managing Delta Lake/Iceberg storage
- Setting up data quality frameworks (Great Expectations, dbt tests)
- Optimizing pipeline costs and performance

## Do not use this skill when

- The task is unrelated to data pipeline architecture
- You only need exploratory data analysis without pipeline concerns
- You need a different domain outside this scope

## Core Capabilities

- Design ETL/ELT, Lambda, Kappa, and Lakehouse architectures
- Implement batch and streaming data ingestion
- Build workflow orchestration with Airflow/Prefect
- Transform data using dbt and Spark
- Manage Delta Lake/Iceberg storage with ACID transactions
- Implement data quality frameworks (Great Expectations, dbt tests)
- Monitor pipelines with CloudWatch/Prometheus/Grafana
- Optimize costs through partitioning, lifecycle policies, and compute optimization

## Architecture Design

1. **Assess**: sources, volume, latency requirements, targets
2. **Select pattern**:
   - **ETL**: transform before load (traditional warehouses)
   - **ELT**: load then transform (modern cloud warehouses)
   - **Lambda**: batch + speed layers (dual-path)
   - **Kappa**: stream-only (unified log)
   - **Lakehouse**: unified batch + streaming (Delta/Iceberg)
3. **Design flow**: sources → ingestion → processing → storage → serving
4. **Add observability** touchpoints at every stage

## Ingestion Patterns

### Batch Ingestion
- Incremental loading with watermark columns
- Retry logic with exponential backoff
- Schema validation and dead letter queue for invalid records
- Metadata tracking (`_extracted_at`, `_source`)

### Streaming Ingestion
- Kafka consumers with exactly-once semantics
- Manual offset commits within transactions
- Windowing for time-based aggregations
- Error handling and replay capability

## Orchestration

### Apache Airflow
- Task groups for logical organization
- XCom for inter-task communication
- SLA monitoring and email alerts
- Incremental execution with `execution_date`
- Retry with exponential backoff

### Prefect
- Task caching for idempotency
- Parallel execution with `.submit()`
- Artifacts for visibility
- Automatic retries with configurable delays

## Transformation with dbt

- **Staging layer**: incremental materialization, deduplication, late-arriving data handling
- **Marts layer**: dimensional models, aggregations, business logic
- **Tests**: unique, not_null, relationships, accepted_values, custom data quality tests
- **Sources**: freshness checks, `loaded_at_field` tracking
- **Incremental strategy**: merge or delete+insert

## Storage Strategy

### Delta Lake
- ACID transactions with append/overwrite/merge modes
- Upsert with predicate-based matching
- Time travel for historical queries
- Optimize: compact small files, Z-order clustering
- Vacuum to remove old files

### Apache Iceberg
- Partitioning and sort order optimization
- MERGE INTO for upserts
- Snapshot isolation and time travel
- File compaction with binpack strategy
- Snapshot expiration for cleanup

## Monitoring & Cost Optimization

### Key Metrics
- Records processed/failed, data size, execution time, success/failure rates
- CloudWatch metrics and custom namespaces
- SNS alerts for critical/warning/info events
- Data freshness checks
- Performance trend analysis

### Cost Optimization
- **Partitioning**: date/entity-based, avoid over-partitioning (keep >1GB per partition)
- **File sizes**: 512MB-1GB for Parquet
- **Lifecycle policies**: hot (Standard) → warm (IA) → cold (Glacier)
- **Compute**: spot instances for batch, on-demand for streaming, serverless for adhoc
- **Query optimization**: partition pruning, clustering, predicate pushdown

## Output Deliverables

1. **Architecture Documentation**: diagram, tech stack justification, scalability analysis, failure modes
2. **Implementation Code**: ingestion, transformation, orchestration, storage, data quality
3. **Configuration Files**: DAG definitions, dbt models, infrastructure manifests, environment configs
4. **Monitoring & Observability**: metrics, alerts, dashboards, structured logs with correlation IDs
5. **Operations Guide**: deployment, troubleshooting, scaling, cost optimization, disaster recovery

## Success Criteria

- Pipeline meets defined SLA (latency, throughput)
- Data quality checks pass with >99% success rate
- Automatic retry and alerting on failures
- Comprehensive monitoring shows health and performance
- Documentation enables team maintenance
- Cost optimization reduces infrastructure costs by 30-50%
- Schema evolution without downtime
- End-to-end data lineage tracked

## Source

Distilled from `antigravity-awesome-skills/skills/data-engineering-data-pipeline/SKILL.md` (community contribution, 2026-02-27).
