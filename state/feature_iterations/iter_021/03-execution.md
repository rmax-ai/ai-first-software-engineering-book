# Execution

## Commands/tools run
- `view` + `rg` over `state/copilot_sdk_smoke_test.py` to inspect existing coverage-guard patterns.
- Edited `state/copilot_sdk_smoke_test.py` to add `run_usage_examples_coverage_guard_mode` and register `usage-examples-coverage-guard`.
- Ran targeted smoke checks:
  - `uv run python state/copilot_sdk_smoke_test.py --mode stub`
  - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-coverage-guard`

## Files changed
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_021/01-task.md`
- `state/feature_iterations/iter_021/02-plan.md`
- `state/feature_iterations/iter_021/03-execution.md`
- `state/feature_iterations/iter_021/04-validation.md`
- `state/feature_iterations/iter_021/05-risks-and-decisions.md`
- `state/feature_iterations/iter_021/06-next-iteration.md`
- `state/feature_iterations/iter_021/07-summary.md`

## Rationale per change
- New guard mode prevents user-facing usage-example drift from mode metadata.
- Iteration artifacts capture traceable execution evidence and the next bounded task.
