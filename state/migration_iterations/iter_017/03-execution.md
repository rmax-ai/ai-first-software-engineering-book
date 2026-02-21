# Execution

## Commands/tools run
- `view state/migration_iterations/iter_016/06-next-iteration.md`
- `view state/copilot-sdk-migration-plan.md`
- Edited `state/copilot_sdk_smoke_test.py` to add stub `send_and_wait` + `get_messages` fallback events.
- `uv run python state/copilot_sdk_smoke_test.py`

## Files changed
- `state/copilot_sdk_smoke_test.py`

## Rationale per change
- Added an event-style stub response (`assistant.message`) without embedded usage.
- Added usage-only fallback events (`assistant.usage`) so `LLMClient` must recover usage from session events.
- Kept existing content/usage assertions to verify behavior without changing public interfaces.
