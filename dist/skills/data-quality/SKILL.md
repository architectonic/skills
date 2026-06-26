---
name: data-quality
description: Implement data quality validation with Great Expectations, dbt tests, and data contracts. Covers 6 quality dimensions, testing pyramid, automated validation pipelines, and data contract specification.
type: Playbook
---

# Data Quality Frameworks

Production patterns for implementing data quality with Great Expectations, dbt tests, and data contracts to ensure reliable data pipelines.

## Use this skill when

- Implementing data quality checks in pipelines
- Setting up Great Expectations validation
- Building comprehensive dbt test suites
- Establishing data contracts between teams
- Monitoring data quality metrics
- Automating data validation in CI/CD

## Do not use this skill when

- The data sources are undefined or unavailable
- You cannot modify validation rules or schemas
- The task is unrelated to data quality or contracts

## Data Quality Dimensions

| Dimension | Description | Example Check |
|-----------|-------------|---------------|
| **Completeness** | No missing values | `expect_column_values_to_not_be_null` |
| **Uniqueness** | No duplicates | `expect_column_values_to_be_unique` |
| **Validity** | Values in expected range | `expect_column_values_to_be_in_set` |
| **Accuracy** | Data matches reality | Cross-reference validation |
| **Consistency** | No contradictions | `expect_column_pair_values_A_to_be_greater_than_B` |
| **Timeliness** | Data is recent | `expect_column_max_to_be_between` |

## Testing Pyramid for Data

```
          /\
         /  \     Integration Tests (cross-table)
        /────\
       /      \   Unit Tests (single column)
      /────────\
     /          \ Schema Tests (structure)
    /────────────\
```

## Great Expectations

### Setup
```bash
pip install great_expectations
great_expectations init
great_expectations datasource new
```

### Expectation Suite Pattern
```python
import great_expectations as gx

context = gx.get_context()
suite = context.add_expectation_suite("orders_suite")

# Schema expectations
suite.add_expectation(gx.expectations.ExpectTableColumnsToMatchSet(
    column_set=["order_id", "customer_id", "amount", "status", "created_at"]
))

# Primary key
suite.add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(column="order_id"))
suite.add_expectation(gx.expectations.ExpectColumnValuesToBeUnique(column="order_id"))

# Categorical values
suite.add_expectation(gx.expectations.ExpectColumnValuesToBeInSet(
    column="status",
    value_set=["pending", "processing", "shipped", "delivered", "cancelled"]
))

# Numeric ranges
suite.add_expectation(gx.expectations.ExpectColumnValuesToBeBetween(
    column="amount", min_value=0, max_value=100000, strict_min=True
))

# Row count sanity
suite.add_expectation(gx.expectations.ExpectTableRowCountToBeBetween(
    min_value=1000, max_value=10000000
))

# Run validation
results = context.run_checkpoint(checkpoint_name="daily_orders")
```

### Checkpoint with Notifications
```yaml
# great_expectations/checkpoints/orders_checkpoint.yml
name: orders_checkpoint
config_version: 1.0
class_name: Checkpoint
run_name_template: "%Y%m%d-%H%M%S-orders-validation"

validations:
  - batch_request:
      datasource_name: warehouse
      data_connector_name: default_inferred_data_connector_name
      data_asset_name: orders
      data_connector_query:
        index: -1
    expectation_suite_name: orders_suite

action_list:
  - name: store_validation_result
    action:
      class_name: StoreValidationResultAction
  - name: update_data_docs
    action:
      class_name: UpdateDataDocsAction
  - name: send_slack_notification
    action:
      class_name: SlackNotificationAction
      slack_webhook: ${SLACK_WEBHOOK}
      notify_on: failure
```

## dbt Data Tests

