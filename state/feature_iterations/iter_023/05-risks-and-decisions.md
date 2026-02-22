# Risks and Decisions

## Risks discovered
- Ordering and coverage checks overlap partially, so future edits must keep each mode’s intent clear.

## Decisions made and trade-offs
- Added a dedicated ordering guard instead of changing existing coverage/duplicate guards to keep failure signals specific.
- Reused existing `_usage_doc_lines()` and `_all_mode_specs()` helpers to avoid new generation paths and reduce drift risk.

## Intentionally deferred
- No consolidation of nearby usage guard modes in this iteration; scope kept to one smallest unfinished task.
