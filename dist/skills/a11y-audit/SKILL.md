---
name: a11y-audit
description: WCAG 2.2 accessibility audit pipeline — scan, fix, and verify Level A/AA compliance across React, Next.js, Vue, Angular, Svelte, and plain HTML. Use when auditing accessibility, fixing a11y violations, checking color contrast, generating compliance reports, or integrating a11y checks into CI/CD.
type: Playbook
---

# Accessibility Audit (a11y-audit)

WCAG 2.2 Level A/AA audit and remediation pipeline. Three-phase workflow: **Scan → Fix → Verify**.

## Severity Classification

| Severity | Definition | Example | SLA |
|----------|-----------|---------|-----|
| **Critical** | Blocks access for entire user groups | Missing alt text, no keyboard access | Fix before release |
| **Major** | Significant barrier degrading experience | Insufficient contrast, missing form labels | Fix within current sprint |
| **Minor** | Usability friction | Redundant ARIA roles, suboptimal heading hierarchy | Fix within 2 sprints |

## Three-Phase Workflow

### Phase 1: Scan
Walk the source tree, detect framework, apply WCAG 2.2 rule set. Output violations with file locations, WCAG criteria references, and severity.

### Phase 2: Fix
Apply framework-specific before/after code patterns per violation. Every fix maps to a specific WCAG success criterion.

### Phase 3: Verify
Re-run scan against baseline. Confirm fixes resolved original violations. Check for regressions.

## Framework Support
Auto-detects: React, Next.js, Vue, Angular, Svelte, plain HTML.

## Common Pitfalls

| Pitfall | Correct Approach |
|---------|-----------------|
| `role="button"` on `<div>` | Use native `<button>` (includes keyboard handling) |
| `tabindex="0"` on everything | Only interactive elements need focus |
| `aria-label` on non-interactive elements | Use `aria-labelledby` pointing to visible text |
| `display: none` for screen reader hiding | Use `.sr-only` class |
| Color alone to convey meaning | Add icons, text labels, or patterns |
| Placeholder as only label | Always provide visible `<label>` |
| `outline: none` without replacement | Provide visible focus indicator via `focus-visible` |
| Empty `alt=""` on informational images | Informational images need descriptive alt text |
| Skipping heading levels (h1 → h3) | Heading levels must be sequential |
| `onClick` without `onKeyDown` | Add keyboard support or prefer native elements |
| Ignoring `prefers-reduced-motion` | Wrap animations in `@media (prefers-reduced-motion: no-preference)` |

## WCAG 2.2 New Criteria (vs 2.1)
- **Focus Appearance** (2.4.11): Visible focus indicator with minimum area
- **Target Size** (2.5.8): Minimum 24×24px touch target
- **Dragging Movements** (2.5.7): Provide single-pointer alternative
- **Consistent Help** (3.2.6): Help mechanisms in consistent location
- **Redundant Entry** (3.3.7): Don't re-ask info already provided
- **Accessible Authentication** (3.3.8): Login without cognitive function test

## CI/CD Integration
GitHub Actions, GitLab CI, Azure DevOps pipeline configs available. Non-zero exit code on critical issues.

## References
- [WCAG 2.2 Specification](https://www.w3.org/TR/WCAG22/)
- [WAI-ARIA Authoring Practices 1.2](https://www.w3.org/WAI/ARIA/apg/)
- [Deque axe-core Rules](https://github.com/dequelabs/axe-core/blob/develop/doc/rule-descriptions.md)
- [eslint-plugin-jsx-a11y](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y)
