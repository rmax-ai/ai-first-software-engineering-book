# Task

## Selected task title
Add bounded startup timeout and explicit bootstrap error mapping for SDK worker-loop startup in `LLMClient`.

## Why this task now
`state/migration_iterations/iter_028/06-next-iteration.md` prioritized deterministic bootstrap failures for the nested-loop SDK bridge.

## Acceptance criteria for this iteration
- `_ensure_sdk_thread_loop` uses a bounded wait.
- Bootstrap failures/timeouts raise `LLMClientError` with clear stage context.
- Existing smoke checks (`stub`, `sdk-unavailable`) pass.
