---
type: Operating Instructions
title: Skills Operator Stability
description: Hardening rules for the skills loop operator so role selection follows ledger, queue pressure, review gates, and package health.
tags: [skills, loop-engineering, operator, stability, queues, package-health]
okf_version: "0.2"
status: active
---

# Skills Operator Stability

## Purpose

The skills loop operator must not choose roles casually. It should be deterministic, ledger-aware, queue-aware, and review/package gated.

## Selection Rule

Role selection is decided in this order:

1. initialize missing daily ledger;
2. respect hard review, risk, catalog, and package-health gates;
3. consume highest-priority concrete queue item;
4. apply São Paulo hour cadence;
5. stop cleanly when no justified work exists.

## Ledger Missing Rule

If `operations/daily/YYYY-MM-DD/status.json` or `queues.json` is missing, initialize both from templates and run only Reporter. Do not discover, review, normalize, package, catalog, or publish in the same run.

## Review Gate

Review and safety outrank growth.

If `queues.risk` has open items, Risk Auditor overrides Radar, Publisher, and broad Normalizer work.

If `queues.review` has high-priority open items, Source Reviewer overrides Radar and Publisher.

If a candidate lacks license/provenance clarity, keep it reference-only or blocked. Do not normalize or publish it as endorsed.

## Catalog / Package Gate

If the ledger reports catalog drift, an uncataloged new skill, stale install metadata, or mismatch between `dist/catalog.json`, `dist/catalog.md`, reports, and `dist/install-manifest.json`, Cataloger overrides Radar, Publisher, and Packager until the surfaces agree or a blocker is recorded.

Any change under `skills/` or `dist/skills/` must create or consume a catalog queue item before publication or packaging endorsement.

## Publication Gate

Publisher may run only when:

- relevant sources are reviewed;
- risk items for those sources are closed or explicitly blocked;
- catalog/install surfaces are fresh;
- the output clearly distinguishes reviewed entries from candidate/reference-only entries.

If those conditions are not met, Publisher must update status and stop or create a concrete queue item.

## Override Logging Rule

If `selected_role` differs from the hour cadence role, the run entry must include:

```json
{
  "scheduled_role": "Role from hour cadence",
  "selected_role": "Actual role",
  "override_reason": "Why queue/review/package state overrode the cadence"
}
```

## No Random Work Rule

If no queue item exists and the scheduled role has no justified action, update status and stop. Do not invent sources, normalize unreviewed material, publish premature outputs, or create decorative reports.

## Current Priority

Until current catalog drift, high-risk review items, and uncataloged high-risk skills are resolved, the loop should favor:

```text
Risk Auditor -> Cataloger -> Source Reviewer -> Cataloger
```

Radar should resume broad discovery only when review/risk/catalog queues are under control.
