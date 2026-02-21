# Task

## Selected task title
Normalize one remaining bare `python` smoke-test snippet to `uv run python`.

## Why this task now
`iter_063/06-next-iteration.md` called for a focused cleanup of legacy bare-`python` command snippets in migration-iteration artifacts.

## Acceptance criteria for this iteration
- `rg -n "python -c \"import copilot\"| python state/copilot_sdk_smoke_test.py" state/migration_iterations` identifies remaining bare-`python` snippets.
- One highest-priority remaining legacy artifact is updated to `uv run python ...`.
- Validation evidence (`rg` + `git --no-pager diff -- <file>`) is captured in iteration artifacts.
