# Task

## Selected task title
Wire bounded LLM client teardown into `run_kernel(...)` via `finally`.

## Why this task now
`iter_001` explicitly recommended this as the next smallest migration step after adding `LLMClient.close()`.

## Acceptance criteria
- `state/kernel.py` always attempts LLM cleanup in a `finally` block when LLM is initialized.
- Cleanup uses `close()` and falls back to `stop()` when `close()` is unavailable.
- Existing kernel flow/return behavior for planner-writer-critic remains unchanged.
