---
name: SQL Optimization Patterns
description: Master SQL query optimization, indexing strategies, and EXPLAIN analysis to dramatically improve database performance and eliminate slow queries. Use when debugging slow queries, designing database schemas, or optimizing application performance.
source: AgentSkillOS/data/skill_seeds/sql-optimization-patterns/SKILL.md
source_license: Apache-2.0 (AgentSkillOS)
type: Playbook
---

# SQL Optimization Patterns

Transform slow database queries into lightning-fast operations through systematic optimization, proper indexing, and query plan analysis.

## When to Use This Skill

- Debugging slow-running queries
- Designing performant database schemas
- Optimizing application response times
- Reducing database load and costs
- Analyzing EXPLAIN query plans
- Implementing efficient indexes
- Resolving N+1 query problems

## Core Concepts

### 1. Query Execution Plans (EXPLAIN)

```sql
-- Basic explain
EXPLAIN SELECT * FROM users WHERE email = 'user@example.com';

-- With actual execution stats
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'user@example.com';

-- Verbose output with buffers
EXPLAIN (ANALYZE, BUFFERS, VERBOSE)
SELECT u.*, o.order_total
FROM users u
JOIN orders o ON u.id = o.user_id
WHERE u.created_at > NOW() - INTERVAL '30 days';
```

**Key Metrics to Watch:**
- **Seq Scan**: Full table scan (usually slow for large tables)
- **Index Scan**: Using index (good)
- **Index Only Scan**: Using index without touching table (best)
- **Nested Loop**: Join method (okay for small datasets)
- **Hash Join**: Join method (good for larger datasets)
- **Merge Join**: Join method (good for sorted data)

### 2. Index Strategies

```sql
-- Standard B-Tree index
CREATE INDEX idx_users_email ON users(email);

-- Composite index (order matters!)
CREATE INDEX idx_orders_user_status ON orders(user_id, status);

-- Partial index (index subset of rows)
CREATE INDEX idx_active_users ON users(email) WHERE status = 'active';

-- Expression index
CREATE INDEX idx_users_lower_email ON users(LOWER(email));

-- Covering index (include additional columns)
CREATE INDEX idx_users_email_covering ON users(email) INCLUDE (name, created_at);

-- Full-text search index
CREATE INDEX idx_posts_search ON posts
USING GIN(to_tsvector('english', title || ' ' || body));
```

### 3. Essential Optimization Patterns

**Avoid SELECT \*:**
```sql
-- Bad
SELECT * FROM users WHERE id = 123;
-- Good
SELECT id, email, name FROM users WHERE id = 123;
```

**Optimize JOINs — filter before join:**
```sql
-- Bad: Cartesian product then filter
SELECT u.name, o.total FROM users u, orders o
WHERE u.id = o.user_id AND u.created_at > '2024-01-01';

-- Good: Filter before join
SELECT u.name, o.total
FROM users u JOIN orders o ON u.id = o.user_id
WHERE u.created_at > '2024-01-01';
```

## Optimization Patterns

### Pattern 1: Eliminate N+1 Queries

```python
# Bad: Executes N+1 queries
users = db.query("SELECT * FROM users LIMIT 10")
for user in users:
    orders = db.query("SELECT * FROM orders WHERE user_id = ?", user.id)

# Good: Single query with JOIN
results = db.query("""
    SELECT u.id, u.name, o.id as order_id, o.total
    FROM users u LEFT JOIN orders o ON u.id = o.user_id
    WHERE u.id IN (1, 2, 3, 4, 5)
""")
```

### Pattern 2: Cursor-Based Pagination

```sql
-- Bad: OFFSET on large tables (slow)
SELECT * FROM users ORDER BY created_at DESC LIMIT 20 OFFSET 100000;

-- Good: Cursor-based (fast)
SELECT * FROM users
WHERE created_at < '2024-01-15 10:30:00'
ORDER BY created_at DESC LIMIT 20;

-- Requires index
CREATE INDEX idx_users_cursor ON users(created_at DESC, id DESC);
```

### Pattern 3: Optimize Aggregates

```sql
-- Use estimates for approximate counts
SELECT reltuples::bigint AS estimate FROM pg_class WHERE relname = 'orders';

-- Filter before counting
SELECT COUNT(*) FROM orders WHERE created_at > NOW() - INTERVAL '7 days';

-- Covering index for GROUP BY
CREATE INDEX idx_orders_user_status ON orders(user_id, status);
```

### Pattern 4: Transform Correlated Subqueries

```sql
-- Bad: Correlated subquery (runs for each row)
SELECT u.name, (SELECT COUNT(*) FROM orders o WHERE o.user_id = u.id) as cnt
FROM users u;

-- Good: JOIN with aggregation
SELECT u.name, COUNT(o.id) as order_count
FROM users u LEFT JOIN orders o ON o.user_id = u.id
GROUP BY u.id, u.name;
```

### Pattern 5: Batch Operations

```sql
-- Batch INSERT
INSERT INTO users (name, email) VALUES
    ('Alice', 'alice@example.com'),
    ('Bob', 'bob@example.com'),
    ('Carol', 'carol@example.com');

-- Batch UPDATE via temp table
CREATE TEMP TABLE temp_updates (id INT, new_status VARCHAR);
INSERT INTO temp_updates VALUES (1, 'active'), (2, 'active');
UPDATE users u SET status = t.new_status FROM temp_updates t WHERE u.id = t.id;
```

## Advanced Techniques

### Materialized Views

```sql
CREATE MATERIALIZED VIEW user_order_summary AS
SELECT u.id, u.name, COUNT(o.id) as total_orders, SUM(o.total) as total_spent
FROM users u LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.name;

CREATE INDEX idx_summary_spent ON user_order_summary(total_spent DESC);
REFRESH MATERIALIZED VIEW CONCURRENTLY user_order_summary;
```

### Table Partitioning

```sql
-- Range partitioning by date
CREATE TABLE orders (
    id SERIAL, user_id INT, total DECIMAL, created_at TIMESTAMP
) PARTITION BY RANGE (created_at);

CREATE TABLE orders_2024_q1 PARTITION OF orders
    FOR VALUES FROM ('2024-01-01') TO ('2024-04-01');
```

## Monitoring Queries

```sql
-- Find slow queries (PostgreSQL)
SELECT query, calls, total_time, mean_time
FROM pg_stat_statements ORDER BY mean_time DESC LIMIT 10;

-- Find missing indexes
SELECT schemaname, tablename, seq_scan, seq_tup_read
FROM pg_stat_user_tables WHERE seq_scan > 0 ORDER BY seq_tup_read DESC LIMIT 10;

-- Find unused indexes
SELECT schemaname, tablename, indexname, idx_scan
FROM pg_stat_user_indexes WHERE idx_scan = 0
ORDER BY pg_relation_size(indexrelid) DESC;
```

## Best Practices

1. **Index Selectively**: Too many indexes slow down writes
2. **Monitor Query Performance**: Use slow query logs
3. **Keep Statistics Updated**: Run `ANALYZE` regularly
4. **Use Appropriate Data Types**: Smaller types = better performance
5. **Connection Pooling**: Reuse database connections
6. **Regular Maintenance**: `VACUUM`, `ANALYZE`, rebuild indexes

## Common Pitfalls

- **Over-Indexing**: Each index slows down INSERT/UPDATE/DELETE
- **Implicit Type Conversion**: Prevents index usage
- **OR Conditions**: Can't use indexes efficiently
- **LIKE with Leading Wildcard**: `LIKE '%abc'` can't use index
- **Function in WHERE**: Prevents index usage unless functional index exists
