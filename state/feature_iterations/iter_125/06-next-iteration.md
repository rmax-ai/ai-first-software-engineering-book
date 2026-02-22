# Next iteration

## Recommended next task
Add an adjacency-order smoke guard mode asserting the new uniqueness guard mode appears immediately before the newest adjacency-order guard mode.

## Why it is next
After adding uniqueness hardening for the newest adjacency-order guard, the smallest follow-up is ordering hardening between the new uniqueness guard and its guarded mode.

## Concrete acceptance criteria
1. Add one smoke mode function in `state/copilot_sdk_smoke_test.py` that asserts `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-guard` appears immediately before `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-guard` in `TRACE_SUMMARY_MODE_SPECS`.
2. Register that new adjacency-order smoke mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic wording.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_126/*.md`
