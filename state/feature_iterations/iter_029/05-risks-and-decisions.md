# Risks and decisions

## Risks discovered
- The regression mode intentionally hard-codes synthetic duplicate counts; if synthetic injection changes, the expected map must be updated.
- Additional mode registration expands generated usage docs, so coverage guards would fail if registration is skipped.

## Decisions and trade-offs
- Reused existing helper functions instead of introducing new helper abstractions to keep the diff minimal.
- Injected duplicates into generated usage lines rather than altering mode registration, avoiding side effects on other guards.

## Deferred
- No extra negative-path assertions were added beyond the exact duplicate-count payload check to keep this iteration tightly scoped.
