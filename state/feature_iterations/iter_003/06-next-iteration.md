# Recommended next task

## Task
Add a focused smoke assertion in `state/copilot_sdk_uv_smoke.py` that validates `trace_summary` presence and required keys in metrics history after a kernel run.

## Why it is next
The new telemetry field is implemented; the smallest follow-up is a deterministic regression check that prevents silent removal or shape drift.

## Acceptance criteria
1. Smoke flow reads `state/metrics.json` and asserts `trace_summary` exists on the latest history entry.
2. Assertion verifies keys: `decision`, `drift_score`, `diff_ratio`, `deterministic_pass`.
3. Existing smoke modes continue passing without behavior changes.

## Expected files to touch
- `state/copilot_sdk_uv_smoke.py`
- Optional: `state/kernel.py` (only if tiny wiring adjustment is required)
