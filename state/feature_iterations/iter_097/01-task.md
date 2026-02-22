# Task

## Selected task title
Add a smoke guard mode that enforces duplicate-count coverage-guard wrappers use PASS message literals containing their registered mode name.

## Why this task now
`state/feature_iterations/iter_096/06-next-iteration.md` identifies PASS message literal drift as the next remaining duplicate-count wrapper payload regression surface after mode-name literal checks.

## Acceptance criteria
1. Add one smoke mode in `state/copilot_sdk_smoke_test.py` that parses duplicate-count coverage-guard wrappers and asserts the second helper argument is a string literal containing each wrapper's registered mode name.
2. Register the mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-pass-message-literal-guard` and capture PASS output.
