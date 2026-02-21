# Validation

## Verification commands run
- `uv run python -c "import copilot; print('copilot import ok')"`
- `uv run python state/copilot_sdk_smoke_test.py --mode live`
- `git --no-pager diff -- state/migration_iterations/iter_047/04-validation.md state/migration_iterations/iter_047/05-risks-and-decisions.md state/migration_iterations/iter_047/07-summary.md`

## Observed outputs/results
- Import check output: `copilot import ok`.
- Live smoke output:
  - `PASS: live Copilot SDK chat works`
  - `provider=copilot model=gpt-4.1-mini`
  - `content='ok'`
  - `usage=prompt_tokens=16620, completion_tokens=22`
- Git diff showed only targeted text updates in the three `iter_047` artifact files.

## Pass/fail against acceptance criteria
- PASS: `uv run python -c "import copilot"` succeeded.
- PASS: `uv run python state/copilot_sdk_smoke_test.py --mode live` succeeded with explicit evidence.
- PASS: Required `iter_047` artifacts were updated with current validation evidence.
