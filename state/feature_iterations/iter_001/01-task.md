# Task: Plan custom state harness improvements

## Why this task now
- `prompts/incremental-improvements/execute.md` defines the seed iteration as a planning-only pass.
- A concrete plan is needed before touching `state/kernel.py` and related harness surfaces.
- Establishing feature, test, and eval scope now reduces drift in later implementation iterations.

## Acceptance criteria
- A concise improvement backlog is documented with clear feature themes for the harness.
- The plan explicitly maps future work to `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, and `evals/*.yaml`.
- Validation notes show how the plan was reviewed against `DEVELOPMENT.md` and current repository eval expectations.
