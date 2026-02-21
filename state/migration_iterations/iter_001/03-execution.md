# Execution

## Commands/tools run
- `apply_patch` to update `state/llm_client.py`
- `python3 -m py_compile state/llm_client.py`
- Python smoke check invoking `LLMClient(provider='mock', model='mock').close()`

## Files changed
- `state/llm_client.py`
  - Added `LLMClient.close()` compatibility hook to support future kernel-side teardown.

## Rationale
Introduces the smallest lifecycle surface needed for migration without altering current request paths.

