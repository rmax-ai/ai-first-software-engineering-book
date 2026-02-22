# Next iteration

## Recommended next task
Add a uniqueness-count smoke guard mode that asserts `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-guard` appears exactly once in `TRACE_SUMMARY_MODE_SPECS`.

## Why it is next
The new adjacency-order guard now enforces ordering, so the smallest follow-up is uniqueness hardening for the newly added guard mode itself.

## Concrete acceptance criteria
1. Add one smoke mode function in `state/copilot_sdk_smoke_test.py` that counts the new `...-order-uniqueness-adjacency-guard` mode and asserts the count is `1`.
2. Register that new uniqueness-count guard mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic wording.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_127/*.md`
