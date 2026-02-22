# Next Iteration

## Recommended next task
Normalize the remaining acceptance-criteria evidence phrase in `state/migration_iterations/iter_080/01-task.md` so it no longer says `pre-edit legacy wording` for an already normalized `uv run python` snippet.

## Why it is next
This is the next adjacent one-line cleanup in the same historical wording stream and keeps scope minimal.

## Concrete acceptance criteria
- `rg -nF 'confirms pre-edit legacy wording' state/migration_iterations/iter_080/01-task.md` confirms the residual phrase.
- Replace it with `confirms the normalized snippet mention` while leaving command text unchanged.
- Capture targeted `rg` checks plus `git --no-pager diff -- state/migration_iterations/iter_080/01-task.md` evidence.

## Expected files to touch
- `state/migration_iterations/iter_080/01-task.md`
- `state/migration_iterations/iter_091/*.md`
