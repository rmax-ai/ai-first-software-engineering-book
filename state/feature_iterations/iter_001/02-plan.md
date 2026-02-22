# Iteration plan

1. Audit current harness flow in `state/kernel.py` to identify observability and determinism extension points (phase traces, budget/eval checkpoints, failure signaling).
2. Define role-I/O scaffold refinements in `state/role_io_templates.py` so future prompt contracts are explicit, testable, and easier to validate.
3. Expand smoke coverage strategy in `state/copilot_sdk_uv_smoke.py` with table-driven modes for new harness behaviors and regression guards.
4. Map eval contract updates in `evals/*.yaml` so harness changes are caught by deterministic gates (quality, style, and drift).
5. Sequence implementation work into smallest safe increments: tracing contract first, then smoke coverage, then eval hardening.
6. Record validation commands and expected evidence format for future iterations (`uv run python state/copilot_sdk_uv_smoke.py`, targeted kernel runs, eval checks).

## Files expected to change in future iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
- Optional targeted tests under `state/` for new pure helpers
