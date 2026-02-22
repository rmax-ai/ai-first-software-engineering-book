# Execution

## Commands/tools run
- `view DEVELOPMENT.md`
- `view state/feature_iterations/iter_135/06-next-iteration.md`
- `rg`/`view` against `state/copilot_sdk_smoke_test.py` to locate insertion points
- `apply_patch` to add the new guard runner and mode registration
- `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-guard`

## Files changed
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_136/01-task.md`
- `state/feature_iterations/iter_136/02-plan.md`
- `state/feature_iterations/iter_136/03-execution.md`
- `state/feature_iterations/iter_136/04-validation.md`
- `state/feature_iterations/iter_136/05-risks-and-decisions.md`
- `state/feature_iterations/iter_136/06-next-iteration.md`
- `state/feature_iterations/iter_136/07-summary.md`

## Short rationale per change
- Added one adjacency-order runner to keep newest long-form guard mode ordering deterministic.
- Added one mode registration so the runner is invocable from the smoke CLI mode switch.
- Added standard iteration artifacts for traceability, validation evidence, and handoff.
