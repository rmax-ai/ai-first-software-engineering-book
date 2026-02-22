# Plan

1. Add one guard runner function in `state/copilot_sdk_smoke_test.py` to compare adjacency order of the newest and prior uniqueness guard mode names.
2. Register a new mode tuple in `TRACE_SUMMARY_MODE_SPECS` for the new runner.
3. Execute only the new mode via `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode>`.
4. Record execution/validation evidence in this iteration folder.
