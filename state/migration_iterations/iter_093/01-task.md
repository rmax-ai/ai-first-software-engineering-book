# Task

## Selected task title
Normalize the analogous acceptance-criteria evidence wording in `state/migration_iterations/iter_091/01-task.md` so line 10 uses `confirms the normalized snippet mention` language.

## Why this task now
`state/migration_iterations/iter_092/06-next-iteration.md` designated this exact one-line wording cleanup as the next smallest unfinished task.

## Acceptance criteria for this iteration
- `rg -nF 'returns no matches' state/migration_iterations/iter_091/01-task.md` confirms the normalized snippet mention.
- Replace the trailing evidence wording with `confirms the normalized snippet mention` while keeping command text unchanged.
- Capture targeted `rg` checks and `git --no-pager diff -- state/migration_iterations/iter_091/01-task.md` evidence.
