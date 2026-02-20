# Plan

1. Update `run_kernel(...)` to wrap the main execution path in `try/finally`.
2. Add bounded cleanup logic in `finally` (`close()` then `stop()` fallback).
3. Run targeted syntax validation for touched Python modules.
4. Record execution and handoff artifacts for the next iteration.

## Files expected to change
- `state/kernel.py`
- `state/migration_iterations/iter_002/*.md`
