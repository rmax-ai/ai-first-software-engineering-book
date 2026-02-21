# Execution

## Commands/tools run
- `python -m py_compile state/llm_client.py state/copilot_sdk_smoke_test.py`
- `uv run python state/copilot_sdk_smoke_test.py --mode stub`
- `uv run python state/copilot_sdk_smoke_test.py --mode fallback`

## Files changed
- `state/copilot_sdk_smoke_test.py`

## Rationale
- Added a committed fallback mode to exercise HTTP fallback deterministically.
- Used a local stdlib HTTP server to avoid network dependencies.
- Forced `copilot` import failure in-test to ensure fallback path executes.
