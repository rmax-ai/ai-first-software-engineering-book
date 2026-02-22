# Task: Plan custom state harness improvements

## Why this task now
No prior `state/feature_iterations/` run exists, so this seed iteration establishes a concrete backlog for improving the custom harness in `state/` with explicit features, tests, and eval alignment.

## Acceptance criteria
- Document concise feature improvements for `state/kernel.py` observability, `state/role_io_templates.py` scaffolding clarity, and deterministic controls.
- Define targeted validation coverage, including `uv run python state/copilot_sdk_uv_smoke.py` and focused harness/unit checks.
- Map regression detection to existing `evals/*.yaml` contracts and expected metrics/ledger signals.
