---
name: Command Dynamic Features
description: Use dynamic arguments ($ARGUMENTS, $1, $2) and file references (@ syntax) in slash commands. Use when building commands that accept user input or include file contents.
tags: [mcp, commands, arguments, file-references, dynamic]
type: Playbook
---

# Command Dynamic Features

## Dynamic Arguments

### Using $ARGUMENTS

Capture all arguments as single string:

```markdown
---
description: Fix issue by number
argument-hint: [issue-number]
---

Fix issue #$ARGUMENTS following our coding standards and best practices.
```

Usage: `/fix-issue 123` → "Fix issue #123 following our coding standards..."

### Using Positional Arguments

Capture individual arguments with `$1`, `$2`, `$3`:

```markdown
---
description: Review PR with priority and assignee
argument-hint: [pr-number] [priority] [assignee]
---

Review pull request #$1 with priority level $2.
After review, assign to $3 for follow-up.
```

### Combining Arguments

```markdown
Deploy $1 to $2 environment with options: $3
```

Usage: `/deploy api staging --force --skip-tests`

## File References

### Using @ Syntax

Include file contents in command:

```markdown
---
description: Review specific file
argument-hint: [file-path]
---

Review @$1 for:
- Code quality
- Best practices
- Potential bugs
```

### Multiple File References

```markdown
Compare @src/old-version.js with @src/new-version.js
Identify breaking changes, new features, and bug fixes.
```

### Static File References

```markdown
Review @package.json and @tsconfig.json for consistency
Ensure TypeScript version matches, dependencies are aligned.
```

## Bash Execution in Commands

Commands can execute bash inline to gather dynamic context:

```markdown
---
description: Check git status and review changes
allowed-tools: Read, Bash(git:*)
---

Files changed: !`git diff --name-only`

Review each file for code quality and potential issues.
```

Use for: git status, environment vars, project state, build context.
