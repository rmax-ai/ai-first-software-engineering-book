# Validation

## Verification commands run
1. `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard`

## Observed outputs/results
- PASS output confirmed the new mode asserts `...uniqueness-guard-adjacency-order-guard-uniqueness-guard` appears immediately before `...uniqueness-guard-adjacency-order-guard`.

## Pass/fail against acceptance criteria
1. Added one runner with the requested adjacency-order assertion: **PASS**
2. Added one `TRACE_SUMMARY_MODE_SPECS` mode registration: **PASS**
3. Executed targeted smoke mode with PASS output: **PASS**
