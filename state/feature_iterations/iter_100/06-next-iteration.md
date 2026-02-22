# Next iteration

## Recommended next task
Add a guard mode that enforces duplicate-count coverage-guard wrappers contain no f-strings in helper delegation arguments.

## Why it is next
Current guards cover delegation shape and PASS message structure but still allow dynamic string construction in wrapper helper arguments, which can reintroduce nondeterministic source drift.

## Concrete acceptance criteria
1. Add one smoke mode in `state/copilot_sdk_smoke_test.py` that parses duplicate-count coverage-guard wrappers and asserts both helper arguments are plain string literals (no f-strings, no concatenation nodes).
2. Register the mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-literal-only-guard` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_101/*.md`
