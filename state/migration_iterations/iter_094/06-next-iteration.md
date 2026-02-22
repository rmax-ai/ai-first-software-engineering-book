# Next Iteration

## Recommended next task
Normalize the analogous acceptance-criteria evidence wording in `state/migration_iterations/iter_093/01-task.md` so line 10 uses `confirms the normalized snippet mention` language consistently.

## Why it is next
This is the adjacent one-line wording cleanup in the same migration-artifact stream and preserves the smallest-task cadence.

## Concrete acceptance criteria
- `rg -nF 'returns no matches' state/migration_iterations/iter_093/01-task.md` confirms the residual phrase on line 10.
- Replace that trailing evidence wording with `confirms the normalized snippet mention` while keeping command text unchanged.
- Capture targeted `rg` checks and `git --no-pager diff -- state/migration_iterations/iter_093/01-task.md` evidence.

## Expected files to touch
- `state/migration_iterations/iter_093/01-task.md`
- `state/migration_iterations/iter_095/*.md`
