# Next Iteration

## Recommended next task
Refactor usage-example guard modes to share a small helper that extracts generated non-`stub` mode names once.

## Why it is next
- `usage-examples-coverage-guard`, `usage-examples-order-guard`, and `usage-examples-mode-set-coverage-guard` now duplicate extraction logic.
- A shared helper will reduce drift risk while preserving focused guard semantics.

## Concrete acceptance criteria
1. Add a private helper in `state/copilot_sdk_smoke_test.py` that returns generated non-`stub` usage mode names.
2. Update usage-example guard modes to use the helper without changing assertion intent.
3. Validate with:
   - `uv run python state/copilot_sdk_smoke_test.py --mode stub`
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-order-guard`
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-mode-set-coverage-guard`

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_025/*.md`
