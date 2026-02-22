# Plan

1. Define the harness feature backlog with emphasis on deterministic controls and observability.
2. Break future implementation into targeted edits for:
   - `state/kernel.py` (trace/logging and deterministic execution controls)
   - `state/role_io_templates.py` (clearer role input/output scaffolds)
   - `state/copilot_sdk_uv_smoke.py` (smoke coverage for new harness behavior)
   - `evals/*.yaml` (regression gates aligned to the new behavior)
3. Specify verification commands for each future change, centered on `uv run python state/copilot_sdk_uv_smoke.py` and targeted kernel runs.
4. Define rollout order to keep diffs small: kernel feature first, then role I/O template updates, then smoke/eval expansion.

## Files expected to change in future iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
