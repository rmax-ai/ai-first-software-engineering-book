# Risks and decisions

## Risks discovered
- Planning-only iterations can drift if the next task is too broad.
- Trace schema changes in `state/kernel.py` may require synchronized smoke/eval updates.

## Decisions made
- Kept scope to roadmap creation only, with no harness code edits, to satisfy the seed-iteration contract.
- Recommended a single narrow next task focused on trace schema formalization to reduce downstream churn.

## Deferred items
- Actual implementation of trace payload updates and smoke/eval assertions is deferred to the next iteration.
