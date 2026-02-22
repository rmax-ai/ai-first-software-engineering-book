# Recommended next task

## Task
Add deterministic malformed latest-history-entry guard coverage in `state/copilot_sdk_smoke_test.py` for `_get_latest_trace_summary`.

## Why it is next
Container-shape checks now cover `chapters` and `history`; the next blind spot is malformed latest history entries before `trace_summary` extraction.

## Acceptance criteria
1. Add exactly one deterministic smoke mode where latest `history` entry is non-dict.
2. Ensure the mode passes only when latest-entry shape assertion failure is detected.
3. Keep existing trace-summary smoke mode behavior unchanged.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
