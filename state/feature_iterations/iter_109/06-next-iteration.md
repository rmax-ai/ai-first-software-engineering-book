# Next iteration

## Recommended next task
Add a smoke guard mode that enforces `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-guard` is registered immediately before `usage-examples-order-guard` in `TRACE_SUMMARY_MODE_SPECS`.

## Why it is next
The new uniqueness guard now checks count safety; locking its relative placement maintains deterministic guard sequencing at the handoff boundary into generic usage-example guards.

## Concrete acceptance criteria
1. Add one mode in `state/copilot_sdk_smoke_test.py` asserting immediate adjacency from `usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-guard` to `usage-examples-order-guard`.
2. Register that mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-guard` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_110/*.md`
