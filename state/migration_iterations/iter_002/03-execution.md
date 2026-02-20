# Execution

## Commands/tools run
- Python scripted edit to wrap `run_kernel(...)` body in `try/finally` and add teardown fallback.
- `python -m py_compile state/kernel.py state/llm_client.py`

## Files changed
- `state/kernel.py`
  - Wrapped `run_kernel(...)` execution path in `try/finally`.
  - Added teardown logic: `client.close()` with `client.stop()` fallback.

## Rationale
This is the smallest change that guarantees cleanup on both success and failure paths without changing the public kernel CLI contract.
