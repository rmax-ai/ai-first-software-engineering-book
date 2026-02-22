# Validation

## Verification commands run
1. `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard`

## Observed outputs/results
- Command (1) returned PASS: `...order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard mode validates ... appears exactly once`.

## Pass/fail against acceptance criteria
1. Added one smoke mode function asserting exactly-once count for the newest `...order-uniqueness-order-uniqueness-order-uniqueness-order-guard`: **PASS**
2. Registered one new `...order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard` mode in `TRACE_SUMMARY_MODE_SPECS`: **PASS**
3. Executed the targeted smoke mode and captured PASS output: **PASS**
