# Execution

## Commands/tools run
- `view DEVELOPMENT.md`
- `view state/feature_iterations/iter_062/06-next-iteration.md`
- `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-kernel`
- `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-kernel-malformed-phase`
- `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-kernel-malformed-phase-payload`
- `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-kernel-missing-phase`
- `uv run python state/copilot_sdk_smoke_test.py --mode mode-choices-coverage-guard`
- `uv run python state/copilot_sdk_smoke_test.py --mode docstring-mode-coverage-guard`

## Files changed
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_063/01-task.md`
- `state/feature_iterations/iter_063/02-plan.md`
- `state/feature_iterations/iter_063/03-execution.md`
- `state/feature_iterations/iter_063/04-validation.md`
- `state/feature_iterations/iter_063/05-risks-and-decisions.md`
- `state/feature_iterations/iter_063/06-next-iteration.md`
- `state/feature_iterations/iter_063/07-summary.md`

## Rationale per change
- Added fixture-backed kernel-run modes to deterministic smoke coverage so runtime trace-summary behavior is checked without manual command execution.
- Centralized subprocess execution and output assertions in `_run_trace_summary_kernel_mode` to keep malformed-mode checks consistent.
- Added explicit ledger immutability assertion around every kernel-backed run to enforce no mutation to repository `state/ledger.json`.
