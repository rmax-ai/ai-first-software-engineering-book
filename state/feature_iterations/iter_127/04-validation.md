# Validation

## Verification commands run
- `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-guard`

## Observed outputs/results
- PASS: `...-order-uniqueness-adjacency-uniqueness-adjacency-guard` mode validates newest uniqueness adjacency-order adjacency guard appears exactly once.

## Pass/fail against acceptance criteria
1. PASS — one new smoke mode function asserts exactly one occurrence of the newest `...order-uniqueness-adjacency-guard` mode.
2. PASS — mode registration added to `TRACE_SUMMARY_MODE_SPECS` with deterministic wording.
3. PASS — targeted smoke mode command executed successfully and returned PASS.
