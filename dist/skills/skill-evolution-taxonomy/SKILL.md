---
name: Skill Evolution Taxonomy
description: Comprehensive taxonomy of agent skill creation, usage, evolution, and evaluation paradigms. Use when classifying skill research, mapping the skill ecosystem, or deciding which evolution strategy applies to a skill lifecycle stage.
tags: [skill-management, taxonomy, skill-evolution, skill-creation, skill-evaluation, research, benchmarks]
runtime_targets: [many]
type: Playbook
---

# Skill Evolution Taxonomy

## Purpose

A comprehensive taxonomy of agent skill lifecycle paradigms — spanning creation, usage, evolution, and evaluation. Use this skill to classify skill research, map the skill ecosystem, or decide which evolution strategy applies.

## The 4 Evolution Paradigms

### 1. Execution Feedback

Skills improve based on feedback from actual execution runs.

| Pattern | What it does | Key papers/repos |
|---------|-------------|-----------------|
| SkillForge | Execution feedback loop | arXiv:2604.08618 |
| CoEvoSkills | Co-evolution via execution feedback | arXiv:2604.01687 |
| EmbodiSkill | Embodied execution feedback | arXiv:2605.10332 |
| Skills-Coach | Coaching via execution feedback | arXiv:2604.27488 |
| Ctx2Skill | Context-to-skill via execution | arXiv:2604.27660 |
| AutoSkill | Automated skill generation from execution | arXiv:2603.01145 |
| SkillClaw | Skill improvement via claw-based feedback | arXiv:2604.08377 |

### 2. Trajectory Distillation

Skills are distilled from successful execution trajectories.

| Pattern | What it does | Key papers/repos |
|---------|-------------|-----------------|
| SPARK | Trajectory distillation | arXiv:2605.09192 |
| Trace2Skill | Trace-to-skill distillation | arXiv:2603.25158 |
| Memento-Skills | Memory-based trajectory distillation | arXiv:2603.18743 |
| XSkill | Cross-trajectory skill extraction | arXiv:2603.12056 |

### 3. Compression & Augmentation

Skills are compressed for efficiency or augmented for broader coverage.

| Pattern | What it does | Key papers/repos |
|---------|-------------|-----------------|
| SkillNet | Skill compression network | arXiv:2603.04448 |
| SkillX | Skill augmentation | arXiv:2604.04804 |
| SkillFoundry | Skill compression + forging | arXiv:2604.03964 |
| SkillReducer | Skill compression | arXiv:2603.29919 |

### 4. Reinforcement Learning

Skills improve via RL-based optimization.

| Pattern | What it does | Key papers/repos |
|---------|-------------|-----------------|
| D2Skill | RL-based skill discovery | arXiv:2603.28716 |
| SkillRL | RL for skill optimization | arXiv:2602.08234 |
| Skill1 | RL-based skill learning | arXiv:2605.06130 |

## Skill Usage Patterns

### Retrieval & Routing

| Pattern | What it does | Key papers/repos |
|---------|-------------|-----------------|
| SkillRouter | Skill retrieval and routing | arXiv:2603.22455 |
| SkillFlow | Skill retrieval flow | arXiv:2504.06188 |
| SkillOrchestra | Skill routing orchestration | arXiv:2602.19672 |
| AgentSkillOS | Skill management + orchestration | arXiv:2603.02176 |

### Management

| Pattern | What it does | Key papers/repos |
|---------|-------------|-----------------|
| SSL | Skill management layer | arXiv:2604.24026 |
| AgentSkillOS | Full skill OS | arXiv:2603.02176 |

## Skill Creation Patterns

| Pattern | What it does | Key papers/repos |
|---------|-------------|-----------------|
| Anthropic Skill Creator | Automatic skill creation | anthropics/skills |
| Voyager | Exploration-based creation | arXiv:2305.16291 |
| SAGE | RL-based creation | arXiv:2512.17102 |
| ARISE | RL-based creation | arXiv:2603.16060 |

## Benchmark Categories

### Skill-Centric Benchmarks

| Benchmark | Focus | Coverage |
|-----------|-------|----------|
| AgentSearchBench | Skill search/retrieval | Bingo-W/AgentSearchBench |
| SWE-Skills-Bench | Skill application | swe-skills-bench |
| SkillResolve-Bench | Skill resolution | agent-skill-safety-benchmarks-2026 |
| HarmfulSkillBench | Safety | agent-skill-safety-benchmarks-2026 |
| MalSkillBench | Malicious skill detection | agent-skill-safety-benchmarks-2026 |

### General-Domain Benchmarks

| Benchmark | Focus |
|-----------|-------|
| SWE-bench | Software engineering |
| WebArena | Web navigation |
| AgentBench | General agent capabilities |
| ToolBench | Tool usage |

## Structural Gaps in Current Benchmarks

1. **No cross-runtime portability metrics** — skills are evaluated within single runtime contexts
2. **Limited skill evolution tracking** — benchmarks measure point-in-time performance, not improvement over evolution cycles
3. **Sparse safety coverage** — only a few benchmarks test for harmful or malicious skill behavior
4. **No skill composition metrics** — how well skills compose is largely unmeasured
5. **Missing skill lifecycle benchmarks** — creation → usage → evolution → retirement is not benchmarked end-to-end

## Decision Tree: Which Evolution Paradigm?

```
Is there execution feedback available?
├── Yes
│   ├── Is the feedback from successful trajectories?
│   │   ├── Yes → Trajectory Distillation
│   │   └── No → Execution Feedback
│   └── Is the skill too large/complex?
│       ├── Yes → Compression & Augmentation
│       └── No → Execution Feedback
└── No
    ├── Is there a reward signal available?
    │   ├── Yes → Reinforcement Learning
    │   └── No → Consider Skill Creation (automatic or manual)
    └── Is retrieval the bottleneck?
        ├── Yes → Retrieval & Routing optimization
        └── No → Management optimization
```

## Verification

When applying this taxonomy:
- [ ] The skill/research is classified into at least one paradigm
- [ ] The classification is grounded in cited source material
- [ ] Structural gaps relevant to the use case are noted
- [ ] Cross-references to related AOMK skills are included

## Source Verification

This taxonomy is grounded in the 2026 survey "Agent Skill Evaluation and Evolution: Frameworks and Benchmarks" (arXiv:2606.11435) and the accompanying repository at https://github.com/Cassie07/AgentSkill_Survey. All paper links and repo references should be verified against the live sources before citation.
