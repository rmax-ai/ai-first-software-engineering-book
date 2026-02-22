# Risks and decisions

## Risks discovered
- Very long mode-name strings remain typo-prone and difficult to review quickly.
- Ordering assertions are sensitive to insertion point changes in `TRACE_SUMMARY_MODE_SPECS`.

## Decisions made and trade-offs
- Kept the existing explicit-string guard style instead of introducing helper abstractions to avoid scope creep.
- Inserted exactly one new mode and one assertion function, then corrected placement to satisfy adjacency semantics.

## Intentionally deferred
- No generalized builder/helper for long guard mode-name chains.
- No broad cleanup of existing mode-registration ordering beyond this task.
