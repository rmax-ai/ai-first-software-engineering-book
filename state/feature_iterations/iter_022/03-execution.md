# Execution

## Commands/tools run
- `view prompts/incremental-improvements/execute.md`
- `view DEVELOPMENT.md`
- `view state/feature_iterations/iter_021/{01-task,02-plan,04-validation,06-next-iteration,07-summary}.md`
- `uv run python state/copilot_sdk_smoke_test.py --mode stub` (baseline)
- Edited `state/copilot_sdk_smoke_test.py` to add `usage-examples-duplicates-guard`
- `uv run python state/copilot_sdk_smoke_test.py --mode stub`
- `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicates-guard`

## Files changed
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_022/01-task.md`
- `state/feature_iterations/iter_022/02-plan.md`
- `state/feature_iterations/iter_022/03-execution.md`
- `state/feature_iterations/iter_022/04-validation.md`
- `state/feature_iterations/iter_022/05-risks-and-decisions.md`
- `state/feature_iterations/iter_022/06-next-iteration.md`
- `state/feature_iterations/iter_022/07-summary.md`

## Rationale per change
- Added a deterministic duplicates guard mode to prevent repeated generated usage command lines.
- Registered the new mode in shared mode specs so parser choices/help/doc generation remain centralized.
- Captured iteration artifacts to preserve verifiable evidence and a single next backlog step.
