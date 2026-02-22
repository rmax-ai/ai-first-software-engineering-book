# Plan custom state harness improvements

## Why this task now
The incremental-improvements runner specifies a seed iteration that creates a written improvement plan before implementation. Producing this plan first establishes a bounded, testable backlog for later iterations and aligns with `DEVELOPMENT.md` guidance for harness-first work.

## Acceptance criteria
- Provide a concise backlog plan covering harness **features**, **tests**, and **evaluations**.
- Define how later iterations will touch `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, and `evals/*.yaml`.
- Leave one concrete next task with explicit acceptance criteria and expected files.
