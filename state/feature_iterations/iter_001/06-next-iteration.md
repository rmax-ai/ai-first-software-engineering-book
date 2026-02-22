# Recommended next iteration

## Next task
Add deterministic trace-phase markers in `state/kernel.py` and validate them via smoke coverage.

## Why this is next
Trace visibility is the lowest-risk, highest-observability slice and creates clear signals for later template and eval tightening.

## Acceptance criteria
- `state/kernel.py` emits explicit trace entries for plan/change/evaluate loop phases.
- `state/copilot_sdk_uv_smoke.py` includes at least one deterministic mode asserting the new trace markers.
- Validation is recorded with `uv run python state/copilot_sdk_uv_smoke.py --mode <new-mode>` output.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/0{1..7}-*.md`
