# Execution

## Commands/tools run
- `view` on `DEVELOPMENT.md` and prior iteration files (`iter_125/04-validation.md`, `iter_125/06-next-iteration.md`).
- `apply_patch` edits in `state/copilot_sdk_smoke_test.py`.
- `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-guard`.

## Files changed
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_126/01-task.md`
- `state/feature_iterations/iter_126/02-plan.md`
- `state/feature_iterations/iter_126/03-execution.md`
- `state/feature_iterations/iter_126/04-validation.md`
- `state/feature_iterations/iter_126/05-risks-and-decisions.md`
- `state/feature_iterations/iter_126/06-next-iteration.md`
- `state/feature_iterations/iter_126/07-summary.md`

## Rationale per change
- Added a new smoke guard mode function and mode registration to enforce deterministic ordering between the newest uniqueness guard and newest adjacency-order guard.
- Reordered the two newest mode entries so the new ordering assertion is true and stable.
- Captured this iteration's task, validation evidence, risks, next step, and summary in the required seven artifact files.
