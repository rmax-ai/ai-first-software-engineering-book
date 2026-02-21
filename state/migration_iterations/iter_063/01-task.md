# Task

## Selected task title
Re-run live SDK smoke validation and refresh `iter_047` evidence with `uv run`-only commands.

## Why this task now
`iter_062/06-next-iteration.md` requested validating live SDK execution in the repository runtime and capturing explicit evidence in the historical iteration artifacts.

## Acceptance criteria for this iteration
- `uv run python -c "import copilot"` succeeds in this repository environment.
- `uv run python state/copilot_sdk_smoke_test.py --mode live` succeeds and evidence is recorded.
- `state/migration_iterations/iter_047/{04-validation,05-risks-and-decisions,07-summary}.md` reflect the latest verification evidence.
