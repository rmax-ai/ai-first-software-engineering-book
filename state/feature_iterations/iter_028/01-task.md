# Task: Include duplicate counts in usage-examples duplicates guard diagnostics

## Why this task now
`state/feature_iterations/iter_027/06-next-iteration.md` identified count-aware duplicate diagnostics as the smallest unfinished improvement to make failure output more actionable.

## Acceptance criteria
1. Update `run_usage_examples_duplicates_guard_mode` in `state/copilot_sdk_smoke_test.py` to report per-mode duplicate counts.
2. Keep duplicate reporting deterministic by expected mode order.
3. Validate with:
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicates-guard`
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-order-guard`
