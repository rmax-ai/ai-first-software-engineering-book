# Plan

1. Review current harness guidance (`DEVELOPMENT.md`) and seed requirements from `prompts/incremental-improvements/execute.md`.
2. Define feature backlog items for later implementation:
   - Add richer trace/event summaries and failure-context logging in `state/kernel.py`.
   - Tighten role prompt input/output scaffolds in `state/role_io_templates.py` for clearer deterministic contracts.
   - Extend smoke coverage in `state/copilot_sdk_uv_smoke.py` for deterministic execution constraints.
3. Define proof strategy:
   - Targeted harness checks via `uv run python state/copilot_sdk_uv_smoke.py` (mode-focused).
   - Unit-level tests for new pure helpers in `state/` modules touched by the backlog.
4. Define eval/regression alignment:
   - Confirm `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml` still gate intended behavior.
   - Verify expected ledger/metrics outcomes in `state/ledger.json` and `state/metrics.json` remain explainable.
5. Stage next iteration as implementation of the smallest high-impact feature from this backlog (kernel trace summary enhancement).

## Expected files to change in later iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
- Targeted tests/assets under `state/` (as required by chosen backlog item)
