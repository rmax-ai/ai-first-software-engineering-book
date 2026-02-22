# Recommended next task

## Task
Implement deterministic trace-summary logging hooks in `state/kernel.py` and cover them in `state/copilot_sdk_uv_smoke.py`.

## Why this is next
- `state/kernel.py` is the harness orchestrator and the highest-value point for observability and deterministic controls.
- Smoke coverage should be added immediately with the feature so regressions are detected early.

## Acceptance criteria
- Add a minimal, explicit trace-summary logging path in `state/kernel.py` that does not alter existing public CLI behavior.
- Add or update smoke coverage in `state/copilot_sdk_uv_smoke.py` validating trace-summary artifacts/signals for both success and guarded-failure runs.
- Run `uv run python state/copilot_sdk_uv_smoke.py` and capture results in the next iteration validation artifact.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/*`
