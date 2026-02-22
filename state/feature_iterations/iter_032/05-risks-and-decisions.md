# Risks and decisions

## Risks discovered
- Guard mode names are intentionally long and repetitive; naming drift is easy without deterministic tests.

## Decisions made and trade-offs
- Reused the existing guard function pattern to minimize risk and keep behavior predictable.
- Changed only one functional file and avoided broader refactors in this iteration.

## Deferred intentionally
- No consolidation/refactor of repetitive guard helpers; preserving minimal-diff iteration scope.
