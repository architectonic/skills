---
name: Command Plugin Integration
description: Integrate commands with plugin components — CLAUDE_PLUGIN_ROOT, agents, skills, hooks, and multi-component workflows. Use when building commands that reference plugin files, trigger agents, or coordinate with hooks.
tags: [mcp, commands, plugins, integration, agents, hooks]
type: Playbook
---

# Command Plugin Integration

## CLAUDE_PLUGIN_ROOT Variable

Plugin commands have access to `${CLAUDE_PLUGIN_ROOT}`, an environment variable that resolves to the plugin's absolute path.

**Purpose:** Reference plugin files portably, execute scripts, load configuration, access templates.

**Basic usage:**

```markdown
---
description: Analyze using plugin script
allowed-tools: Bash(node:*)
---

Run analysis: !`node ${CLAUDE_PLUGIN_ROOT}/scripts/analyze.js $1`
Review results and report findings.
```

**Common patterns:**

```markdown
# Execute plugin script
!`bash ${CLAUDE_PLUGIN_ROOT}/scripts/script.sh`

# Load plugin configuration
@${CLAUDE_PLUGIN_ROOT}/config/settings.json

# Use plugin template
@${CLAUDE_PLUGIN_ROOT}/templates/report.md

# Access plugin resources
@${CLAUDE_PLUGIN_ROOT}/docs/reference.md
```

Why use it: Works across installations, portable, no hardcoded paths.

## Plugin Command Organization

Plugin commands discovered automatically from `commands/` directory:

```
plugin-name/
├── commands/
│   ├── foo.md              # /foo (plugin:plugin-name)
│   ├── bar.md              # /bar (plugin:plugin-name)
│   └── utils/
│       └── helper.md       # /helper (plugin:plugin-name:utils)
└── plugin.json
```

Namespace benefits: Logical grouping, shown in `/help`, avoids name conflicts.

## Plugin Command Patterns

### Configuration-based

```markdown
---
description: Deploy using plugin configuration
argument-hint: [environment]
allowed-tools: Read, Bash(*)
---

Load configuration: @${CLAUDE_PLUGIN_ROOT}/config/$1-deploy.json
Deploy to $1 using configuration settings.
Monitor deployment and report status.
```

### Template-based

```markdown
---
description: Generate docs from template
argument-hint: [component]
---

Template: @${CLAUDE_PLUGIN_ROOT}/templates/docs.md
Generate documentation for $1 following template structure.
```

### Multi-script

```markdown
---
description: Complete build workflow
allowed-tools: Bash(*)
---

Build: !`bash ${CLAUDE_PLUGIN_ROOT}/scripts/build.sh`
Test: !`bash ${CLAUDE_PLUGIN_ROOT}/scripts/test.sh`
Package: !`bash ${CLAUDE_PLUGIN_ROOT}/scripts/package.sh`
Review outputs and report workflow status.
```

## Integration with Plugin Components

### Agent Integration

Launch plugin agents for complex tasks:

```markdown
---
description: Deep code review
argument-hint: [file-path]
---

Initiate comprehensive review of @$1 using the code-reviewer agent.
The agent will analyze: Code structure, Security issues, Performance, Best practices
Agent uses plugin resources:
- ${CLAUDE_PLUGIN_ROOT}/config/rules.json
- ${CLAUDE_PLUGIN_ROOT}/checklists/review.md
```

Key points: Agent must exist in `plugin/agents/`, document agent capabilities.

### Skill Integration

Leverage plugin skills for specialized knowledge:

```markdown
---
description: Document API with standards
argument-hint: [api-file]
---

Document API in @$1 following plugin standards.
Use the api-docs-standards skill to ensure:
Complete endpoint documentation, Consistent formatting, Example quality, Error documentation.
```

### Hook Coordination

Design commands that work with plugin hooks:
- Commands prepare state for hooks to process
- Hooks execute automatically on tool events
- Commands should document expected hook behavior

## Validation Patterns

### Argument Validation

```markdown
---
description: Deploy with validation
argument-hint: [environment]
---

Validate environment: !`echo "$1" | grep -E "^(dev|staging|prod)$" || echo "INVALID"`
If $1 is valid: Deploy to $1
Otherwise: Explain valid environments: dev, staging, prod
```

### File Existence Checks

```markdown
---
description: Process configuration
argument-hint: [config-file]
---

Check file exists: !`test -f $1 && echo "EXISTS" || echo "MISSING"`
If file exists: Process configuration: @$1
Otherwise: Explain where to place config file
```

### Plugin Resource Validation

```markdown
---
description: Run plugin analyzer
allowed-tools: Bash(test:*)
---

Validate plugin setup:
- Script: !`test -x ${CLAUDE_PLUGIN_ROOT}/bin/analyze && echo "✓" || echo "✗"`
- Config: !`test -f ${CLAUDE_PLUGIN_ROOT}/config.json && echo "✓" || echo "✗"`
If all checks pass, run analysis. Otherwise, report missing components.
```

### Error Handling

```markdown
---
description: Build with error handling
allowed-tools: Bash(*)
---

Execute build: !`bash ${CLAUDE_PLUGIN_ROOT}/scripts/build.sh 2>&1 || echo "BUILD_FAILED"`
If build succeeded: Report success and output location
If build failed: Analyze error output, suggest likely causes, provide troubleshooting steps
```

Best practices: Validate early, provide helpful error messages, suggest corrective actions, handle edge cases.
