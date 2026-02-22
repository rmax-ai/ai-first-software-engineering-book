# Plan custom state harness improvements

## Why this task now
The feature-iteration runner requires a seed planning iteration before implementation work. A concrete plan now reduces churn and keeps later diffs small and verifiable.

## Acceptance criteria
- Defines proposed harness features touching `state/kernel.py` and `state/role_io_templates.py`.
- Defines targeted tests including `uv run python state/copilot_sdk_uv_smoke.py` and focused deterministic checks.
- Defines regression-eval mapping for `evals/*.yaml`, `state/metrics.json`, and expected signals.
- Provides one concrete next implementation task with file paths.
