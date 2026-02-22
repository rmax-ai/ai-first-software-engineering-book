# Plan

1. Baseline harness contracts in `DEVELOPMENT.md` and map concrete extension points in `state/kernel.py`, `state/role_io_templates.py`, and `state/copilot_sdk_uv_smoke.py`.
2. Define feature backlog for `state/kernel.py`:
   - richer deterministic trace logging checkpoints,
   - clearer execution-budget visibility and failure surfaces,
   - explicit role I/O handshake signals for planner/writer/critic flow.
3. Define scaffold improvements for `state/role_io_templates.py`:
   - normalize role input/output blocks,
   - make template fields explicit for traceability and replayability.
4. Define smoke-test expansion in `state/copilot_sdk_uv_smoke.py`:
   - add focused scenarios proving new trace and role-IO behavior,
   - keep smoke cases deterministic under `uv run python ...`.
5. Define eval alignment updates in `evals/*.yaml`:
   - capture new observability and determinism expectations,
   - tie checks to measurable signals (including `state/metrics.json` impacts when applicable).
6. Prepare implementation sequence for future iterations:
   - first add kernel logging/control primitives,
   - then align role templates,
   - then expand smoke coverage,
   - finally tighten eval gates and reconcile expected outputs.
7. Validate this plan document set for completeness against `prompts/incremental-improvements/execute.md` and `DEVELOPMENT.md`.

## Expected files to change in later iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
