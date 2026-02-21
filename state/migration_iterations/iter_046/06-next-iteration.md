# Next Iteration

## Recommended next task
Install the `copilot` package in the execution environment and rerun the live SDK smoke mode.

## Why it is next
The current iteration is blocked only by missing runtime dependency; resolving it enables direct verification of M1 live-provider behavior.

## Concrete acceptance criteria
- `python -c "import copilot"` succeeds in this repository environment.
- `python state/copilot_sdk_smoke_test.py --mode live` executes and records pass/fail evidence.
- Update iteration artifacts with command output and response/usage extraction observations.

## Expected files to touch
- `state/migration_iterations/iter_047/04-validation.md`
- `state/migration_iterations/iter_047/05-risks-and-decisions.md`
- `state/migration_iterations/iter_047/07-summary.md`
