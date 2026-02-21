# Execution

## Commands/tools run
- `python -m py_compile state/llm_client.py state/copilot_sdk_smoke_test.py`
- `python state/copilot_sdk_smoke_test.py --mode stub`
- `python state/copilot_sdk_smoke_test.py --mode fallback`
- `python state/copilot_sdk_smoke_test.py --mode fallback-error`
- `python state/copilot_sdk_smoke_test.py --mode fallback-invalid-json`
- `for i in $(seq 1 10); do python state/copilot_sdk_smoke_test.py --mode fallback-error >/dev/null; done`

## Files changed
- `state/copilot_sdk_smoke_test.py`

## Short rationale per change
- Consumed inbound POST request bytes in fallback error-path handlers before sending responses to avoid intermittent socket-level resets in repeated local runs.
