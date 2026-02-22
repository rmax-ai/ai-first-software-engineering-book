# Next iteration

## Recommended next task
Add deterministic assertions that non-kernel trace-summary modes also clean up fixture data under `state/.smoke_fixtures/trace_summary/repo` after each run.

## Why it is next
Kernel-backed fixture cleanup is now guaranteed; matching cleanup coverage for non-kernel fixture modes closes the remaining trace-summary fixture-leak surface.

## Concrete acceptance criteria
1. Add one deterministic mode in `state/copilot_sdk_smoke_test.py` that runs non-kernel trace-summary variants and asserts `state/.smoke_fixtures/trace_summary/repo` is removed after each run.
2. Preserve existing non-kernel trace-summary success/failure expectations.
3. Record verification results in `state/feature_iterations/iter_065/04-validation.md`.

## Expected files to touch
- `state/copilot_sdk_uv_smoke.py`
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_065/*.md`
