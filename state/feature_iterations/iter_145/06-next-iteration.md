# Next iteration

## Recommended next task
Add adjacency-order smoke coverage ensuring the new `...-adjacency-order-guard-uniqueness-guard` uniqueness-count mode appears immediately before `...-adjacency-order-guard`.

## Why it is next
After exact-once coverage is in place for the newest long-form mode, the next smallest guard is to pin deterministic ordering between the uniqueness-count mode and its paired adjacency-order mode.

## Concrete acceptance criteria
1. Add one smoke runner in `state/copilot_sdk_smoke_test.py` asserting the new uniqueness-count mode is immediately followed by its paired adjacency-order mode.
2. Register one new `TRACE_SUMMARY_MODE_SPECS` mode for that adjacency-order assertion.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_146/*.md`
