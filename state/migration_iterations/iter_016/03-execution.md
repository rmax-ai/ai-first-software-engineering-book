# Execution

## Commands/tools run
- Read migration source of truth: `state/copilot-sdk-migration-plan.md`
- Inspected implementation: `state/llm_client.py`, `state/kernel.py`, `state/copilot_sdk_smoke_test.py`
- Applied minimal patch to `state/llm_client.py`

## Files changed
- `state/llm_client.py`

## Change rationale
- In `_normalize_sdk_session_result`, when `assistant.message` has no usage payload, the client now fetches `session.get_messages()` and reuses `_response_from_sdk_events(...)` to extract usage.
- This preserves existing response content while backfilling usage counters from event stream data.
