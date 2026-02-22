# Execution

## Commands/tools run
- `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary`
- `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-missing-entry-guard`
- `uv run python state/copilot_sdk_smoke_test.py --mode stop-close-idempotency`
- `uv run python -m py_compile state/copilot_sdk_smoke_test.py`

## Files changed
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_014/01-task.md`
- `state/feature_iterations/iter_014/02-plan.md`
- `state/feature_iterations/iter_014/03-execution.md`
- `state/feature_iterations/iter_014/04-validation.md`
- `state/feature_iterations/iter_014/05-risks-and-decisions.md`
- `state/feature_iterations/iter_014/06-next-iteration.md`
- `state/feature_iterations/iter_014/07-summary.md`

## Rationale per change
- `state/copilot_sdk_smoke_test.py`: replaced repeated trace-summary mode wiring with one table-driven mapping used for choices/help/dispatch.
- Iteration docs: captured task, plan, validation evidence, and follow-up backlog handoff.
