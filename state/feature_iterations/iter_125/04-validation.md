# Validation

## Verification commands run
- `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-guard`

## Observed outputs/results
- PASS: `...-order-uniqueness-guard` mode validates newest uniqueness adjacency-order guard appears exactly once.

## Pass/fail against acceptance criteria
1. PASS — a new function counts the newest adjacency-order guard mode and asserts count is `1`.
2. PASS — a new uniqueness mode is registered in `TRACE_SUMMARY_MODE_SPECS` with deterministic wording.
3. PASS — targeted smoke mode command executed and returned PASS.
