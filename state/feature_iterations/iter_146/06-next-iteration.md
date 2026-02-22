# Next iteration

## Recommended next task
Add exact-once smoke coverage for the newest long-form adjacency-order guard mode (`...-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard`).

## Why it is next
After adding adjacency ordering coverage for the pair, the next smallest guard is to enforce single registration for that newest long-form adjacency-order guard mode.

## Concrete acceptance criteria
1. Add one smoke runner in `state/copilot_sdk_smoke_test.py` asserting the newest long-form adjacency-order guard mode appears exactly once in `TRACE_SUMMARY_MODE_SPECS`.
2. Register one new `TRACE_SUMMARY_MODE_SPECS` mode for that exact-once assertion.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_147/*.md`
