---
name: Snowflake Data Pipeline Development
description: Build data pipelines with Snowflake Dynamic Tables, Streams+Tasks, Cortex AI functions, Snowpark Python, and dbt integration. Covers SQL best practices, MERGE upserts, semi-structured data, and performance tuning.
tags: [data-science, snowflake, data-engineering, dynamic-tables, cortex, snowpark, dbt, sql]
type: Playbook
---

# Snowflake Development

Build data pipelines with Snowflake Dynamic Tables, Streams+Tasks, Cortex AI functions, Snowpark Python, and dbt integration. Covers SQL best practices, MERGE upserts, semi-structured data, and performance tuning.

## Source

Distilled from claude-skills (`engineering-team/snowflake-development`), MIT license.
Originally contributed by [James Cha-Earley](https://github.com/jamescha-earley).

## When to Use

- Writing Snowflake SQL or building data pipelines
- Setting up Dynamic Tables or Streams+Tasks for CDC
- Using Cortex AI functions (AI_COMPLETE, AI_CLASSIFY, AI_FILTER, etc.)
- Writing Snowpark Python code
- Configuring dbt for Snowflake
- Troubleshooting Snowflake errors

## SQL Best Practices

- Use `snake_case` for all identifiers. Avoid double-quoted identifiers — they force case-sensitive names.
- Use CTEs (`WITH` clauses) over nested subqueries.
- Use `CREATE OR REPLACE` for idempotent DDL.
- Use explicit column lists — never `SELECT *` in production. Snowflake's columnar storage scans only referenced columns.

## Stored Procedures — Colon Prefix Rule

In SQL stored procedures (BEGIN...END blocks), variables and parameters **must** use the colon `:` prefix inside SQL statements. Without it, Snowflake treats them as column identifiers and raises "invalid identifier" errors.

```sql
-- WRONG: missing colon prefix
SELECT name INTO result FROM users WHERE id = p_id;

-- CORRECT: colon prefix on both variable and parameter
SELECT name INTO :result FROM users WHERE id = :p_id;
```

## Semi-Structured Data

- VARIANT, OBJECT, ARRAY for JSON/Avro/Parquet/ORC.
- Access nested fields: `src:customer.name::STRING`. Always cast with `::TYPE`.
- VARIANT null vs SQL NULL: JSON `null` is stored as the string `"null"`. Use `STRIP_NULL_VALUE = TRUE` on load.
- Flatten arrays: `SELECT f.value:name::STRING FROM my_table, LATERAL FLATTEN(input => src:items) f;`

## Data Pipelines — Choosing Your Approach

| Approach | When to Use |
|----------|-------------|
| Dynamic Tables | Declarative transformations. **Default choice.** Define the query, Snowflake handles refresh. |
| Streams + Tasks | Imperative CDC. Use for procedural logic, stored procedure calls, complex branching. |
| Snowpipe | Continuous file loading from cloud storage (S3, GCS, Azure). |

### Dynamic Tables

```sql
CREATE OR REPLACE DYNAMIC TABLE cleaned_events
    TARGET_LAG = '5 minutes'
    WAREHOUSE = transform_wh
    AS
    SELECT event_id, event_type, user_id, event_timestamp
    FROM raw_events
    WHERE event_type IS NOT NULL;
```

Key rules:
- Set `TARGET_LAG` progressively: tighter at the top of the DAG, looser downstream.
- Incremental DTs cannot depend on Full-refresh DTs.
- `SELECT *` breaks on upstream schema changes — use explicit column lists.
- Views cannot sit between two Dynamic Tables in the DAG.

### Streams and Tasks

```sql
CREATE OR REPLACE STREAM raw_stream ON TABLE raw_events;

CREATE OR REPLACE TASK process_events
    WAREHOUSE = transform_wh
    SCHEDULE = 'USING CRON 0 */1 * * * America/Los_Angeles'
    WHEN SYSTEM$STREAM_HAS_DATA('raw_stream')
    AS INSERT INTO cleaned_events SELECT ... FROM raw_stream;

-- Tasks start SUSPENDED. You MUST resume them.
ALTER TASK process_events RESUME;
```

## Cortex AI Functions

| Function | Purpose |
|----------|---------|
| `AI_COMPLETE` | LLM completion (text, images, documents) |
| `AI_CLASSIFY` | Classify text into categories (up to 500 labels) |
| `AI_FILTER` | Boolean filter on text or images |
| `AI_EXTRACT` | Structured extraction from text/images/documents |
| `AI_SENTIMENT` | Sentiment score (-1 to 1) |
| `AI_PARSE_DOCUMENT` | OCR or layout extraction from documents |
| `AI_REDACT` | PII removal from text |

**Deprecated names (do NOT use):** `COMPLETE`, `CLASSIFY_TEXT`, `EXTRACT_ANSWER`, `PARSE_DOCUMENT`, `SUMMARIZE`, `TRANSLATE`, `SENTIMENT`, `EMBED_TEXT_768`.

### TO_FILE — Common Pitfall

Stage path and filename are **separate** arguments:

```sql
-- WRONG: single combined argument
TO_FILE('@stage/file.pdf')

-- CORRECT: two arguments
TO_FILE('@db.schema.mystage', 'invoice.pdf')
```

## Snowpark Python

```python
from snowflake.snowpark import Session
import os

session = Session.builder.configs({
    "account": os.environ["SNOWFLAKE_ACCOUNT"],
    "user": os.environ["SNOWFLAKE_USER"],
    "password": os.environ["SNOWFLAKE_PASSWORD"],
    "role": "my_role", "warehouse": "my_wh",
    "database": "my_db", "schema": "my_schema"
}).create()
```

- Never hardcode credentials. Use environment variables or key pair auth.
- DataFrames are lazy — executed on `collect()` / `show()`.
- Do NOT call `collect()` on large DataFrames. Process server-side with DataFrame operations.
- Use **vectorized UDFs** (10-100x faster) for batch and ML workloads.

## dbt on Snowflake

```sql
-- Dynamic table materialization (streaming/near-real-time marts):
{{ config(materialized='dynamic_table', snowflake_warehouse='transforming', target_lag='1 hour') }}

-- Incremental materialization (large fact tables):
{{ config(materialized='incremental', unique_key='event_id') }}

-- Snowflake-specific configs (combine with any materialization):
{{ config(transient=true, copy_grants=true, query_tag='team_daily') }}
```

- Do NOT use `{{ this }}` without `{% if is_incremental() %}` guard.
- Use `dynamic_table` materialization for streaming or near-real-time marts.

## Performance

- **Cluster keys**: Only for multi-TB tables. Apply on WHERE / JOIN / GROUP BY columns.
- **Search Optimization**: `ALTER TABLE t ADD SEARCH OPTIMIZATION ON EQUALITY(col);`
- **Warehouse sizing**: Start X-Small, scale up. Set `AUTO_SUSPEND = 60`, `AUTO_RESUME = TRUE`.
- **Separate warehouses** per workload (load, transform, query).

## Security

- Follow least-privilege RBAC. Use database roles for object-level grants.
- Audit ACCOUNTADMIN regularly: `SHOW GRANTS OF ROLE ACCOUNTADMIN;`
- Use network policies for IP allowlisting.
- Use masking policies for PII columns and row access policies for multi-tenant isolation.

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| "Object does not exist" | Wrong database/schema context or missing grants | Fully qualify names (`db.schema.table`), check grants |
| "Invalid identifier" in procedure | Missing colon prefix on variable | Use `:variable_name` inside SQL statements |
| "Numeric value not recognized" | VARIANT field not cast | Cast explicitly: `src:field::NUMBER(10,2)` |
| Task not running | Forgot to resume after creation | `ALTER TASK task_name RESUME;` |
| DT refresh failing | Schema change upstream or tracking disabled | Use explicit columns, verify change tracking |
| TO_FILE error | Combined path as single argument | Split into two args: `TO_FILE('@stage', 'file.pdf')` |

## Anti-Patterns

| Anti-Pattern | Why It Fails | Better Approach |
|---|---|---|
| `SELECT *` in Dynamic Tables | Schema changes upstream break the DT silently | Use explicit column lists |
| Missing colon prefix in procedures | "Invalid identifier" runtime error | Always use `:variable_name` in SQL blocks |
| Single warehouse for all workloads | Contention between load, transform, and query | Separate warehouses per workload type |
| Hardcoded credentials in Snowpark | Security risk, breaks in CI/CD | Use `os.environ[]` or key pair auth |
| `collect()` on large DataFrames | Pulls entire result set to client memory | Process server-side with DataFrame operations |
| Nested subqueries instead of CTEs | Unreadable, hard to debug | Use `WITH` clauses |
| Using deprecated Cortex functions | Will be removed | Use `AI_CLASSIFY`, `AI_COMPLETE` etc. |
| Tasks without `WHEN SYSTEM$STREAM_HAS_DATA` | Task runs on schedule even with no new data | Add the WHEN clause for stream-driven tasks |
| Double-quoted identifiers | Forces case-sensitive names across all queries | Use `snake_case` unquoted identifiers |

## Cross-References

- Related: `data-science/data-quality-auditor` — data quality checks for pipeline outputs
- Related: `devops/terraform-patterns` — infrastructure provisioning for Snowflake resources
- Related: `software-development/sql-optimization-patterns` — general SQL optimization
