# Plan

1. Add a new wrapper smoke mode function in `state/copilot_sdk_smoke_test.py` that enforces uniqueness (`count == 1`) for the newest adjacency-order guard mode name.
2. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` adjacent to the newest adjacency-order guard entry to keep deterministic ordering expectations clear.
3. Execute the new mode with `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode>` to verify PASS.
4. Record execution evidence, risks, and the next smallest guard task in this iteration folder.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_125/01-task.md`
- `state/feature_iterations/iter_125/02-plan.md`
- `state/feature_iterations/iter_125/03-execution.md`
- `state/feature_iterations/iter_125/04-validation.md`
- `state/feature_iterations/iter_125/05-risks-and-decisions.md`
- `state/feature_iterations/iter_125/06-next-iteration.md`
- `state/feature_iterations/iter_125/07-summary.md`
