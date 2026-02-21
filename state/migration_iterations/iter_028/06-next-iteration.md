# Next Iteration

## Recommended next task
Add bounded startup timeout and explicit error mapping for SDK worker-loop bootstrap in `LLMClient`.

## Why it is next
The nested-loop bridge now works, but bootstrap failure handling can be made deterministic and actionable.

## Acceptance criteria
- `_ensure_sdk_thread_loop` uses a bounded wait and raises `LLMClientError` on startup failure/timeout.
- Failure message identifies bootstrap stage clearly.
- Existing smoke checks (`stub`, `sdk-unavailable`) remain passing.

## Expected files to touch
- `state/llm_client.py`
