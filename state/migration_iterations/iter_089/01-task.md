# Task

## Selected task title
Normalize the legacy fallback-error snippet wording in `state/migration_iterations/iter_083/06-next-iteration.md` so it uses `uv run python`.

## Why this task now
This was the highest-priority follow-up from `state/migration_iterations/iter_088/06-next-iteration.md` and is a one-line historical artifact cleanup.

## Acceptance criteria for this iteration
- Run `rg -nF 'python state/copilot_sdk_smoke_test.py --mode fallback-error' state/migration_iterations/iter_083/06-next-iteration.md` to confirm the legacy snippet mention.
- Replace that mention with `uv run python state/copilot_sdk_smoke_test.py --mode fallback-error` wording.
- Capture targeted `rg` checks plus `git --no-pager diff -- state/migration_iterations/iter_083/06-next-iteration.md` evidence.
