# Task: Plan custom state harness improvements

## Why this task now
`prompts/incremental-improvements/execute.md` defines the seed iteration as a planning-only pass for the custom harness in `state/`. Establishing a concrete, testable backlog first reduces implementation churn in later iterations.

## Acceptance criteria
- Produce a concise plan that covers harness **features**, **tests**, and **eval/regression signals**.
- Define a sequenced follow-up path touching `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, and `evals/*.yaml`.
- Keep this iteration planning-only (no harness behavior changes).
