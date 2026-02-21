# Execution

## Commands/tools run
- `apply_patch` on `state/copilot_sdk_smoke_test.py` to add the dual-failure close-idempotency mode and CLI wiring.
- Task agent command to run `python state/copilot_sdk_smoke_test.py --mode stop-failure-destroy-failure-close-idempotency`.
- Task agent command to run deterministic non-live smoke matrix:
  - `stub`
  - `sdk-unavailable`
  - `bootstrap-failure`
  - `shutdown-failure`
  - `stop-unavailable`
  - `destroy-unavailable`
  - `destroy-failure`
  - `force-stop-unavailable`
  - `force-stop-close-idempotency`
  - `stop-close-idempotency`
  - `close-idempotency`
  - `destroy-close-idempotency`
  - `destroy-unavailable-close-idempotency`
  - `stop-destroy-unavailable-close-idempotency`
  - `stop-failure-destroy-unavailable-close-idempotency`
  - `stop-failure-destroy-failure-close-idempotency`

## Files changed
- `state/copilot_sdk_smoke_test.py`
- `state/migration_iterations/iter_044/01-task.md`
- `state/migration_iterations/iter_044/02-plan.md`
- `state/migration_iterations/iter_044/03-execution.md`
- `state/migration_iterations/iter_044/04-validation.md`
- `state/migration_iterations/iter_044/05-risks-and-decisions.md`
- `state/migration_iterations/iter_044/06-next-iteration.md`
- `state/migration_iterations/iter_044/07-summary.md`

## Change rationale
- Added coverage for the final missing dual-failure shutdown branch while preserving existing smoke-test structure.
- Kept the change minimal by following the existing mode pattern and assertions used in nearby idempotency tests.
