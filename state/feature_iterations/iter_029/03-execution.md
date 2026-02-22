# Execution

## Commands/tools run
- Read prior guidance: `state/feature_iterations/iter_028/06-next-iteration.md`
- Edited `state/copilot_sdk_smoke_test.py` to add and register deterministic duplicate-count regression mode.
- Ran smoke validations:
  - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicates-guard`
  - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-regression-guard`

## Files changed
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_029/01-task.md`
- `state/feature_iterations/iter_029/02-plan.md`
- `state/feature_iterations/iter_029/03-execution.md`
- `state/feature_iterations/iter_029/04-validation.md`
- `state/feature_iterations/iter_029/05-risks-and-decisions.md`
- `state/feature_iterations/iter_029/06-next-iteration.md`
- `state/feature_iterations/iter_029/07-summary.md`

## Rationale per change
- Added a forced-duplicate mode so duplicate-count diagnostics are directly regression-tested.
- Reused usage-line and expected-mode helpers to keep ordering and mode selection deterministic.
- Registered mode in shared metadata to preserve argparse/docstring/usage generation consistency.
