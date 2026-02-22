# Recommended next task

## Task
Add deterministic missing-trace-summary guard coverage in `state/copilot_sdk_smoke_test.py` for `_get_latest_trace_summary`.

## Why it is next
Shape guards now cover container and chapter-metrics types; an explicit missing `trace_summary` entry scenario would complete validation around latest-entry payload completeness.

## Acceptance criteria
1. Add exactly one deterministic smoke mode where latest history entry is a dictionary without `trace_summary`.
2. Ensure the mode passes only when `expected latest history entry to contain trace_summary dictionary` assertion failure is detected.
3. Keep existing trace-summary smoke mode behavior unchanged.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
