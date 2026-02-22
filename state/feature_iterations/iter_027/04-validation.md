# Validation

## Verification commands run
- `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicates-guard`
- `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-coverage-guard`

## Observed outputs/results
- `PASS: usage-examples-duplicates-guard mode validates generated usage examples contain no duplicates`
- `PASS: usage-examples-coverage-guard mode validates generated usage examples for non-stub modes`

## Pass/fail against acceptance criteria
- ✅ `run_usage_examples_duplicates_guard_mode` now reuses `_expected_non_stub_mode_names(...)`.
- ✅ Duplicate assertion computes and reports deterministic offending mode names.
- ✅ Both required smoke-validation commands passed.
