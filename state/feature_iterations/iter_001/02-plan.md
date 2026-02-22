# Plan

1. Review `DEVELOPMENT.md` and align improvements with deterministic, modular harness constraints.
2. Define feature backlog slices:
   - richer trace/decision logging in `state/kernel.py`
   - clearer role I/O template scaffolding in `state/role_io_templates.py`
   - deterministic smoke coverage extensions in `state/copilot_sdk_uv_smoke.py`
3. Define proof strategy:
   - targeted deterministic smoke modes via `uv run python state/copilot_sdk_uv_smoke.py ...`
   - focused kernel/unit checks for pure helpers and orchestration boundaries
4. Define eval regression wiring:
   - map expected signals to `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml`
   - ensure planned outputs remain observable through `state/metrics.json` and iteration artifacts
5. Sequence next implementation iteration to deliver the smallest high-value logging feature first, with explicit validation commands.

## Files expected to change in later iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
- harness test assets under `state/` or `book/` as needed
