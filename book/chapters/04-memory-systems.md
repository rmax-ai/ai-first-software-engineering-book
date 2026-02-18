# Chapter 04 — Memory Systems

## Thesis
Memory is a system component, not a transcript. It must be structured, queryable, and governed (with provenance) to improve long-horizon work.

Hypothesis: uncurated memory increases confidence without increasing correctness, by amplifying earlier mistakes.

## Why This Matters
- Long projects exceed context windows; without memory, work becomes repetitive and inconsistent.
- Without provenance, persistent memory becomes a source of silent drift.
- Production environments need data minimization and retention policies for stored traces and summaries.

## System Breakdown
- **Memory classes**:
  - Episodic: traces of actions/tool I/O/diffs.
  - Semantic: stable project facts and conventions.
  - Decisions: recorded trade-offs and constraints.
  - State: current plan, progress, open issues.
- **Write policy**: what gets stored, when, by whom, and with what validation.
- **Read policy**: retrieval filters, ranking, freshness, and provenance checks.
- **Governance**: retention, access control, redaction, and correction mechanisms.

## Concrete Example 1
Decision memory for an architecture choice.
- Store: decision record with options, chosen approach, constraints, and rationale.
- Enforce: future changes must reference the decision or explicitly supersede it.

## Concrete Example 2
Trace-indexed memory for debugging.
- Store: tool outputs and diffs keyed by task/iteration.
- Use: when a regression occurs, retrieve prior similar traces and compare failure signatures.

## Trade-offs
- More memory improves continuity but increases risk of stale or incorrect retrieval.
- Strong provenance improves trust but adds overhead to writing and updating memory.
- Aggressive retention helps debugging but increases privacy and storage costs.

## Failure Modes
- **Stale retrieval dominance**: old assumptions override new evidence.
- **Summarization loss**: key constraints disappear in compression.
- **Memory poisoning**: incorrect conclusions become “facts” through repetition.

## Research Directions
- Memory scoring with automated freshness and provenance signals.
- Mechanisms for correcting memory (retractions, superseding records).
- Evaluations for memory usefulness (measuring reduced iterations without increased regressions).
