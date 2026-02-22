# Recommended next task

## Task
Implement deterministic trace-summary enrichment in `state/kernel.py` and verify it with one new targeted smoke mode in `state/copilot_sdk_uv_smoke.py`.

## Why this is next
The plan identifies trace observability as the highest-leverage harness enhancement, and it can be validated with a narrowly scoped smoke addition before broader template/eval updates.

## Acceptance criteria
- Add trace-summary fields in `state/kernel.py` that remain deterministic across repeated runs.
- Add one smoke mode in `state/copilot_sdk_uv_smoke.py` that fails when the new trace-summary shape is missing or malformed.
- Record the verification command and outcome using `uv run python state/copilot_sdk_uv_smoke.py --mode <new-mode>` in the new iteration validation artifact.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/03-execution.md`
- `state/feature_iterations/iter_002/04-validation.md`
