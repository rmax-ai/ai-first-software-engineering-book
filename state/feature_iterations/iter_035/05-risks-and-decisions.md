# Risks and Decisions

## Risks discovered
- The deterministic mode list continues to grow with very long names, increasing maintenance overhead for repetitive guard-chain tasks.

## Decisions made and trade-offs
- Kept the existing table-driven pattern and added one minimal new mode entry to avoid unrelated refactors.
- Accepted incremental repetition to preserve deterministic behavior and low-risk diffs.

## Deferred
- Refactoring repetitive guard-chain mode handlers into a generator/helper remains deferred to keep this iteration scoped to one queued task.
