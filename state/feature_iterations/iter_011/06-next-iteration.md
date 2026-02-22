# Recommended next task

## Task
Add deterministic chapter-metrics-shape guard coverage in `state/copilot_sdk_smoke_test.py` for `_get_latest_trace_summary`.

## Why it is next
Missing chapter coverage is now present; explicit non-dict chapter-metrics coverage would complete guard assertions around `chapter_metrics` shape.

## Acceptance criteria
1. Add exactly one deterministic smoke mode where `chapters[chapter_id]` is present but not a dictionary.
2. Ensure the mode passes only when `expected chapter metrics dictionary` assertion failure is detected.
3. Keep existing trace-summary smoke mode behavior unchanged.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
