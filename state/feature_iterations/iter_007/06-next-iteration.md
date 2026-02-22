# Recommended next task

## Task
Add deterministic malformed `history` container guard coverage in `state/copilot_sdk_smoke_test.py` for `_get_latest_trace_summary`.

## Why it is next
Current container-shape coverage now protects `chapters`, but not malformed `history` payloads before latest-entry lookup.

## Acceptance criteria
1. Add exactly one deterministic smoke mode where `history` is not a list.
2. Ensure the mode passes only when container-shape assertion failure is detected.
3. Keep existing smoke mode behavior unchanged.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
