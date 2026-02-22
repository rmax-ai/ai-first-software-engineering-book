# Plan

1. Review constraints from `DEVELOPMENT.md` and `prompts/incremental-improvements/execute.md`.
2. Define feature backlog slices for:
   - `state/kernel.py` (trace logging, deterministic guards, clearer failure telemetry),
   - `state/role_io_templates.py` (explicit role I/O scaffolds and validation hooks),
   - `state/copilot_sdk_uv_smoke.py` (table-driven smoke coverage expansion),
   - `evals/*.yaml` (regression gates aligned with new harness behavior).
3. Define targeted verification plan per slice:
   - `uv run python state/copilot_sdk_uv_smoke.py`,
   - focused kernel run(s) via `uv run python state/kernel.py --chapter-id <id>`,
   - eval gate checks mapped to `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml`.
4. Sequence follow-up iterations from lowest risk/highest observability to broader eval enforcement.

## Expected files to change in future iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`

