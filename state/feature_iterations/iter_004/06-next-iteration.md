# Recommended next task

## Task
Add a deterministic trace-summary regression case to `state/copilot_sdk_smoke_test.py` covering both success and missing-key failure paths.

## Why it is next
This will move validation from ad-hoc fixture invocation to the existing deterministic smoke matrix.

## Acceptance criteria
1. Add at least one passing mode that validates trace_summary required keys.
2. Add one failure mode that proves missing keys are detected.
3. Keep existing smoke matrix behavior unchanged for current modes.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- Optional: `state/copilot_sdk_uv_smoke.py` (only for shared helper extraction)
