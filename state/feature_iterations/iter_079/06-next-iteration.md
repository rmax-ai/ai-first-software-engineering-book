# Next iteration

## Recommended next task
Introduce a small wrapper runner helper to reduce repeated `all_mode_specs`/`target_mode_name` boilerplate in duplicate-count coverage-guard wrappers.

## Why it is next
Now that assertion logic is fully centralized, wrapper functions still repeat setup lines; extracting that setup is the next smallest safe cleanup.

## Concrete acceptance criteria
1. Add one helper that accepts `target_mode_name` and reused PASS message text while preserving wrapper-specific output.
2. Migrate exactly two duplicate-count coverage-guard wrappers to the new helper as a proving slice.
3. Run:
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-mode-coverage-guard`
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-mode-coverage-guard-coverage-guard`

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_080/*.md`
