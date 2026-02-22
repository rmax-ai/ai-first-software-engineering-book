# Next iteration

## Recommended next task
Add adjacency-order smoke coverage ensuring the new `...uniqueness-guard-adjacency-order-guard-uniqueness-guard` mode is positioned immediately before `...uniqueness-guard-adjacency-order-guard`.

## Why it is next
This iteration added uniqueness-count coverage; the smallest follow-up is an order assertion that protects deterministic placement between the new count-guard mode and the prior adjacency-order mode.

## Concrete acceptance criteria
1. Add one smoke mode runner in `state/copilot_sdk_smoke_test.py` that asserts `...uniqueness-guard-adjacency-order-guard-uniqueness-guard` appears immediately before `...uniqueness-guard-adjacency-order-guard` in `TRACE_SUMMARY_MODE_SPECS`.
2. Register one new `TRACE_SUMMARY_MODE_SPECS` mode for that adjacency-order assertion.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_142/*.md`
