# Plan

1. Inspect harness guidance in `DEVELOPMENT.md` and align improvements with UV-based execution and eval contracts.
2. Define feature workstream for `state/kernel.py`:
   - Add richer trace logging checkpoints for loop phases and failure reasons.
   - Add deterministic execution controls (budget/result constraints surfaced in trace summary).
3. Define role I/O scaffolding workstream for `state/role_io_templates.py`:
   - Clarify role input/output envelopes and validation expectations.
   - Add template-level metadata fields that can be asserted in tests.
4. Define smoke verification workstream for `state/copilot_sdk_uv_smoke.py`:
   - Add targeted deterministic smoke modes for new trace and scaffold behaviors.
   - Keep CLI mode matrix explicit and table-driven.
5. Define eval alignment workstream for `evals/*.yaml`:
   - Map new observability controls to specific gates in `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml`.
   - Specify metric signals to confirm expected outcomes in `state/metrics.json`.
6. Define test assets and validation strategy:
   - Add/extend harness-focused tests under `state/` for helper-level behavior.
   - Validate integration with `uv run python state/copilot_sdk_uv_smoke.py --mode ...` and targeted kernel runs.

## Expected files to change in future iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
- Harness-focused tests under `state/`
