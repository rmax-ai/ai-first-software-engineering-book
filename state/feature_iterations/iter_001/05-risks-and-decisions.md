# Risks and Decisions

## Risks discovered
- Plan breadth could lead to oversized future diffs if not split into single-surface iterations.
- New trace signals may require synchronized updates across smoke tests and eval expectations.

## Decisions made and trade-offs
- Chosen scope is planning-only to satisfy seed-iteration contract and avoid premature code churn.
- Backlog is organized by deterministic harness surfaces (`kernel`, role templates, smoke, evals) to keep later work reviewable.

## Intentionally deferred
- No code implementation in `state/*.py` during this iteration.
- No eval YAML edits until corresponding harness behavior exists.
