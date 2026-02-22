# Next Iteration

## Recommended next task
Normalize the escaped fallback-error command snippet in `state/migration_iterations/iter_083/03-execution.md` so the command example uses escaped ``uv run python ...`` wording.

## Why it is next
It is a one-line adjacent cleanup in the same iteration folder and continues the minimal-risk normalization sequence.

## Concrete acceptance criteria
- `rg -nF "\\`python state/copilot_sdk_smoke_test.py --mode fallback-error\\`" state/migration_iterations/iter_083/03-execution.md` confirms the remaining legacy escaped snippet mention.
- Replace that escaped snippet mention with ``\`uv run python state/copilot_sdk_smoke_test.py --mode fallback-error\``` wording.
- Capture targeted `rg` checks plus `git --no-pager diff -- state/migration_iterations/iter_083/03-execution.md` evidence.

## Expected files to touch
- `state/migration_iterations/iter_083/03-execution.md`
- `state/migration_iterations/iter_086/*.md`
