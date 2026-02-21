# Task

## Selected task title
Normalize the remaining bare fallback-error snippet mention in `state/migration_iterations/iter_066/04-validation.md` command 1.

## Why this task now
`state/migration_iterations/iter_068/06-next-iteration.md` marked this as the next smallest unfinished migration cleanup, scoped to a one-line documentation correction.

## Acceptance criteria for this iteration
- Confirm command 1 in `state/migration_iterations/iter_066/04-validation.md` contains bare snippet wording before edit.
- Replace bare `python state/copilot_sdk_smoke_test.py --mode fallback-error` snippet text with `uv run python state/copilot_sdk_smoke_test.py --mode fallback-error`.
- Capture targeted `rg` checks and `git --no-pager diff -- state/migration_iterations/iter_066/04-validation.md` evidence.
