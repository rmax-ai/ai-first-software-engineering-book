# Task

## Selected task title
Introduce a wrapper runner helper and migrate two duplicate-count coverage-guard wrappers as a proving slice.

## Why this task now
`state/feature_iterations/iter_079/06-next-iteration.md` marked wrapper setup boilerplate reduction as the next smallest unfinished cleanup.

## Acceptance criteria
1. Add one helper that accepts `target_mode_name` and reused PASS message text while preserving wrapper-specific output.
2. Migrate exactly two duplicate-count coverage-guard wrappers to the new helper.
3. Run:
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-mode-coverage-guard`
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-mode-coverage-guard-coverage-guard`
