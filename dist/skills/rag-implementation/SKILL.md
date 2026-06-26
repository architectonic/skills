---
name: rag-implementation
description: Build Retrieval-Augmented Generation (RAG) systems for LLM applications. Use when implementing knowledge-grounded AI, building document Q&A systems, integrating LLMs with external knowledge bases, reducing hallucinations, or creating documentation assistants. Covers vector databases, embeddings, retrieval strategies, reranking, chunking, and advanced RAG patterns.
type: Playbook
---

# RAG Implementation

Build LLM applications that provide accurate, grounded responses using external knowledge sources.

## Core Components

### Vector Databases

| Database | Characteristics |
|----------|----------------|
| **Pinecone** | Managed, scalable, serverless |
| **Weaviate** | Open-source, hybrid search, GraphQL |
| **Milvus** | High performance, on-premise |
| **Chroma** | Lightweight, local development |
| **Qdrant** | Fast, filtered search, Rust-based |
| **pgvector** | PostgreSQL extension, SQL integration |

### Embedding Models (2026)

| Model | Dimensions | Best For |
|-------|------------|----------|
| **voyage-3-large** | 1024 | Claude apps (Anthropic recommended) |
| **voyage-code-3** | 1024 | Code search |
| **text-embedding-3-large** | 3072 | OpenAI apps, high accuracy |
| **text-embedding-3-small** | 1536 | OpenAI apps, cost-effective |
| **bge-large-en-v1.5** | 1024 | Open source, local deployment |
| **multilingual-e5-large** | 1024 | Multi-language support |

### Retrieval Strategies

- **Dense Retrieval**: Semantic similarity via embeddings
- **Sparse Retrieval**: Keyword matching (BM25, TF-IDF)
- **Hybrid Search**: Combine dense + sparse with weighted fusion
- **Multi-Query**: Generate multiple query variations
- **HyDE**: Generate hypothetical documents for better retrieval

### Reranking

- **Cross-Encoders**: BERT-based reranking (ms-marco-MiniLM)
- **Cohere Rerank**: API-based reranking
- **MMR**: Maximal Marginal Relevance for diversity + relevance
- **LLM-based**: Use LLM to score relevance

## Quick Start (LangGraph)

```python
from langgraph.graph import StateGraph, START, END
from langchain_anthropic import ChatAnthropic
from langchain_voyageai import VoyageAIEmbeddings
from langchain_pinecone import PineconeVectorStore

llm = ChatAnthropic(model="claude-sonnet-4-6")
embeddings = VoyageAIEmbeddings(model="voyage-3-large")
vectorstore = PineconeVectorStore(index_name="docs", embedding=embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

async def retrieve(state):
    docs = await retriever.ainvoke(state["question"])
    return {"context": docs}

async def generate(state):
    context_text = "\n\n".join(doc.page_content for doc in state["context"])
    response = await llm.ainvoke(rag_prompt.format_messages(context=context_text, question=state["question"]))
    return {"answer": response.content}

builder = Graph()
builder.add_node("retrieve", retrieve)
builder.add_node("generate", generate)
builder.add_edge(START, "retrieve")
builder.add_edge("retrieve", "generate")
builder.add_edge("generate", END)
```

## Advanced Patterns

### Hybrid Search with RRF

```python
from langchain.retrievers import EnsembleRetriever

bm25_retriever = BM25Retriever.from_documents(documents)
dense_retriever = vectorstore.as_retriever(search_kwargs={"k": 10})

ensemble = EnsembleRetriever(
    retrievers=[bm25_retriever, dense_retriever],
    weights=[0.3, 0.7]  # 30% keyword, 70% semantic
)
```

### Parent Document Retriever

Small chunks for precise retrieval, large chunks for context:

```python
from langchain.retrievers import ParentDocumentRetriever

child_splitter = RecursiveCharacterTextSplitter(chunk_size=400)
parent_splitter = RecursiveCharacterTextSplitter(chunk_size=2000)

retriever = ParentDocumentRetriever(
    vectorstore=vectorstore, docstore=InMemoryStore(),
    child_splitter=child_splitter, parent_splitter=parent_splitter
)
```

### HyDE (Hypothetical Document Embeddings)

Generate a hypothetical answer document, use it for retrieval:

```python
async def generate_hypothetical(state):
    response = await llm.ainvoke(f"Write a passage that answers: {state['question']}")
    return {"hypothetical_doc": response.content}

async def retrieve_with_hyde(state):
    docs = await retriever.ainvoke(state["hypothetical_doc"])
    return {"context": docs}
```

## Document Chunking Strategies

| Strategy | When to use |
|----------|-------------|
| **Recursive Character** | General purpose, respects separators |
| **Token-Based** | When token budget matters |
| **Semantic** | When semantic coherence matters most |
| **Markdown Header** | When documents have clear structure |

## Metadata Filtering

```python
# Add metadata during indexing
doc.metadata.update({"source": "...", "category": "technical", "date": datetime.now().isoformat()})

# Filter during retrieval
results = await vectorstore.asimilarity_search("query", filter={"category": "technical"}, k=5)
```

## Best Practices

1. **Use hybrid search** for production (dense + sparse)
2. **Rerank results** before passing to LLM
3. **Chunk appropriately** — too small loses context, too large dilutes relevance
4. **Add metadata** for filtering and provenance
5. **Use MMR** to avoid redundant results
6. **Evaluate retrieval quality** with relevance metrics
7. **Version your embeddings** when changing models
8. **Monitor token costs** — retrieved context counts against context window

## Source

Distilled from `GeniusHTX/SWE-Skills-Bench` → `skills/rag-implementation/SKILL.md` (MIT).
