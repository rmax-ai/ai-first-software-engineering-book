# Plan

1. Baseline current harness flow in `state/kernel.py` and isolate where richer trace metadata and deterministic constraints should be surfaced.
2. Specify role I/O scaffold updates in `state/role_io_templates.py` so planner/writer/critic exchanges are easier to inspect and validate.
3. Define smoke-test additions in `state/copilot_sdk_uv_smoke.py` to assert new observability/control paths and failure behavior.
4. Map regression detection to `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml`, including expected signal changes in `state/metrics.json`.
5. Sequence implementation into minimal follow-up iterations: kernel trace schema first, then template wiring, then smoke/eval hardening.

## Expected files to change in later iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
- `state/metrics.json` (observed outputs, not manual edits unless needed)

