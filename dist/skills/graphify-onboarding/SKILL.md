---
name: Graphify Onboarding
description: Operating discipline for using Graphify as a project-discovery accelerator. Use when onboarding into an unfamiliar repository, mapping dependencies, or generating project profiles from source artifacts.
tags: [agent-operations, agent-operations, onboarding, graphify, discovery, project-mapping]
type: Playbook
---

# Graphify Onboarding

Graphify is a project-discovery accelerator that generates a queryable graph from source files, documentation, and other project artifacts. Use it to help an agent understand a project faster. Do not treat its output as canonical truth.

## Use Case

Graphify supports project onboarding by producing derived artifacts:
- `graph.html` — interactive graph visualization
- `GRAPH_REPORT.md` — community structure, god nodes, cross-file relationships
- `graph.json` — raw graph data

These outputs help populate:
- `templates/project_profile.md`
- `templates/project_memory.md`

## Required First Step: Configure Ignore Rules

Before running Graphify on any repository or knowledge vault, create and review ignore rules.

### Minimum Ignore Rules

```
.env
.env.*
*.pem
*.key
*.p12
*.pfx
secrets/
credentials/
private/
node_modules/
.git/
.DS_Store
```

### For Private Operating-Memory Vaults

Also ignore canonical memory and ontology files unless the run is explicitly meant to analyze them:

```
AGENTS.md
START_HERE.md
memory_model.md
memory/
ontology/
knowledge/
identity/
goals/
decisions/
sources/private/
```

### For Public Template Repositories

Protect framework-defining files from accidental rewrite or generated drift:

```
AGENTS.md
START_HERE.md
repo_contract.md
memory_model.md
ontology/
roles/
skills/
runbooks/
templates/
```

## Operating Rules

1. Graphify may read project sources to create a derived discovery report.
2. Graphify output must **not** directly overwrite: ontology files, memory model files, role definitions, canonical decisions, source indexes, project profiles, or project memory files.
3. An agent may use Graphify output as **input** when drafting those files, but the final files must be reviewed against source artifacts.

## Source Hierarchy

Treat Graphify output as a derived source aid:

```
actual repository / docs
  > Graphify report
    > agent summary
      > inference
```

When Graphify and source files disagree, trust the source files.

## Safe Workflow

1. Configure ignore rules.
2. Run Graphify only on the intended project scope.
3. Review generated outputs before committing them.
4. Use `GRAPH_REPORT.md` to identify architecture, terminology, and questions.
5. Fill `project_profile.md` and `project_memory.md` manually or through an agent review step.
6. Label uncertain conclusions as assumptions or open questions.
7. Do not commit generated graph outputs if they contain private, sensitive, or irrelevant material.

## ABKB-Style Onboarding Pattern

For a private project-memory vault:

```
source repo
  → Graphify discovery report
    → project profile draft
      → project memory draft
        → source review
          → canonical project memory
```

The discovery report accelerates onboarding. It does not replace source review.

## Good Fit

Use Graphify when:
- Entering an unfamiliar repo
- Onboarding a project agent
- Mapping dependencies and terminology
- Finding candidate architecture questions
- Creating a first project profile draft

## Poor Fit

Do not use Graphify as:
- Canonical memory
- A replacement for source review
- An automatic ontology writer
- An automatic decision recorder
- A justification for committing generated artifacts blindly

## Caveats

- Generated graphs can encode stale, inferred, or incomplete relationships.
- Large generated files can pollute small memory repos.
- Assistant config changes should be reviewed before commit.
- Query logs and generated reports may expose sensitive details.
- Private projects require stricter ignore rules than public projects.

## Trigger
Use when:
- Entering an unfamiliar repository for the first time
- Creating a project profile or project memory from scratch
- Mapping cross-file relationships and dependencies
- The user asks for a project overview or architecture summary

## Procedure
1. Configure ignore rules appropriate to the project type (public/private/template).
2. Run Graphify on the project scope.
3. Read `GRAPH_REPORT.md` for community structure and god nodes.
4. Identify key terminology, architecture patterns, and open questions.
5. Draft `project_profile.md` and `project_memory.md` using Graphify output as input.
6. Review all drafts against actual source artifacts.
7. Label uncertain conclusions as assumptions.
8. Commit only reviewed, source-grounded outputs.

## Verification
- Ignore rules are configured before running Graphify.
- Generated outputs are reviewed before committing.
- Project profile and memory files are grounded in source artifacts, not just Graphify output.
- No private or sensitive material is committed in generated files.

## Failure Modes
- Running Graphify without ignore rules → secrets or private files in graph output.
- Treating Graphify output as canonical → stale or inferred relationships become "truth".
- Committing generated files blindly → pollution of memory repo with unvetted content.
- Using Graphify to overwrite canonical files → loss of human-reviewed knowledge.
