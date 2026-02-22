# Execution

## Commands/tools run
- `view prompts/incremental-improvements/execute.md`
- `view DEVELOPMENT.md`
- `view state/feature_iterations/iter_012/06-next-iteration.md`
- `apply_patch state/copilot_sdk_smoke_test.py`
- `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-missing-entry-guard`
- `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-chapter-metrics-shape-guard`
- `uv run python -m py_compile state/copilot_sdk_smoke_test.py`

## Files changed
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_013/01-task.md`
- `state/feature_iterations/iter_013/02-plan.md`
- `state/feature_iterations/iter_013/03-execution.md`
- `state/feature_iterations/iter_013/04-validation.md`
- `state/feature_iterations/iter_013/05-risks-and-decisions.md`
- `state/feature_iterations/iter_013/06-next-iteration.md`
- `state/feature_iterations/iter_013/07-summary.md`

## Rationale
- Implemented the smallest unfinished backlog task from `iter_012`.
- Kept the diff minimal by adding one deterministic guard mode and wiring existing CLI surfaces.
