# Task

## Selected task title
Normalize SDK smoke-test command examples to `uv run python`.

## Why this task now
The prior iteration flagged mixed command examples as a recurring source of avoidable environment issues.

## Acceptance criteria for this iteration
- `state/copilot_sdk_smoke_test.py` usage text uses `uv run python ...` consistently.
- Migration guidance includes `uv run python ...` for live SDK smoke validation.
- At least one updated command is executed successfully.
