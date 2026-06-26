---
name: open-notebook
description: Use when deploying or using Open Notebook — a self-hosted, open-source alternative to Google NotebookLM. Covers Docker deployment, notebook/source/note management via REST API, context-aware chat with documents, full-text and vector search, multi-speaker podcast generation, and content transformations. Triggers on requests to organize research materials, chat with documents, generate podcasts from research, or self-host a NotebookLM-like tool.
tags: [research, notebook, self-hosted, rag, podcast, document-analysis]
type: API Endpoint
---

# Open Notebook

## Overview

Open Notebook is an open-source, self-hosted alternative to Google NotebookLM. It enables researchers to organize materials, generate AI-powered insights, create podcasts, and have context-aware conversations with documents — all while maintaining complete data privacy.

**Repository:** https://github.com/lfnovo/open-notebook

**Key advantages over NotebookLM:**
- Full REST API for programmatic access and automation
- Choice of 16+ AI providers (not locked to Google models)
- Multi-speaker podcast generation with 1-4 customizable speakers
- Complete data sovereignty through self-hosting
- Open source and fully extensible (MIT license)

## When to use

- Organizing research materials into notebooks with sources, notes, and chat sessions
- Ingesting diverse content: PDFs, videos, audio, web pages, Office documents
- Generating AI-powered notes and summaries from research materials
- Creating multi-speaker podcasts from research
- Chatting with documents using context-aware AI that cites sources
- Searching across materials with full-text and vector search
- Running custom content transformations (summarization, extraction, analysis)

## Quick Start

### Prerequisites

- Docker Desktop installed
- API key for at least one AI provider (or local Ollama for free local inference)

### Deployment

```bash
# Download docker-compose file
curl -o docker-compose.yml https://raw.githubusercontent.com/lfnovo/open-notebook/main/docker-compose.yml

# Set required encryption key
export OPEN_NOTEBOOK_ENCRYPTION_KEY="your-secret-key-here"

# Launch services
docker-compose up -d
```

Access points:
- **Frontend UI:** http://localhost:8502
- **REST API:** http://localhost:5055
- **API Docs:** http://localhost:5055/docs

### Configure AI Provider

After startup, configure at least one AI provider via the UI (Settings > API Keys) or via the REST API.

## Core Workflows

### 1. Create a Notebook

Organize research into separate notebooks, each containing sources, notes, and chat sessions.

```python
import requests
BASE_URL = "http://localhost:5055/api"

response = requests.post(f"{BASE_URL}/notebooks", json={
    "name": "Research Project",
    "description": "Literature review on topic X"
})
notebook = response.json()
notebook_id = notebook["id"]
```

### 2. Ingest Sources

Add diverse content types: PDFs, videos, audio, web pages, Office documents.

```python
# Add a web URL source
response = requests.post(f"{BASE_URL}/sources", data={
    "url": "https://arxiv.abs/2301.00001",
    "notebook_id": notebook_id,
    "process_async": "true"
})

# Upload a PDF file
with open("paper.pdf", "rb") as f:
    response = requests.post(f"{BASE_URL}/sources",
        data={"notebook_id": notebook_id},
        files={"file": ("paper.pdf", f, "application/pdf")})
```

### 3. Context-Aware Chat

Chat with research materials using AI that cites sources.

```python
session = requests.post(f"{BASE_URL}/chat/sessions", json={
    "notebook_id": notebook_id,
    "title": "Research Discussion"
}).json()

response = requests.post(f"{BASE_URL}/chat/execute", json={
    "session_id": session["id"],
    "message": "What are the key findings across my sources?",
    "context": {"include_sources": True, "include_notes": True}
})
```

### 4. Search

Full-text and vector (semantic) search across all materials.

```python
# Vector search
results = requests.post(f"{BASE_URL}/search", json={
    "query": "key research topic",
    "search_type": "vector",
    "limit": 10
}).json()

# AI-powered question answering
answer = requests.post(f"{BASE_URL}/search/ask/simple", json={
    "query": "What does the literature say about X?"
}).json()
```

### 5. Podcast Generation

Generate multi-speaker podcasts from research materials.

```python
job = requests.post(f"{BASE_URL}/podcasts/generate", json={
    "notebook_id": notebook_id,
    "episode_profile_id": episode_profile_id,
    "speaker_profile_ids": [speaker1_id, speaker2_id]
}).json()

# Check status, then download audio when ready
```

### 6. Content Transformations

Apply custom AI-powered transformations for summarization, extraction, analysis.

```python
transform = requests.post(f"{BASE_URL}/transformations", json={
    "name": "extract_methods",
    "title": "Extract Methods",
    "prompt": "Extract and summarize the methodology section...",
    "apply_default": False
}).json()

result = requests.post(f"{BASE_URL}/transformations/execute", json={
    "transformation_id": transform["id"],
    "input_text": "...",
    "model_id": "model_id_here"
}).json()
```

## Supported AI Providers

Open Notebook supports 16+ providers via the Esperanto library: OpenAI, Anthropic, Google GenAI, Vertex AI, Ollama, Groq, Mistral, Azure OpenAI, DeepSeek, xAI, OpenRouter, ElevenLabs, Perplexity, Voyage.

For free local inference without API costs, use Ollama.

## Architecture

- **Backend:** Python with FastAPI
- **Database:** SurrealDB (document + relational)
- **AI Integration:** LangChain with Esperanto multi-provider library
- **Frontend:** Next.js with React
- **Deployment:** Docker Compose with persistent volumes

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPEN_NOTEBOOK_ENCRYPTION_KEY` | Secret key for encrypting stored credentials | Yes |
| `OPEN_NOTEBOOK_PASSWORD` | Optional password protection for the UI | No |

## Verification

After deployment:
1. Check services are running: `docker-compose ps`
2. Access the UI at http://localhost:8502
3. Configure at least one AI provider
4. Create a test notebook and add a source
5. Verify chat returns responses with source citations

## Pitfalls

- `OPEN_NOTEBOOK_ENCRYPTION_KEY` must be set before first launch and kept consistent across restarts
- At least one AI provider must be configured for AI features to work
- Large PDFs may take significant time to process — use `process_async: true`
- All data is stored in Docker volumes — back up volumes for data persistence

## Source

Distilled from K-Dense-AI/scientific-agent-skills — `skills/open-notebook/SKILL.md` (MIT license)
