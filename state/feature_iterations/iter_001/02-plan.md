# Plan

1. Review current harness contracts in `DEVELOPMENT.md`, `state/kernel.py`, and existing eval definitions under `evals/`.
2. Define feature backlog slices for later implementation:
   - richer phase-trace observability and deterministic trace summaries in `state/kernel.py`
   - clearer role scaffolding and validation hooks in `state/role_io_templates.py`
   - smoke-mode coverage and regression guards in `state/copilot_sdk_uv_smoke.py`
3. Map each feature slice to targeted tests:
   - focused unit coverage for parsing/validation helpers in `state/kernel.py`
   - smoke invocations via `uv run python state/copilot_sdk_uv_smoke.py --mode <mode>`
   - fixture/assertion updates for new trace guard paths
4. Map each feature slice to eval signals:
   - align with `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml`
   - ensure metrics/trace outputs remain compatible with existing deterministic gates
5. Capture one immediate follow-up implementation task in `06-next-iteration.md` with concrete acceptance criteria and touched files.

## Files expected to change in later iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
