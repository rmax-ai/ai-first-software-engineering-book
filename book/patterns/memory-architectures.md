# Memory Architectures

## Context
Agents are limited by context window, variability across runs, and the need to operate over long-lived projects. Memory mechanisms can improve continuity, but they also introduce drift, privacy risk, and debugging complexity.

## Problem
How do you add memory so the system remains reproducible and governable?

## Forces
- **Recall vs. precision**: retrieving more increases coverage but adds noise.
- **Freshness vs. stability**: updating memory improves relevance but can rewrite history.
- **Privacy vs. utility**: storing more can leak sensitive data and expand retention obligations.
- **Debuggability**: implicit retrieval is harder to reason about than explicit records.
- **Versioning**: memory must evolve with code; unversioned memory becomes a hidden dependency.

## Solution
Prefer layered, explicit memory with clear scopes, schemas, and write rules.

### Layer 1: Run-local working memory (scratch)
- **What**: transient notes, intermediate calculations, short summaries.
- **Scope**: one run.
- **Write rule**: always safe to overwrite; never treated as durable truth.
- **Example**: “Files touched: A, B. Hypothesis: failing test caused by null handling.”

### Layer 2: Session memory (task state)
- **What**: structured state for a multi-step task (checklists, open questions, next steps).
- **Scope**: until task completion.
- **Write rule**: update on each step; clear on task close.
- **Example**: a JSON task record containing acceptance criteria and verification status.

### Layer 3: Project memory (durable facts)
- **What**: stable, reviewable records: architecture decisions, interface contracts, runbooks.
- **Scope**: long-lived.
- **Write rule**: write only after verification passes and with a source-of-truth reference.
- **Example**: ADR-style entries with links to code and traces.

### Layer 4: Retrieval index (searchable corpus)
- **What**: embeddings or keyword index over docs/issues/traces.
- **Scope**: long-lived, but treated as *derived* data.
- **Write rule**: rebuildable; never the only place a critical fact exists.
- **Example**: “retrieve top 5 related incidents” feeding short excerpts into context.

## Implementation sketch
Write rules that keep memory auditable and safe:

- Only write durable memory after verification passes.
- Store sources (file paths, URLs, trace IDs, commit hashes) with each memory item.
- Separate schemas for different types of memory: facts, decisions, preferences, open questions.
- Treat retrieval as a *hint*; require confirmation against sources for critical claims.
- Version memory alongside the system (or tie it to a release identifier).
- Support redaction and retention policies (delete by scope, delete by source, delete by time).

Example durable-memory record schema (conceptual):

```json
{
  "type": "decision",
  "title": "Prefer golden tests for CLI help output",
  "status": "accepted",
  "sources": ["docs/cli.md", "trace:2026-02-18T10:14Z"],
  "rationale": "Help output is user-facing and easy to regress",
  "verified_by": ["npm test", "snapshot update reviewed"],
  "created_at": "2026-02-18"
}
```

### Concrete example
Bugfix agent memory layout:

- **Run-local**: stack trace notes and hypotheses.
- **Session**: checklist of reproduction steps + test plan + files changed.
- **Project**: “Root cause and fix” note linked to the failing test and the patch.
- **Retrieval**: search prior traces for similar failure signatures.

## Failure modes
- **Stale memory**: outdated assumptions persist after refactors; fixes target the wrong code.
- **Memory poisoning**: incorrect entries are stored as facts and bias future actions.
- **Over-retrieval**: too many irrelevant items drown the signal and dilute constraints.
- **Silent mutation**: memory is updated without review; history is effectively rewritten.
- **Unversioned dependency**: behavior depends on memory that is not tied to code/version.
- **Privacy leakage**: sensitive content is stored, retrieved, or logged without appropriate handling.

## When not to use
- Short-lived tasks where the context window is sufficient.
- High-sensitivity domains without a clear retention/redaction policy.
- Systems that require strict reproducibility but cannot version memory with code.
