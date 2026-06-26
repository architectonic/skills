---
name: API Design Reviewer — Linting, Breaking Change Detection, and Scorecards
description: Comprehensive REST API design review with automated linting, breaking-change detection, and design scorecards. Catches inconsistent conventions, missing versioning, and design smells before APIs ship. Use when reviewing a PR that adds or changes API endpoints, auditing an existing API for v2 migration, or establishing API standards for a team.
version: 1.0.0
source: claude-skills/engineering/api-design-reviewer (MIT)
author: Claude Skills Team (distilled by Agent-Memory-Ops-Kit)
tags: [software-development, engineering, api, rest, design-review, breaking-change, linting, openapi]
type: API Endpoint
---

# API Design Reviewer — Linting, Breaking Change Detection, and Scorecards

Comprehensive analysis and review of API designs, focusing on REST conventions, best practices, and industry standards. Helps engineering teams build consistent, maintainable, and well-designed APIs.

## When to use

- Reviewing a PR that adds or changes API endpoints.
- Auditing an existing API for v2 migration.
- Establishing API standards for a team.
- Pre-release API quality gate.

## Core Capabilities

### 1. API Linting and Convention Analysis

- **Resource Naming Conventions**: Enforces kebab-case for resources, camelCase for fields
- **HTTP Method Usage**: Validates proper use of GET, POST, PUT, PATCH, DELETE
- **URL Structure**: Analyzes endpoint patterns for consistency and RESTful design
- **Status Code Compliance**: Ensures appropriate HTTP status codes are used
- **Error Response Formats**: Validates consistent error response structures
- **Documentation Coverage**: Checks for missing descriptions and documentation gaps

### 2. Breaking Change Detection

- **Endpoint Removal**: Detects removed or deprecated endpoints
- **Response Shape Changes**: Identifies modifications to response structures
- **Field Removal**: Tracks removed or renamed fields in API responses
- **Type Changes**: Catches field type modifications that could break clients
- **Required Field Additions**: Flags new required fields that could break existing integrations
- **Status Code Changes**: Detects changes to expected status codes

### 3. API Design Scoring

| Dimension | Weight | Criteria |
|-----------|--------|----------|
| Consistency | 30% | Naming conventions, response patterns, structural structure |
| RESTfulness | 25% | Proper HTTP methods, resource-oriented URLs, statelessness |
| Error handling | 20% | Consistent error format, appropriate status codes, useful messages |
| Documentation | 15% | Complete descriptions, examples, OpenAPI spec coverage |
| Versioning | 10% | Clear versioning strategy, backward compatibility |

Grades: A (90+), B (80-89), C (70-79), D (60-69), F (<60)

## API Design Smells

Watch for these anti-patterns:

1. **Inconsistent naming**: `/users` vs `/UserAccounts` vs `/account_list`
2. **RPC-style endpoints**: `/getUser`, `/createOrder` (should be resource-oriented)
3. **Missing error schema**: 200 for success, but no consistent error format for 4xx/5xx
4. **No versioning**: Breaking changes shipped without version bump
5. **Over-fetching**: Every endpoint returns the full object graph
6. **Under-fetching**: Client needs 3 API calls to render one page
7. **Missing pagination**: List endpoints return all records
8. **Inconsistent auth**: Some endpoints use Bearer, others use API key, others use cookies

## Review Workflow

1. **Lint**: Run API linting against OpenAPI/Swagger spec or route definitions.
2. **Detect breaking changes**: Compare current spec against previous version.
3. **Score**: Compute design quality grade.
4. **Report**: Present findings with severity (CRITICAL / WARNING / INFO).
5. **Fix**: Address findings, re-run until clean.

## Source

Distilled from `claude-skills/engineering/skills/api-design-reviewer/SKILL.md` (Claude Skills Team, MIT).
Adapted for Hermes Agent — removed Claude Code-specific tool references.
