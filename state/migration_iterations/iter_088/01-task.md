# Task

## Selected task title
Verify whether `state/migration_iterations/iter_083/05-risks-and-decisions.md` still contains an escaped legacy fallback-error snippet mention and normalize it only if present.

## Why this task now
This is the highest-priority follow-up from `state/migration_iterations/iter_087/06-next-iteration.md`, scoped to a single historical artifact.

## Acceptance criteria for this iteration
- Run `rg -nF "\\`python state/copilot_sdk_smoke_test.py --mode fallback-error\\`" state/migration_iterations/iter_083/05-risks-and-decisions.md` to confirm whether an escaped legacy snippet remains.
- If matched, replace with escaped ``\`uv run python state/copilot_sdk_smoke_test.py --mode fallback-error\``` wording; if not matched, record no-op evidence.
- Produce `iter_088` artifacts with targeted validation evidence.
