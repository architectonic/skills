---
name: skill-contract-schema
description: Five-tuple skill contract schema (Precondition, Operation, Artifact, Validator, Failure-modes) for treating skills as explicit, auditable units. Use when designing skill libraries that need maintenance, composition, or automated diagnosis.
type: Playbook
---

# Skill Contract Schema

Every skill in a maintainable library should be modeled as an explicit five-tuple contract. This schema enables automated maintenance actions (merge, repair, retire, add_validator, add_adapter) and inter-skill composition.

## The Five-Tuple

```yaml
skill_contract:
  name: string                    # Unique, human-readable name
  precondition:                   # When this skill applies
    input_type: string            # Expected input domain
    required_context: [string]    # What must be true before execution
    triggers: [string]            # Phrases or conditions that activate this skill
  operation:                      # What the skill does
    steps: [string]               # Ordered procedure
    allowed_tools: [string]       # Tools the skill may invoke
    side_effects: [string]        # External mutations (files, APIs, accounts)
  artifact:                       # What the skill produces
    output_type: string           # Expected output format
    output_path: string           # Where outputs are written (if any)
    deliverables: [string]        # Named outputs
  validator:                      # How to verify correctness
    postconditions: [string]      # Must be true after execution
    test_inputs: [object]         # Held-out test cases
    success_criteria: string      # Measurable pass condition
  failure_modes:                  # Known ways the skill can fail
    - mode: string                # Name of failure mode
      detection: string           # How to detect it
      mitigation: string          # How to recover
      severity: critical|high|medium|low
```

## External Graph Edges

Skills in a library are connected by typed edges:

| Edge Type | Meaning | Maintenance Action |
|-----------|---------|-------------------|
| `dependency` | Skill A requires Skill B to run | Retire B → cascade to A |
| `compatibility` | Skills A and B can compose without conflict | Flag incompatibility on change |
| `redundancy` | Skills A and B overlap in capability | Merge candidates |
| `alternative` | Skills A and B solve the same problem differently | Prefer higher-scoring one |
| `lineage` | Skill B evolved from Skill A | Track provenance, rollback path |

## Maintenance Actions

Five core library-level operations:

1. **merge**: Combine redundant skills into one, preserving the stronger validator
2. **repair**: Fix a degraded skill's operation or validator based on failure evidence
3. **retire**: Move a skill to deprecated/archived state, update dependents
4. **add_validator**: Strengthen a skill's postconditions when failure modes are discovered
5. **add_adapter**: Insert a compatibility shim when a skill's interface drifts from its consumers

## Library-Time vs Runtime

- **Runtime**: Agent selects and executes a skill (uses the 5-tuple)
- **Library-Time**: Maintenance engine runs between agent sessions (uses the graph edges)

Keep these separate. The maintenance engine should never mutate skills during agent execution.

## Validation Budget

Each skill should have a validation budget:
- Maximum N held-out test cases per promotion gate
- Test cases must be representative of real usage
- Tests must be hidden from the skill's training/optimization loop to prevent overfitting

## Source

Distilled from SkillOps (`arxiv:2605.13716`), which implements this as `SkillContract` and `SkillLibrary` Python classes with a `MaintenanceEngine` that sweeps the library between runs.
