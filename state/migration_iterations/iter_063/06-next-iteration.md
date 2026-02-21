# Next Iteration

## Recommended next task
Run a focused audit to normalize remaining migration-iteration snippets that still use bare `python` instead of `uv run python`.

## Why it is next
This iteration completed the live smoke evidence refresh; the remaining risk is inconsistent command guidance across older iteration artifacts.

## Concrete acceptance criteria
- `rg -n "python -c \\\"import copilot\\\"| python state/copilot_sdk_smoke_test.py" state/migration_iterations` identifies remaining bare-`python` snippets.
- Update exactly one highest-priority remaining file to `uv run python ...` command form.
- Capture targeted validation (`rg` + `git show -- <file>`) in the new iteration artifacts.

## Expected files to touch
- `state/migration_iterations/iter_0XX/*.md` (one targeted legacy artifact file discovered by search)
