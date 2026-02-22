# Plan

1. Baseline current harness guidance from `DEVELOPMENT.md` and align proposed work with deterministic, minimal-diff iteration flow.
2. Define **feature backlog** for the custom harness:
   - Add richer trace-summary observability in `state/kernel.py` for iteration outputs and guard outcomes.
   - Clarify role I/O scaffolds in `state/role_io_templates.py` so writer/critic transitions are easier to validate deterministically.
   - Add deterministic UV smoke coverage in `state/copilot_sdk_uv_smoke.py` for new trace and role-template invariants.
3. Define **test backlog** to prove feature work:
   - Add/extend focused smoke modes in `state/copilot_sdk_uv_smoke.py`.
   - Add targeted unit-level checks (or deterministic helper checks) for trace-summary shape and role-template contracts.
   - Validate via `uv run python state/copilot_sdk_uv_smoke.py --mode <new-mode>`.
4. Define **evaluation backlog** to prevent regressions:
   - Ensure eval contracts in `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml` reflect new expected signals.
   - Confirm harness outputs remain compatible with `state/metrics.json` and iteration artifact requirements.
5. Sequence future work as smallest tasks:
   - Iteration N+1: implement one trace-summary observability improvement in `state/kernel.py` with a deterministic smoke assertion.
   - Iteration N+2: tighten `state/role_io_templates.py` scaffolds and add coverage.
   - Iteration N+3: wire eval contract refinements under `evals/*.yaml`.

## Files expected to change in future iterations

- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
