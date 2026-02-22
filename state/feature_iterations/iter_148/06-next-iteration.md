# Next iteration

## Recommended next task
Add exact-once smoke coverage for the newest long-form uniqueness-order adjacency-order mode immediately following the just-validated adjacency-order guard pair.

## Why it is next
- This extends deterministic sequencing/uniqueness guarantees one step deeper while reusing the same guard pattern.

## Concrete acceptance criteria
1. Add one smoke runner that asserts the newest long-form uniqueness-order adjacency-order mode appears exactly once.
2. Register one new `TRACE_SUMMARY_MODE_SPECS` mode for that assertion.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_149/*.md`
