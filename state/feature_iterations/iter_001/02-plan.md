# Plan

1. Baseline current harness contracts from `DEVELOPMENT.md`, `state/kernel.py`, `state/role_io_templates.py`, and `state/copilot_sdk_uv_smoke.py`.
2. Define feature backlog items for deterministic execution controls and observability:
   - richer phase/budget tracing in `state/kernel.py`
   - clearer role-input/output scaffolds in `state/role_io_templates.py`
   - stronger trace-summary and failure-mode coverage in `state/copilot_sdk_uv_smoke.py`
3. Define test strategy:
   - targeted smoke modes via `uv run python state/copilot_sdk_uv_smoke.py --mode <mode>`
   - focused unit-style checks for parser/trace helpers in `state/kernel.py` (new tests under `state/` if introduced)
4. Define evaluation strategy:
   - map behavior signals to `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml`
   - document expected metric/trace deltas in `state/metrics.json` and iteration validation notes
5. Capture risks, sequencing, and one smallest next implementation task.

## Expected files to change in future iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
- Optional new targeted harness tests under `state/`
