# Next Iteration Recommendation

## Recommended next task
Wire bounded LLM client teardown into `run_kernel(...)` via `finally`.

## Why this is next
The close hook now exists; the next smallest step is to guarantee shutdown on success and failure paths.

## Acceptance criteria
- `state/kernel.py` ensures cleanup in a `finally` block when LLM mode is enabled.
- Cleanup attempts `close()` (and/or `stop()` fallback) without changing planner/writer/critic behavior.
- Existing kernel return codes and error mapping remain unchanged.

## Expected files to touch
- `state/kernel.py`
- `state/migration_iterations/iter_002/*.md`

