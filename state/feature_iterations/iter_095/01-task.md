# Task

## Selected task title
Add a deterministic smoke guard that enforces canonical helper signature usage in duplicate-count coverage-guard wrappers.

## Why this task now
`state/feature_iterations/iter_094/06-next-iteration.md` prioritized signature-shape validation after single-delegation enforcement to close the next wrapper-regression vector.

## Acceptance criteria
1. Add one smoke mode in `state/copilot_sdk_smoke_test.py` that asserts each duplicate-count coverage-guard wrapper delegates with exactly two string arguments.
2. Register the mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-signature-guard` and capture PASS output.
