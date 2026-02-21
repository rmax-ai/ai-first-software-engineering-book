# Task

## Selected task title
Normalize the remaining bare fallback-timeout snippet mention in `state/migration_iterations/iter_064/06-next-iteration.md` acceptance criteria.

## Why this task now
`iter_067/06-next-iteration.md` explicitly recommends this as the next low-risk cleanup task, and it is a one-line migration consistency fix.

## Acceptance criteria for this iteration
- Confirm target bare snippet mention in `state/migration_iterations/iter_064/06-next-iteration.md` acceptance criteria.
- Replace bare `python state/copilot_sdk_smoke_test.py --mode fallback-timeout` wording with `uv run python state/copilot_sdk_smoke_test.py --mode fallback-timeout`.
- Capture targeted `rg` and `git --no-pager diff` evidence for the edited file.
