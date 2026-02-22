# Next Iteration

## Recommended next task
Normalize the escaped fallback-error snippet wording in `state/migration_iterations/iter_083/05-risks-and-decisions.md` to use escaped ``\`uv run python ...\``` wording if any escaped legacy mention remains.

## Why it is next
It continues the same low-risk, one-line cleanup pattern within the same historical iteration bundle.

## Concrete acceptance criteria
- `rg -nF "\\`python state/copilot_sdk_smoke_test.py --mode fallback-error\\`" state/migration_iterations/iter_083/05-risks-and-decisions.md` confirms whether a legacy escaped snippet remains.
- If found, replace with ``\\`uv run python state/copilot_sdk_smoke_test.py --mode fallback-error\\``` wording in that file.
- Capture targeted `rg` checks plus `git --no-pager diff -- state/migration_iterations/iter_083/05-risks-and-decisions.md` evidence.

## Expected files to touch
- `state/migration_iterations/iter_083/05-risks-and-decisions.md` (if legacy escaped snippet exists)
- `state/migration_iterations/iter_088/*.md`
