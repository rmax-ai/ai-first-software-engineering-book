# Plan

1. Baseline harness touchpoints and constraints from:
   - `DEVELOPMENT.md`
   - `state/kernel.py`
   - `state/role_io_templates.py`
   - `state/copilot_sdk_uv_smoke.py`
   - `evals/chapter-quality.yaml`
   - `evals/style-guard.yaml`
   - `evals/drift-detection.yaml`
2. Define feature backlog for deterministic harness improvements:
   - richer kernel trace summary fields and explicit failure metadata in `state/kernel.py`.
   - clearer role IO template coverage and invariants in `state/role_io_templates.py`.
   - stronger UV smoke assertions and mode coverage in `state/copilot_sdk_uv_smoke.py`.
3. Define test strategy:
   - targeted unit tests for pure helpers introduced/expanded in `state/kernel.py`.
   - deterministic smoke invocations using `uv run python state/copilot_sdk_uv_smoke.py --mode ...`.
   - fixture-driven checks for template/render contract updates.
4. Define evaluation strategy:
   - map each planned feature to expected signals in `evals/*.yaml`.
   - ensure iteration validation captures command outputs and expected guard behavior.
   - require regression evidence aligned with `state/metrics.json` trend consistency.
5. Sequence future execution into smallest tasks, one per iteration:
   - trace schema enhancement and tests.
   - role template contract hardening and tests.
   - UV smoke expansion and eval wiring checks.

## Expected files to change in future iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
- targeted test assets under `state/` and/or `book/` as required.
