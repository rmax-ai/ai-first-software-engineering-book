# Execution

## Commands/tools run
1. `view state/copilot_sdk_smoke_test.py`
2. `rg "timed out|timeout|fallback" state/llm_client.py`
3. `python -m py_compile state/copilot_sdk_smoke_test.py state/llm_client.py`
4. `uv run python state/copilot_sdk_smoke_test.py --mode fallback-timeout`

## Files changed
- `state/copilot_sdk_smoke_test.py`

## Short rationale per change
- Added `fallback-timeout` smoke mode to deterministically verify HTTP fallback timeout error mapping.
- Updated CLI mode choices/help/dispatch and top-level usage docs so the new mode is discoverable and runnable.
