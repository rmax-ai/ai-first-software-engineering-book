# Validation

## Verification commands
1. `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicates-guard`
2. `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-regression-guard`

## Observed results
- Command 1: PASS
- Command 2: PASS

## Acceptance criteria check
1. Added deterministic duplicate-count regression mode: **PASS**
2. Expected duplicate diagnostics derived using `_expected_non_stub_mode_names(...)` ordering: **PASS**
3. Required smoke commands executed and passing: **PASS**
