# Execution

## Commands/tools run
- `apply_patch` to add a new smoke mode function and register it in `TRACE_SUMMARY_MODE_SPECS`.
- `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-guard`

## Files changed
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_117/01-task.md`
- `state/feature_iterations/iter_117/02-plan.md`
- `state/feature_iterations/iter_117/03-execution.md`
- `state/feature_iterations/iter_117/04-validation.md`
- `state/feature_iterations/iter_117/05-risks-and-decisions.md`
- `state/feature_iterations/iter_117/06-next-iteration.md`
- `state/feature_iterations/iter_117/07-summary.md`

## Short rationale per change
- Added one deterministic adjacency guard mode to prevent ordering drift around the newest uniqueness guard registration.
- Added iteration artifacts required by the execution contract for reproducibility and handoff.
