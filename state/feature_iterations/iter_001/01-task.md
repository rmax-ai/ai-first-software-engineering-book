# Task: Plan custom state harness improvements

## Why this task now
- `state/feature_iterations/` has no prior iteration history, so the seed task should establish a concrete improvement backlog.
- A written plan reduces implementation drift across `state/kernel.py`, role-IO scaffolds, smoke checks, and eval contracts.

## Acceptance criteria
- Define concise feature improvements for harness behavior, observability, and deterministic controls.
- Define targeted test strategy (including `uv run python state/copilot_sdk_uv_smoke.py`) for future implementation validation.
- Define evaluation coverage tied to existing `evals/*.yaml` gates and `state/metrics.json` signals.
- Provide exactly one concrete next iteration task with specific files and measurable checks.
