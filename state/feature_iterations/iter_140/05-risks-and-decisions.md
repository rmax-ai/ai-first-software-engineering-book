# Risks and Decisions

## Risks discovered
- Long mode identifiers are error-prone; a typo in one segment can silently target the wrong mode.

## Decisions made and trade-offs
- Reused exact long-form mode strings already present in `TRACE_SUMMARY_MODE_SPECS` to minimize naming drift.
- Added only one new runner and one new mode to preserve minimal-change scope.

## Intentionally deferred
- Broader refactoring of repetitive long-form helper names.
