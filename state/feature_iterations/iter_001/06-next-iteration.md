# Recommended next task

## Task
Implement deterministic trace-summary enrichment in `state/kernel.py` and prove it via smoke mode coverage.

## Why this is next
- It is the highest-impact feature from this planning pass and directly improves harness observability without changing public interfaces.
- It unlocks meaningful follow-up work in smoke assertions and eval signal checks.

## Acceptance criteria
1. `state/kernel.py` emits a richer, deterministic phase trace summary payload for completed runs.
2. `state/copilot_sdk_uv_smoke.py` (and `state/copilot_sdk_smoke_test.py` if needed) validates the new payload shape in at least one dedicated mode.
3. Validation evidence includes a successful targeted command: `uv run python state/copilot_sdk_uv_smoke.py --mode trace-summary`.
4. Iteration docs record any needed updates to eval expectations in `evals/*.yaml` or explain why no eval contract changes were required.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/copilot_sdk_smoke_test.py` (if matrix/assertion updates are required)
- `state/feature_iterations/iter_002/*`
