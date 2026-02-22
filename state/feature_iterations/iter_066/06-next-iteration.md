# Next iteration

## Recommended next task
Add deterministic kernel fixture-root cleanup coverage mirroring the new non-kernel root-clean mode.

## Why it is next
Kernel and non-kernel trace-summary cleanup guarantees should be symmetric to prevent environment-specific fixture leakage regressions.

## Concrete acceptance criteria
1. Add one mode in `state/copilot_sdk_smoke_test.py` that runs kernel trace-summary variants and asserts root-level fixture directory cleanup after each run.
2. Preserve current kernel trace-summary success/failure assertions.
3. Record validation evidence under `state/feature_iterations/iter_067/04-validation.md`.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_067/*.md`
