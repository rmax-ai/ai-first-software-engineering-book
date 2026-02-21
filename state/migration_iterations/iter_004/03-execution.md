# Execution

## Commands/tools run
1. `apply_patch` on `state/llm_client.py` to add SDK usage extraction helpers.
2. `python -m py_compile state/llm_client.py state/kernel.py`
3. Inline Python smoke check validating direct usage and event usage aggregation.

## Files changed
- `state/llm_client.py`
  - Updated `_normalize_sdk_response(...)` to centralize usage extraction.
  - Added `_extract_sdk_usage(...)` to aggregate `assistant.usage` events.
  - Added `_usage_from_any(...)` to normalize token fields across usage shapes.

## Rationale per change
- Keeps migration scope minimal while hardening accounting behavior requested by the prior iteration.
- Preserves existing public interfaces and mock/legacy routing.
