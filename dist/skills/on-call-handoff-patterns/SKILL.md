---
name: on-call-handoff-patterns
description: Effective patterns for on-call shift transitions, ensuring continuity, context transfer, and reliable incident response across shifts. Use when transitioning on-call responsibilities, writing shift handoff summaries, documenting ongoing investigations, or establishing on-call rotation procedures.
tags: [on-call, handoff, shift-transition, incident-response, devops, reliability, sre]
type: Playbook
---

# On-Call Handoff Patterns

Effective patterns for on-call shift transitions, ensuring continuity, context transfer, and reliable incident response across shifts.

**Source:** Distilled from `antigravity-awesome-skills/skills/on-call-handoff-patterns/SKILL.md` (MIT).

## When to Use This Skill

- Transitioning on-call responsibilities
- Writing shift handoff summaries
- Documenting ongoing investigations
- Establishing on-call rotation procedures
- Improving handoff quality
- Onboarding new on-call engineers

## When NOT to Use This Skill

- The task is unrelated to on-call handoff patterns
- You need a different domain or tool outside this scope

## Core Concepts

### 1. Handoff Components

| Component | Purpose |
|-----------|---------|
| **Active Incidents** | What's currently broken |
| **Ongoing Investigations** | Issues being debugged |
| **Recent Changes** | Deployments, configs |
| **Known Issues** | Workarounds in place |
| **Upcoming Events** | Maintenance, releases |

### 2. Handoff Timing

```
Recommended: 30 min overlap between shifts

Outgoing:
├── 15 min: Write handoff document
└── 15 min: Sync call with incoming

Incoming:
├── 15 min: Review handoff document
├── 15 min: Sync call with outgoing
└── 5 min: Verify alerting setup
```

## Templates

### Template 1: Shift Handoff Document

```markdown
# On-Call Handoff: [Team Name]

**Outgoing**: @alice (YYYY-MM-DD to YYYY-MM-DD)
**Incoming**: @bob (YYYY-MM-DD to YYYY-MM-DD)
**Handoff Time**: YYYY-MM-DD HH:MM UTC

---

## 🔴 Active Incidents

### None currently active
No active incidents at handoff time.

---

## 🟡 Ongoing Investigations

### 1. [Issue Title] (TICKET-1234)
**Status**: Investigating
**Started**: YYYY-MM-DD
**Impact**: [Description]

**Context**:
- [Key context]
- [Theories]
- [Recent findings]

**Next Steps**:
- [ ] [Action item]

**Resources**:
- Dashboard: [Link]
- Thread: #channel (date, time)

---

## 🟢 Resolved This Shift

### [Incident Title] (YYYY-MM-DD)
- **Duration**: [Duration]
- **Root Cause**: [Cause]
- **Resolution**: [What was done]
- **Postmortem**: [Link]
- **Follow-up tickets**: TICKET-XXX

---

## 📋 Recent Changes

### Deployments
| Service | Version | Time | Notes |
|---------|---------|------|-------|
| [service] | vX.Y.Z | Date HH:MM | [Notes] |

### Configuration Changes
- [Change description]

### Infrastructure
- [Change description]

---

## ⚠️ Known Issues & Workarounds

### 1. [Issue Title]
**Issue**: [Description]
**Workaround**: [What to do]
**Ticket**: TICKET-XXX (Priority)

---

## 📅 Upcoming Events

| Date | Event | Impact | Contact |
|------|-------|--------|---------|
| YYYY-MM-DD HH:MM | [Event] | [Impact] | @contact |

---

## 📞 Escalation Reminders

| Issue Type | First Escalation | Second Escalation |
|------------|------------------|-------------------|
| [Type] | @contact | @contact |

---

## 🔧 Quick Reference

### Common Commands
```bash
# Check service health
kubectl get pods -A | grep -v Running

# Recent deployments
kubectl get events --sort-by='.lastTimestamp' | tail -20
```

### Important Links
- [Runbooks](link)
- [Service Catalog](link)
- [Incident Slack](link)
- [PagerDuty](link)

---

## Handoff Checklist

### Outgoing Engineer
- [ ] Document active incidents
- [ ] Document ongoing investigations
- [ ] List recent changes
- [ ] Note known issues
- [ ] Add upcoming events
- [ ] Sync with incoming engineer

### Incoming Engineer
- [ ] Read this document
- [ ] Join sync call
- [ ] Verify PagerDuty is routing to you
- [ ] Verify Slack notifications working
- [ ] Check VPN/access working
- [ ] Review critical dashboards
```

