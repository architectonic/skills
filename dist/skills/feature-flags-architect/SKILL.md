---
name: feature-flags-architect
description: Use when adding, retiring, or auditing feature flags. Triggers on "add a flag", "ship behind a flag", "rollout plan", "kill switch", "stale flags", "flag debt", or any progressive-delivery question. Treats flags as a controlled lifecycle with measurable debt — classify, ship, ramp, retire.
tags: [software-development, feature-flags, progressive-delivery, rollout, kill-switch, release-engineering]
type: Playbook
---

# Feature Flags Architect

End-to-end discipline for feature flags: classify them, ship them, ramp them, and retire them. Most teams treat flags as throwaway `if`-statements; this skill treats them as a controlled lifecycle with measurable debt.

## When to use

- Adding a new flag and need a rollout plan
- Auditing a codebase for stale or orphaned flags
- Choosing a flag provider (LaunchDarkly vs GrowthBook vs Statsig vs Unleash vs Flipt vs build-your-own)
- Designing a kill-switch path for a risky launch
- Cleaning up flag debt before a release freeze
- Reviewing whether a feature should ship behind a flag at all

## Core principle: flags are a lifecycle, not an `if`

```
request → design → ship → ramp → cleanup → archive
```

Flags that skip cleanup become debt: dead branches, stale defaults, untested code paths, unbounded blast radius.

## The 4 flag types (taxonomy)

Different flag types have different lifespans and ownership. Misclassifying creates debt.

| Type | Purpose | Typical lifespan | Owner | Cleanup trigger |
|---|---|---|---|---|
| **Release** | Hide unfinished features in production | days–weeks | Eng | 100% rollout reached |
| **Experiment** | A/B test variants | weeks | Product/Marketing | Test concluded; winner picked |
| **Operational** | Circuit breakers, perf toggles, kill switches | months–years | Eng/SRE | Replaced by autoscaling/feature retirement |
| **Permission** | Entitlements per user/account/plan | years (permanent) | Product | Plan/role removed |

Only Release and Experiment flags should be on a debt-scanner watchlist. Operational and Permission flags are by design long-lived.

## Provider chooser (5 + DIY)

| Provider | Best for | Pricing model | Lock-in risk | OSS option |
|---|---|---|---|---|
| **LaunchDarkly** | Enterprise, complex targeting, audit/compliance | Per-MAU, expensive | High | No |
| **GrowthBook** | Mid-market, A/B testing focused, OSS-friendly | Per-MAU + OSS | Low | Yes (self-host) |
| **Statsig** | Growth/product teams, advanced experimentation | Free tier + per-MAU | Medium | No |
| **Unleash** | OSS-first, self-hosted, dev-friendly | OSS + Enterprise | Low | Yes |
| **Flipt** | Lightweight, k8s-native, simple needs | OSS-only | None | Yes |
| **DIY** | <100 flags, no targeting, full control | None | None | N/A |

Decision rules:
- <50 flags + no targeting → DIY with config file or env vars
- Need analytics + experimentation → Statsig or GrowthBook
- Compliance/SOC2 audit logs required → LaunchDarkly
- Self-hosting required (data residency / air-gapped) → Unleash or Flipt

## Workflows

### Workflow 1: Ship a new feature behind a flag

```
1. Classify: which of the 4 flag types? (Release is most common for engineering work)
2. Design the rollout: ring (1%→5%→25%→50%→100%), linear, log, or cohort strategy
3. Add flag entry to docs/feature-flags.md BEFORE writing code:
   - name, owner, type, kill-switch trigger, dashboard URL
4. Write the code with the flag
5. Verify kill_switch_audit passes before merge
6. Deploy at 0%; verify kill switch works
7. Execute rollout schedule; abort if abort criteria met
8. At 100% for 7+ days: remove flag, delete dead branch, archive doc entry
```

### Workflow 2: Quarterly flag cleanup

```
1. Scan repo for flags older than 90 days with low usage
2. For each flagged item:
   a. Confirm it reached 100% (or was killed)
   b. Find the issue/PR that introduced it; verify owner agrees to remove
   c. Delete dead branches; remove flag config
3. Update CHANGELOG: "Removed N stale flags"
```

### Workflow 3: Design a kill switch

```
1. Identify the failure modes:
   - Latency spike (which threshold?)
   - Error rate spike (which threshold?)
   - Business metric regression (which threshold?)
2. Wire each to an abort:
   - Manual: dashboard link + on-call playbook
   - Automated: alert threshold flips flag back to 0%
3. Test the kill switch in staging BEFORE production rollout
4. Document in flag-doc
```

## Anti-patterns

- **Permanent flag with `if (FLAG_FOO)` in 50 places** — should be a Permission flag with runtime config, not a Release flag
- **Flag with no owner** — when the original engineer leaves, no one cleans it up
- **No kill switch documented** — when the feature breaks, no one knows how to disable it
- **A/B test that ran 6 months** — pick a winner; running indefinitely is debt
- **Flags as feature toggles for cosmetic changes** — ship via deploy, not flag

## Verifiable success

- 100% of new flags pass kill-switch audit at merge time
- Flag debt scan (90-day threshold) returns ≤5 stale flags repo-wide
- Every flag has a documented owner, type, and kill switch
- Mean time to retire a Release flag: <60 days from 100% rollout
