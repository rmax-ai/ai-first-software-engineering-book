# Next iteration

## Recommended next task
Add a uniqueness smoke guard mode asserting the newest adjacency-order guard mode appears exactly once in `TRACE_SUMMARY_MODE_SPECS`.

## Why it is next
The adjacency-order guard has been added; the smallest follow-up is uniqueness hardening so duplicate registrations are caught deterministically.

## Concrete acceptance criteria
1. Add one smoke mode function in `state/copilot_sdk_smoke_test.py` that counts `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-guard` and asserts count is 1.
2. Register that new uniqueness mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic wording.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_125/*.md`
