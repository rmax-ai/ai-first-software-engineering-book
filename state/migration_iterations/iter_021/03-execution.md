# Execution

## Commands/tools run
1. `python -m py_compile state/llm_client.py state/copilot_sdk_smoke_test.py`
2. `python state/copilot_sdk_smoke_test.py --mode stub`
3. `python state/copilot_sdk_smoke_test.py --mode fallback`
4. `python state/copilot_sdk_smoke_test.py --mode fallback-invalid-json`

## Files changed
- `state/copilot_sdk_smoke_test.py`

## Rationale per change
- Added `run_fallback_invalid_json_mode()` to exercise the fallback path against a non-JSON response body and assert actionable error mapping.
- Added CLI wiring (`--mode` choices/help/dispatch) and usage/mode docs for the new smoke mode.
