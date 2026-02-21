# Task

## Selected task title
Normalize the legacy fallback-error snippet reference in `state/migration_iterations/iter_065/06-next-iteration.md`.

## Why this task now
`iter_066/06-next-iteration.md` explicitly prioritized this adjacent one-line command-normalization cleanup.

## Acceptance criteria for this iteration
- Replace bare `python state/copilot_sdk_smoke_test.py --mode fallback-error` reference(s) in `state/migration_iterations/iter_065/06-next-iteration.md` with `uv run python state/copilot_sdk_smoke_test.py --mode fallback-error` wording.
- Keep the change minimal and limited to that file.
- Capture targeted `rg`/`git` evidence in this iteration folder.
