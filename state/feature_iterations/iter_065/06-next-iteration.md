# Next iteration

## Recommended next task
Add a deterministic guard mode that asserts non-kernel trace-summary runs leave no residual directories under `state/.smoke_fixtures/trace_summary/` beyond the per-run repo cleanup target.

## Why it is next
Current coverage asserts `repo` cleanup only; validating the fixture root remains clean closes directory-leak regressions if future fixture assets are introduced.

## Concrete acceptance criteria
1. Add one deterministic mode in `state/copilot_sdk_smoke_test.py` that runs non-kernel trace-summary variants and asserts `state/.smoke_fixtures/trace_summary/` has no unexpected residual directories after each invocation.
2. Preserve existing non-kernel trace-summary success/failure expectations.
3. Record validation results in `state/feature_iterations/iter_066/04-validation.md`.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_066/*.md`
