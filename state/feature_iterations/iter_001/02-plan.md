# Iteration plan

1. Audit current harness responsibilities from `DEVELOPMENT.md` and identify planning surfaces in:
   - `state/kernel.py`
   - `state/role_io_templates.py`
   - `state/copilot_sdk_uv_smoke.py`
   - `evals/*.yaml`
2. Define a features backlog for upcoming iterations:
   - Structured trace logging and per-phase timing in `state/kernel.py`.
   - Stronger role-IO template validation and schema checks in `state/role_io_templates.py`.
   - Deterministic smoke coverage expansion in `state/copilot_sdk_uv_smoke.py` for new harness invariants.
3. Define tests by surface:
   - Add focused kernel unit tests for new trace/timing helpers.
   - Extend smoke modes in `state/copilot_sdk_uv_smoke.py` to validate deterministic behaviors.
   - Add/adjust assertions for role-IO template contract checks.
4. Define evaluation integration:
   - Map each feature to expected checks in `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml`.
   - Require metrics deltas to be recorded in `state/metrics.json` for added signals.
5. Set the next single executable task to implement kernel trace summary hardening first, because it unlocks observability for subsequent work.

## Files expected to change in later iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
- `state/metrics.json`
