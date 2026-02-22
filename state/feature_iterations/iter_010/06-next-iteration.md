# Recommended next task

## Task
Add deterministic missing-chapter guard coverage in `state/copilot_sdk_smoke_test.py` for `_get_latest_trace_summary`.

## Why it is next
Container shape, empty history, and malformed latest entry are covered; explicit missing chapter coverage would complete the guard matrix around chapter lookup semantics.

## Acceptance criteria
1. Add exactly one deterministic smoke mode where the requested chapter key is absent from `chapters`.
2. Ensure the mode passes only when the `expected metrics history for chapter ...` assertion failure is detected.
3. Keep existing trace-summary smoke mode behavior unchanged.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
