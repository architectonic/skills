---
name: Code Review Excellence
description: Master effective code review practices to provide constructive feedback, catch bugs early, and foster knowledge sharing while maintaining team morale. Use when reviewing pull requests, establishing review standards, or mentoring developers.
tags: [software-development, code-review, engineering-management, mentoring, collaboration]
domain: software-engineering
risk_level: medium
requires_review: true
review_gate: repository-owner-authorized-review-only
source: AgentSkillOS/data/skill_seeds/code-review-excellence/SKILL.md
source_license: Apache-2.0 (AgentSkillOS)
source_status: reviewed-metadata-only
review_notes: Review may affect merge decisions and expose sensitive repository context; keep use bounded to authorized repositories and do not repeat secrets from reviewed code.
type: Playbook
---

# Code Review Excellence

Transform code reviews from gatekeeping to knowledge sharing through constructive feedback, systematic analysis, and collaborative improvement.

## When to Use This Skill

- Reviewing pull requests and code changes
- Establishing code review standards for teams
- Mentoring junior developers through reviews
- Conducting architecture reviews
- Improving team collaboration and reducing review cycle time

## Core Principles

**Goals of Code Review:**
- Catch bugs and edge cases
- Ensure code maintainability
- Share knowledge across team
- Enforce coding standards
- Build team culture

**Not the Goals:**
- Show off knowledge
- Nitpick formatting (use linters)
- Block progress unnecessarily
- Rewrite to your preference

## Effective Feedback Patterns

```
❌ Bad: "This is wrong."
✅ Good: "This could cause a race condition when multiple users
         access simultaneously. Consider using a mutex here."

❌ Bad: "Rename this variable."
✅ Good: "[nit] Consider `userCount` instead of `uc` for clarity.
         Not blocking if you prefer to keep it."
```

## Review Process

### Phase 1: Context Gathering (2-3 min)
1. Read PR description and linked issue
2. Check PR size (>400 lines? Ask to split)
3. Review CI/CD status (tests passing?)
4. Understand the business requirement

### Phase 2: High-Level Review (5-10 min)
1. **Architecture & Design** — Does the solution fit? Simpler approaches? Consistent with existing patterns?
2. **File Organization** — Right places? Logical grouping?
3. **Testing Strategy** — Tests present? Edge cases covered? Readable?

### Phase 3: Line-by-Line Review (10-20 min)
For each file, check: Logic & Correctness, Security, Performance, Maintainability

### Phase 4: Summary & Decision (2-3 min)
1. Summarize key concerns
2. Highlight what you liked
3. Make clear decision: ✅ Approve / 💬 Comment / 🔄 Request Changes

## Review Techniques

### Severity Labels

```
🔴 [blocking] — Must fix before merge
🟡 [important] — Should fix, discuss if disagree
🟢 [nit] — Nice to have, not blocking
💡 [suggestion] — Alternative approach to consider
📚 [learning] — Educational comment, no action needed
🎉 [praise] — Good work, keep it up!
```

### The Question Approach

```
❌ "This will fail if the list is empty."
✅ "What happens if `items` is an empty array?"

❌ "This is inefficient."
✅ "I see this loops through all users. Have we considered
    the performance impact with 100k users?"
```

### Suggest, Don't Command

```
❌ "You must change this to use async/await"
✅ "Suggestion: async/await might make this more readable.
    What do you think?"
```

### Differentiate Severity
Use collaborative language and always offer to pair on complex issues.

## Review Checklists

**Security:**
- [ ] User input validated and sanitized
- [ ] SQL queries use parameterization
- [ ] Authentication/authorization checked
- [ ] Secrets not hardcoded
- [ ] Error messages don't leak info

**Performance:**
- [ ] No N+1 queries
- [ ] Database queries indexed
- [ ] Large lists paginated
- [ ] Expensive operations cached

**Testing:**
- [ ] Happy path tested
- [ ] Edge cases covered
- [ ] Error cases tested
- [ ] Test names are descriptive
- [ ] Tests are deterministic

## Language-Specific Patterns

### Python
```python
# ❌ Mutable default arguments (shared across calls!)
def add_item(item, items=[]):

# ✅ Use None as default
def add_item(item, items=None):
    if items is None:
        items = []

# ❌ Catching too broad
except:
    pass

# ✅ Catch specific exceptions
except ValueError as e:
    logger.error(f"Invalid value: {e}")
    raise
```

### TypeScript/JavaScript
```typescript
// ❌ Using any defeats type safety
function processData(data: any) {

// ✅ Use proper types
interface DataPayload { value: string; }
function processData(data: DataPayload) {

// ❌ Not handling async errors
async function fetchUser(id: string) {
    const response = await fetch(`/api/users/${id}`);
    return response.json();
}

// ✅ Handle errors properly
async function fetchUser(id: string): Promise<User> {
    try {
        const response = await fetch(`/api/users/${id}`);
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        return await response.json();
    } catch (error) {
        console.error('Failed to fetch user:', error);
        throw error;
    }
}
```

## Handling Disagreements

1. **Seek to Understand** — "Help me understand your approach."
2. **Acknowledge Valid Points** — "That's a good point about X."
3. **Provide Data** — "Can we add a benchmark to validate?"
4. **Escalate if Needed** — "Let's get the architect to weigh in."
5. **Know When to Let Go** — Perfection is the enemy of progress.

## Best Practices

1. **Review Promptly**: Within 24 hours, ideally same day
2. **Limit PR Size**: 200-400 lines max for effective review
3. **Review in Time Blocks**: 60 minutes max, take breaks
4. **Automate What You Can**: Linters, formatters, security scans
5. **Build Rapport**: Emoji, praise, and empathy matter
6. **Be Available**: Offer to pair on complex issues

## Common Pitfalls

- **Perfectionism**: Blocking PRs for minor style preferences
- **Scope Creep**: "While you're at it, can you also..."
- **Delayed Reviews**: Letting PRs sit for days
- **Rubber Stamping**: Approving without actually reviewing
- **Bike Shedding**: Debating trivial details extensively
