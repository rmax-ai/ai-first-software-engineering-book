# Risks and decisions

## Risks discovered
- Planning quality risk: without explicit acceptance checks, future iterations could drift into broad refactors.
- Signal risk: new telemetry fields may be added without eval updates, reducing regression detectability.

## Decisions and trade-offs
- Chose a planning-only iteration per prompt requirements; deferred all runtime code edits.
- Chose minimal, file-targeted backlog items to keep subsequent diffs small and reviewable.
- Kept compatibility as a first-order constraint (future work should preserve existing public interfaces).

## Deferred intentionally
- Implementation of trace schema updates in `state/kernel.py`.
- Smoke/eval contract updates until after trace schema is finalized in the next iteration.
