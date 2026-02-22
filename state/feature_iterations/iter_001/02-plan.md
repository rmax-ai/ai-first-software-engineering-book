# Plan

1. Review governance and implementation guidance in `DEVELOPMENT.md` and `prompts/incremental-improvements/execute.md`.
2. Define harness feature backlog items focused on deterministic behavior, observability, and execution controls:
   - richer phase/step trace summaries in `state/kernel.py`
   - clearer role I/O schema scaffolds in `state/role_io_templates.py`
   - expanded smoke-mode coverage and assertions in `state/copilot_sdk_uv_smoke.py`
3. Map each feature item to tests:
   - targeted unit tests for parser/validator helpers in `state/`
   - smoke coverage via `uv run python state/copilot_sdk_uv_smoke.py --mode ...`
4. Map each feature item to eval impact:
   - confirm compatibility with `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml`
   - define expected signal updates in `state/metrics.json` and iteration evidence docs
5. Capture risks/decisions and recommend exactly one next implementation task with concrete acceptance criteria.

## Expected files to change in later iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
- `state/copilot_sdk_smoke_test.py` (if smoke matrix coverage expands)
