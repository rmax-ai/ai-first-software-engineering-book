# Task: Plan custom state harness improvements

## Why this task now
- `prompts/incremental-improvements/execute.md` specifies the seed iteration must produce a planning-only backlog for custom harness improvements in `state/`.
- A concrete plan is required before implementation iterations can safely modify kernel behavior, scaffolds, smoke coverage, and eval contracts.

## Acceptance criteria
- Produce a concise plan that explicitly covers required **features**, **tests**, and **evaluations**.
- Include stepwise implementation guidance for future iterations touching:
  - `state/kernel.py`
  - `state/role_io_templates.py`
  - `state/copilot_sdk_uv_smoke.py`
  - `evals/*.yaml`
- Keep this iteration planning-only (no production code behavior changes).
