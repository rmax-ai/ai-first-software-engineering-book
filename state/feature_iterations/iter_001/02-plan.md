# Plan

1. Review harness guidance in `DEVELOPMENT.md` and prompt constraints in `prompts/incremental-improvements/execute.md`.
2. Define feature workstreams for:
   - Observability and trace controls in `state/kernel.py`.
   - Clearer role I/O scaffolds in `state/role_io_templates.py`.
   - Deterministic smoke coverage extensions in `state/copilot_sdk_uv_smoke.py`.
3. Define test strategy:
   - Add/extend focused harness tests in `state/` for new kernel/role-IO behavior.
   - Use `uv run python state/copilot_sdk_uv_smoke.py` scenarios for regression checks.
4. Define eval integration strategy:
   - Map planned behavior to `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml`.
   - Document expected signal changes and metrics checks (`state/metrics.json`).
5. Capture execution ordering for future iterations: implement smallest kernel logging slice first, then role-IO template constraints, then smoke/eval tightening.

## Expected files to change in future iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
- Targeted harness tests under `state/`
