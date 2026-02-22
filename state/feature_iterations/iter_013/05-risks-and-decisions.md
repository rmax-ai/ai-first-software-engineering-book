# Risks and Decisions

## Risks discovered
- CLI help text is a long single string; adding modes increases maintenance burden.
- Deterministic guards rely on exact assertion strings, so wording changes can break tests.

## Decisions made
- Reused the existing assertion string from `_get_latest_trace_summary` to avoid behavior drift.
- Added only one new mode as requested and avoided broader refactors.

## Deferred
- Refactoring mode registration/help text into structured data is deferred to keep this iteration minimal.
