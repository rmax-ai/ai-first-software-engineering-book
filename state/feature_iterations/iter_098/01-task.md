# Task

## Selected task title
Add a smoke guard mode that enforces duplicate-count coverage-guard wrappers use canonical PASS message prefixes.

## Why this task now
`state/feature_iterations/iter_097/06-next-iteration.md` identifies PASS message prefix drift as the next smallest deterministic regression surface after mode-name literal and PASS message literal checks.

## Acceptance criteria
1. Add one smoke mode in `state/copilot_sdk_smoke_test.py` that parses duplicate-count coverage-guard wrappers and asserts the second helper argument starts with `PASS: <registered mode name> mode validates`.
2. Register the mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-pass-message-prefix-guard` and capture PASS output.
