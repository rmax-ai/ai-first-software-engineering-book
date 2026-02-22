# Plan

1. **Inventory harness surfaces**
   - Re-read `DEVELOPMENT.md` and current `state/` helpers to keep planned changes consistent with UV-first execution and deterministic guardrails.
2. **Define feature backlog slices**
   - `state/kernel.py`: add richer trace summary fields and stricter deterministic execution checks.
   - `state/role_io_templates.py`: tighten role I/O templates for clearer prompt/response contracts and observable handoff markers.
   - `state/copilot_sdk_uv_smoke.py`: extend smoke scenarios to cover new trace outputs and failure-path observability.
3. **Define tests for each slice**
   - Add/extend deterministic smoke modes in `state/copilot_sdk_smoke_test.py` for trace shape and role-IO constraints.
   - Keep command contracts on `uv run python state/copilot_sdk_smoke_test.py --mode <mode>`.
4. **Define evaluation integration**
   - Update relevant rules in `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and/or `evals/drift-detection.yaml` so regressions in harness signals are detected.
   - Ensure expected outputs remain reflected in `state/metrics.json` update pathways.
5. **Execution order for future iterations**
   - Start with kernel trace contract changes.
   - Then align smoke tests.
   - Finally wire eval gates and validate end-to-end with UV commands.

## Files expected to change in later iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/copilot_sdk_smoke_test.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
