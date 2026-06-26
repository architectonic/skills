---
name: Database Design
description: Database design principles and decision-making. Schema design, indexing strategy, ORM selection, serverless databases, and safe migration patterns.
tags: [software-development, database, schema, orm, sql, migrations, design]
type: Playbook
---

# Database Design

## When to Use
- Designing a new database schema for an application
- Choosing between database systems (PostgreSQL, MySQL, SQLite, Neon, Turso, etc.)
- Selecting an ORM (Drizzle, Prisma, Kysely, SQLAlchemy, etc.)
- Planning indexing strategies for performance
- Designing safe database migration workflows
- Optimizing schema for query patterns

## When NOT to Use
- Simple key-value storage needs (use a cache or document store)
- Non-relational requirements (graph, time-series, vector databases)
- The task is purely about query writing, not schema design

## Database Selection Decision Tree

| Requirement | Recommended |
|---|---|
| Complex transactions, ACID | PostgreSQL |
| Simple CRUD, serverless | Turso (SQLite), Neon (PostgreSQL) |
| Embedded / local | SQLite, DuckDB |
| High-write throughput | ScyllaDB, Cassandra |
| Full-text search | PostgreSQL, Meilisearch |
| Caching layer | Redis, KeyDB |
| Time-series | TimescaleDB, InfluxDB |
| Graph relationships | Neo4j |
| Vector search | pgvector, Pinecone, Weaviate |

## Schema Design Principles

### Normalization vs Denormalization
- **Normalize** when: write performance matters, data consistency is critical, storage is constrained
- **Denormalize** when: read performance matters, query patterns are known, data is read-heavy
- **Start normalized**, denormalize selectively based on measured query patterns

### Primary Keys
- Use UUIDs for distributed systems (no collision risk, no sequential info leakage)
- Use auto-increment integers for single-instance databases (smaller index size, faster joins)
- Use composite natural keys only when the natural key is truly immutable

### Relationships
- **One-to-Many**: Foreign key on the "many" side
- **Many-to-Many**: Junction/bridge table with both foreign keys
- **One-to-One**: Shared primary key or unique foreign key constraint
- **Polymorphic**: Use a `type` column + separate tables per type, or JSONB for flexible attributes

### Indexing Strategy
- Index columns used in WHERE, JOIN, ORDER BY clauses
- Composite indexes: put equality columns first, range columns last
- Don't over-index — each index slows writes and consumes storage
- Use partial indexes for queries that filter on a subset of rows
- Monitor index usage and remove unused indexes (`pg_stat_user_indexes`)

## ORM Selection

| ORM | Language | Best For |
|---|---|---|
| Drizzle | TypeScript | Type-safe SQL, tree-shakeable, edge-compatible |
| Prisma | TypeScript | Rapid prototyping, type-safe, migrations built-in |
| Kysely | TypeScript | Composable query builder, SQL-first |
| SQLAlchemy | Python | Mature ecosystem, complex queries |
| SQLModel | Python | Pydantic integration, FastAPI projects |
| Eloquent | PHP | Laravel projects, simple Active Record |
| Active Record | Ruby | Rails projects, convention over configuration |

## Safe Migration Patterns

1. **Expand-Contract Pattern**: Add new columns/tables → deploy code using both → remove old columns/tables
2. **Blue-Green Migrations**: Run migrations on a green database, switch traffic after verification
3. **Backward-Compatible Changes**: Never rename or drop columns in a single release
4. **Rollback Plans**: Every migration must have a tested rollback procedure
5. **Non-Null Defaults**: Add columns with defaults or make nullable, backfill, then set NOT NULL

## Anti-Patterns to Avoid

- Defaulting to PostgreSQL for simple apps (SQLite may suffice)
- Skipping indexes on foreign keys
- Using SELECT * in production queries
- Storing JSON when structured data is better
- Ignoring N+1 queries (use eager loading or batch queries)
- Using UUIDs as clustered primary keys (causes page splits in MySQL/InnoDB)
- Over-normalizing for read-heavy workloads

## Related Skills
- `software-development/sql-optimization-patterns.md` — query-level optimization
- `software-development/postgresql-table-design.md` — PostgreSQL-specific design
- `software-development/schema-versioning.md` — schema versioning workflows
- `software-development/database-migration.md` — migration pipelines
