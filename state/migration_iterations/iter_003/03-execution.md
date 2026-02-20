# Execution

## Commands/tools run
1. `apply_patch` on `state/llm_client.py` to add guarded SDK bridge + fallback routing.
2. `python -m py_compile state/llm_client.py state/kernel.py`

## Files changed
- `state/llm_client.py`
  - Added guarded SDK routing for non-mock providers in `chat(...)`.
  - Added lazy SDK client/session lifecycle fields and async bridge helper.
  - Added SDK response normalization into existing `LLMResponse/LLMUsage` shape.
  - Extended `close()` to stop/force-stop SDK client when initialized.

## Rationale per change
- Keep migration surface minimal by preserving existing public API and legacy provider methods.
- Ensure fallback behavior remains available when SDK module is disabled/missing.
