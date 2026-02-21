# Execution

## Commands/tools run
- `apply_patch` on `state/copilot_sdk_smoke_test.py` to add mode `stop-unavailable-destroy-failure-close-idempotency` and CLI wiring.
- `uv run python state/copilot_sdk_smoke_test.py --mode stop-unavailable-destroy-failure-close-idempotency`
- Deterministic non-live matrix:
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
  - `stop-unavailable-destroy-failure-close-idempotency`
  - `stop-failure-destroy-unavailable-close-idempotency`
  - `stop-failure-destroy-failure-close-idempotency`

## Files changed
- `state/copilot_sdk_smoke_test.py`
- `state/migration_iterations/iter_045/01-task.md`
- `state/migration_iterations/iter_045/02-plan.md`
- `state/migration_iterations/iter_045/03-execution.md`
- `state/migration_iterations/iter_045/04-validation.md`
- `state/migration_iterations/iter_045/05-risks-and-decisions.md`
- `state/migration_iterations/iter_045/06-next-iteration.md`
- `state/migration_iterations/iter_045/07-summary.md`

## Change rationale
- Covered the mixed shutdown branch where `stop()` is unavailable while `session.destroy()` fails.
- Preserved existing smoke-test structure by mirroring nearby close-idempotency mode patterns.
