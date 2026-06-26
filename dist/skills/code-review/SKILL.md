---
name: Code Review
description: Pre-landing PR review analyzing diff for structural issues, security concerns, and correctness. Use when asked to "review this PR", "code review", "check my diff", or before merging any pull request.
tags: [software-development, software-development, code-review, pull-request, security]
type: Playbook
---

# Code Review

Pre-landing PR review. Analyzes diff against the base branch for structural issues, security concerns, and correctness.

## When to invoke

- Before merging any pull request
- When asked "review this PR" or "check my diff"
- Proactively before pushing to main

## Review checklist

### Correctness
- Logic errors or off-by-one bugs
- Edge cases (empty arrays, null/undefined, race conditions)
- Incorrect variable references or unused imports
- Missing error handling for fallible operations

### Security
- SQL injection vectors
- XSS vulnerabilities (unsanitized user input)
- Authentication/authorization gaps
- Secrets or credentials in code
- LLM trust boundary violations (prompt injection)

### Structure
- Unnecessary complexity or over-abstraction
- Duplicated code that should be extracted
- Inconsistent patterns with existing codebase
- Missing tests for new behavior

### Performance
- N+1 queries
- Unnecessary re-renders or allocations
- Missing caching for expensive operations
- Blocking operations on hot paths

## Output format

For each finding:
1. **Severity**: critical | major | minor | nit
2. **File:line**: location in the diff
3. **Issue**: what's wrong
4. **Suggestion**: how to fix (with code example if helpful)

End with: APPROVE | REQUEST_CHANGES | COMMENT

## Key principles

- Review the diff, not the whole codebase
- Distinguish "must fix" from "nice to have"
- Always suggest a fix, don't just point out problems
- Check that tests cover the new behavior
- Verify no regressions in existing tests
