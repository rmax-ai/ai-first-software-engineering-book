# Risks and Decisions

## Risks discovered
- The duplicates guard filters by a fixed usage-line prefix; if usage formatting changes intentionally, this guard will need coordinated updates.

## Decisions made and trade-offs
- Reused existing usage-line extraction logic pattern to keep assertions aligned with current generated doc structure.
- Kept the new mode in `TRACE_SUMMARY_MODE_SPECS` to preserve existing centralized parser/doc wiring instead of introducing special-case plumbing.

## Intentionally deferred
- A stricter normalization guard that trims/normalizes whitespace before duplicate detection was deferred to keep this iteration minimal.
