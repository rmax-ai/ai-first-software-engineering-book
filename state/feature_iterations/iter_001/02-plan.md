# Plan
1. Confirm iteration context from `DEVELOPMENT.md` and the execute prompt contract.
2. Define a feature backlog for deterministic harness behavior across:
   - `state/kernel.py` (execution controls, traceability, guard rails)
   - `state/role_io_templates.py` (clearer role I/O scaffolds)
   - `state/copilot_sdk_uv_smoke.py` (smoke coverage for new controls)
3. Map each planned feature to concrete tests and validation commands.
4. Map each planned feature to evaluation signals in `evals/*.yaml` and `state/metrics.json`.
5. Record risks, decisions, and one smallest recommended next implementation task.

## Expected files to change in later iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
