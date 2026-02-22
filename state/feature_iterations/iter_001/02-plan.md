# Plan

1. Capture current harness constraints from `DEVELOPMENT.md` and core files:
   - `state/kernel.py`
   - `state/role_io_templates.py`
   - `state/copilot_sdk_uv_smoke.py`
   - `evals/chapter-quality.yaml`
   - `evals/style-guard.yaml`
   - `evals/drift-detection.yaml`
2. Define feature backlog slices for later implementation iterations:
   - richer kernel trace summaries and deterministic decision metadata in `state/kernel.py`,
   - clearer role I/O scaffold contracts and validation flags in `state/role_io_templates.py`,
   - expanded smoke modes plus harness-level assertions in `state/copilot_sdk_uv_smoke.py`.
3. Define test strategy for each slice:
   - targeted smoke modes via `uv run python state/copilot_sdk_uv_smoke.py --mode ...`,
   - focused unit coverage for pure helper paths in `state/kernel.py` and template generation logic.
4. Define evaluation strategy:
   - map new signals and regressions to existing eval contracts in `evals/*.yaml`,
   - ensure outputs can be traced through `state/metrics.json` and iteration artifacts.
5. Produce a single concrete next task in `06-next-iteration.md` for immediate implementation.
