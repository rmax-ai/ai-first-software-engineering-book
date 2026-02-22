# Task

## Selected task title
Normalize the residual acceptance-criteria evidence phrase in `state/migration_iterations/iter_080/01-task.md` so it no longer says `confirms pre-edit legacy wording`.

## Why this task now
`state/migration_iterations/iter_090/06-next-iteration.md` identified this exact one-line cleanup as the next smallest unfinished migration task.

## Acceptance criteria for this iteration
- `rg -nF 'confirms pre-edit legacy wording' state/migration_iterations/iter_080/01-task.md` confirms the normalized snippet mention.
- `rg -nF 'confirms the normalized snippet mention' state/migration_iterations/iter_080/01-task.md` returns the updated evidence note.
- `git --no-pager diff -- state/migration_iterations/iter_080/01-task.md` shows exactly the one-line wording correction.
