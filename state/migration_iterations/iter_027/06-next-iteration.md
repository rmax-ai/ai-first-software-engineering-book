# Next Iteration

## Recommended next task
Refactor `LLMClient._run_async` to avoid creating ad-hoc event loops when already inside a running loop, and document the lifecycle guarantee.

## Why it is next
The migration now has SDK-only routing and cleaned smoke scaffolding; the next reliability hotspot is async/sync bridging in nested-loop environments.

## Acceptance criteria
- `_run_async` handles running-loop contexts without creating unsafe side loops.
- Existing synchronous `chat(...)` public API remains unchanged.
- Smoke checks (`stub`, `sdk-unavailable`) still pass.

## Expected files to touch
- `state/llm_client.py`
- `state/copilot_sdk_smoke_test.py` (only if test updates are required)
