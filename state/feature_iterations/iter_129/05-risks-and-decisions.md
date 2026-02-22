# Risks and Decisions

## Risks discovered
- Long, repeated mode identifiers are typo-prone; a single segment mismatch can invalidate uniqueness checks.
- `TRACE_SUMMARY_MODE_SPECS` ordering and naming are tightly coupled to guard semantics, so nearby edits can break related coverage modes.

## Decisions made and trade-offs
- Implemented one narrowly scoped uniqueness-count guard instead of refactoring shared naming helpers to keep diff risk low.
- Reused the existing deterministic guard-mode naming/description pattern for consistency and easier review.

## Intentionally deferred
- Full smoke matrix execution was deferred; only the directly affected guard mode path was validated.
