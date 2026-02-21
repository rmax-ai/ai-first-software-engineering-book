# Execution

## Commands/tools run
- `apply_patch` on `state/copilot_sdk_smoke_test.py` to add mode and assertions.
- `uv run python state/copilot_sdk_smoke_test.py --mode stub`
- `uv run python state/copilot_sdk_smoke_test.py --mode sdk-unavailable`
- `uv run python state/copilot_sdk_smoke_test.py --mode bootstrap-failure`
- `uv run python state/copilot_sdk_smoke_test.py --mode shutdown-failure`
- `uv run python state/copilot_sdk_smoke_test.py --mode stop-unavailable`
- `uv run python state/copilot_sdk_smoke_test.py --mode destroy-failure`

## Files changed
- `state/copilot_sdk_smoke_test.py`
- `state/migration_iterations/iter_033/01-task.md`
- `state/migration_iterations/iter_033/02-plan.md`
- `state/migration_iterations/iter_033/03-execution.md`
- `state/migration_iterations/iter_033/04-validation.md`
- `state/migration_iterations/iter_033/05-risks-and-decisions.md`
- `state/migration_iterations/iter_033/06-next-iteration.md`
- `state/migration_iterations/iter_033/07-summary.md`

## Rationale per change
- Added deterministic coverage for the `stop() unavailable` shutdown branch so shutdown error aggregation remains regression-safe.
- Updated smoke CLI docs/routing so this branch is directly testable via `--mode stop-unavailable`.
