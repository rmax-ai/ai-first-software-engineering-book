# Task

## Selected task title
Normalize the remaining acceptance-criteria evidence phrase in `state/migration_iterations/iter_090/01-task.md` so it uses `confirms the normalized snippet mention` wording.

## Why this task now
`state/migration_iterations/iter_091/06-next-iteration.md` identified this exact adjacent one-line cleanup as the next smallest unfinished migration task.

## Acceptance criteria for this iteration
- `rg -nF 'confirms pre-edit legacy wording' state/migration_iterations/iter_090/01-task.md` confirms the normalized snippet mention.
- The evidence wording in that line says `confirms the normalized snippet mention`.
- `git --no-pager diff -- state/migration_iterations/iter_090/01-task.md` shows exactly the one-line wording correction.
