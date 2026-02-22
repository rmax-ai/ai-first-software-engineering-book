# Task

## Selected task title
Add a deterministic trace-summary smoke fixture builder in `state/copilot_sdk_uv_smoke.py`.

## Why this task now
`state/feature_iterations/iter_055/06-next-iteration.md` prioritized removing ad hoc fixture dependence so trace-summary observability checks stay reproducible.

## Acceptance criteria
1. Trace-summary mode can generate and read a minimal built-in fixture in a controlled location.
2. `uv run python state/copilot_sdk_uv_smoke.py --mode trace-summary` passes without relying on pre-created repository fixtures.
3. Validation evidence is recorded in this iteration folder.
