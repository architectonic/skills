---
name: chaos-engineering
description: Use when planning, running, or learning from chaos engineering experiments. Triggers on "chaos experiment", "fault injection", "gameday", "resilience test", "blast radius", "steady state", "abort criteria", or any deliberate failure-injection question. Enforces hypothesis-driven experiment design with mandatory abort criteria and blast-radius bounds.
tags: [devops, chaos-engineering, resilience, fault-injection, gameday, sre, reliability]
type: Playbook
---

# Chaos Engineering

Design experiments that surface real weaknesses in production systems — without becoming outages. Most "chaos engineering" attempts skip steady-state measurement, define no abort criteria, and have no blast-radius bound. This skill enforces the discipline that makes chaos experiments safe and useful.

## When to use

- Planning a chaos experiment (what to break, where, when, how to abort)
- Calculating blast radius before running the experiment
- Reviewing an existing experiment plan for safety
- Choosing a chaos tool (Chaos Toolkit / Chaos Mesh / Litmus / Gremlin / AWS FIS)
- Writing a chaos experiment postmortem
- Running a Game Day exercise

## When NOT to use

- General incident response
- Threat hunting / red-team
- Performance load testing (chaos is about failure modes, not capacity)
- Production debugging (chaos discovers weaknesses preemptively)

## Core principle: chaos without abort criteria is an outage

The 4 Principles of Chaos Engineering (Netflix, 2016):

1. **Build a hypothesis around steady-state behavior.** Not "what breaks?" but "X holds; will it still hold under fault Y?"
2. **Vary real-world events.** Inject realistic failures: kill nodes, slow networks, lose cache, throttle dependencies.
3. **Run experiments in production.** Staging never has the same failure modes. Start small.
4. **Automate experiments to run continuously.** One-off chaos is a press release; continuous chaos is engineering.

Add a fifth: **Define abort criteria up front.** A chaos experiment with no abort criteria is an outage by another name.

## The 7 attack types

| Attack | What it tests | Tooling |
|---|---|---|
| **Latency** | Timeouts, retries, circuit breakers | tc, Chaos Mesh `NetworkChaos` |
| **Error** | Error handling, fallback paths | Chaos Mesh `HTTPChaos`, Toxiproxy |
| **Resource** (CPU, memory, disk) | Saturation handling, autoscaling | Chaos Mesh `StressChaos`, stress-ng |
| **Network partition** | Split-brain, consensus, failover | Chaos Mesh `NetworkChaos` partition |
| **Dependency failure** | Graceful degradation, fallback | Service mesh fault injection |
| **Time** | Clock skew, NTP issues | libfaketime, Chaos Mesh `TimeChaos` |
| **Infrastructure** (kill instance) | Auto-recovery, failover | AWS FIS, Chaos Monkey |

Pick the attack that matches the hypothesis. "What happens if X is slow?" → latency. "What happens if X loses network?" → partition.

## Tooling chooser

| Tool | Best for | Pricing | Stack |
|---|---|---|---|
| **Chaos Toolkit** | Lightweight, language-agnostic, JSON experiments | OSS | Any |
| **Chaos Mesh** | Kubernetes-native, rich CRDs, in-cluster | OSS | Kubernetes |
| **Litmus** | Kubernetes, Argo-integrated, large library | OSS + Enterprise | Kubernetes |
| **Gremlin** | Enterprise SaaS, multi-cloud, audit | Paid | Any |
| **AWS FIS** | AWS-native, IAM-integrated, EC2/ECS/EKS | Paid (AWS) | AWS |

Decision rules:
- k8s-only + OSS → Chaos Mesh or Litmus (Litmus has bigger experiment library)
- Multi-cloud + OSS → Chaos Toolkit
- AWS-heavy + simple needs → AWS FIS
- Enterprise + audit/compliance → Gremlin

## Workflows

### Workflow 1: Design and run a single experiment

```
1. State a hypothesis: "When [fault], steady-state metric X stays within Y."
2. Identify the steady-state metric — must be measurable BEFORE the experiment.
3. Calculate blast radius — confirm GREEN (<1% error budget) before proceeding.
4. Produce the plan with: hypothesis, steady-state, attack, magnitude, duration, blast radius, abort criteria, rollback.
5. Get a peer review of the plan; confirm abort criteria are concrete.
6. Notify the on-call team.
7. Run the experiment with monitoring open.
8. If abort criteria are hit, abort immediately; record what happened.
9. Produce postmortem: summary, hypothesis confirmed/refuted, learnings, follow-up actions.
10. File follow-up actions; link to next experiment.
```

### Workflow 2: Game Day exercise

```
1. Pick a scenario (e.g., "primary database fails over").
2. Identify all dependent services that should keep working.
3. Build a multi-experiment plan covering each layer.
4. Schedule with stakeholders; on-call coverage required.
5. Run with a facilitator who manages the scenario.
6. Capture observations in a shared doc as they happen.
7. Single combined postmortem covering all observations.
8. Track follow-up actions in a board with owners.
```

### Workflow 3: Continuous chaos (game days → daily)

```
1. Start: weekly Game Day in staging.
2. Move to: weekly Game Day in production with limited blast radius.
3. Mature to: continuous chaos via scheduled experiments.
4. Wire to deployment: every prod deploy triggers a baseline chaos sweep.
5. Track: experiments per week, weaknesses discovered, MTTR trend.
```

## Anti-patterns

- **No hypothesis** — "let's break things" is sabotage, not engineering
- **No steady-state metric** — without a baseline, you can't tell if X broke
- **No blast radius bound** — full-prod experiment without limits = outage
- **No abort criteria** — mandatory, not optional
- **No on-call coverage** — chaos without monitoring is unmonitored production
- **Chaos in staging only** — staging never has prod failure modes
- **One-off chaos** — single experiment is a press release; learning requires recurrence
- **Blame-laden postmortem** — record causes, not blame; teams stop running chaos otherwise

## Verifiable success

- 100% of chaos experiments have a written hypothesis, abort criteria, and blast-radius calculation
- Blast radius for any single experiment never exceeds 10% of error budget
- Mean time between chaos experiments <14 days (continuous, not one-off)
- Each experiment produces ≥1 follow-up action that gets shipped
- No chaos experiment escalates to a customer-impacting incident in trailing 90 days
