# Task

## Selected task title
Normalize the analogous acceptance-criteria evidence wording in `state/migration_iterations/iter_092/01-task.md` so line 10 uses `confirms the normalized snippet mention` language.

## Why this task now
`state/migration_iterations/iter_093/06-next-iteration.md` designated this exact one-line wording cleanup as the next smallest unfinished migration task.

## Acceptance criteria for this iteration
- `rg -nF 'confirms pre-edit legacy wording' state/migration_iterations/iter_092/01-task.md` confirms the normalized snippet mention.
- Keep the command text unchanged while normalizing only the trailing evidence wording.
- Capture targeted `rg` checks and `git --no-pager diff -- state/migration_iterations/iter_092/01-task.md` evidence.
