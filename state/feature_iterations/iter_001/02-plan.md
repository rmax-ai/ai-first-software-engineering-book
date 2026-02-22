# Iteration plan

1. Audit current harness touchpoints in `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, and `evals/*.yaml` to anchor realistic follow-up work.
2. Define feature backlog items:
   - richer trace logging and deterministic phase accounting in `state/kernel.py`;
   - clearer role I/O scaffolds and placeholder validation in `state/role_io_templates.py`;
   - expanded smoke modes and failure diagnostics in `state/copilot_sdk_uv_smoke.py`.
3. Define test backlog items:
   - add/extend targeted smoke modes in `state/copilot_sdk_uv_smoke.py`;
   - run `uv run python state/copilot_sdk_uv_smoke.py` for regression coverage;
   - add focused unit tests for pure helper logic introduced in kernel/template modules.
4. Define eval backlog items:
   - map planned behavior checks into `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml`;
   - ensure signals can be reconciled with `state/metrics.json` and iteration validation artifacts.
5. Sequence next implementation iteration to deliver the smallest high-value slice: trace summary observability in kernel plus matching smoke/eval updates.

## Files expected to change (future iterations)
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
- `state/metrics.json` (only when behavior/output schema changes)
