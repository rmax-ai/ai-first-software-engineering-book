# Execution

## Commands/tools run
- `uv run python state/copilot_sdk_smoke_test.py --mode stub`
- `uv run python state/copilot_sdk_smoke_test.py --mode sdk-unavailable`
- Patch edits in:
  - `state/llm_client.py`
  - `state/copilot_sdk_smoke_test.py`

## Files changed
- `state/llm_client.py`: removed unused `urllib` imports and `_chat_copilot_http` fallback method.
- `state/copilot_sdk_smoke_test.py`: removed fallback-only helper functions and now-unused imports.
- `state/migration_iterations/iter_027/01-task.md`
- `state/migration_iterations/iter_027/02-plan.md`
- `state/migration_iterations/iter_027/03-execution.md`
- `state/migration_iterations/iter_027/04-validation.md`
- `state/migration_iterations/iter_027/05-risks-and-decisions.md`
- `state/migration_iterations/iter_027/06-next-iteration.md`
- `state/migration_iterations/iter_027/07-summary.md`

## Short rationale per change
Both runtime and smoke scaffolding now match the SDK-only migration state, reducing dead code and maintenance ambiguity.
