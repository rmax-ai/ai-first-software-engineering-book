# Plan

1. Review `prompts/incremental-improvements/execute.md` and `DEVELOPMENT.md` to align with iteration contract and harness guidelines.
2. Define feature workstreams:
   - Add richer trace lifecycle events and failure taxonomy in `state/kernel.py`.
   - Clarify role handoff schema constraints in `state/role_io_templates.py`.
   - Expand smoke coverage for deterministic trace/eval signaling in `state/copilot_sdk_uv_smoke.py`.
3. Define test strategy:
   - Run `uv run python state/copilot_sdk_uv_smoke.py` with focused modes validating new trace and scaffold guarantees.
   - Add/extend targeted kernel helper tests (if present) for parser/validator behavior touched by new events.
4. Define evaluation strategy:
   - Map harness output signals to `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml` checks.
   - Ensure plan includes expected `state/metrics.json` and artifact evidence alignment.
5. Record risks, decisions, and a single concrete next task to begin implementation in the next iteration.

## Files expected to change in later execution iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
