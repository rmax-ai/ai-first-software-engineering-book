# Task

## Selected task title
Align `state/migration_iterations/iter_082/01-task.md` acceptance-criteria evidence wording with the already-normalized `uv run python` snippet.

## Why this task now
`state/migration_iterations/iter_089/06-next-iteration.md` pointed at this file for normalization, and review confirmed the snippet was already normalized while one evidence phrase still described it as legacy.

## Acceptance criteria for this iteration
- `rg -nF 'confirms pre-edit legacy wording' state/migration_iterations/iter_082/01-task.md` confirms the normalized snippet mention.
- `rg -nF 'confirms the normalized snippet mention' state/migration_iterations/iter_082/01-task.md` returns the updated evidence note.
- `git --no-pager diff -- state/migration_iterations/iter_082/01-task.md` shows exactly the one-line wording correction.
