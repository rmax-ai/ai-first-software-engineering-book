# Next iteration

## Recommended next task
Add a guard mode that verifies duplicate-count coverage-guard wrappers use canonical PASS message literals aligned with each wrapper mode name.

## Why it is next
Mode-name literal parity is now enforced for helper arguments; PASS message literals are the remaining wrapper payload surface that can still drift silently.

## Concrete acceptance criteria
1. Add one smoke mode in `state/copilot_sdk_smoke_test.py` that parses duplicate-count coverage-guard wrappers and asserts their second helper argument is a string literal containing the wrapper's registered mode name.
2. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-pass-message-literal-guard` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_097/*.md`
