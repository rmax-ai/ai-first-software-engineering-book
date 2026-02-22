# Plan

1. Add a small helper in `state/kernel.py` to emit normalized `phase_trace` entries with timing and budget metadata.
2. Instrument three deterministic phases in the kernel loop:
   - role output readiness
   - evaluation
   - state persistence
3. Extend `state/copilot_sdk_uv_smoke.py` trace-summary mode to assert the phase trace schema and required phase names.
4. Run targeted validation commands and capture evidence in this iteration folder.

## Files expected to change
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_055/*.md`
