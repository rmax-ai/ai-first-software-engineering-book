# Validation

## Verification commands run
- `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-guard`

## Observed outputs/results
- PASS: `...-order-uniqueness-adjacency-uniqueness-adjacency-order-guard` mode validates newest uniqueness adjacency-order adjacency guard appears immediately before prior uniqueness adjacency-order guard.

## Pass/fail against acceptance criteria
1. PASS — one new smoke mode function compares mode indices and asserts immediate adjacency.
2. PASS — new adjacency-order guard mode was registered in `TRACE_SUMMARY_MODE_SPECS` with deterministic wording.
3. PASS — targeted smoke mode command executed successfully and returned PASS.
