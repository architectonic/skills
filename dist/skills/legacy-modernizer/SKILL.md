---
name: Legacy Modernizer
description: Refactor legacy codebases, migrate outdated frameworks, and implement gradual modernization. Handles technical debt, dependency updates, and backward compatibility.
tags: [agent-operations, legacy, refactoring, migration, modernization, technical-debt]
type: Playbook
---

# Legacy Modernizer

## When to Use
- Migrating from an outdated framework version to a modern one (e.g., jQuery→React, Java 8→17, Python 2→3)
- Decomposing a monolith into microservices incrementally
- Modernizing database access (stored procs → ORM, raw SQL → query builder)
- Updating dependencies with known security vulnerabilities
- Adding test coverage to untested legacy code
- Implementing API versioning and backward compatibility during modernization

## When NOT to Use
- Greenfield projects (use current best practices from the start)
- When a full rewrite is justified and feasible (big bang may be safer than incremental)
- When the codebase is too small to justify incremental migration overhead

## Core Principles

1. **Risk Mitigation First**: Never break existing functionality without a migration path
2. **Strangler Fig Pattern**: Gradually replace legacy components while keeping the system running
3. **Tests Before Refactoring**: Add characterization tests before changing any code
4. **Backward Compatibility**: Maintain API contracts for consumers during migration
5. **Feature Flags**: Use feature flags to control rollout of modernized components

## Migration Strategies

### Framework Migration (e.g., jQuery → React)
1. Identify leaf components with fewest dependencies
2. Add characterization tests for current behavior
3. Create adapter layer between old and new components
4. Replace leaf components one at a time
5. Integration test after each replacement
6. Remove adapter layer once migration is complete

### Language Version Migration (e.g., Python 2 → 3)
1. Add `__future__` imports for forward compatibility
2. Run `2to3` or `futurize` for automated fixes
3. Fix remaining incompatibilities manually
4. Add type hints incrementally
5. Update CI to test both versions during transition
6. Drop old version support once all tests pass

### Monolith to Microservices Decomposition
1. Identify bounded contexts using domain-driven design
2. Start with the least coupled module
3. Create API contracts for inter-service communication
4. Extract data ownership per service
5. Route traffic through an API gateway
6. Monitor and verify each extraction before proceeding

### Dependency Updates
1. Audit current dependencies for known CVEs
2. Update minor versions first (semver-compatible)
3. Test thoroughly after each update
4. For major version bumps, update code for breaking changes
5. Use lockfiles to ensure reproducible builds
6. Automate with Dependabot or Renovate

## Output Deliverables
- Migration plan with phases, milestones, and rollback procedures
- Refactored code with preserved functionality
- Characterization test suite for legacy behavior
- Compatibility shim/adapter layers where needed
- Deprecation warnings and timelines for consumers
- Rollback procedures for each phase

## Anti-Patterns to Avoid
- Starting refactoring without tests
- Changing behavior and API simultaneously
- Skipping the adapter/shim layer
- Migrating everything at once (big bang)
- Not communicating breaking changes to consumers
- Ignoring performance regression after migration

## Related Skills
- `software-development/refactoring-patterns.md` — behavior-preserving refactoring moves
- `software-development/legacy-code-safety.md` — seams, characterization tests, dependency breaking
- `software-development/migration-architect.md` — zero-downtime migration planning
- `software-development/dependency-auditor.md` — dependency auditing and CVE scanning
