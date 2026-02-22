# Recommended next task

## Task
Add deterministic empty-history guard coverage in `state/copilot_sdk_smoke_test.py` for `_get_latest_trace_summary`.

## Why it is next
Container and latest-entry malformed paths are covered; the next gap is explicitly verifying rejection when `history` is a valid list container but empty.

## Acceptance criteria
1. Add exactly one deterministic smoke mode where `history` is an empty list.
2. Ensure the mode passes only when the `expected metrics history for chapter ...` assertion failure is detected.
3. Keep existing trace-summary smoke mode behavior unchanged.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
