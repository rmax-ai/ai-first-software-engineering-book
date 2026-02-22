# Task: Plan custom state harness improvements

## Why this task now

The repository-specific seed instruction for incremental improvements requires the first feature iteration to produce a concrete improvement plan for the custom harness in `state/`, with explicit feature, test, and evaluation coverage.

## Acceptance criteria

1. Plan identifies concrete harness features touching `state/kernel.py`, `state/role_io_templates.py`, and observability/control surfaces under `state/`.
2. Plan defines targeted tests, including `uv run python state/copilot_sdk_uv_smoke.py` and focused harness/unit checks.
3. Plan maps regression detection to existing eval contracts under `evals/*.yaml` and expected verification signals.
4. Iteration folder includes all seven required artifacts under `state/feature_iterations/iter_001/`.
