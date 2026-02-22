# Next iteration

## Recommended next task
Add a smoke guard mode that enforces adjacency between `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-guard` and `usage-examples-order-guard` in `TRACE_SUMMARY_MODE_SPECS`.

## Why it is next
After uniqueness is locked, adjacency should also be fixed so registration order drift is detected immediately.

## Concrete acceptance criteria
1. Add one mode in `state/copilot_sdk_smoke_test.py` asserting `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-guard` appears immediately before `usage-examples-order-guard`.
2. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-guard` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_112/*.md`
