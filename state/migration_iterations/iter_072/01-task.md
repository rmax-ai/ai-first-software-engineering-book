# Task

## Selected task title
Normalize the remaining fallback-error snippet mention in `state/migration_iterations/iter_068/06-next-iteration.md` acceptance criteria to use `uv run python` wording.

## Why this task now
`state/migration_iterations/iter_071/06-next-iteration.md` explicitly handed off this exact one-line cleanup as the next smallest unfinished migration task.

## Acceptance criteria for this iteration
- Replace `uv run python state/copilot_sdk_smoke_test.py --mode fallback-error` snippet mention with `uv run python state/copilot_sdk_smoke_test.py --mode fallback-error` in `state/migration_iterations/iter_068/06-next-iteration.md`.
- Keep edits limited to the single targeted line.
- Capture validation with literal `rg` checks and `git --no-pager diff -- state/migration_iterations/iter_068/06-next-iteration.md`.
