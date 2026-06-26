---
name: Code Documentation Generator
description: Generate professional, comprehensive documentation for software projects, codebases, libraries, and APIs. Covers README generation, API reference documentation, architecture docs, inline code comments for multiple languages (Python, TypeScript, Go, Rust, Java), developer guides, and changelogs. Follows industry best practices from React, Django, Stripe, and Kubernetes.
source: deer-flow/skills/public/code-documentation/SKILL.md (MIT license, https://github.com/deer-flow/deer-flow)
category: software-development
tags: [software-development, documentation, readme, api-reference, architecture, code-comments, multi-language, developer-guide]
type: Playbook
---

# Code Documentation Generator

## Overview

Generate professional, comprehensive documentation for software projects, codebases, libraries, and APIs. Follows industry best practices from projects like React, Django, Stripe, and Kubernetes to produce documentation that is accurate, well-structured, and useful for both new contributors and experienced developers.

The output ranges from single-file READMEs to multi-document developer guides, always matched to the project's complexity and the user's needs.

## When to Use This Skill

- User asks to "document", "create docs", or "write documentation" for any code
- User requests a README, API reference, or developer guide
- User shares a codebase or repository and wants documentation generated
- User asks to improve or update existing documentation
- User needs architecture documentation, including diagrams
- User requests a changelog or migration guide

## Documentation Workflow

### Phase 1: Codebase Analysis

Before writing any documentation, thoroughly understand the codebase.

#### Step 1.1: Project Discovery

Identify the project fundamentals:

| Field | How to Determine |
|-------|-----------------|
| **Language(s)** | Check file extensions, `package.json`, `pyproject.toml`, `go.mod`, `Cargo.toml` |
| **Framework** | Look at dependencies for known frameworks (React, Django, Express, Spring) |
| **Build System** | Check for `Makefile`, `CMakeLists.txt`, `webpack.config.js`, `build.gradle` |
| **Package Manager** | npm/yarn/pnpm, pip/uv/poetry, cargo, go modules |
| **Project Structure** | Map out the directory tree to understand the architecture |
| **Entry Points** | Find main files, CLI entry points, exported modules |
| **Existing Docs** | Check for existing README, docs/, wiki, or inline documentation |

#### Step 1.2: Identify Documentation Scope

Based on analysis, determine what documentation to produce:

| Project Size | Recommended Documentation |
|-------------|--------------------------|
| **Single file / script** | Inline comments + usage header |
| **Small library** | README with API reference |
| **Medium project** | README + API docs + examples |
| **Large project** | README + Architecture + API + Contributing + Changelog |

### Phase 2: Documentation Generation

#### README Generation

Every project needs a README. Follow this structure:

```markdown
# Project Name

[One-line project description — what it does and why it matters]

## Features
- [Key feature 1]
- [Key feature 2]

## Quick Start

### Prerequisites
- [Prerequisite 1 with version requirement]

### Installation
[Installation commands with copy-paste-ready code blocks]

### Basic Usage
[Minimal working example that demonstrates core functionality]

## API Reference
[Inline API reference for smaller projects OR link to generated docs]

## Configuration
[Environment variables, config files, or runtime options]

## Examples
[2-3 practical examples covering common use cases]

## Development
### Setup / Testing / Building

## Contributing
[Contribution guidelines or link to CONTRIBUTING.md]

## License
[License information]
```

#### API Reference Generation

For each public API surface, document:

**Function / Method Documentation**:

```markdown
### `functionName(param1, param2, options?)`

Brief description of what this function does.

**Parameters:**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `param1` | `string` | Yes | — | Description of param1 |
| `options` | `Object` | No | `{}` | Configuration options |

**Returns:** `Promise<Result>` — Description of return value

**Throws:**
- `ValidationError` — When param1 is empty

**Example:**

​```javascript
const result = await functionName("hello", 42, { timeout: 10000 });
console.log(result.data);
​```
```

#### Architecture Documentation

For medium-to-large projects, include architecture documentation with Mermaid diagrams:

````markdown
# Architecture Overview

## System Diagram

​```mermaid
graph TD
    A[Client] --> B[API Gateway]
    B --> C[Service A]
    B --> D[Service B]
    C --> E[(Database)]
    D --> E
​```

## Component Overview

### Component Name
- **Purpose**: What this component does
- **Location**: `src/components/name/`
- **Dependencies**: What it depends on
- **Public API**: Key exports or interfaces

## Data Flow
[Describe how data flows through the system for key operations]

## Design Decisions

### Decision Title
- **Context**: What situation led to this decision
- **Decision**: What was decided
- **Rationale**: Why this approach was chosen
- **Trade-offs**: What was sacrificed
````

#### Inline Code Documentation

Generate language-appropriate inline documentation:

**Python (Google-style docstrings)**:
```python
def process_data(input_path: str, options: dict | None = None) -> ProcessResult:
    """Process data from the given file path.

    Reads the input file, applies transformations based on the provided
    options, and returns a structured result object.

    Args:
        input_path: Absolute path to the input data file.
            Supports CSV, JSON, and Parquet formats.
        options: Optional configuration dictionary.
            - "validate" (bool): Enable input validation. Defaults to True.
            - "format" (str): Output format ("json" or "csv"). Defaults to "json".

    Returns:
        A ProcessResult containing the transformed data and metadata.

    Raises:
        FileNotFoundError: If input_path does not exist.
        ValidationError: If validation is enabled and data is malformed.

    Example:
        >>> result = process_data("/data/input.csv", {"validate": True})
        >>> print(result.row_count)
        1500
    """
```

**TypeScript (JSDoc / TSDoc)**:
```typescript
/**
 * Fetches user data from the API and transforms it for display.
 *
 * @param userId - The unique identifier of the user
 * @param options - Configuration options for the fetch operation
 * @returns The transformed user data ready for rendering
 * @throws {NotFoundError} When the user ID does not exist
 *
 * @example
 * const user = await fetchUser("usr_123", { includeProfile: true });
 * console.log(user.displayName);
 */
```

**Go (GoDoc)**:
```go
// ProcessData reads the input file at the given path, applies the specified
// transformations, and returns the processed result.
//
// The input path must be an absolute path to a CSV or JSON file.
// If options is nil, default options are used.
//
// ProcessData returns an error if the file does not exist or cannot be parsed.
func ProcessData(inputPath string, options *ProcessOptions) (*Result, error) {
```

### Phase 3: Quality Assurance

#### Documentation Completeness Check

Verify the documentation covers:
- [ ] **What it is** — Clear project description that a newcomer can understand
- [ ] **Why it exists** — Problem it solves and value proposition
- [ ] **How to install** — Copy-paste-ready installation commands
- [ ] **How to use** — At least one minimal working example
- [ ] **API surface** — All public functions, classes, and types documented
- [ ] **Configuration** — All environment variables, config files, and options
- [ ] **Error handling** — Common errors and how to resolve them
- [ ] **Contributing** — How to set up dev environment and submit changes

#### Quality Standards

| Standard | Check |
|----------|-------|
| **Accuracy** | Every code example must actually work with the described API |
| **Completeness** | No public API surface left undocumented |
| **Consistency** | Same formatting and structure throughout |
| **Freshness** | Documentation matches the current code, not an older version |
| **Accessibility** | No jargon without explanation, acronyms defined on first use |
| **Examples** | Every complex concept has at least one practical example |

#### Language-Specific Conventions

| Language | Doc Format | Style Guide |
|----------|-----------|-------------|
| Python | Google-style docstrings | PEP 257 |
| TypeScript/JavaScript | TSDoc / JSDoc | TypeDoc conventions |
| Go | GoDoc comments | Effective Go |
| Rust | Rustdoc (`///`) | Rust API Guidelines |
| Java | Javadoc | Oracle Javadoc Guide |
| C/C++ | Doxygen | Doxygen manual |

## Writing Principles

1. **Lead with the "why"** — Before explaining how something works, explain why it exists
2. **Progressive disclosure** — Start simple, add complexity gradually
3. **Show, don't tell** — Prefer code examples over lengthy explanations
4. **Active voice** — "The function returns X" not "X is returned by the function"
5. **Present tense** — "The server starts on port 8080"
6. **Second person** — "You can configure..." not "Users can configure..."

## Notes

- Always analyze the actual code before writing documentation — never guess at API signatures or behavior
- When existing documentation exists, preserve its structure unless the user explicitly asks for a rewrite
- For large codebases, prioritize documenting the public API surface and key abstractions first
- Documentation should be written in the same language as the project's existing docs; default to English if none exist
- When generating changelogs, use the Keep a Changelog format
