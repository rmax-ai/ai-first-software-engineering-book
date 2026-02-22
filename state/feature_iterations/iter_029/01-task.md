# Task: Add deterministic duplicate-count regression smoke mode

## Why this task now
`state/feature_iterations/iter_028/06-next-iteration.md` identified a remaining gap: the duplicate guard reports counts, but there was no forced-duplicate regression mode asserting the exact `{mode: count}` diagnostic payload.

## Acceptance criteria
1. Add one deterministic mode in `state/copilot_sdk_smoke_test.py` that injects duplicate usage lines and asserts expected duplicate-count diagnostics.
2. Keep expected duplicate diagnostics ordered via `_expected_non_stub_mode_names(...)`.
3. Validate with:
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicates-guard`
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-regression-guard`
