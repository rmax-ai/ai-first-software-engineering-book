# Next Iteration

## Recommended next task
Normalize migration validation commands to use `uv run python ...` consistently across docs and smoke script usage text.

## Why it is next
Current live verification is successful in the project-managed runtime, but command inconsistency (`python` vs `uv run python`) can recreate false blockers.

## Concrete acceptance criteria
- Update command examples in `state/copilot_sdk_smoke_test.py` header/help text to prefer `uv run python ...`.
- Update any migration-plan/iteration guidance that still assumes bare `python` for SDK-import checks.
- Confirm updated command examples still match an executed successful run.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/copilot-sdk-migration-plan.md`
- `state/migration_iterations/iter_048/04-validation.md`
