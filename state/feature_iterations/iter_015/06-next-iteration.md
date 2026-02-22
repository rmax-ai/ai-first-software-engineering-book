# Recommended next task

## Task
Table-drive the remaining base smoke modes (`stub`, `sdk-unavailable`, `bootstrap-failure`, `live`) in `state/copilot_sdk_smoke_test.py` for `choices`, help text, and dispatch.

## Why it is next
- Shutdown and trace-summary mode drift is now reduced; the remaining hard-coded base mode branches are the next duplication hotspot.

## Acceptance criteria
1. Introduce one mapping for base mode name, handler, and description.
2. Reuse base, shutdown, and trace-summary mappings together for full `--mode` choices/help and dispatch.
3. Re-run at least `stub`, `bootstrap-failure`, and `trace-summary`.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_016/*`
