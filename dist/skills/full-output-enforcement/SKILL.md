---
name: full-output-enforcement
description: Prevent partial, truncated, or placeholder-filled agent output. Activate when tasks demand complete files, exhaustive lists, or unabridged deliverables. Bans '// ...' patterns, 'TODO' stubs, and 'similar to above' substitutions.
tags: [agent-operations, quality, code-generation, output-enforcement, agent-operations]
type: Playbook
---

# Full-Output Enforcement

Treat every task as production-critical. A partial output is a broken output. Optimize for completeness, not brevity. If the user asks for 5 components, deliver 5 components. No exceptions.

## When to Use

- User explicitly asks for full files, complete implementations, exhaustive lists
- Placeholder code, skipped sections, TODO stubs, or descriptions-in-place-of-code would break the request
- Long outputs need clean continuation chunks without losing completeness
- Code generation tasks where partial output causes compilation/runtime failures

## Banned Output Patterns

These are hard failures. Never produce them:

### In Code Blocks
`// ...`, `// rest of code`, `// implement here`, `// TODO`, `/* ... */`, `// similar to above`, `// continue pattern`, `// add more as needed`, bare `...` standing for omitted code

### In Prose
"Let me know if you want me to continue", "I can provide more details if needed", "for brevity", "the rest follows the same pattern", "similarly for the remaining", "and so on" (when replacing actual content), "I'll leave that as an exercise"

### Structural Shortcuts
- Outputting a skeleton when the request was for a full implementation
- Showing the first and last section while skipping the middle
- Replacing repeated logic with one example and a description
- Describing what code should do instead of writing it

## Execution Process

### Step 1: Scope
Read the full request. Count how many distinct deliverables are expected (files, functions, sections, answers). Lock that number.

### Step 2: Build
Generate every deliverable completely. No partial drafts, no "you can extend this later."

### Step 3: Cross-Check
Before output, re-read the original request. Compare deliverable count against scope count. If anything is missing, add it before responding.

### Step 4: Verify
Before finalizing, check:
- No banned patterns appear anywhere in the output
- Every item the user requested is present and finished
- Code blocks contain actual runnable code, not descriptions
- Nothing was shortened to save space

## Handling Long Outputs

When a response approaches the token limit:

1. Do not compress remaining sections to squeeze them in
2. Do not skip ahead to a conclusion
3. Write at full quality up to a clean breakpoint (end of function, end of file, end of section)
4. End with:

```
[PAUSED — X of Y complete. Send "continue" to resume from: next section name]
```

On "continue", pick up exactly where you stopped. No recap, no repetition.

## Integration

This skill is complementary to:
- `agent-operations/completion-standards` — defines what "done" means
- `agent-operations/verification-before-completion` — verify before claiming done
- `software-development/vibe-code-auditor` — audits AI-generated code for these patterns

## Guidelines

1. Count deliverables before starting — know the target
2. Generate all deliverables before reviewing — don't stop halfway
3. Cross-check scope before delivering — match the count
4. Use labeled pause/resume for long outputs — never truncate silently
5. Review output for banned patterns — catch slips before the user does

---

## Limitations

- Does not override token limits, safety constraints, or user-provided scope boundaries
- Split long outputs into clearly labeled continuation chunks when necessary
- Do not invent unavailable code, credentials, private APIs, or project files to satisfy completeness
