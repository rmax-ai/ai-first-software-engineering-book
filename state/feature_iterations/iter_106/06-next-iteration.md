# Next iteration

## Recommended next task
Add a smoke guard mode that enforces `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-guard` is registered immediately after `usage-examples-duplicate-count-wrapper-helper-uniqueness-adjacency-guard` in `TRACE_SUMMARY_MODE_SPECS`.

## Why it is next
The new registration-order guard now protects one adjacency pair; locking the new mode’s placement after the uniqueness-adjacency guard prevents drift in the hardening sequence itself.

## Concrete acceptance criteria
1. Add one smoke mode in `state/copilot_sdk_smoke_test.py` asserting `usage-examples-duplicate-count-wrapper-helper-uniqueness-adjacency-guard` appears immediately before `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-guard` in `TRACE_SUMMARY_MODE_SPECS`.
2. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-guard` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_107/*.md`
