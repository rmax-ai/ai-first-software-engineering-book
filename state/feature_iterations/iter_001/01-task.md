# Task: Plan custom state harness improvements

## Why this task now
- This is the seed iteration requested by `prompts/incremental-improvements/execute.md`.
- A concrete plan is required before any harness implementation work to keep subsequent diffs focused and verifiable.

## Acceptance criteria
1. The plan clearly lists harness feature improvements with target files under `state/`.
2. The plan defines targeted tests for each improvement area (including `uv run python state/copilot_sdk_uv_smoke.py` where relevant).
3. The plan maps changes to regression detection via existing eval gates in `evals/` and harness signals (`state/metrics.json`).
4. Iteration artifacts are complete (01-07) and concise.
