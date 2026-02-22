# Execution

## Commands/tools run
- `view prompts/incremental-improvements/execute.md`
- `view DEVELOPMENT.md`
- `view state/feature_iterations/iter_058/06-next-iteration.md`
- `uv run python state/copilot_sdk_uv_smoke.py --mode trace-summary`
- `uv run python state/copilot_sdk_uv_smoke.py --mode trace-summary-malformed-phase`
- `uv run python state/copilot_sdk_uv_smoke.py --mode trace-summary-malformed-phase-payload`
- `uv run python state/copilot_sdk_uv_smoke.py --mode trace-summary-missing-phase`

## Files changed
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_059/01-task.md`
- `state/feature_iterations/iter_059/02-plan.md`
- `state/feature_iterations/iter_059/03-execution.md`
- `state/feature_iterations/iter_059/04-validation.md`
- `state/feature_iterations/iter_059/05-risks-and-decisions.md`
- `state/feature_iterations/iter_059/06-next-iteration.md`
- `state/feature_iterations/iter_059/07-summary.md`

## Short rationale per change
- Added a fixture toggle to omit `evaluation` phase traces and trigger deterministic required-phase validation.
- Added a dedicated CLI mode to exercise this new failure path without affecting existing modes.
- Captured iteration evidence and next-step handoff in the required seven artifacts.
