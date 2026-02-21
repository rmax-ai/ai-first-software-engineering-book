# Execution

## Commands/tools run
- Read guidance: `state/migration_iterations/iter_028/06-next-iteration.md`
- Edited: `state/llm_client.py`
- Validation: `uv run python state/copilot_sdk_smoke_test.py --mode stub && uv run python state/copilot_sdk_smoke_test.py --mode sdk-unavailable`

## Files changed
- `state/llm_client.py`
  - Added bounded startup wait (`1s..10s`, capped by `timeout_s`).
  - Added explicit bootstrap timeout/error/loop-missing error mapping to `LLMClientError`.
- `state/migration_iterations/iter_029/01-task.md`
- `state/migration_iterations/iter_029/02-plan.md`
- `state/migration_iterations/iter_029/03-execution.md`
- `state/migration_iterations/iter_029/04-validation.md`
- `state/migration_iterations/iter_029/05-risks-and-decisions.md`
- `state/migration_iterations/iter_029/06-next-iteration.md`
- `state/migration_iterations/iter_029/07-summary.md`

## Short rationale per change
The bootstrap path previously blocked indefinitely on thread readiness and could fail with opaque exceptions; this iteration makes startup deterministic and stage-labeled.
