# Validation

## Verification commands run
- `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicates-guard`
- `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-order-guard`

## Observed outputs/results
- `PASS: usage-examples-duplicates-guard mode validates generated usage examples contain no duplicates`
- `PASS: usage-examples-order-guard mode validates generated usage examples preserve registration order`

## Pass/fail against acceptance criteria
- ✅ `run_usage_examples_duplicates_guard_mode` now reports duplicate diagnostics as deterministic mode-to-count mappings.
- ✅ Duplicate diagnostic ordering is tied to `_expected_non_stub_mode_names(...)`.
- ✅ Both required smoke-validation commands passed after the change.
