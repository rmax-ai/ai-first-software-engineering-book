# Execution

## Commands/tools run
- `apply_patch` to add a new adjacency smoke guard function and mode registration in `state/copilot_sdk_smoke_test.py`.
- `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-guard`

## Files changed
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_122/01-task.md`
- `state/feature_iterations/iter_122/02-plan.md`
- `state/feature_iterations/iter_122/03-execution.md`
- `state/feature_iterations/iter_122/04-validation.md`
- `state/feature_iterations/iter_122/05-risks-and-decisions.md`
- `state/feature_iterations/iter_122/06-next-iteration.md`
- `state/feature_iterations/iter_122/07-summary.md`

## Short rationale per change
- Added deterministic adjacency-order coverage for the newest uniqueness guard mode to prevent registration-order drift.
- Registered the new mode in the trace-summary mode matrix so it is executable and documented.
- Captured required iteration artifacts for handoff.
