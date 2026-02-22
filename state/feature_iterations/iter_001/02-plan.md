# Plan

1. Inventory current harness surfaces in `state/` and identify gaps in trace visibility, role IO consistency, and deterministic execution controls.
2. Propose feature work for:
   - `state/kernel.py`: richer trace-summary telemetry and stricter loop-level guard checks.
   - `state/role_io_templates.py` and `state/role_io/`: clearer role input/output scaffold parity checks.
   - `state/copilot_sdk_uv_smoke.py`: smoke modes proving new telemetry and guard behavior.
3. Map future verification:
   - Script-level checks via `uv run python state/copilot_sdk_uv_smoke.py`.
   - Focused kernel execution checks via `uv run python state/kernel.py --chapter-id <id>`.
4. Map eval regression detection to `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml`, plus metrics verification in `state/metrics.json`.
5. Write follow-up iteration task that implements the smallest high-leverage slice first (trace-summary coverage guard wiring).

## Files expected to change in future implementation iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
- `state/metrics.json`
