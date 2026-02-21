# Task

## Selected task title
Add deterministic smoke coverage for Copilot SDK shutdown failure handling in `state/llm_client.py`.

## Why this task now
`state/migration_iterations/iter_030/06-next-iteration.md` prioritized shutdown reliability coverage after bootstrap-failure coverage landed.

## Acceptance criteria for this iteration
- `state/copilot_sdk_smoke_test.py` includes a `shutdown-failure` mode.
- The mode asserts `Copilot SDK shutdown failed:` context.
- The mode exercises both `stop()` and `force_stop()` failure paths.
- Existing `stub`, `sdk-unavailable`, and `bootstrap-failure` modes still pass.
