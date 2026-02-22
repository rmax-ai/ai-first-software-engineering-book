# Task: Add deterministic empty-history guard smoke mode

## Why this task now
`state/feature_iterations/iter_009/06-next-iteration.md` identified empty `history` guard coverage as the next unfinished `_get_latest_trace_summary` gap.

## Acceptance criteria
1. Add exactly one deterministic smoke mode where `history` is an empty list.
2. Ensure the mode passes only when `expected metrics history for chapter ...` assertion failure is detected.
3. Keep existing trace-summary smoke mode behavior unchanged.
