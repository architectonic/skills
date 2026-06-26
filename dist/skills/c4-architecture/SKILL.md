---
name: c4-architecture
description: Generate comprehensive C4 architecture documentation for an existing repository/codebase using a bottom-up analysis approach. Creates Context, Container, Component, and Code level documentation with Mermaid diagrams.
type: Playbook
---

# C4 Architecture Documentation Workflow

Generate comprehensive C4 architecture documentation for an existing repository/codebase using a bottom-up analysis approach.

## When to Use

- Documenting an existing codebase's architecture
- Onboarding new team members who need system understanding
- Creating architecture documentation for stakeholders
- Reviewing system design before major changes
- Generating documentation that serves both technical and non-technical audiences

## When NOT to Use

- The task is unrelated to architecture documentation
- The codebase is trivial (single file, no structure)
- You need real-time architecture monitoring (this generates static docs)

## Overview

This workflow creates comprehensive C4 architecture documentation following the [official C4 model](https://c4model.com/diagrams) by:

1. **Code Level**: Analyzing every subdirectory bottom-up to create code-level documentation
2. **Component Level**: Synthesizing code documentation into logical components within containers
3. **Container Level**: Mapping components to deployment containers with API documentation
4. **Context Level**: Creating high-level system context with personas and user journeys

**Note**: According to the C4 model, you don't need all 4 levels — system context and container diagrams are sufficient for most teams. This workflow generates all levels for completeness.

All documentation is written to a new `C4-Documentation/` directory in the repository root.

## Phase 1: Code-Level Documentation (Bottom-Up Analysis)

### 1.1 Discover All Subdirectories

- Use codebase search to identify all subdirectories in the repository
- Sort directories by depth (deepest first) for bottom-up processing
- Filter out common non-code directories (node_modules, .git, build, dist, etc.)
- Create list of directories to process

### 1.2 Process Each Directory (Bottom-Up)

For each directory, starting from the deepest:

1. Analyze the code in the directory
2. Create documentation covering:
   - **Overview**: Name, description, location, language, purpose
   - **Code Elements**: All functions/methods with complete signatures (name, parameters with types, return type, description, file path and line numbers, dependencies), all classes/modules
   - **Dependencies**: Internal (other code in repo) and external (libraries, frameworks, services)
   - **Relationships**: Optional Mermaid diagram if relationships are complex

Save as: `C4-Documentation/c4-code-[directory-name].md`

## Phase 2: Component-Level Synthesis

### 2.1 Analyze All Code-Level Documentation

- Collect all `c4-code-*.md` files from Phase 1
- Analyze code structure, dependencies, and relationships
- Identify logical component boundaries based on:
  - Domain boundaries (related business functionality)
  - Technical boundaries (shared frameworks, libraries)
  - Organizational boundaries (team ownership, if evident)

### 2.2 Create Component Documentation

For each identified component, document:
- **Overview**: Name, description, type (Application, Service, Library), technology
- **Purpose**: What it does, problems it solves, role in the system
- **Software Features**: List of features with descriptions
- **Code Elements**: Links to contained `c4-code-*.md` files
- **Interfaces**: All interfaces with protocol (REST, GraphQL, gRPC, Events), description, operations
- **Dependencies**: Components used, external systems
- **Component Diagram**: Mermaid diagram showing relationships

Save as: `C4-Documentation/c4-component-[component-name].md`

### 2.3 Create Master Component Index

Generate a master `c4-component.md` listing all components with descriptions and a Mermaid relationship diagram.

## Phase 3: Container-Level Synthesis

### 3.1 Analyze Components and Deployment Definitions

- Review all `c4-component-*.md` files
- Search for deployment/infrastructure definitions: Dockerfiles, Kubernetes manifests, Docker Compose, Terraform/CloudFormation, cloud service definitions, CI/CD pipeline definitions

### 3.2 Map Components to Containers

For each container, document:
- **Containers**: Name, description, type (Web App, API, Database, Message Queue), technology, deployment target
- **Components**: List of deployed components with links
- **Interfaces**: All APIs with protocol, OpenAPI/Swagger specs saved to `C4-Documentation/apis/[container-name]-api.yaml`
- **Dependencies**: Other containers, external systems, communication protocols
- **Infrastructure**: Deployment config links, scaling strategy, resource requirements
- **Container Diagram**: Mermaid diagram showing all containers and relationships

Save as: `C4-Documentation/c4-container.md`

## Phase 4: Context-Level Documentation

### 4.1 Analyze System Documentation

- Review container and component documentation
- Search for: README files, architecture docs, requirements, design docs, test files, API docs, user docs

### 4.2 Create Context Documentation

Document:
- **System Overview**: Short and long descriptions
- **Personas**: Human users and programmatic "users" with type, description, goals, key features used
- **System Features**: High-level features with descriptions, linked personas, user journey maps
- **User Journeys**: Step-by-step journeys for each key feature and persona, including programmatic users
- **External Systems**: All external dependencies with type, description, integration type, purpose
- **System Context Diagram**: Mermaid C4Context diagram

Save as: `C4-Documentation/c4-context.md`

## Output Structure

```
C4-Documentation/
├── c4-code-*.md              # Code-level docs (one per directory)
├── c4-component-*.md          # Component-level docs (one per component)
├── c4-component.md            # Master component index
├── c4-container.md            # Container-level docs
├── c4-context.md              # Context-level docs
└── apis/                      # API specifications
    ├── [container]-api.yaml   # OpenAPI specs for each container
    └── ...
```

## Success Criteria

- Every subdirectory has a corresponding `c4-code-*.md` file
- All code-level documentation includes complete function signatures
- Components are logically grouped with clear boundaries
- All components have interface documentation
- Master component index created with relationship diagram
- Containers map to actual deployment units
- All container APIs documented with OpenAPI/Swagger specs
- System context includes all personas (human and programmatic)
- User journeys documented for all key features
- All external systems and dependencies identified
- Context diagram shows system, users, and external systems

## Best Practices

- **Bottom-up processing**: Process directories from deepest to shallowest
- **Incremental synthesis**: Each level builds on the previous level's documentation
- **Complete coverage**: Every directory must have code-level documentation before synthesis
- **Link consistency**: All documentation files link to each other appropriately
- **Stakeholder-friendly**: Context documentation should be understandable by non-technical stakeholders
- **Mermaid diagrams**: Use proper C4 Mermaid notation for all diagrams

## Related Skills

- `architecture-review-loop` — for reviewing existing architecture
- `software-architecture` — for general architecture patterns
- `documentation-and-adrs` — for ADR and documentation standards
