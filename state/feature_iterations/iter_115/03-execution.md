# Execution

## Commands/tools run
1. `rg "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order" state/copilot_sdk_smoke_test.py`
2. `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-guard` (initially failed due registration placement)
3. `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-guard` (pass after tuple reorder)

## Files changed
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_115/01-task.md`
- `state/feature_iterations/iter_115/02-plan.md`
- `state/feature_iterations/iter_115/03-execution.md`
- `state/feature_iterations/iter_115/04-validation.md`
- `state/feature_iterations/iter_115/05-risks-and-decisions.md`
- `state/feature_iterations/iter_115/06-next-iteration.md`
- `state/feature_iterations/iter_115/07-summary.md`

## Short rationale per change
- Added one targeted adjacency guard mode to preserve deterministic ordering constraints.
- Registered the new mode near related guards while keeping the asserted neighbor pair untouched.
- Recorded iteration artifacts for reproducibility and handoff.
