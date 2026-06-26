---
name: Command Organization
description: Organize commands with namespaces, follow best practices, and use common patterns (review, testing, documentation, workflow). Use when structuring a command library or designing multi-command workflows.
tags: [mcp, commands, organization, patterns, namespaces]
type: Playbook
---

# Command Organization

## Flat Structure

Simple organization for small command sets (5-15 commands):

```
.claude/commands/
├── build.md
├── test.md
├── deploy.md
├── review.md
└── docs.md
```

## Namespaced Structure

Organize commands in subdirectories (15+ commands):

```
.claude/commands/
├── ci/
│   ├── build.md        # /build (project:ci)
│   ├── test.md         # /test (project:ci)
│   └── lint.md         # /lint (project:ci)
├── git/
│   ├── commit.md       # /commit (project:git)
│   └── pr.md           # /pr (project:git)
└── docs/
    ├── generate.md     # /generate (project:docs)
    └── publish.md      # /publish (project:docs)
```

Benefits: Logical grouping, namespace in `/help`, avoids name conflicts

## Naming Conventions

- Use descriptive action names
- Avoid generic names (test, run)
- Use verb-noun pattern: `review-pr`, `fix-issue`
- Use hyphens for multi-word names

## Best Practices

### Command Design

1. **Single responsibility:** One command, one task
2. **Clear descriptions:** Self-explanatory in `/help`
3. **Explicit dependencies:** Use `allowed-tools` when needed
4. **Document arguments:** Always provide `argument-hint`
5. **Consistent naming:** Use verb-noun pattern

### Argument Handling

1. **Validate arguments:** Check for required arguments
2. **Provide defaults:** Suggest defaults when arguments missing
3. **Document format:** Explain expected argument format
4. **Handle edge cases:** Consider missing or invalid arguments

### Documentation

1. **Add comments:** Explain complex logic
2. **Provide examples:** Show usage in comments
3. **List requirements:** Document dependencies
4. **Version commands:** Note breaking changes

## Common Patterns

### Review Pattern

```markdown
---
description: Review code changes
allowed-tools: Read, Bash(git:*)
---

Files changed: !`git diff --name-only`
Review each file for code quality, bugs, test coverage, documentation needs.
```

### Testing Pattern

```markdown
---
description: Run tests for specific file
argument-hint: [test-file]
allowed-tools: Bash(npm:*)
---

Run tests: !`npm test $1`
Analyze results and suggest fixes for failures.
```

### Documentation Pattern

```markdown
---
description: Generate documentation for file
argument-hint: [source-file]
---

Generate comprehensive documentation for @$1 including:
Function/class descriptions, parameter docs, return values, usage examples, edge cases.
```

### Workflow Pattern

```markdown
---
description: Complete PR workflow
argument-hint: [pr-number]
allowed-tools: Bash(gh:*), Read
---

PR #$1 Workflow:
1. Fetch PR: !`gh pr view $1`
2. Review changes
3. Run checks
4. Approve or request changes
```
