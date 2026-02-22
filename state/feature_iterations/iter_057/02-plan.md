# Plan

1. Extend trace-summary fixture generation to optionally emit malformed `phase_trace` payload data.
2. Add a new deterministic smoke mode that expects and validates `phase_trace` schema failure.
3. Keep existing trace-summary success path unchanged.
4. Run targeted smoke commands for both success and malformed modes and document outputs.

## Files expected to change
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_057/*.md`
