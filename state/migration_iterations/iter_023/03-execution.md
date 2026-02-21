# Execution

## Commands/tools run
- `python -m py_compile state/llm_client.py state/copilot_sdk_smoke_test.py`
- `python state/copilot_sdk_smoke_test.py --mode fallback-connection-error`
- `python state/copilot_sdk_smoke_test.py --mode fallback`
- `python state/copilot_sdk_smoke_test.py --mode fallback-error`
- `python state/copilot_sdk_smoke_test.py --mode fallback-invalid-json`

## Files changed
- `state/copilot_sdk_smoke_test.py`

## Short rationale per change
- Added `fallback-connection-error` mode that monkeypatches fallback transport to raise `URLError`, ensuring deterministic coverage for connection-failure mapping.
- Wired the new mode through CLI choices/help and mode dispatch.
