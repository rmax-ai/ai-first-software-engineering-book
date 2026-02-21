# Task

## Selected task title
Normalize the remaining bare `fallback-error` smoke command snippet in `state/migration_iterations/iter_055/06-next-iteration.md`.

## Why this task now
`state/migration_iterations/iter_065/06-next-iteration.md` explicitly recommended this single-line cleanup as the smallest unfinished migration task.

## Acceptance criteria for this iteration
- The bare snippet ``python state/copilot_sdk_smoke_test.py --mode fallback-error`` is no longer present in `state/migration_iterations/iter_055/06-next-iteration.md`.
- The normalized snippet `uv run python state/copilot_sdk_smoke_test.py --mode fallback-error` is present in that file.
- Targeted search and diff evidence are captured.
