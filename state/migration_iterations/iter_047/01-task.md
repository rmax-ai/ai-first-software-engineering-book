# Task

## Selected task title
Run the Copilot SDK live smoke mode using the repository-managed Python environment.

## Why this task now
`iter_046` identified missing runtime availability of the `copilot` module as the direct blocker for M1 live-provider verification.

## Acceptance criteria for this iteration
- `uv run python -c "import copilot"` succeeds.
- `uv run python state/copilot_sdk_smoke_test.py --mode live` executes and records result evidence.
- Validation artifact includes observed provider/model/content/usage output.
