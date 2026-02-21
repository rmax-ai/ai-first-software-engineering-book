# Next Iteration

## Recommended next task
Install the `copilot` package in the environment and run the live SDK smoke test.

## Why it is next
The normalized command snippets are in place; the next highest-value step is to unblock and verify real SDK live-mode execution.

## Concrete acceptance criteria
- `uv run python -c "import copilot"` succeeds in this repository environment.
- `uv run python state/copilot_sdk_smoke_test.py --mode live` runs and records pass/fail evidence.
- Update iteration artifacts with command output and any usage/response observations.

## Expected files to touch
- `state/migration_iterations/iter_047/04-validation.md`
- `state/migration_iterations/iter_047/05-risks-and-decisions.md`
- `state/migration_iterations/iter_047/07-summary.md`