### Schema Tests (YAML)
```yaml
# models/marts/core/_core__models.yml
version: 2

models:
  - name: fct_orders
    description: Order fact table
    tests:
      - dbt_utils.recency:
          datepart: day
          field: created_at
          interval: 1
      - dbt_utils.at_least_one
      - dbt_utils.expression_is_true:
          expression: "total_amount >= 0"

    columns:
      - name: order_id
        tests:
          - unique
          - not_null

      - name: customer_id
        tests:
          - not_null
          - relationships:
              to: ref('dim_customers')
              field: customer_id

      - name: order_status
        tests:
          - accepted_values:
              values: ['pending', 'processing', 'shipped', 'delivered', 'cancelled']

      - name: total_amount
        tests:
          - not_null
          - dbt_utils.expression_is_true:
              expression: ">= 0"
```

### Custom dbt Tests
```sql
-- tests/generic/test_row_count_in_range.sql
{% test row_count_in_range(model, min_count, max_count) %}
with row_count as (
    select count(*) as cnt from {{ model }}
)
select cnt from row_count
where cnt < {{ min_count }} or cnt > {{ max_count }}
{% endtest %}
```

### Singular Tests (Business Rules)
```sql
-- tests/singular/assert_orders_customers_match.sql
with orders_customers as (
    select distinct customer_id from {{ ref('fct_orders') }}
),
dim_customers as (
    select customer_id from {{ ref('dim_customers') }}
),
orphaned_orders as (
    select o.customer_id
    from orders_customers o
    left join dim_customers c using (customer_id)
    where c.customer_id is null
)
select * from orphaned_orders
-- Test passes if this returns 0 rows
```

## Data Contracts

```yaml
# contracts/orders_contract.yaml
apiVersion: datacontract.com/v1.0.0
kind: DataContract
metadata:
  name: orders
  version: 1.0.0
  owner: data-platform-team

info:
  title: Orders Data Contract
  description: Contract for order event data from the ecommerce platform

schema:
  properties:
    order_id:
      type: string
      format: uuid
      required: true
      unique: true
    customer_id:
      type: string
      format: uuid
      required: true
      pii: true
    total_amount:
      type: number
      minimum: 0
      maximum: 100000
    status:
      type: string
      enum: [pending, processing, shipped, delivered, cancelled]

quality:
  type: SodaCL
  specification:
    checks for orders:
      - row_count > 0
      - missing_count(order_id) = 0
      - duplicate_count(order_id) = 0
      - freshness(created_at) < 24h

sla:
  availability: 99.9%
  freshness: 1 hour
  latency: 5 minutes
```

## Automated Quality Pipeline

```python
import great_expectations as gx
from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict, Any

@dataclass
class QualityResult:
    table: str
    passed: bool
    total_expectations: int
    failed_expectations: int
    details: List[Dict[str, Any]]
    timestamp: datetime

class DataQualityPipeline:
    def __init__(self, context: gx.DataContext):
        self.context = context
        self.results: List[QualityResult] = []

    def validate_table(self, table: str, suite: str) -> QualityResult:
        checkpoint_config = {
            "name": f"{table}_validation",
            "config_version": 1.0,
            "class_name": "Checkpoint",
            "validations": [{
                "batch_request": {
                    "datasource_name": "warehouse",
                    "data_asset_name": table,
                },
                "expectation_suite_name": suite,
            }],
        }
        result = self.context.run_checkpoint(**checkpoint_config)
        validation_result = list(result.run_results.values())[0]
        results = validation_result.results
        failed = [r for r in results if not r.success]

        return QualityResult(
            table=table,
            passed=result.success,
            total_expectations=len(results),
            failed_expectations=len(failed),
            details=[{
                "expectation": r.expectation_config.expectation_type,
                "success": r.success,
                "observed_value": r.result.get("observed_value"),
            } for r in results],
            timestamp=datetime.now()
        )

    def run_all(self, tables: Dict[str, str]) -> Dict[str, QualityResult]:
        results = {}
        for table, suite in tables.items():
            results[table] = self.validate_table(table, suite)
        return results
```

## Safety

- Avoid blocking critical pipelines without a fallback plan
- Handle sensitive data securely in validation outputs
- Use dead letter queues for invalid records rather than silent drops

## Source

Distilled from `antigravity-awesome-skills/skills/data-quality-frameworks/SKILL.md` and `skills/data-quality-frameworks/resources/implementation-playbook.md` (community contribution, 2026-02-27).
