# Task

## Selected task title
Add smoke adjacency coverage for the newest long-form `...-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard` mode chain.

## Why this task now
The latest coverage block had uniqueness-count and adjacency-order guard modes but lacked a dedicated adjacency assertion mode for the newest long-form pair.

## Acceptance criteria
1. Add one smoke runner in `state/copilot_sdk_smoke_test.py` that asserts the paired uniqueness-count mode is immediately before the long-form adjacency-order guard mode.
2. Register one `TRACE_SUMMARY_MODE_SPECS` mode entry for the new runner.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode>` and capture PASS output.
