# Task: Refactor usage-examples duplicates guard helper usage

## Why this task now
`state/feature_iterations/iter_026/06-next-iteration.md` identified `usage-examples-duplicates-guard` as the remaining guard not reusing `_expected_non_stub_mode_names(...)`.

## Acceptance criteria
1. Update `run_usage_examples_duplicates_guard_mode` in `state/copilot_sdk_smoke_test.py` to reuse `_expected_non_stub_mode_names(...)`.
2. Keep duplicate assertions deterministic and explicit about offending mode names.
3. Validate with:
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicates-guard`
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-coverage-guard`
