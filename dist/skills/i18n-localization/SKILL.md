---
name: i18n-localization
description: Internationalization and localization patterns. Detecting hardcoded strings, managing translations, locale files, RTL support. Use when making a web app translatable, managing multi-language content, or implementing RTL language support.
type: Playbook
---

# i18n & Localization

> Internationalization (i18n) and Localization (L10n) best practices for making web applications translatable.

## When to Use

- Making a web app translatable for multiple languages
- Managing multi-language content and locale files
- Implementing RTL (right-to-left) language support
- Detecting and fixing hardcoded strings in components
- Setting up translation infrastructure for a new or existing project

## When NOT to Use

- Single-language internal tools with no internationalization plans
- Machine translation of content (this is about engineering infrastructure, not translation itself)

## Core Concepts

| Term | Meaning |
|------|---------|
| **i18n** | Internationalization — making app translatable |
| **L10n** | Localization — actual translations per locale |
| **Locale** | Language + Region (en-US, tr-TR) |
| **RTL** | Right-to-left languages (Arabic, Hebrew) |

## i18n Need by Project Type

| Project Type | i18n Needed? |
|--------------|--------------|
| Public web app | Yes |
| SaaS product | Yes |
| Internal tool | Maybe |
| Single-region app | Consider future |
| Personal project | Optional |

## Implementation Patterns

### React (react-i18next)

```tsx
import { useTranslation } from 'react-i18next';

function Welcome() {
  const { t } = useTranslation();
  return <h1>{t('welcome.title')}</h1>;
}
```

### Next.js (next-intl)

```tsx
import { useTranslations } from 'next-intl';

export default function Page() {
  const t = useTranslations('Home');
  return <h1>{t('title')}</h1>;
}
```

### Python (gettext)

```python
from gettext import gettext as _

print(_("Welcome to our app"))
```

## File Structure

```
locales/
├── en/
│   ├── common.json
│   ├── auth.json
│   └── errors.json
├── tr/
│   ├── common.json
│   ├── auth.json
│   └── errors.json
└── ar/          # RTL
    └── ...
```

## Best Practices

### DO

- Use translation keys, not raw text
- Namespace translations by feature
- Support pluralization
- Handle date/number formats per locale
- Plan for RTL from the start
- Use ICU message format for complex strings

### DON'T

- Hardcode strings in components
- Concatenate translated strings
- Assume text length (German is ~30% longer than English)
- Forget about RTL layout
- Mix languages in the same file

## Common Issues

| Issue | Solution |
|-------|----------|
| Missing translation | Fallback to default language |
| Hardcoded strings | Use linter/checker script |
| Date format | Use `Intl.DateTimeFormat` |
| Number format | Use `Intl.NumberFormat` |
| Pluralization | Use ICU message format |

## RTL Support

```css
/* CSS Logical Properties */
.container {
  margin-inline-start: 1rem;  /* Not margin-left */
  padding-inline-end: 1rem;   /* Not padding-right */
}

[dir="rtl"] .icon {
  transform: scaleX(-1);
}
```

## Pre-Ship Checklist

- [ ] All user-facing strings use translation keys
- [ ] Locale files exist for all supported languages
- [ ] Date/number formatting uses Intl API
- [ ] RTL layout tested (if applicable)
- [ ] Fallback language configured
- [ ] No hardcoded strings in components

## Verification

Run an i18n audit:
```bash
python scripts/i18n_checker.py <project_path>
```

Look for: hardcoded strings, missing translations, inconsistent locale files, missing pluralization rules.
