---
name: mcp-server-builder
description: Comprehensive guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services. Covers four-phase development workflow (research, implementation, review, evaluation), tool design patterns, framework selection (TypeScript/Python), auth, testing with MCP Inspector, and evaluation creation. Use when building MCP servers to integrate external APIs or services.
type: Playbook
---

# MCP Server Builder

Source: anthropics/skills (Apache-2.0). Adapted for Hermes Agent.

Build high-quality MCP servers that enable LLMs to interact with external services through well-designed tools. Quality is measured by how well the server enables LLMs to accomplish real-world tasks.

## High-Level Workflow (4 Phases)

### Phase 1: Deep Research and Planning

#### Understand Modern MCP Design

- **API Coverage vs. Workflow Tools**: Balance comprehensive API coverage with specialized workflow tools. When uncertain, prioritize comprehensive API coverage.
- **Tool Naming**: Clear, descriptive names with consistent prefixes (e.g., `github_create_issue`)
- **Context Management**: Concise tool descriptions, filter/paginate results, focused data
- **Actionable Error Messages**: Guide agents toward solutions with specific suggestions

#### Study MCP Protocol

- Start with sitemap: `https://modelcontextprotocol.io/sitemap.xml`
- Fetch specific pages with `.md` suffix
- Key topics: specification, transport (streamable HTTP, stdio), tool/resource/prompt definitions

#### Choose Stack

- **Language**: TypeScript (recommended) or Python
- **Transport**: Streamable HTTP for remote servers, stdio for local
- **TypeScript SDK**: `https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md`
- **Python SDK**: `https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md`

### Phase 2: Implementation

#### Core Infrastructure

Create shared utilities:
- API client with authentication
- Error handling helpers
- Response formatting (JSON/Markdown)
- Pagination support

#### Tool Implementation

For each tool:
- **Input Schema**: Zod (TS) or Pydantic (Python), with constraints and examples
- **Output Schema**: Define `outputSchema` for structured data
- **Description**: Concise summary, parameter descriptions, return type
- **Annotations**: `readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`
- **Implementation**: Async/await, proper error handling, pagination support

### Phase 3: Review and Test

- No duplicated code (DRY)
- Consistent error handling
- Full type coverage
- Clear tool descriptions
- **TypeScript**: `npm run build` then test with `npx @modelcontextprotocol/inspector`
- **Python**: `python -m py_compile` then test with MCP Inspector

### Phase 4: Create Evaluations

Create 10 evaluation questions to test whether LLMs can effectively use your MCP server:

1. **Tool Inspection**: List available tools and understand capabilities
2. **Content Exploration**: Use READ-ONLY operations to explore data
3. **Question Generation**: Create 10 complex, realistic questions
4. **Answer Verification**: Solve each question yourself first

Each question must be: independent, read-only, complex (multiple tool calls), realistic, verifiable (single clear answer), stable (answer won't change).

Output format:
```xml
<evaluation>
  <qa_pair>
    <question>Your question here</question>
    <answer>Verified answer</answer>
  </qa_pair>
</evaluation>
```
