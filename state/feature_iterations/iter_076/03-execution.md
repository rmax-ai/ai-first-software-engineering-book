# Execution

## Commands/tools run
- `view DEVELOPMENT.md`
- `view state/feature_iterations/iter_075/06-next-iteration.md`
- `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-fixture-cleanup-parity-mode-choices-usage-examples-adjacency-guard`
- `uv run python state/copilot_sdk_smoke_test.py --mode mode-choices-coverage-guard`

## Files changed
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_076/01-task.md`
- `state/feature_iterations/iter_076/02-plan.md`
- `state/feature_iterations/iter_076/03-execution.md`
- `state/feature_iterations/iter_076/04-validation.md`
- `state/feature_iterations/iter_076/05-risks-and-decisions.md`
- `state/feature_iterations/iter_076/06-next-iteration.md`
- `state/feature_iterations/iter_076/07-summary.md`

## Rationale per change
- Introduced `_mode_action_for_parser` to centralize `--mode` action lookup and assertion.
- Replaced repeated lookup boilerplate in parity guard modes with helper calls.
- Added iteration artifacts documenting task, plan, evidence, decisions, next step, and summary.
