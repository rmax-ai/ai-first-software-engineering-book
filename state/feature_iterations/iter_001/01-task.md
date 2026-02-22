# Task: Plan custom state harness improvements

## Why this task now
- `prompts/incremental-improvements/execute.md` seeds iteration one as a planning-only pass for the custom harness in `state/`.
- A concrete plan is required before implementation iterations can change `state/kernel.py` and related verification assets safely.

## Acceptance criteria
1. The plan defines prioritized harness feature improvements across `state/kernel.py` and `state/role_io_templates.py`.
2. The plan defines concrete validation tests, including `uv run python state/copilot_sdk_uv_smoke.py` and focused kernel checks.
3. The plan maps regression evaluation to specific `evals/*.yaml` gates and expected signals.
4. This iteration writes all seven required artifacts under `state/feature_iterations/iter_001/`.
