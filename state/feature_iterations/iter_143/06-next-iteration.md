# Next iteration

## Recommended next task
Add adjacency-order smoke coverage ensuring `...uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard-uniqueness-guard` appears immediately before `...uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard`.

## Why it is next
After adding exact-once coverage for the newest long-form mode, the smallest follow-up is ordering coverage between that new mode and the prior mode.

## Concrete acceptance criteria
1. Add one smoke runner in `state/copilot_sdk_smoke_test.py` that asserts `...uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard-uniqueness-guard` appears immediately before `...uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard` in `TRACE_SUMMARY_MODE_SPECS`.
2. Register one new `TRACE_SUMMARY_MODE_SPECS` mode for that adjacency-order assertion.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_144/*.md`