### Template 2: Quick Handoff (Async)

```markdown
# Quick Handoff: @alice → @bob

## TL;DR
- No active incidents
- 1 investigation ongoing ([issue], see TICKET-1234)
- Major release tomorrow (YYYY-MM-DD) - be ready for issues

## Watch List
1. [Item to watch]

## Recent
- [Recent change]

## Coming Up
- YYYY-MM-DD HH:MM - [Event]

## Questions?
I'll be available on Slack until HH:MM today.
```

### Template 3: Incident Handoff (Mid-Incident)

```markdown
# INCIDENT HANDOFF: [Title]

**Incident Start**: YYYY-MM-DD HH:MM UTC
**Current Status**: Mitigating
**Severity**: SEV2

---

## Current State
- Error rate: X% (down from Y%)
- Mitigation in progress: [Description]
- ETA to resolution: ~30 min

## What We Know
1. Root cause: [Cause]
2. Triggered by: [Trigger]
3. Contributing: [Factor]

## What We've Done
- [Action taken]

## What Needs to Happen
1. [Next step]

## Key People
- Incident Commander: @alice (handing off)
- Technical Lead: @bob (incoming)

## Resources
- Incident channel: #inc-XXXX
- Dashboard: [Link]
- Runbook: [Link]

---

**Incoming on-call (@bob) - Please confirm you have:**
- [ ] Joined incident channel
- [ ] Access to dashboards
- [ ] Understand current state
- [ ] Know escalation path
```

## Handoff Sync Meeting Agenda (15 minutes)

1. **Active Issues (5 min)** — Walk through ongoing incidents. Transfer context and theories.
2. **Recent Changes (3 min)** — Deployments to watch. Config changes. Known regressions.
3. **Upcoming Events (3 min)** — Maintenance windows. Expected traffic changes. Releases.
4. **Questions (4 min)** — Clarify anything unclear. Confirm access and alerting.

## On-Call Best Practices

### Pre-Shift Checklist

**Access Verification**
- [ ] VPN working
- [ ] kubectl access to all clusters
- [ ] Database read access
- [ ] Log aggregator access
- [ ] PagerDuty app installed and logged in

**Alerting Setup**
- [ ] PagerDuty schedule shows you as primary
- [ ] Phone notifications enabled
- [ ] Slack notifications for incident channels
- [ ] Test alert received and acknowledged

**Knowledge Refresh**
- [ ] Review recent incidents (past 2 weeks)
- [ ] Check service changelog
- [ ] Skim critical runbooks
- [ ] Know escalation contacts

### During Your Shift

**Morning**
- [ ] Check overnight alerts
- [ ] Review dashboards for anomalies
- [ ] Check for any P0/P1 tickets created

**Throughout Day**
- [ ] Respond to alerts within SLA
- [ ] Document investigation progress
- [ ] Update team on significant issues

**End of Day**
- [ ] Hand off any active issues
- [ ] Update investigation docs

### After Your Shift

- [ ] Complete handoff document
- [ ] Sync with incoming on-call
- [ ] Verify PagerDuty routing changed
- [ ] Close/update investigation tickets
- [ ] File postmortems for any incidents

## Escalation Guidelines

### Immediate Escalation
- SEV1 incident declared
- Data breach suspected
- Unable to diagnose within 30 min
- Customer or legal escalation received

### Consider Escalation
- Issue spans multiple teams
- Requires expertise you don't have
- Business impact exceeds threshold
- You're uncertain about next steps

### How to Escalate
1. Page the appropriate escalation path
2. Provide brief context in Slack
3. Stay engaged until escalation acknowledges
4. Hand off cleanly, don't just disappear

## Best Practices

### Do's
- **Document everything** — Future you will thank you
- **Escalate early** — Better safe than sorry
- **Take breaks** — Alert fatigue is real
- **Keep handoffs synchronous** — Async loses context
- **Test your setup** — Before incidents, not during

### Don'ts
- **Don't skip handoffs** — Context loss causes incidents
- **Don't hero** — Escalate when needed
- **Don't ignore alerts** — Even if they seem minor
- **Don't work sick** — Swap shifts instead
- **Don't disappear** — Stay reachable during shift

## Resources

- [Google SRE - Being On-Call](https://sre.google/sre-book/being-on-call/)
- [PagerDuty On-Call Guide](https://www.pagerduty.com/resources/learn/on-call-management/)
- [Increment On-Call Issue](https://increment.com/on-call/)

## Limitations

- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
