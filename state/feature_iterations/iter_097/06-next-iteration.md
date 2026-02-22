# Next iteration

## Recommended next task
Add a guard mode that enforces duplicate-count coverage-guard wrapper PASS messages use the canonical prefix `PASS: <mode-name> mode validates`.

## Why it is next
Current checks ensure mode-name inclusion but still allow silent drift in the deterministic PASS message structure expected by downstream logs and smoke evidence.

## Concrete acceptance criteria
1. Add one smoke mode in `state/copilot_sdk_smoke_test.py` that parses duplicate-count coverage-guard wrappers and asserts the second helper argument starts with `PASS: <registered mode name> mode validates`.
2. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-pass-message-prefix-guard` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_098/*.md`
