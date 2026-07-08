---
name: assessing-vector-and-embedding-weaknesses
title: Assessing Vector and Embedding Weaknesses
description: Review RAG/vector-store exposure to inversion, membership inference, tenant leakage, retrieval poisoning, and indirect prompt injection without providing default executable attack procedures.
domain: security-defensive
risk_level: high
requires_review: true
source_family: okf-security
source_status: review-gated-redacted
source_license: Apache-2.0
tags:
  - ai-security
  - rag-security
  - vector-database
  - embedding-security
  - tenant-isolation
  - retrieval-augmented-generation
  - prompt-injection
  - defensive-review
license: Apache-2.0
type: Playbook
---

# Assessing Vector and Embedding Weaknesses

## Review Gate

Use this skill only for authorized defensive review of RAG systems, embedding endpoints, and vector stores that the operator owns or is explicitly approved to assess.

This package-facing version is intentionally review-gated. It preserves the defensive assessment model and reporting procedure, but removes default executable code and step-by-step attack mechanics for embedding inversion, membership inference, cross-tenant probing, retrieval poisoning, and indirect prompt-injection testing. Those procedures can expose sensitive corpus data or degrade a live retrieval system when run outside a scoped test environment.

## Trigger

Use this skill when a RAG or vector-search application needs a security review for one or more of these risks:

- embeddings or similarity scores leaking source-document information;
- queries revealing whether a document, user, tenant, or sensitive phrase exists in the corpus;
- tenant isolation depending on client-side filters instead of server-side authorization;
- untrusted documents influencing retrieval ranking or model behavior;
- retrieved chunks carrying indirect prompt-injection content into downstream prompts;
- production-readiness review before exposing embedding or retrieval endpoints.

## Inputs Required

Collect these inputs before any test design is approved:

- written authorization and target scope;
- application owner and data owner contacts;
- environment classification: production, staging, isolated test, or synthetic lab;
- vector store type, tenancy model, namespaces/collections, and access-control boundaries;
- embedding model and whether raw embeddings or similarity scores are exposed;
- chunking strategy, metadata schema, retrieval filters, top-k defaults, and reranking path;
- corpus sensitivity classification;
- approved test dataset or synthetic corpus;
- allowed read/write operations and explicit no-touch production constraints;
- rollback plan for any test data inserted into a non-production collection.

## Ordered Procedure

### 1. Confirm authorization and data boundaries

Document who approved the review, which tenants and collections are in scope, which endpoints are allowed, and which data classes must not be queried. Do not proceed when authorization is unclear or when the only available environment contains sensitive production data without an approved test plan.

### 2. Inventory the retrieval pipeline

Map the full retrieval path from user query to embedding generation, vector search, metadata filtering, reranking, prompt assembly, model response, logging, and telemetry. Record where tenant identity and authorization are enforced.

The inventory must answer:

- Which service owns tenant authorization?
- Are tenant filters enforced server-side, or supplied by the client?
- Are raw vectors, similarity scores, nearest-neighbor IDs, or chunk text exposed to users?
- Can users add or modify corpus documents?
- Are retrieved chunks scanned before prompt assembly?

### 3. Classify exposure areas

Classify each exposure as one of:

- `inversion_or_reconstruction`: embeddings or neighbors may reveal original text;
- `membership_inference`: retrieval behavior may reveal corpus membership;
- `tenant_leakage`: one tenant can access another tenant's chunks;
- `retrieval_poisoning`: untrusted content can dominate or manipulate retrieval;
- `indirect_prompt_injection`: retrieved content can alter downstream model instructions;
- `observability_gap`: logs or traces are insufficient to prove isolation or cleanup.

### 4. Design non-destructive tests first

Prefer static configuration review, synthetic corpora, isolated collections, and read-only checks. Any write test must use a synthetic marker in a test collection and include an owner-approved cleanup plan. Do not insert adversarial or instruction-hijacking payloads into production or shared corpora.

### 5. Evaluate tenant isolation defensively

Verify that tenant scoping is enforced by backend authorization and cannot be bypassed by omitting, modifying, or replaying client-side filters. Record only whether isolation holds or fails; do not publish tenant-specific query strings, sensitive chunk text, or leaked identifiers in package-facing documentation.

### 6. Evaluate membership and reconstruction risk defensively

Assess whether API behavior, exact-match retrieval, raw vectors, similarity scores, or repeated queries can reveal corpus membership or source text. Use synthetic examples or approved test records. Report the risk pattern and control gap, not a reusable extraction recipe.

### 7. Evaluate poisoning and indirect-injection risk defensively

Review document-ingestion controls, source provenance, chunk validation, deduplication, retrieval diversity limits, and prompt-assembly sanitization. In isolated test environments, use benign canary text to measure whether one source can dominate retrieval. Do not add real prompt-hijack instructions or harmful content to shared indexes.

### 8. Recommend controls

Map each finding to concrete controls:

- server-side tenant filters or separate tenant collections;
- authorization checks at retrieval, not only at UI/API entry;
- reduced exposure of raw vectors, raw similarity scores, and nearest-neighbor metadata;
- rate limits and anomaly detection on embedding and retrieval endpoints;
- corpus provenance, allowlists, review workflows, and rollback for user-supplied content;
- retrieval diversity caps and source-level dominance limits;
- chunk sanitization before prompt assembly;
- test fixtures proving tenant isolation and cleanup behavior;
- logging that preserves evidence without storing sensitive corpus text unnecessarily.

### 9. Produce a reviewed finding set

For each finding, record:

- scope and environment;
- exposure class;
- evidence type without sensitive text;
- affected tenant or corpus class, if approved for disclosure;
- severity and likelihood;
- recommended control;
- owner;
- retest criteria;
- cleanup confirmation for any test data.

## Verification

The review is complete only when:

- authorization and scope are attached to the review record;
- production data was not modified unless explicitly approved;
- synthetic or approved test records were used for sensitive checks;
- tenant isolation was verified at the server-side enforcement layer;
- retrieval poisoning and indirect-injection checks used benign canaries or static review;
- no sensitive chunk text, raw embedding vectors, or tenant identifiers were copied into public/package-facing artifacts;
- remediation owners and retest criteria are recorded;
- cleanup evidence exists for any test collection or marker data.

## Failure Modes

Stop and escalate to a human security reviewer when:

- authorization is missing or ambiguous;
- the target is a third-party system outside the approved scope;
- only production data is available and write tests are requested;
- tests could expose another tenant's data;
- the operator is asked to reconstruct source text, infer membership for real users, or produce reusable extraction procedures;
- retrieved chunks include secrets, regulated data, or private tenant content;
- cleanup cannot be verified;
- a candidate procedure would materially improve unauthorized data extraction or retrieval manipulation.

## Package Boundary Decision

This skill is `high` risk and `requires_review: true`. It is suitable as a defensive planning and review wrapper in the installed package. Detailed executable inversion, membership-inference, cross-tenant probing, and poisoning procedures must remain outside the default package surface unless a separate human risk review confirms authorization, license/provenance, usefulness, and safe distribution boundaries.
