# Next iteration

## Recommended next task
Add a guard mode that enforces helper hardening mode uniqueness before adjacency checks, asserting both positional-only and arg-order helper guards appear exactly once in `TRACE_SUMMARY_MODE_SPECS`.

## Why it is next
After locking adjacency, uniqueness is the smallest follow-up to prevent duplicate registration from producing false-positive adjacency while still masking configuration drift.

## Concrete acceptance criteria
1. Add one smoke mode in `state/copilot_sdk_smoke_test.py` that counts occurrences of `usage-examples-duplicate-count-wrapper-helper-positional-only-guard` and `usage-examples-duplicate-count-wrapper-helper-arg-order-guard` in `TRACE_SUMMARY_MODE_SPECS` and requires exactly one each before checking adjacency.
2. Register the mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-adjacency-guard` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_105/*.md`
