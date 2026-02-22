# Recommended next task

## Task
Add deterministic malformed-container guard coverage in `state/copilot_sdk_smoke_test.py` for invalid `chapters`, `history`, or latest-history-entry shapes consumed by `_get_latest_trace_summary`.

## Why it is next
Current trace-summary coverage validates key presence and payload type, but does not protect against upstream container-shape regressions before `trace_summary` lookup.

## Acceptance criteria
1. Add exactly one deterministic smoke mode with malformed container fixtures (`chapters`, `history`, or latest entry).
2. Ensure the mode passes only when container-shape assertion failures are detected.
3. Keep existing mode behavior unchanged.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
