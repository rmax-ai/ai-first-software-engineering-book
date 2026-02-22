# Execution

## Commands/tools run
- `view prompts/incremental-improvements/execute.md`
- `view DEVELOPMENT.md`
- `view state/feature_iterations/iter_074/06-next-iteration.md`
- `apply_patch state/copilot_sdk_smoke_test.py` (extract helper + tuple callsite migration)
- `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-fixture-cleanup-parity-mode-choices-usage-examples-uniqueness-adjacency-guard`
- `uv run python state/copilot_sdk_smoke_test.py --mode mode-choices-coverage-guard`

## Files changed
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_075/01-task.md`
- `state/feature_iterations/iter_075/02-plan.md`
- `state/feature_iterations/iter_075/03-execution.md`
- `state/feature_iterations/iter_075/04-validation.md`
- `state/feature_iterations/iter_075/05-risks-and-decisions.md`
- `state/feature_iterations/iter_075/06-next-iteration.md`
- `state/feature_iterations/iter_075/07-summary.md`

## Short rationale per change
- Centralized parity target mode names to eliminate duplicated literals across parity guard modes.
- Kept assertions and mode wiring unchanged to preserve deterministic behavior while reducing maintenance risk.
- Captured complete iteration evidence in the seven required artifacts.
