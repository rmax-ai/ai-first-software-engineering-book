# Risks and Decisions

## Risks discovered
- Very long mode identifiers remain typo-prone and can invalidate assertions if any segment drifts.

## Decisions made and trade-offs
- Reused the exact existing long-form mode string from `TRACE_SUMMARY_MODE_SPECS` to avoid naming drift.
- Added only one runner and one registration to keep this iteration strictly minimal.

## Intentionally deferred
- Refactoring repetitive long-form mode names into shared constants/helpers.
