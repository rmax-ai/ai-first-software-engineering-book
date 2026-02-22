# Next Iteration

## Recommended next task
Include duplicate counts in `usage-examples-duplicates-guard` failure diagnostics.

## Why it is next
The guard now reports deterministic duplicate mode names; adding counts is the smallest follow-up to improve debugging precision without broad refactoring.

## Concrete acceptance criteria
1. Update `run_usage_examples_duplicates_guard_mode` to include per-mode duplicate counts in assertion failure output.
2. Keep duplicate reporting deterministic by expected mode order.
3. Validate with:
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicates-guard`
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-order-guard`

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_028/*.md`
