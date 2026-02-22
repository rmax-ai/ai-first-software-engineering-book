# Next iteration

## Recommended next task
Add deterministic smoke coverage for missing required `phase_trace` phases (e.g., `evaluation`) in fixture mode.

## Why it is next
Current guards validate payload shape and keys, but explicit phase-presence failure coverage will close a remaining trace-summary schema gap.

## Concrete acceptance criteria
1. Add a deterministic fixture path that omits one required `phase_trace` phase and asserts expected failure text.
2. Keep `trace-summary`, `trace-summary-malformed-phase`, and `trace-summary-malformed-phase-payload` green.
3. Record command evidence in `iter_059/04-validation.md`.

## Expected files to touch
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_059/*.md`
