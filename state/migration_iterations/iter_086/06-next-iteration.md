# Next Iteration

## Recommended next task
Normalize the escaped fallback-error snippet wording in `state/migration_iterations/iter_083/04-validation.md` so it uses escaped ``uv run python ...`` wording.

## Why it is next
It is the next adjacent one-line normalization in the same iteration folder and continues the minimal-risk cleanup chain.

## Concrete acceptance criteria
- `rg -nF "\\`python state/copilot_sdk_smoke_test.py --mode fallback-error\\`" state/migration_iterations/iter_083/04-validation.md` confirms the remaining legacy escaped snippet mention.
- Replace that escaped snippet mention with ``\\`uv run python state/copilot_sdk_smoke_test.py --mode fallback-error\\``` wording.
- Capture targeted `rg` checks plus `git --no-pager diff -- state/migration_iterations/iter_083/04-validation.md` evidence.

## Expected files to touch
- `state/migration_iterations/iter_083/04-validation.md`
- `state/migration_iterations/iter_087/*.md`
