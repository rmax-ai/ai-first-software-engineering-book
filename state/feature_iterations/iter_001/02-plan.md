# Plan

1. Review governance and harness guidance (`AGENTS.md`, `DEVELOPMENT.md`) to constrain scope and validation style.
2. Define feature backlog slices:
   - `state/kernel.py`: richer deterministic phase tracing, tighter budget failure diagnostics, explicit guardrail reason codes.
   - `state/role_io_templates.py`: clearer role I/O scaffolds with normalized sections for reproducible parsing.
   - `state/copilot_sdk_uv_smoke.py`: table-driven smoke expansion for new harness controls and failure-shape assertions.
3. Define test strategy:
   - Add/extend targeted unit tests around parser/validator helpers in `state/`.
   - Extend smoke checks with `uv run python state/copilot_sdk_uv_smoke.py` mode coverage for planned behaviors.
4. Define evaluation strategy:
   - Map each planned behavior to checks in `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml`.
   - Require measurable signals in harness outputs (ledger fields and `state/metrics.json`) to detect regressions.
5. Sequence future execution:
   - Iteration N+1: implement kernel trace + diagnostics feature with targeted tests.
   - Iteration N+2: update role I/O templates and parser compatibility checks.
   - Iteration N+3: extend smoke/eval gates and finalize regression criteria.

## Files expected to change in later iterations

- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
- `state/metrics.json` (only if signal schema changes are required)
