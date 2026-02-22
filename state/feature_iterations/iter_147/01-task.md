# Task

## Selected task title
Add exact-once smoke coverage for the newest long-form adjacency-order guard mode.

## Why this task now
`iter_146/06-next-iteration.md` explicitly prioritized this guard to ensure the newest long-form adjacency-order mode is registered exactly once.

## Acceptance criteria
1. Add one smoke runner in `state/copilot_sdk_smoke_test.py` that asserts the newest long-form adjacency-order guard mode appears exactly once in `TRACE_SUMMARY_MODE_SPECS`.
2. Register one new `TRACE_SUMMARY_MODE_SPECS` mode wired to that runner.
3. Run targeted validation with `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and capture PASS output.
