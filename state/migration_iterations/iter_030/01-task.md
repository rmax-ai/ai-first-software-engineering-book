# Task

## Selected task title
Add a deterministic smoke-test mode for SDK worker-loop bootstrap failure.

## Why this task now
`state/migration_iterations/iter_029/06-next-iteration.md` prioritized locking in new bootstrap error handling.

## Acceptance criteria for this iteration
- `state/copilot_sdk_smoke_test.py` adds one mode for bootstrap failure simulation.
- The mode asserts `Copilot SDK worker-loop bootstrap` error context.
- Existing `stub` and `sdk-unavailable` modes still pass.
