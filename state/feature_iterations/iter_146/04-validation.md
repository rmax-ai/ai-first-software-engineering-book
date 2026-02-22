# Validation

## Verification commands run
1. `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard`

## Observed outputs/results
- `PASS: usage-examples-duplicate-count-wrapper-helper-...-uniqueness-guard-adjacency-order-guard mode validates the paired uniqueness-count mode appears immediately before the long-form adjacency-order guard mode`

## Pass/fail against acceptance criteria
1. Added one runner and mode assertion for the long-form pair ordering: **PASS**
2. Registered one `TRACE_SUMMARY_MODE_SPECS` mode entry for that assertion: **PASS**
3. Targeted smoke mode executed with PASS output: **PASS**
