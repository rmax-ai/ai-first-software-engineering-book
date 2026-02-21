# Next Iteration Recommendation

## Recommended next task
Add explicit SDK session teardown in `LLMClient.close()` by invoking `session.destroy()` (when available) before client shutdown.

## Why it is next
M2 still targets no leaked runtime state across repeated runs; explicit session teardown is the next smallest hardening step.

## Concrete acceptance criteria
- `close()` calls session `destroy()` when a session exists and the method is available.
- Session teardown errors are mapped to actionable `LLMClientError` messages.
- Existing stop/force-stop fallback behavior remains intact.

## Expected files to touch
- `state/llm_client.py`
- `state/migration_iterations/iter_007/*.md`
