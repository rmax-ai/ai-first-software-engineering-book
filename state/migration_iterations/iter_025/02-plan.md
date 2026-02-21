# Plan

1. Extend smoke test CLI docs and mode choices with `fallback-non-object`.
2. Add `run_fallback_non_object_mode()` that:
   - forces Copilot SDK import failure,
   - serves a deterministic JSON list payload via local HTTP server,
   - asserts `LLMClientError` message includes `HTTP fallback returned non-object payload`.
3. Run targeted smoke validation for `stub` and `fallback-non-object`.

## Expected files to change
- `state/copilot_sdk_smoke_test.py`

