# Task

## Selected task title
Add a smoke guard mode that enforces duplicate-count coverage-guard wrappers use exactly one `mode validates` PASS-message delimiter.

## Why this task now
`state/feature_iterations/iter_099/06-next-iteration.md` identifies delimiter multiplicity as the next smallest deterministic regression surface after prefix and suffix guard coverage.

## Acceptance criteria
1. Add one smoke mode in `state/copilot_sdk_smoke_test.py` that parses duplicate-count coverage-guard wrappers and asserts each wrapper helper PASS message includes exactly one `mode validates` delimiter.
2. Register the mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-pass-message-delimiter-guard` and capture PASS output.
