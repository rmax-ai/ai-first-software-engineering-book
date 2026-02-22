# Plan

1. Review `DEVELOPMENT.md` and extract mandatory harness touchpoints: `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, and `evals/*.yaml`.
2. Define feature-track items for future iterations:
   - richer kernel trace logging and structured state snapshots in `state/kernel.py`
   - clearer role I/O scaffold contracts in `state/role_io_templates.py`
   - deterministic smoke controls and assertions in `state/copilot_sdk_uv_smoke.py`
3. Define test-track items and exact commands for each feature track:
   - focused unit tests for helper-level behavior in `state/`
   - deterministic smoke runs via `uv run python state/copilot_sdk_uv_smoke.py`
   - targeted kernel checks via `uv run python state/kernel.py --chapter-id <id>`
4. Define evaluation-track wiring against `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml` with expected pass/fail signals.
5. Capture risk, decision, and sequencing guidance so the next iteration can implement one smallest backlog item safely.

## Expected files to change this iteration
- `state/feature_iterations/iter_001/01-task.md`
- `state/feature_iterations/iter_001/02-plan.md`
- `state/feature_iterations/iter_001/03-execution.md`
- `state/feature_iterations/iter_001/04-validation.md`
- `state/feature_iterations/iter_001/05-risks-and-decisions.md`
- `state/feature_iterations/iter_001/06-next-iteration.md`
- `state/feature_iterations/iter_001/07-summary.md`
