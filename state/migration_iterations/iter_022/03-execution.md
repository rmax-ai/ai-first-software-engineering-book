# Execution

## Commands/tools run
- `python -m py_compile state/llm_client.py state/copilot_sdk_smoke_test.py`
- `uv run python state/copilot_sdk_smoke_test.py --mode stub`
- `uv run python state/copilot_sdk_smoke_test.py --mode fallback`
- `uv run python state/copilot_sdk_smoke_test.py --mode fallback-error`
- `uv run python state/copilot_sdk_smoke_test.py --mode fallback-invalid-json`
- `for i in $(seq 1 10); do uv run python state/copilot_sdk_smoke_test.py --mode fallback-error >/dev/null; done`

## Files changed
- `state/copilot_sdk_smoke_test.py`

## Short rationale per change
- Consumed inbound POST request bytes in fallback error-path handlers before sending responses to avoid intermittent socket-level resets in repeated local runs.
