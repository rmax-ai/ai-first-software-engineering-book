# Next Iteration

## Recommended next task
Normalize the bare snippet in `state/migration_iterations/iter_055/06-next-iteration.md` from `python state/copilot_sdk_smoke_test.py --mode fallback-error` to `uv run python state/copilot_sdk_smoke_test.py --mode fallback-error`.

## Why it is next
It is another direct legacy smoke-test command still present in migration handoff guidance and can be fixed with a one-line, low-risk edit.

## Concrete acceptance criteria
- `rg -n '\`python state/copilot_sdk_smoke_test.py --mode fallback-error\`' state/migration_iterations/iter_055/06-next-iteration.md` finds the legacy snippet before edit.
- Replace it with `uv run python state/copilot_sdk_smoke_test.py --mode fallback-error`.
- Capture `rg` and `git --no-pager diff -- state/migration_iterations/iter_055/06-next-iteration.md` evidence.

## Expected files to touch
- `state/migration_iterations/iter_055/06-next-iteration.md`
- `state/migration_iterations/iter_0XX/*.md` (new iteration handoff artifacts)
