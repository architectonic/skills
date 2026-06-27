---
name: context-compression
title: Context Compression Strategies
description: 'When agent sessions generate massive context histories, compression
  becomes mandatory. The naive approach optimizes tokens-per-request. The correct
  optimization target is **tokens-per-task**: total tokens consumed to complete a
  task, including re-fetching costs when compression loses critical information.'
type: Playbook
domain: agent-operations
tags:
- agent-operations
- okf
risk_level: medium
requires_review: true
source_family: agent-skills-standard
source_status: adapted
---

# Context Compression Strategies

When agent sessions generate massive context histories, compression becomes mandatory. The naive approach optimizes tokens-per-request. The correct optimization target is **tokens-per-task**: total tokens consumed to complete a task, including re-fetching costs when compression loses critical information.

## When to Use

- Agent sessions approach context window limits (70-80% utilization)
- Codebases exceed context windows (5M+ token systems)
- Designing conversation summarization strategies
- Debugging cases where agents "forget" what files they modified
- Building evaluation frameworks for compression quality

## Three Compression Methods

### 1. Anchored Iterative Summarization (Recommended)
Maintain structured, persistent summaries with explicit sections. On each compression trigger, summarize only the newly-truncated span and merge into existing sections. Structure forces preservation.

**Quality**: 3.70/5.0 | **Compression**: 98.6%

### 2. Regenerative Full Summary
Generate detailed structured summaries on each compression. Produces readable output but may lose details across repeated compression cycles.

**Quality**: 3.44/5.0 | **Compression**: 98.7%

### 3. Opaque Compression
Produce compressed representations optimized for reconstruction fidelity. Highest compression ratios but sacrifices interpretability. Cannot verify what was preserved.

**Quality**: 3.35/5.0 | **Compression**: 99.3%

## Structured Summary Template

```markdown
## Session Intent
[What the user is trying to accomplish]

## Files Modified
- auth.controller.ts: Fixed JWT token generation
- config/redis.ts: Updated connection pooling

## Decisions Made
- Using Redis connection pool instead of per-request connections
- Retry logic with exponential backoff for transient failures

## Current State
- 14 tests passing, 2 failing
- Remaining: mock setup for session service tests

## Next Steps
1. Fix remaining test failures
2. Run full test suite
3. Update documentation
```

## Execution Steps

### Step 1: Define Summary Sections
Create explicit sections matching your agent's needs:
- Session Intent, Files Modified, Decisions Made, Current State, Next Steps

### Step 2: Trigger Compression at 70-80% Context
Don't compress too early — the 0.7% additional tokens retained by structured summarization buys 0.35 quality points.

### Step 3: Incremental Merging
On first compression, summarize truncated history into sections. On subsequent compressions, summarize only new truncated content. Merge into existing sections rather than regenerating.

### Step 4: Track Artifact Trail Separately
Artifact trail integrity is the weakest dimension (2.2-2.5/5.0). Track file modifications separately from general summarization — a dedicated file-state index or explicit file tracking in scaffolding.

### Step 5: Probe-Based Evaluation
Test compression quality by asking questions after compression:
- **Recall**: "What was the original error message?"
- **Artifact**: "Which files have we modified?"
- **Continuation**: "What should we do next?"
- **Decision**: "What did we decide about the Redis issue?"

## Three-Phase Compression Workflow for Large Codebases

1. **Research Phase**: Produce a research document from architecture diagrams, documentation, and key interfaces. Output: single research document.
2. **Planning Phase**: Convert research into implementation specification. A 5M token codebase compresses to ~2,000 words of specification.
3. **Implementation Phase**: Execute against specification. Context stays focused on spec rather than raw codebase exploration.

## Six Evaluation Dimensions

| Dimension | What It Tests | Weakest Method |
|-----------|---------------|----------------|
| Accuracy | Technical details (file paths, function names, error codes) | Opaque |
| Context Awareness | Current conversation state | Opaque |
| Artifact Trail | Which files were read or modified | All (2.2-2.5/5.0) |
| Completeness | All parts of question addressed | Opaque |
| Continuity | Can work continue without re-fetching | Opaque |
| Instruction Following | Respects stated constraints | Opaque |

## Decision Matrix

| Situation | Best Method |
|-----------|-------------|
| Long-running sessions (100+ messages) | Anchored Iterative |
| File tracking matters (coding, debugging) | Anchored Iterative |
| Verify what was preserved | Anchored Iterative |
| Maximum token savings required | Opaque |
| Short sessions, low re-fetch cost | Opaque |
| Interpretability critical | Regenerative |
| Clear phase boundaries | Regenerative |

## Guidelines

1. Optimize for tokens-per-task, not tokens-per-request
2. Use structured summaries with explicit sections for file tracking
3. Trigger compression at 70-80% context utilization
4. Implement incremental merging rather than full regeneration
5. Test compression quality with probe-based evaluation
6. Track artifact trail separately if file tracking is critical
7. Accept slightly lower compression ratios for better quality retention
8. Monitor re-fetching frequency as a compression quality signal

## Integration

This skill connects to:
- `agent-operations/context-degradation-patterns` — Compression mitigates degradation
- `agent-operations/context-window-management` — Compression is one window management technique
- `agent-operations/memory-ops-doctrine` — Compression quality affects memory fidelity

## References

- Factory Research: Evaluating Context Compression for AI Agents (December 2025)
- Netflix Engineering: "The Infinite Software Crisis" (AI Summit 2025)
- Zheng et al.: LLM-as-judge evaluation methodology (2023)

---

## Limitations

- Compression always trades information for tokens; choose method based on task criticality
- Artifact trail is inherently weak across all methods; supplement with explicit file tracking
- Probe-based evaluation requires designing good test questions; misses are silent
